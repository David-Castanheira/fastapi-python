from jwt import decode 
from utils.security import SECRET_KEY, create_access_token

def test_token_jwt():
    data = {'password': 'password'}
    token = create_access_token(data)

    jwt_decoded = decode(token, SECRET_KEY, algorithms=['HS256'])

    assert jwt_decoded['password'] == data['password']
    assert 'expire' in jwt_decoded