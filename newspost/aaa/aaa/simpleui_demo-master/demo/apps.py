from django.apps import AppConfig
# my_project_app/apps.py
# from suit.apps import DjangoSuitConfig

# class SuitConfig(DjangoSuitConfig):
#     layout = 'vertical'

class DemoConfig(AppConfig):
    name = 'demo'
    verbose_name = 'News Post'

