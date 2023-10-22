from flask_app import create_app
from flask_app import exc_celery

app = create_app()
app.app_context().push()

celery = exc_celery.celery

# if __name__ == '__main__':
#     app.run(port=5001)
