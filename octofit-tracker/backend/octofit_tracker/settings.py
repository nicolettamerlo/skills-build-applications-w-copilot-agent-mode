# Add the new app to the INSTALLED_APPS list
INSTALLED_APPS = [
    # ...existing apps...
    'octofit_tracker_app',
]

# Add the djongo database engine
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Enable CORS
INSTALLED_APPS += [
    'corsheaders',
]

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
]

# Allow all hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'solid-goldfish-v6v79r7v6v9rfx7vv-8000.app.github.dev']