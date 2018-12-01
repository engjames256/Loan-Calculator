from app.views import app
from flask import Flask, jsonify, request


if __name__ == "__main__":
    app.run(debug=True,port=8080)
