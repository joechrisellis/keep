from flask import current_app, Blueprint, jsonify, make_response
from app.mod_root.models import Link

# Define blueprint.
mod_api = Blueprint("api", __name__, url_prefix="/api")


@mod_api.route("/export/json")
def export_json():
    json_links = [
        link.to_dictionary()
        for link in Link.query.order_by(Link.created_on.desc()).all()
    ]
    return jsonify(json_links)


@mod_api.route("/export/text")
def export_text():
    text_links = [
        str(link) for link in Link.query.order_by(Link.created_on.desc()).all()
    ]

    response = make_response("\n".join(text_links), 200)
    response.mimetype = "text/plain"
    return response
