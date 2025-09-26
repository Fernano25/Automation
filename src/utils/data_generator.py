import random
import string
from faker import Faker

class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def random_string(self, length: int = 10) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def random_title(self) -> str:
        return self.fake.sentence()

    def random_body(self) -> str:
        return self.fake.paragraph()

    def random_user_id(self) -> int:
        return random.randint(1, 10)

    def generate_post_data(self) -> dict:
        return {
            "userId": self.random_user_id(),
            "title": self.random_title(),
            "body": self.random_body()
        }