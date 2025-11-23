from flask import Flask, render_template, request, redirect, url_for, session
import json
import os
from datetime import datetime
import random


DATA_FILE = "mood_data.json"

def load_history():
    """Load mood data safely."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        print("Error loading mood data - resetting to empty list.")
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
        return []
    

def save_history(data):
    """Save mood data safely."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


app = Flask(__name__)

app.secret_key = "supersecretkey123"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mood', methods=['POST'])
def mood():
    mood = request.form.get('mood')
    reflection = request.form.get('reflection', '')
    response = {
        "happy": [
            "That's awesome! Keep smiling. You are incredible.",
            "Your happiness is contagious. You should share it today.",
            "You deserve this joy. Keep soaking it in.",
            "A happy heart is the best reflection of peace. You deserve it."
        ],
        "calm": [
            "Embrace your peace and enjoy the moment. Your peace is powerful.",
            "Stillness looks great on you. Take a deep breath and give yourself the love you deserve.",
            "You're centered and composed. Keep protecting that peace.",
            "Peace ia your superpower today."
        ],
        "anxious": [
            "You are human. It's okay to feel how you are feeling.",
            "Your thoughts do not define you. This moment will pass.",
            "Pause, breathe, and remember your strength. You've got this.",
            "Even when your mind races, your heart knows the truth. You're safe."
        ],
        "sad": [
            "It's okay to feel vulnerable. Your value has not decreased.",
            "Some days are heavy but you are learning resilience.",
            "Tears mean you've cared deeply. That's strength, not weakness.",
            "Let yourself rest. Better days are always ahead."
        ],
        "motivated": [
            "Amazing! Use that energy to be kind to yourself, celebrate youself, and love others.",
            "You're unstoppable! Make something happen today.",
            "Your drive is inspiring. Keep that fire alive.",
            "Every small action you take today moves you closer to greatness."
        ],
        "tired": [
            "You've been doing your best. It's okay to slow down.",
            "Rest isn't a reward. It's something that's significant and important for you.",
            "Take a break. You'll future self will thank you for it.",
            "Just recharge today so tomorrow feels a lot lighter."
        ],
        "grateful": [
            "A grateful heart changes everything. You should hold onto that peace.",
            "You noticed the beauty. That's incredible mindfulness.",
            "Gratitude attracts more incredible things towards you.",
            "Keep counting your blessings, they are meant for you"
        ],
        "angry": [
            "It's okay to feel frustrated right now. It means you cared deeply and you're stronger than your situation. Sooner or later others will start accepting you.",
            "Breathe through it. You can respond, but be respectful focus on resolving the issue.",
            "Your emotions are extremely valid; channel them into something productive.",
            "Calm minds make powerful decisions. Just give yourself time."
        ],
        "confident": [
            "You are radiating strength! Keep trusting yourself.",
            "Confidence looks amazing on you. Own it!",
            "You've got everything you need within you.",
            "Walk like you already are who you are meant to be. This is your story and your moment."
        ]

    }

    history = load_history()
    timestamp = datetime.now().strftime("%I:%M %p")
    history.append([mood, timestamp, reflection])
    save_history(history)

    message = random.choice(response.get(mood, ["Thank you for sharing."]))
    return render_template('result.html', message=message, mood=mood)

@app.route('/history_data')
def history_data():
    """Return mood data as JSON for the live chart"""
    data = load_history()
    return json.dumps(data)


@app.route('/history')
def history():
    data = load_history() 
    fixed = []
    for entry in data:
        if isinstance(entry, list):
            if len(entry) == 3:
                mood, timestamp, reflection = entry
            elif len(entry) == 2:
                mood, timestamp = entry
                refelction = ""
            else:
                continue
            fixed.append((mood, timestamp, reflection))
    
    return render_template('history.html', history=fixed)

@app.route('/clear_history', methods=['POST'])
def clear_history():
    save_history([])
    return ("OK", 200)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/search")
def search():
    query = request.args.get("q", "").lower()

    history = load_history()

    results = []
    for mood, time, reflection in history:
        if query in mood.lower() or query in reflection.lower():
            results.append((mood, time, reflection))
    return render_template("search.html", results=results, query=query)

from flask import send_file

@app.route("/export")
def export_history():
    """Download mood history as a JSON file."""

    history = load_history()

    export_filename = "mood_export.json"

    with open(export_filename, "w") as f:
        json.dump(history, f, indent=4)

    return send_file(export_filename, as_attachment=True)
    
if __name__ == '__main__':
    app.run(debug=True)