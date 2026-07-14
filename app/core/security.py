from passlib.context import CryptContext 

# imoport CryptContext from passlib.context 

# this is a password hashing context that uses the bcrypt algorithm to hash passwords. The deprecated parameter is set to "auto" to automatically handle any deprecated algorithms.
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
# this function takes a password as input and returns the hashed version of the password using the bcrypt algorithm.
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# this function takes a plain password and a hashed password as input and returns a boolean indicating whether the plain password matches the hashed password.
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
