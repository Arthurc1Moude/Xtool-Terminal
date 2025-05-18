def execute(*args):
    """
    A simple hello command that greets the user
    Usage: hello [name]
    """
    if args:
        return f"Hello, {' '.join(args)}! Welcome to Xtool CMD Terminal."
    else:
        return "Hello, World! Welcome to Xtool CMD Terminal."