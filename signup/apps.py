'''Required app imports
'''
from django.apps import AppConfig


class SignupConfig(AppConfig):
    '''Import signup app
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signup'
