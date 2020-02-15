from app import db
from app.database import Base
from sqlalchemy.ext.hybrid import hybrid_property
from urllib.parse import urlparse


class Link(Base):
    """Shared link."""

    __tablename__ = "link"

    title = db.Column(db.String(256), index=True, nullable=False)
    url = db.Column(db.String(512), index=True, nullable=False)
    tags = db.Column(db.String(512))

    def parse_url(self):
        try:
            return urlparse(self.url)
        except:
            return None

    @hybrid_property
    def link_tags(self):
        return (
            [tag.strip() for tag in self.tags.split(",")] if self.tags else []
        )

    @link_tags.expression
    def link_tags(cls):
        return (
            [tag.strip() for tag in cls.tags.split(",")] if cls.tags else []
        )

    def to_dictionary(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "created_on": self.created_on,
        }

    def __str__(self):
        return "{} ({}) - submitted {}".format(
            self.title, self.url, self.created_on
        )
