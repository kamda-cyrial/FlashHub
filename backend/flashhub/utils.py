from dotenv import load_dotenv
import os
import hashlib
from ecdsa import SigningKey, SECP256k1
from rest_framework.exceptions import ValidationError
import jwt
from social.models import Notification
from users.models import User, UserToken

#constants
JWT_ISSUER = "flashhub"
WAIT_DAYS_AFTER_FRIEND_REQUEST = 30

#helper functions
def get_jwt_keys():
    load_dotenv()
    passphrase = os.environ.get("KEY_PASSPHRASE")
    if not passphrase:
        raise ValueError("KEY_PASSPHRASE environment variable not set")
    passphrase_hash = hashlib.sha256(passphrase.encode()).digest()

    sk = SigningKey.from_string(passphrase_hash, curve=SECP256k1)
    vk = sk.verifying_key

    return sk.to_pem().decode("utf-8"), vk.to_pem().decode("utf-8")


def get_ecdsa_jwt_public_key():
    _, vk = get_jwt_keys()
    return vk

def get_valid_decoded_flashub_jwt(jwt_token):
    vk = get_ecdsa_jwt_public_key()
    try:
        return jwt.decode(jwt_token, vk, algorithms=["ES256"], verify=True, audience=JWT_ISSUER, issuer=JWT_ISSUER)
    except jwt.exceptions.ExpiredSignatureError:
        raise ValidationError("JWT has expired")
    except jwt.exceptions.InvalidSignatureError:
        raise ValidationError("Invalid JWT signature")
    except jwt.exceptions.InvalidIssuerError:
        raise ValidationError("Invalid JWT issuer")
    except jwt.exceptions.InvalidAudienceError:
        raise ValidationError("Invalid JWT audience")
    except jwt.exceptions.InvalidTokenError:
        raise ValidationError("Invalid JWT")
    
def get_request_jwt(request):
    request_jwt = request.headers.get('jwt')
    if not request_jwt:
        raise ValidationError("No JWT provided")
    
    if not UserToken.objects.get(token=request_jwt):
        raise ValidationError("Invalid JWT")
    return request_jwt

def get_validated_request_user(request):
    request_jwt = get_request_jwt(request)
    decoded_jwt = get_valid_decoded_flashub_jwt(request_jwt)
    user_id = decoded_jwt.get("user_id")
    user = User.objects.get(id=user_id)
    if not user:
        raise ValidationError("Invalid user")
    return user

def notify_user(user, message):
    nofitication = Notification(user=user, message=message)
    nofitication.save()
    return nofitication