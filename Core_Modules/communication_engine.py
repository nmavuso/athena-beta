# Core_Modules/communication_engine.py
def send_notification(message, user_id=None):
    """
    Sends a notification to a user.
    In this stub, we simply print the notification.
    """
    recipient = user_id if user_id else "all users"
    print(f"Notification sent to {recipient}: {message}")

def send_message(sender, recipient, message):
    """
    Facilitates sending a message between users.
    """
    print(f"Message from {sender} to {recipient}: {message}")
