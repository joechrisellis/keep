from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
import config

app = Flask(__name__)
app.config.from_object("config.ProductionConfig")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
Markdown(app)

# Import blueprints
from app.mod_root.controllers import mod_root as root_module
from app.mod_self.controllers import mod_self as self_module
from app.mod_api.controllers import mod_api as api_module

# Register blueprints
app.register_blueprint(root_module)
app.register_blueprint(self_module)
app.register_blueprint(api_module)

from app import errors
