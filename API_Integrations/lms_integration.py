# API_Integrations/lms_integration.py
import requests

def send_grade_to_canvas(student_id, course_id, grade):
    """
    Sends grade information to a Canvas LMS.
    This stub simply prints the action.
    """
    print(f"Sending grade {grade} for {student_id} in {course_id} to Canvas.")
    # In a real system, use requests.post() with the proper endpoint and authentication.
    return True
