"""Views."""

from flask_admin.contrib.sqla import ModelView


class UsersView(ModelView):
    """User view."""

    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = ["discord_id", "user_name", "birth_date"]

    column_sortable_list = ["birth_date"]

    edit_template = "user_edit.html"
