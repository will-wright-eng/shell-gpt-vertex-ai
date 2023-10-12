import google.auth
import google.auth.transport.requests
# from google.auth.transport.requests import AuthorizedSession


def get_session():
    # Obtain the credentials
    credentials, project = google.auth.default()

    # Create an authenticated session
    authed_session = google.auth.transport.requests.AuthorizedSession(credentials)
    return authed_session
