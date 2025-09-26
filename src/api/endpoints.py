from enum import Enum

class Endpoints(Enum):
    BASE_URL = "https://jsonplaceholder.typicode.com"
    POSTS = "/posts"
    POST_BY_ID = "/posts/{id}"
    COMMENTS = "/posts/{id}/comments"
    USERS = "/users"
    USER_BY_ID = "/users/{id}"