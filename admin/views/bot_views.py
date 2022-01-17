from flask_admin.contrib.sqla import ModelView


class BookClubView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = ['deadline', 'book_name']
    column_sortable_list = ['deadline']


class ReactionView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = [
        'trigger',
        'reaction_list'
    ]


class ActivityListView(ModelView):
    can_edit = True
    can_create = False
    can_delete = True
    can_view_details = True

    form_columns = [
        'activity',
    ]
