from pathlib import Path
from typing import Optional, Self

from google.oauth2.credentials import Credentials as OAuthCredentials
from google.auth.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.discovery import Resource

from gcal_manager.domain.model.account_id import AccountId

scopes = ["https://www.googleapis.com/auth/calendar"]

class GoogleCalendarGateway():

    def __init__(self, directory: Path, account_id: AccountId) -> Self:
        self.directory = directory
        self.account_id = account_id

        creds = credentials(self.account_id)
        self.client = auth(creds)

    def calendars(self):
        return self.client.calendarList().list().execute()


def credentials(directory: Path) -> Optional[Credentials]:
    def token_path() -> Path:
        return Path(f"{directory.absolute()}/token.json")
    
    def cred_path() -> Path:
        return Path(f"{directory.absolute()}/credentials.json")
    
    if not directory.exists():
        return None
    
    creds = None

    if token_path().exists():
        creds = OAuthCredentials.from_authorized_user_file(token_path().absolute(), scopes)

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    if creds and creds.valid:
        return creds

    if cred_path().exists():
        flow = InstalledAppFlow.from_client_secrets_file(cred_path().absolute(), scopes)
        creds = flow.run_local_server(port=0)

        with token_path().open("w") as token:
            token.write(creds.to_json())    

    return creds
    
def auth(credentials) -> Resource:
    return build("calendar", "v3", credentials)
