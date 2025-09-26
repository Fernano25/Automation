import pytest
from src.api.clients.http_client import HttpClient
from src.api.endpoints import Endpoints
from src.utils.assertions import Assertions
from src.utils.data_generator import DataGenerator

class TestE2EFlows:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = HttpClient()
        self.assertions = Assertions()
        self.data_gen = DataGenerator()
        self.created_resources = []
        yield
        self.cleanup()

    def cleanup(self):
        """Cleanup all created test data"""
        for resource_id in self.created_resources:
            try:
                self.client.delete(Endpoints.POST_BY_ID.value.format(id=resource_id))
            except:
                pass

    def test_e2e_post_creation_flow(self):
        """E2E Flow: Create Post → Verify Creation → Update → Verify Update → Delete"""
        # Step 1: Create post
        post_data = self.data_gen.generate_post_data()
        create_response = self.client.post(Endpoints.POSTS.value, data=post_data)
        post_id = create_response.json()["id"]
        self.created_resources.append(post_id)
        
        self.assertions.assert_status_code(create_response.status_code, 201)
        self.assertions.assert_json_contains(create_response.json(), post_data)

        # Step 2: Verify post was created
        get_response = self.client.get(Endpoints.POST_BY_ID.value.format(id=post_id))
        self.assertions.assert_status_code(get_response.status_code, 200)
        self.assertions.assert_json_contains(get_response.json(), post_data)

        # Step 3: Update post
        update_data = {"title": "Updated E2E Title", "body": "Updated E2E Content"}
        update_response = self.client.put(
            Endpoints.POST_BY_ID.value.format(id=post_id),
            data=update_data
        )
        self.assertions.assert_status_code(update_response.status_code, 200)

        # Step 4: Verify update
        verify_response = self.client.get(Endpoints.POST_BY_ID.value.format(id=post_id))
        self.assertions.assert_status_code(verify_response.status_code, 200)
        self.assertions.assert_json_contains(verify_response.json(), update_data)

        # Step 5: Delete post
        delete_response = self.client.delete(Endpoints.POST_BY_ID.value.format(id=post_id))
        self.assertions.assert_status_code(delete_response.status_code, 200)

        # Remove from cleanup since it's already deleted
        self.created_resources.remove(post_id)

    def test_e2e_user_posts_flow(self):
        """E2E Flow: Get User → Get User's Posts → Verify Posts Structure"""
        # Step 1: Get user
        user_id = 1
        user_response = self.client.get(Endpoints.USER_BY_ID.value.format(id=user_id))
        self.assertions.assert_status_code(user_response.status_code, 200)

        # Step 2: Get user's posts
        posts_response = self.client.get(Endpoints.POSTS.value, params={"userId": user_id})
        self.assertions.assert_status_code(posts_response.status_code, 200)
        
        # Step 3: Verify all posts belong to the user
        for post in posts_response.json():
            assert post["userId"] == user_id, f"Post {post['id']} doesn't belong to user {user_id}"