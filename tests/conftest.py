import pytest
from fastapi_jwt_auth2 import AuthJWT

@pytest.fixture(scope="module")
def Authorize():
    return AuthJWT()
