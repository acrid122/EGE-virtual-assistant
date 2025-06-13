from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

@app.route("/")
def index():
    return {"message": "EGE Virtual Assistant Backend"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)