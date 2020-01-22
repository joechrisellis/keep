from app import app, db
from app.mod_root.models import Link


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Link": Link,
    }


@app.context_processor
def inject_globals():
    return dict(
        sitename="Keep",
        general_contact_email="joechrisellis@gmail.com",
    )
