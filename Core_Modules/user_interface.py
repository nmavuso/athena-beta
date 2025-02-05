# Core_Modules/user_interface.py
from flask import Blueprint, request, jsonify
from Core_Modules.assessment_engine import generate_quiz, grade_quiz
from Core_Modules.learning_engine import adjust_learning_path
from Core_Modules.communication_engine import send_notification
from Core_Modules.nlp_engine import process_text

ui_blueprint = Blueprint('ui', __name__, template_folder='templates')

@ui_blueprint.route('/')
def home():
    return "Welcome to Athena - Your AI Teaching Assistant"

@ui_blueprint.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_message = request.json.get('message')
        # Process the message using the NLP engine (stub)
        response = process_text(user_message)
        return jsonify({'response': response})
    return "Chat interface (POST your messages to get responses)"

@ui_blueprint.route('/quiz', methods=['GET'])
def quiz():
    quiz_data = generate_quiz()
    return jsonify(quiz_data)

@ui_blueprint.route('/grade', methods=['POST'])
def grade():
    answers = request.json.get('answers')
    score = grade_quiz(answers)
    # Adjust the learning path based on performance (stub)
    adjust_learning_path(score)
    send_notification("Quiz graded. Score: {}".format(score))
    return jsonify({'score': score})
