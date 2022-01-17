"""Определение представлений."""

from flask_admin.contrib.sqla import ModelView


class BookClubView(ModelView):
    """Представление для отображения дедлайна книжного клуба."""

    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = ["deadline", "book_name"]
    column_sortable_list = ["deadline"]


class ReactionView(ModelView):
    """Представление для отображения реакций в виде emoji на определённые сообщения."""

    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = ["trigger", "reaction_list"]


class ActivityListView(ModelView):
    """Отображение списка активностей бота."""

    can_edit = True
    can_create = False
    can_delete = True
    can_view_details = True

    form_columns = [
        "activity",
    ]
