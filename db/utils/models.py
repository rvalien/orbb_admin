import sqlalchemy as sa

from db.utils.base import BaseTable


class Users(BaseTable):
    """Данные о пользователе"""
    discord_id = sa.Column(sa.Integer, nullable=False, unique=True, doc='discord id пользователя')
    user_name = sa.Column(sa.Text, nullable=False, doc='имя пользователя')
    birth_date = sa.Column(sa.Date, nullable=False, doc='Дата рождения')


class BookClubDeadline(BaseTable):
    """Данные о дате обсуждения книг в книжном клубе."""
    deadline = sa.Column(sa.Date, nullable=True, doc='день обсуждения')
    book_name = sa.Column(sa.String, nullable=True, doc='Выбранная книга')


class AddReaction(BaseTable):
    trigger = sa.Column(sa.String, nullable=False, doc='триггер слово')
    reaction_list = sa.Column(sa.String, nullable=True, doc='реакции')
