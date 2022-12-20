from flask import Flask
import os

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__, static_url_path='/static')

app.run(host='0.0.0.0', port=port)


from app import routes