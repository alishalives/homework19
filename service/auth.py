import base64
import hashlib
import hmac
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class AuthService:
    def compare_passwords(self, hash_password, user_password):
        return hmac.compare_digest(
            base64.b64decode(hash_password),
            hashlib.pbkdf2_hmac(
                "sha256",
                user_password.encode("utf-8"),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            )
        )



