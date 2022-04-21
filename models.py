"""
This file defines the database models
"""

import datetime
from email.policy import default
import string

from importlib_metadata import requires
from .common import db, Field, auth
from pydal.validators import *


def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None


def get_time():
    return datetime.datetime.utcnow()


db.define_table(
    'bird',
    Field('bird', requires=IS_NOT_EMPTY()),
    Field('weight', 'integer', requires=IS_NOT_EMPTY()),
    Field('diet', requires=IS_NOT_EMPTY()),
    Field('habitat', requires=IS_NOT_EMPTY()),
    Field('n_sightings', 'integer', default=1),
    Field('user_email', default=get_user_email)
)

db.bird.id.readable = db.bird.id.writable = False

db.commit()
