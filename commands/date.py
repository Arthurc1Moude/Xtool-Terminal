import datetime

def execute(*args):
    """
    Display the current date and time
    Usage: date
    """
    now = datetime.datetime.now()
    return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"