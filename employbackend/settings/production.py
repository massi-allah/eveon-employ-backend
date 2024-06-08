from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]


CORS_ALLOWED_ORIGINS = [
    "https://eveon-employ-frontend-d5a386bd6b6f.herokuapp.com",
]

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}
