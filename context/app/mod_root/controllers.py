from flask import (
    current_app,
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)
from werkzeug.security import check_password_hash
from app.mod_root.forms import SubmitForm
from app.mod_root.models import Link
from app import db

# Define blueprint.
mod_root = Blueprint("root", __name__)


@mod_root.route("/", methods=["GET", "POST"])
@mod_root.route("/index", methods=["GET", "POST"])
def index():
    """Main index page showing companies/jobs."""

    page = request.args.get("page", 1, type=int)
    links = Link.query.order_by(Link.created_on.desc()).paginate(
        page, current_app.config["LINKS_PER_PAGE"], False
    )
    next_url = (
        url_for("root.index", page=links.next_num) if links.has_next else None
    )
    prev_url = (
        url_for("root.index", page=links.prev_num) if links.has_prev else None
    )

    return render_template(
        "index.html",
        page=page,
        links_per_page=current_app.config["LINKS_PER_PAGE"],
        links=links.items,
        next_url=next_url,
        prev_url=prev_url,
    )


@mod_root.route("/submit", methods=["GET", "POST"])
def submit():
    """Submit page where a new link can be submitted."""

    form = SubmitForm(request.form)

    # If the submit form was submitted...
    if form.validate_on_submit():
        pin_guess = form.pin.data
        if not check_password_hash(current_app.config["HASHED_PIN"], pin_guess):
            flash("Invalid PIN.")
            return redirect(url_for("root.submit"))

        new_link = Link(title=form.title.data, url=form.url.data)
        db.session.add(new_link)
        db.session.commit()

        flash("Successful submission!")
        return redirect(url_for("root.index"))

    return render_template("submit.html", title="Submit", form=form)


@mod_root.route("/about")
def about():
    return render_template("about.html", title="About")


@mod_root.route("/why-is-the-page-so-basic")
def why_is_the_page_so_basic():
    return render_template(
        "why-is-the-page-so-basic.html", title="Why is the page so basic?"
    )

@mod_root.route("/export-links")
def export_links():
    return render_template(
        "export-links.html", title="Export Links"
    )
