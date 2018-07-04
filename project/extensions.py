from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

debug_toolbar = DebugToolbarExtension()
csrf = CSRFProtect()
db = SQLAlchemy()
ma = Marshmallow()
