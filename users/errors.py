import enum


class Errors(enum.Enum):
    AUTH_USER_MISMATCH = "This login cannot be used here"
    AUTH_USER_NOT_FOUND = "Auth User not found"
    AUTH_USER_INACTIVE = "This user can not be authenticated"
    PASSWORDS_MUST_MATCH = "Passwords must match"
