# Xtool CMD - Web Terminal

A stylish web-based terminal application with custom commands and extensive CSS styling.

## Features

- Web-based terminal interface with rich styling
- Custom command system with easy extensibility
- Command history and tab completion
- Matrix-style background animation
- Responsive design for different screen sizes

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Available Commands

- `hello [name]` - Greet the user
- `echo [text]` - Echo back the provided text
- `ls [directory]` - List files in a directory
- `date` - Display the current date and time
- `calc [expression]` - Simple calculator
- `weather [city]` - Display simulated weather information
- `addcmd [name] [code]` - Add a new custom command

## Creating Custom Commands

You can add custom commands in two ways:

1. Create a Python file in the `commands` directory with an `execute` function:

```python
# commands/mycommand.py
def execute(*args):
    """
    My custom command
    Usage: mycommand [args]
    """
    return "This is my custom command output"
```

2. Use the `addcmd` command in the terminal:

```
addcmd greet "def execute(*args):\n    name = args[0] if args else 'World'\n    return f'Hello, {name}!'"
```

After adding a new command, restart the server to use it.

## License

MIT License