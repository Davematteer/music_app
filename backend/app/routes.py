from flask import Flask, Blueprint, jsonify

app = Blueprint("app",__name__)

@app.route('/')
def home():
    return jsonify({"message":"Welcome to the music app"})

@app.route('/trending')
def trending_music():
    return jsonify({"trending":["Song A","Song B"]})

