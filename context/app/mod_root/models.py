from urllib.parse import urlparse
from app import db
from app.database import Base


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

    def get_tags(self):
        return (
            [tag.strip() for tag in self.tags.split(",")] if self.tags else []
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
