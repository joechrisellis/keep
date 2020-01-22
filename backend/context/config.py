import os


class Config:
    """Base configuration."""

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PUBLIC_DIR = os.path.join("/", "usr", "src", "app", "public")
    POSTS_DIR = os.path.join(PUBLIC_DIR, "selfposts")

    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    HASHED_PIN = os.environ.get("HASHED_PIN")

    # Database related.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LINKS_PER_PAGE = 20


class ProductionConfig(Config):
    """Production configuration."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        Config.PUBLIC_DIR, "app.db"
    )

    # Application threads. A common general assumption is using 2 per available
    # processor cores - to handle incoming requests using one and performing
    # background operations using the other.
    THREADS_PER_PAGE = 2


class DebugConfig(Config):
    """Debug configuration."""

    DEBUG = True

    PUBLIC_DIR = os.path.join(Config.BASE_DIR, "public")
    POSTS_DIR = os.path.join(PUBLIC_DIR, "selfposts")

    # Database related.
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(PUBLIC_DIR, "app.db")
