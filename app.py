import os
import importlib.util
import sys
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary to store all available commands
commands = {}

def load_commands():
    """Load all command modules from the commands directory"""
    commands_dir = os.path.join(os.path.dirname(__file__), 'commands')
    
    # Ensure commands directory exists
    if not os.path.exists(commands_dir):
        os.makedirs(commands_dir)
    
    # Get all Python files in the commands directory
    command_files = [f for f in os.listdir(commands_dir) 
                    if f.endswith('.py') and not f.startswith('__')]
    
    # Load each command module
    for command_file in command_files:
        command_name = command_file[:-3]  # Remove .py extension
        module_path = os.path.join(commands_dir, command_file)
        
        try:
            # Load the module
            spec = importlib.util.spec_from_file_location(command_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Check if the module has the required execute function
            if hasattr(module, 'execute'):
                commands[command_name] = module.execute
                print(f"Loaded command: {command_name}")
            else:
                print(f"Warning: Command {command_name} does not have an execute function")
        except Exception as e:
            print(f"Error loading command {command_name}: {str(e)}")

@app.route('/')
def index():
    """Render the main terminal interface"""
    return render_template('index.html', commands=list(commands.keys()))

@app.route('/execute', methods=['POST'])
def execute_command():
    """Execute a command and return the result"""
    data = request.json
    command_input = data.get('command', '').strip()
    
    if not command_input:
        return jsonify({'output': 'Please enter a command'})
    
    # Parse the command and arguments
    parts = command_input.split()
    command_name = parts[0]
    args = parts[1:] if len(parts) > 1 else []
    
    # Check if the command exists
    if command_name in commands:
        try:
            result = commands[command_name](*args)
            return jsonify({'output': result})
        except Exception as e:
            return jsonify({'output': f"Error executing command: {str(e)}"})
    elif command_name == "help":
        return jsonify({'output': "Available commands: " + ", ".join(list(commands.keys()))})
    else:
        return jsonify({'output': f"Command not found: {command_name}. Type 'help' to see available commands."})

if __name__ == '__main__':
    # Load all commands
    load_commands()
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)