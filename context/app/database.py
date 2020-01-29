from app import db


class Base(db.Model):
    """Base model for all other database models to inherit from."""

    # Special directive; tells SQLAlchemy not to create a table for this
    # particular model, allowing us to use it for inheritance.
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now()
    )
