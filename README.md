# testTaskStarNavi

Object of this task is to create a simple REST API. Using Django and Django rest framework.

## Social Network

### Installation/Usage:

For run development server you need to use python 3.5+

First, need to install requirements from file:
```shell
pip install -r requirements.txt
```
Then you need to do some things from base django dir (social_network):

- Then need to migrate database:
```shell
python manage.py migrate
```

- Optional you can create superuser:
```shell
python manage.py createsuperuser
```

- Finally you can run development server:
```shell
python manage.py runserver
```
For test system using bot you just need switch directory to bot, and run:
```shell
python main.py
```
- You can change your bot configuration in file /bot/config.py

### About task:

Basic models:
- User
- Post (always made by a user)

Basic features:
- user signup
- user login
- post creation
- post like
- post unlike

  For User and Post objects, candidate is free to define attributes as they see fit.

Requirements:
- Token authentication (JWT is prefered)
-use Django with any other Django batteries, databases etc.

Optional (will be a plus):
- use clearbit.com/enrichment for getting additional data for the user on signup
- use emailhunter.co for verifying email existence on signup

Automated bot
  Object of this bot demonstrate functionalities of the system according to defined rules.
This bot should read rules from a config file (in any format chosen by the candidate), but
should have following fields (all integers, candidate can rename as they see fit):
- number_of_users
- max_posts_per_user
- max_likes_per_user

Bot should read the configuration and create this activity:
- signup users (number provided in config)
- each user creates random number of posts with any content (up to
max_posts_per_user)
- After creating the signup and posting activity, posts should be liked randomly, posts
can be liked multiple times
Notes
- emailhunter and clearbit have either free pricing plans or free trial, the candidate can
use their own account if he would like implement the functionality
- visual aspect of the project is not important, the candidate can create a frontend for
viewing the result, but it is not necessary (will be a plus). Clean and usable REST
API is important
- the project is not defined in detail, the candidate should use their best judgment for
every non-specified requirements (including chosen tech, third party apps, etc),
however
- every decision must be explained and backed by arguments in the interview
- Result should be sent by providing a Git url. This is a mandatory requirement.
