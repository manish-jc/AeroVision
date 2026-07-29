import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

TOKEN_URL = (
    "https://auth.opensky-network.org/auth/realms/opensky-network/"
    "protocol/openid-connect/token"
)


def get_access_token():
    """
    Authenticate with OpenSky and return an OAuth2 access token.
    """

    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    response = requests.post(TOKEN_URL, data=payload)

    if response.status_code == 200:
        token = response.json()["access_token"]
        print("✅ Authentication Successful!")
        return token

    print("❌ Authentication Failed!")
    print("Status Code:", response.status_code)
    print(response.text)
    return None


# Test authentication
if __name__ == "__main__":
    token = get_access_token()

    if token:
        print("\nAccess Token (first 50 chars):")
        print(token[:50] + "...")