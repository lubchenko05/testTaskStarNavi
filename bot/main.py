import random
import string

import requests
from faker import Faker

import config


class Bot:
    def __init__(self):
        self.fake = Faker('en_US')
        self.config = config
        self.users = []
        self.posts = []

    def signup_user(self, username=None, email=None, password=None):

        url = self.config.api_root_url + self.config.api_user_prefix

        if not username or email:
            user = self.fake.simple_profile(sex=None)
            if not username:
                username = user['username']
            if not email:
                email = user['mail']
        if not password:
            password = self._get_random_password(8)

        payload = {
            'username': username,
            'email': email,
            'password': password
        }

        response = requests.post(url, payload)

        if response.status_code == 201:
            payload['token'] = ''
            payload['id'] = response.json().get('id')
            self.users.append(payload)
            return True

    def auth_user(self, username, password):
        url = self.config.api_root_url + self.config.api_auth_prefix

        payload = {
            'username': username,
            'password': password
        }

        response = requests.post(url, payload)
        if response.status_code == 200:
            return response.json().get('token')

    def _get_random_password(self, char_count):
        return ''.join(random.choices(
            string.ascii_uppercase + string.digits,
            k=char_count or self.config.password_char_count)
        )

    def _print_users(self):
        print('Users:', end='')
        for user in self.users:
            print(''.join(['\n\t%s - %s' % (key, value) for key, value in user.items()]) + '\n')

    def _print_posts(self):
        print('Posts:', end='')
        for post in self.posts:
            print(''.join(['\n\t%s - %s' % (key, value) for key, value in post.items()]) + '\n')

    def create_random_post(self, title=None, text=None, user=None):
        url = self.config.api_root_url + self.config.api_post_list_prefix

        if not title:
            title = self.fake.text()[:100]
        if not text:
            text = self.fake.text()
        if not user:
            user = random.choice(self.users)

        headers = {
            'Authorization': 'JWT ' + user.get('token', '')
        }

        payload = {
            'title': title,
            'text': text,
        }

        response = requests.post(url, payload, headers=headers)

        if response.status_code == 201:
            self.posts.append(response.json())
            return True

    def like_random_post(self, post_id=None, user=None):
        if not post_id:
            post_id = str(random.choice(self.posts)['id'])

        if not user:
            user = random.choice(self.users)

        url = \
            self.config.api_root_url + \
            self.config.api_post_list_prefix +\
            post_id + '/' + \
            self.config.api_post_like_prefix

        headers = {
            'Authorization': 'JWT ' + user.get('token', '')
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True

    def test_functionality(self):
        # sign up users
        for _ in range(self.config.number_of_users):
            self.signup_user()

        # auth users
        for index in range(len(self.users)):
            self.users[index]['token'] = self.auth_user(self.users[index]['username'], self.users[index]['password'])

        # print users for debug
        if self.config.DEBUG:
            self._print_users()

        # create new posts
        for user in self.users:
            count = random.choice(range(self.config.max_posts_per_user + 1))

            for _ in range(count):
                self.create_random_post(user=user)

        # like posts
        for index in range(len(self.users)):
            count = random.choice(range(self.config.max_likes_per_user + 1))
            for _ in range(count):
                # filter posts because user can like post once.
                post_id = random.choice([x for x in self.posts if self.users[index]['id'] not in x['likes']])['id']

                if not post_id:
                    break

                if self.like_random_post(user=self.users[index]):
                    for post in self.posts:
                        if post["id"] == post_id:
                            post['likes'].append(self.users[index]['id'])

        # print posts for debug
        if self.config.DEBUG:
            self._print_posts()


if __name__ == "__main__":
    social_bot = Bot()
    social_bot.test_functionality()

