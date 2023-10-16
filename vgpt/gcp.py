"""
Source code for google.auth.transport.requests
https://googleapis.dev/python/google-auth/latest/_modules/google/auth/transport/requests.html#AuthorizedSession

class AuthorizedSession(requests.Session):
    A Requests Session class with credentials.

    This class is used to perform requests to API endpoints that require
    authorization::

        from google.auth.transport.requests import AuthorizedSession

        authed_session = AuthorizedSession(credentials)

        response = authed_session.request(
            'GET', 'https://www.googleapis.com/storage/v1/b')


    The underlying :meth:`request` implementation handles adding the
    credentials' headers to the request and refreshing credentials as needed
"""

import google.auth
import google.auth.transport.requests


def get_session():
    # Obtain the credentials
    credentials, project = google.auth.default()
    # Create an authenticated session
    authed_session = google.auth.transport.requests.AuthorizedSession(credentials)
    return authed_session
