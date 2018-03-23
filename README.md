# django + oauth2 + swagger example

This is an example `settings.py` to get an `OAUTH2` flow working with `python` `django` and `swagger`.

This has been tested on Django 2.0


Follow basic setup instructions from:

https://github.com/evonove/django-oauth-toolkit

and

https://github.com/axnsan12/drf-yasg


Then use the `settings.py` file as an example to follow off of.

Ensure your `application` is set to something like:

```
Client type: confidential
Authorization Grant Type: authorization-code
Redirect Uris: 'http://localhost/static/drf-yasg/swagger-ui-dist/oauth2-redirect.html'

```

This example uses the `accessCode` flow.

`SWAGGER_SETTINGS` References:

https://github.com/swagger-api/swagger-ui/blob/245428e7cd866f7bb3d07dc36ea23bc144308ea9/docs/usage/oauth2.md

https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#security-definitions-object

`OAUTH2 redirect url reference`
(note the static path)
https://github.com/axnsan12/drf-yasg/blob/master/src/drf_yasg/static/drf-yasg/swagger-ui-dist/oauth2-redirect.html
