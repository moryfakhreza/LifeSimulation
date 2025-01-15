from flask import Flask, render_template, request, jsonify
from character import Character
from education import Education
from career import Career
from relationships import Relationship
from events import random_event
from crime import commit_crime
from assets import buy_asset, sell_asset
from health import visit_doctor, plastic_surgery
from death import check_death

app = Flask(__name__)

# Global variables for simplicity
player = None
education = Education()
career = Career()
relationships = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_character', methods=['POST'])
def create_character():
    global player
    name = request.form['name']
    country = request.form.get('country', None)
    gender = request.form.get('gender', None)
    player = Character(name, country=country, gender=gender)
    return jsonify({"status": "Character created", "character": player.__dict__})

@app.route('/age_up', methods=['POST'])
def age_up():
    global player
    player.age_up()
    if check_death(player):
        return jsonify({"status": "Character has died", "character": player.__dict__})
    return jsonify({"status": "Aged up", "character": player.__dict__})

@app.route('/random_event', methods=['POST'])
def random_event_route():
    global player
    random_event(player)
    return jsonify({"status": "Random event occurred", "character": player.__dict__})

@app.route('/education', methods=['POST'])
def education_route():
    global player
    education.choose_school(player.age)
    return jsonify({"status": "Education updated", "education": education.__dict__})

@app.route('/career', methods=['POST'])
def career_route():
    global player
    career.choose_career(player.age)
    return jsonify({"status": "Career updated", "career": career.__dict__})

@app.route('/relationships', methods=['POST'])
def relationships_route():
    global relationships
    relation_name = request.form['relation_name']
    relation_type = request.form['relation_type']
    relationships.append(Relationship(relation_name, relation_type))
    return jsonify({"status": "Relationship added", "relationships": [rel.__dict__ for rel in relationships]})

@app.route('/crime', methods=['POST'])
def crime_route():
    global player
    commit_crime(player)
    return jsonify({"status": "Crime committed", "character": player.__dict__})

@app.route('/assets', methods=['POST'])
def assets_route():
    global player
    action = request.form['action']
    asset_name = request.form['asset_name']
    value = int(request.form['value'])
    if action == 'buy':
        buy_asset(player, asset_name, value)
    elif action == 'sell':
        sell_asset(player, asset_name, value)
    return jsonify({"status": "Asset transaction completed", "character": player.__dict__})

@app.route('/health', methods=['POST'])
def health_route():
    global player
    action = request.form['action']
    if action == 'visit_doctor':
        visit_doctor(player)
    elif action == 'plastic_surgery':
        plastic_surgery(player)
    return jsonify({"status": "Health action completed", "character": player.__dict__})

if __name__ == '__main__':
    app.run(debug=True)