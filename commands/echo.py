def execute(*args):
    """
    Echo back the provided arguments
    Usage: echo [text]
    """
    return " ".join(args) if args else "echo: No input provided"