from . import admin


@admin.route('/admin')
def index():
    return "<h1>admin</h1>"