from flask import Flask, render_template

import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return render_template('index.html')
    


    from routes.patients import auth
    app.register_blueprint(auth.userAuth)
    return app

if __name__ == '__main__':
    create_app().run(debug=True)
