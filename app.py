
from flask import Flask, render_template, request, jsonify
from database import Database
import os

app = Flask(__name__)
db = Database()

# Routes for web interface
@app.route('/')
def index():
    return render_template('index.html')

# API Routes
@app.route('/api/notes', methods=['GET', 'POST'])
def handle_notes():
    if request.method == 'POST':
        content = request.json.get('content')
        return jsonify(db.create_note(content))
    return jsonify(db.get_all_notes())

@app.route('/api/notes/<int:note_id>', methods=['GET', 'DELETE'])
def handle_note(note_id):
    if request.method == 'DELETE':
        return jsonify(db.delete_note(note_id))
    return jsonify(db.get_note(note_id))

if __name__ == '__main__':
    app.run(debug=True)