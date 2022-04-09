from flask import Flask

application = Flask(__name__)

application.secret_key = "Utn34dfRgfdi23"
application.config['SESSION_COOKIE_NAME'] = 'User Cookie'


@application.route('/')
def index():
	return "Hello Kevin, Vinayak, Guo, and Jack! This is additional message. We have now updated with Git. boom!"

# Notes: pip freeze > requirements.txt to get requirements for project
# database username: admin password: CSDS341_Database


if __name__ == '__main__':
	application.run(port=5000, debug=True)