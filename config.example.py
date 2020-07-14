MODE = "Development"


class Config():
    REGISTRATIONS_ENABLED = False
    OAUTH2_REFRESH_TOKEN_GENERATOR = True
    DEBUG_MODE = False
    POSTGRES_CREDENTIALS = {}


class Development(Config):
    DEBUG_MODE = True
    POSTGRES_HOST = "raspberry"
    POSTGRES_USER = "raspberry"
    POSTGRES_PASSWORD = "raspberry"
    POSTGRES_DB = "raspberry"


class Production(Config):
    REGISTRATIONS_ENABLED = True
    POSTGRES_HOST = "raspberry"
    POSTGRES_USER = "raspberry"
    POSTGRES_PASSWORD = "raspberry"
    POSTGRES_DB = "raspberry"
