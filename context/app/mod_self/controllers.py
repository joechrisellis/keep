from flask import current_app, Blueprint, render_template, abort
from http import HTTPStatus
from werkzeug.utils import secure_filename
import os

# Define blueprint.
mod_self = Blueprint("self", __name__, url_prefix="/self")


@mod_self.route("/<post_name>")
def self_post(post_name):
    """Visit a self post."""

    try:
        secure_post_name = secure_filename(post_name)
        secure_post_name += ".md"
        the_post_path = os.path.join(
            current_app.config["POSTS_DIR"], secure_post_name
        )
        
        with open(the_post_path) as the_post:
            post_md = the_post.read()
    except FileNotFoundError:
        abort(HTTPStatus.NOT_FOUND)

    title = post_md.split("\n")[0]
    return render_template("self.html", title=title, post_md=post_md)
