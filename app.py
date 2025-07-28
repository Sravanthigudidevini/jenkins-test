from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    """Returns a simple greeting."""
    return "Hello, World! This is a sample Python application running in a Docker container."

if __name__ == "__main__":
    # The app runs on port 5000 by default.
    # Docker will map this port to a port on the host machine.
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)