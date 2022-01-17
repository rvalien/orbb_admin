from typing import cast

from flask import Flask
from flask_admin import Admin, AdminIndexView

from db import current_session
from db.utils import models


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['FLASK_ADMIN_SWATCH'] = 'Cosmo'
    app.secret_key = 'kek'

    admin = Admin(app, name='Orbb Admin', index_view=AdminIndexView(name='📃', url='/'), template_mode='bootstrap4')

    from admin.views.bot_views import BookClubView, ReactionView
    from admin.views.users import UsersView

    admin.add_view(UsersView(models.Users, current_session, name='дни рождения'))
    admin.add_view(BookClubView(models.BookClubDeadline, current_session, name='Книжный Клуб'))
    admin.add_view(ReactionView(models.AddReaction, current_session, name='Реакции Бота'))

    return cast(Flask, admin.app)


if __name__ == '__main__':
    from db import DBSettings

    DBSettings().setup_db()

    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
