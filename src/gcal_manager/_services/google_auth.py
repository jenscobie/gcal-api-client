"""Authentication and authorization for the Google APIs."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from google.auth.credentials import Credentials

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials as OAuthCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import Resource, build

scopes = ["https://www.googleapis.com/auth/calendar"]


def credentials(directory: Path) -> Credentials | None:
    """Locate credentials at the specified path.

    Returns:
        A valid credentials object, or None if credentials cannot be loaded.
    """

    def token_path() -> Path:
        return Path(f"{directory.absolute()}/token.json")

    def cred_path() -> Path:
        return Path(f"{directory.absolute()}/credentials.json")

    if not directory.exists():
        return None

    creds = None

    if token_path().exists():
        creds = OAuthCredentials.from_authorized_user_file(
            token_path().absolute(), scopes
        )

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    if creds and creds.valid:
        return creds

    if cred_path().exists():
        flow = InstalledAppFlow.from_client_secrets_file(
            cred_path().absolute(), scopes
        )
        creds = flow.run_local_server(port=0)

        with token_path().open("w") as token:
            token.write(creds.to_json())

    return creds


def auth(credentials: Credentials) -> Resource:
    """Returns a Google Calendar API resource.

    Authenticate against the Google Calendar API and return a resource for
    querying the calendar.

    Args:
        credentials: Secrets used to connect to Google Calendar API.
    """
    return build("calendar", "v3", credentials=credentials)
