import random
import string

from faker import Faker

from . import config


class Bot:
    def __init__(self):
        self.fake = Faker('en_US')
        self.config = config
        self.users = []

    def sigup_user(self, username=None, email=None, password=None):
        if not username or email:
            user = self.fake.simple_profile(sex=None)
            if not username:
                username = user['username']
            if not email:
                email = user['mail']
        if not password:
            password = self._get_random_password(8)

        # TODO: ACTION WITH API

        self.users.append({'username': username, 'email': email, 'password': password, 'token': ''})
        return True

    def auth_user(self, username, password):
        # TODO: ACTION WITH API
        pass

    def _get_random_password(self, char_count):
        return ''.join(random.choices(
            string.ascii_uppercase + string.digits,
            k=char_count or self.config.password_char_count)
        )

    def create_random_post(self, title=None, text=None, user=None):
        if not title:
            title = self.fake.text()[:100]
        if not text:
            text = self.fake.text()
        if not user:
            user = random.choice(self.users)

        # TODO: ACTION WITH API

    def like_random_post(self, post_id=None, user=None):
        if not user:
            user = random.choice(self.users)
        # TODO: ACTION WITH API


if __name__ == "__main__":
    social_bot = Bot()
