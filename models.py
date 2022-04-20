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


# Define your table below
#
# db.define_table('thing', Field('name'))
#
# always commit your models to avoid problems later

db.define_table(
    'bird',
    Field('bird_name', requires=IS_NOT_EMPTY()),
    Field('weight', 'integer', default=0),
    Field('diet', requires=IS_NOT_EMPTY()),
    Field('habitat', requires=IS_NOT_EMPTY()),
    Field('n_sightings', 'integer', default=1),
    Field('user_email', default=get_user_email)
)

db.commit()
