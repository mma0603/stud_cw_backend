from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from internal.config import settings
from internal.config.database import current_session
from internal.entity import feedback, order, product, user


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(settings)

    admin = Admin(
        app=app,
        url='/',
        name='Admin',
        template_mode='bootstrap4',
    )
    admin.add_view(ModelView(user.User, current_session))
    admin.add_view(ModelView(order.Order, current_session))
    admin.add_view(ModelView(product.Product, current_session))
    admin.add_view(ModelView(feedback.Feedback, current_session))
    admin.add_view(ModelView(product.ProductType, current_session))

    return app
