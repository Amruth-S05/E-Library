from .secret import Secret


class Config(Secret):  # inherited from Secret class
    DEBUG = True
    DEVELOPMENT = True
