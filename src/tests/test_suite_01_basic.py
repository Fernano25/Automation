import pytest
from src.api.clients.http_client import HttpClient
from src.api.endpoints import Endpoints
from src.utils.assertions import Assertions
from src.api.schemas.posts import PostSchema

class TestBasicOperations:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = HttpClient()
        self.assertions = Assertions()
        yield
        # Cleanup if needed

    def test_get_all_posts(self):
        """Test GET /posts - Retrieve all posts"""
        response = self.client.get(Endpoints.POSTS.value)
        
        self.assertions.assert_status_code(response.status_code, 200)
        self.assertions.assert_schema(response.json()[0], PostSchema)
        self.assertions.assert_list_length(response.json(), 100)

    def test_get_post_by_id(self):
        """Test GET /posts/{id} - Retrieve specific post"""
        post_id = 1
        response = self.client.get(Endpoints.POST_BY_ID.value.format(id=post_id))
        
        self.assertions.assert_status_code(response.status_code, 200)
        self.assertions.assert_schema(response.json(), PostSchema)
        self.assertions.assert_json_contains(response.json(), {"id": post_id})