# Core_Modules/knowledge_base.py
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'User_Data')

def load_student_profiles():
    path = os.path.join(DATA_DIR, 'student_profiles.json')
    with open(path, 'r') as f:
        return json.load(f)

def load_instructor_profiles():
    path = os.path.join(DATA_DIR, 'instructor_profiles.json')
    with open(path, 'r') as f:
        return json.load(f)

def get_course_content(course_id):
    # Dynamically load course-specific content
    if course_id == 'Course_A':
        from Course_Specific_Modules.Course_A import course_content
        return course_content.get_content()
    elif course_id == 'Course_B':
        from Course_Specific_Modules.Course_B import course_content
        return course_content.get_content()
    else:
        return {}
