import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Heroku!"

if __name__ == "__main__":
    # app.run(debug=True)
    port = int(os.inviron.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)