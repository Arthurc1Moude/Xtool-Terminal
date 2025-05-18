import os
import re

def execute(*args):
    """
    Add a new custom command
    Usage: addcmd name "command_code"
    Example: addcmd greet "def execute(*args):\\n    name = args[0] if args else 'World'\\n    return f'Hello, {name}!'"
    """
    if len(args) < 2:
        return "Usage: addcmd name \"command_code\"\nThe command_code must include a function named 'execute'."
    
    cmd_name = args[0]
    # Join the rest of the arguments as the command code
    cmd_code = " ".join(args[1:])
    
    # Validate command name
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', cmd_name):
        return "Error: Command name must start with a letter and contain only letters, numbers, and underscores."
    
    # Check if the command already exists
    commands_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'commands')
    cmd_path = os.path.join(commands_dir, f"{cmd_name}.py")
    
    if os.path.exists(cmd_path):
        return f"Error: Command '{cmd_name}' already exists."
    
    # Validate that the code contains an execute function
    if "def execute" not in cmd_code:
        return "Error: Command code must include a function named 'execute'."
    
    try:
        # Write the command file
        with open(cmd_path, 'w') as f:
            f.write(cmd_code)
        
        return f"Command '{cmd_name}' added successfully. Restart the server to use it."
    except Exception as e:
        return f"Error creating command: {str(e)}"