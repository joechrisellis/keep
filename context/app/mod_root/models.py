from urllib.parse import urlparse
from app import db
from app.database import Base


class Link(Base):
    """Shared link."""

    __tablename__ = "link"

    title = db.Column(db.String(256), index=True, nullable=False)
    url = db.Column(db.String(512), index=True, nullable=False)

    def parse_url(self):
        try:
            return urlparse(self.url)
        except:
            return None

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
