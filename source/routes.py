#Routing and view functions
from source import app


@app.route('/')
def home():
    return 'Welcome to the library management system!'