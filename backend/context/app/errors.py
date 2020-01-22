from flask import current_app, render_template, request
from app import app

error_messages = {
    403: ("Sorry!", "You're not allowed to access this resource."),
    404: ("Oops!", "Looks like that page doesn't exist."),
}


@app.errorhandler(403)  # unauthorised
@app.errorhandler(404)  # not found
def error(flask_error):

    err = error_messages.get(
        flask_error.code, ("Oops!", "Something went wrong!")
    )
    return (
        render_template(
            "error.html",
            pagetitle=flask_error.code,
            flask_error=flask_error,
            error_msg=err,
        ),
        flask_error.code,
    )
