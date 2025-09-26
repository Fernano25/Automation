import pytest
from src.api.clients.http_client import HttpClient
from src.api.endpoints import Endpoints
from src.utils.assertions import Assertions
from src.utils.data_generator import DataGenerator
from src.api.schemas.posts import CreatePostSchema

class TestCRUDOperations:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = HttpClient()
        self.assertions = Assertions()
        self.data_gen = DataGenerator()
        self.created_posts = []
        yield
        self.cleanup()

    def cleanup(self):
        """Cleanup created test data"""
        for post_id in self.created_posts:
            try:
                self.client.delete(Endpoints.POST_BY_ID.value.format(id=post_id))
            except:
                pass

    @pytest.mark.parametrize("test_data", [
        {"title": "Test Post", "body": "Test content", "userId": 1},
        {"title": "Another Post", "body": "Another content", "userId": 2}
    ])
    def test_create_post(self, test_data):
        """Test POST /posts - Create new post with parametrized data"""
        response = self.client.post(Endpoints.POSTS.value, data=test_data)
        
        self.assertions.assert_status_code(response.status_code, 201)
        self.assertions.assert_schema(response.json(), CreatePostSchema)
        self.assertions.assert_json_contains(response.json(), test_data)
        
        # Store for cleanup
        self.created_posts.append(response.json()["id"])

    def test_update_post(self):
        """Test PUT /posts/{id} - Update existing post"""
        # First create a post
        post_data = self.data_gen.generate_post_data()
        create_response = self.client.post(Endpoints.POSTS.value, data=post_data)
        post_id = create_response.json()["id"]
        self.created_posts.append(post_id)

        # Update the post
        update_data = {"title": "Updated Title", "body": "Updated content"}
        response = self.client.put(
            Endpoints.POST_BY_ID.value.format(id=post_id),
            data=update_data
        )
        
        self.assertions.assert_status_code(response.status_code, 200)
        self.assertions.assert_json_contains(response.json(), update_data)

    def test_delete_post(self):
        """Test DELETE /posts/{id} - Delete post"""
        # First create a post
        post_data = self.data_gen.generate_post_data()
        create_response = self.client.post(Endpoints.POSTS.value, data=post_data)
        post_id = create_response.json()["id"]

        # Delete the post
        response = self.client.delete(Endpoints.POST_BY_ID.value.format(id=post_id))
        
        self.assertions.assert_status_code(response.status_code, 200)