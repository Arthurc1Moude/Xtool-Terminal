# Xtool CMD - Web Terminal

A stylish web-based terminal application with custom commands and extensive CSS styling.

## Features

- Web-based terminal interface with rich styling
- Custom command system with easy extensibility
- Command history and tab completion
- Matrix-style background animation
- Responsive design for different screen sizes

## Installation

### Solution 1: Universal installation

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

### Solution 2: Adaptive installation

1. Clone this repository
2. Install the Pyinstaller:

```bash
pip install pyinstaller
```
3. You may have the `build.spec`, if you don't then you may have to create one:

```spec
# -*- mode: python -*-

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('static', 'static'),
        ('templates', 'templates'),
        ('commands', 'commands')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='YourApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 改为 False 可隐藏控制台
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```
4. Execute packaging:

```bash
pyinstaller build.spec
```

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
