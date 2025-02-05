# Core_Modules/assessment_engine.py
import random

def generate_quiz():
    """
    Generates a simple quiz with dummy questions.
    """
    quiz = {
        "questions": [
            {"id": 1, "question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
            {"id": 2, "question": "What is the capital of France?", "options": ["Berlin", "London", "Paris"], "answer": "Paris"}
        ]
    }
    return quiz

def grade_quiz(answers):
    """
    Grades the quiz based on provided answers.
    Assumes answers is a dict {question_id: answer}.
    """
    correct_answers = {1: "4", 2: "Paris"}
    score = 0
    for qid, ans in answers.items():
        if correct_answers.get(int(qid)) == ans:
            score += 50  # For example, each question worth 50 points.
    return score
