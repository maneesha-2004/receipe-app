#!/usr/bin/env python3
"""
Setup script for the Recipe Management Application
This script helps you set up and run the application
"""

import os
import sys
import subprocess
import platform

def run_command(command, cwd=None):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=True, check=True, cwd=cwd, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def setup_backend():
    """Set up the Flask backend"""
    print("\n🔧 Setting up Flask Backend...")
    
    # Check if backend directory exists
    if not os.path.exists('backend'):
        print("❌ Backend directory not found")
        return False
    
    # Create virtual environment
    print("Creating virtual environment...")
    success, output = run_command('python -m venv venv', cwd='backend')
    if not success:
        print(f"❌ Failed to create virtual environment: {output}")
        return False
    
    # Activate virtual environment and install dependencies
    if platform.system() == "Windows":
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    print("Installing Python dependencies...")
    success, output = run_command(f'{pip_cmd} install -r requirements.txt', cwd='backend')
    if not success:
        print(f"❌ Failed to install dependencies: {output}")
        return False
    
    print("✅ Backend setup completed")
    return True

def setup_frontend():
    """Set up the React frontend"""
    print("\n🔧 Setting up React Frontend...")
    
    # Check if frontend directory exists
    if not os.path.exists('frontend'):
        print("❌ Frontend directory not found")
        return False
    
    # Check if Node.js is installed
    success, output = run_command('node --version')
    if not success:
        print("❌ Node.js is not installed. Please install Node.js first.")
        return False
    
    print(f"✅ Node.js {output.strip()} detected")
    
    # Install npm dependencies
    print("Installing npm dependencies...")
    success, output = run_command('npm install', cwd='frontend')
    if not success:
        print(f"❌ Failed to install npm dependencies: {output}")
        return False
    
    print("✅ Frontend setup completed")
    return True

def main():
    """Main setup function"""
    print("🍳 Recipe Management Application Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Setup backend
    if not setup_backend():
        sys.exit(1)
    
    # Setup frontend
    if not setup_frontend():
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 To run the application:")
    print("1. Start the backend:")
    print("   cd backend")
    print("   python app.py")
    print("\n2. In a new terminal, start the frontend:")
    print("   cd frontend")
    print("   npm start")
    print("\n3. Open your browser and go to: http://localhost:3000")
    print("\n📚 For more information, see the README.md file")

if __name__ == "__main__":
    main() 