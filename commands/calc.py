def execute(*args):
    """
    Simple calculator
    Usage: calc expression
    Example: calc 2+2
    """
    if not args:
        return "Usage: calc <expression>\nExample: calc 2+2"
    
    try:
        # Join all arguments to handle expressions with spaces
        expression = ''.join(args)
        # Evaluate the expression (with safety restrictions)
        result = eval(expression, {"__builtins__": {}}, {})
        return f"{expression} = {result}"
    except Exception as e:
        return f"Error: {str(e)}"