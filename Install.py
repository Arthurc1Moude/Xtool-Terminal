#!/usr/bin/env python3
"""
Xtool CMD Web Terminal Installer
This script installs Xtool CMD, a web-based terminal with custom commands.
"""

import os
import sys
import platform
import subprocess

class XtoolInstaller:
    def __init__(self):
        self.app_name = "Xtool CMD"
        self.version = "1.0.0"
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        self.commands_dir = os.path.join(self.project_dir, 'commands')
        self.static_dir = os.path.join(self.project_dir, 'static')
        self.templates_dir = os.path.join(self.project_dir, 'templates')
        
    def run_installation(self):
        """Run the installation process"""
        self.print_welcome()
        
        # Check Python version
        self.check_python_version()
        
        # Create required directories if they don't exist
        self.create_directories()
        
        # Install dependencies
        self.install_dependencies()
        
        # Set file permissions
        self.set_permissions()
        
        # Print success message
        self.print_success()
    
    def print_welcome(self):
        """Print welcome message"""
        print(f"{'='*60}")
        print(f"{self.app_name} Web Terminal Installer v{self.version}".center(60))
        print(f"{'='*60}")
        print("This installer will set up Xtool CMD Web Terminal on your system.")
        print("It will create necessary directories and install required dependencies.")
        print(f"{'='*60}\n")
    
    def check_python_version(self):
        """Check if Python version is compatible"""
        print("Checking Python version...")
        major, minor = sys.version_info[:2]
        if major < 3 or (major == 3 and minor < 6):
            print("Error: Python 3.6 or higher is required.")
            sys.exit(1)
        print(f"Python {major}.{minor} detected. ✓\n")
    
    def create_directories(self):
        """Create required directories if they don't exist"""
        print("Creating required directories...")
        
        directories = [
            self.commands_dir,
            self.static_dir,
            os.path.join(self.static_dir, 'css'),
            os.path.join(self.static_dir, 'js'),
            self.templates_dir
        ]
        
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Created directory: {directory}")
            else:
                print(f"Directory already exists: {directory}")
        
        print("All directories created successfully. ✓\n")
    
    def install_dependencies(self):
        """Install required Python dependencies"""
        print("Installing required dependencies...")
        
        requirements_file = os.path.join(self.project_dir, 'requirements.txt')
        
        if not os.path.exists(requirements_file):
            print("Error: requirements.txt not found.")
            sys.exit(1)
        
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
            print("Dependencies installed successfully. ✓\n")
        except subprocess.CalledProcessError:
            print("Error: Failed to install dependencies.")
            sys.exit(1)
    
    def set_permissions(self):
        """Set executable permissions for the main script"""
        print("Setting file permissions...")
        
        app_script = os.path.join(self.project_dir, 'app.py')
        
        if platform.system() != "Windows":
            try:
                os.chmod(app_script, 0o755)
                print(f"Set executable permission for {app_script}")
            except Exception as e:
                print(f"Warning: Could not set permissions: {str(e)}")
        
        print("File permissions set. ✓\n")
    
    def print_success(self):
        """Print success message with instructions"""
        print(f"{'='*60}")
        print(f"Installation Completed Successfully!".center(60))
        print(f"{'='*60}")
        print("\nTo start Xtool CMD Web Terminal, run:")
        print(f"  cd \"{self.project_dir}\" && python app.py")
        print("\nThen open your web browser and navigate to:")
        print("  http://localhost:5000")
        print("\nEnjoy your new web terminal!")
        print(f"{'='*60}\n")

if __name__ == "__main__":
    installer = XtoolInstaller()
    installer.run_installation()