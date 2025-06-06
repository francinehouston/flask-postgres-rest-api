# app.py

# Import the 'Flask' class from the 'flask' library.
from flask import Flask

# Initialize Flask
# We'll use the pre-defined global '__name__' variable to tell Flask where it is.
app = Flask(__name__)

# Define our route
# This syntax is using a Python decorator, which is essentially a 
# succinct way to wrap a function in another function.
@app.route('/')
def index():
  return "Hello, world!"

# Run our application, by default on port 5000
app.run()
