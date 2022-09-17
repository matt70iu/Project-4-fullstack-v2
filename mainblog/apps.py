'''required imports'''

from django.apps import AppConfig


class MainblogConfig(AppConfig):

    ''' Add main app to admin panel
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainblog'
