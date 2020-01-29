from flask import current_app, Blueprint, render_template, abort
from app.mod_root.models import Link
from http import HTTPStatus

# Define blueprint.
mod_discuss = Blueprint("discuss", __name__, url_prefix="/discuss")


@mod_discuss.route("/<post_id>")
def discuss(post_id):
    """Discuss a link."""
    the_link = Link.query.filter_by(id=post_id).first()

    if not the_link:
        abort(HTTPStatus.NOT_FOUND)

    return render_template(
        "discuss.html", title=the_link.title, the_link=the_link
    )
