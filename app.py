import os

from flask import send_from_directory

from application import app, jwt, socketio
from application.api import *
from application.models import User

EXEC_ENV = os.environ.get('EXEC_ENV')

# BLUEPRINT REGISTRATION
app.register_blueprint(auth_blueprint, url_prefix='/auth')


@jwt.user_lookup_loader
def _user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    # Retrieve the user object based on the identity (user ID)
    user = User.query.filter_by(id=identity).first()
    return user


if __name__ == '__main__':
    # socketio.run(app, host='0.0.0.0', port=2000, debug=True)
    app.run(host='0.0.0.0', port=8000, debug=True)
    # app.run(port=5000, debug=True)
