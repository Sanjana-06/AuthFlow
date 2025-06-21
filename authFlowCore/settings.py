INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 3rd party
    'rest_framework',
    'rest_framework.authtoken',
    
    # Your apps
    'main',


]

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
