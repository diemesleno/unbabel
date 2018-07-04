from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

debug_toolbar = DebugToolbarExtension()
csrf = CSRFProtect()
db = SQLAlchemy()
