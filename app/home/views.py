from . import home


@home.route('/')
def index():
    return "<h1>home</h1>"
