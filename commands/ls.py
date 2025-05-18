import os

def execute(*args):
    """
    List files in the current directory or specified directory
    Usage: ls [directory]
    """
    try:
        path = args[0] if args else "."
        files = os.listdir(path)
        return "\n".join(files) if files else "No files found"
    except Exception as e:
        return f"Error: {str(e)}"