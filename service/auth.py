import hashlib
import hmac
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class AuthService:
    def compare_passwords(self, password_hash, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")

        return hmac.compare_digest(password_hash, hash_digest)

