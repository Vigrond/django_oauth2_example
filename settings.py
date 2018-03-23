INSTALLED_APPS = [
    ...
    'oauth2_provider',
    'rest_framework',
    'drf_yasg',
]

...

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    )
}

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        "Your App API - Swagger": {
            "type": "oauth2",
            'authorizationUrl': '/yourapp/o/authorize',
            'tokenUrl': '/yourapp/o/token/',
            "flow": "accessCode",
            "scopes": {
                'read groups': 'read groups',
            }
        }
    },
    'OAUTH2_REDIRECT_URL': 'http://localhost/static/drf-yasg/swagger-ui-dist/oauth2-redirect.html',
    'OAUTH2_CONFIG': {
        'clientId': 'yourAppClientId',
        'clientSecret': 'yourAppClientSecret',
        'appName': 'your application name'

    },
}
