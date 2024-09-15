import os
import sys

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path):
    with open(path, 'a'):
        os.utime(path, None)

def create_project_structure(project_name):
    base_path = os.path.join(os.getcwd(), project_name)
    
    # Create directories
    directories = [
        'data/raw', 'data/processed', 'data/external', 'data/interim',
        'notebooks/exploratory', 'notebooks/reports',
        'src/data', 'src/features', 'src/models', 'src/visualization', 'src/config', 'src/utils',
        'tests/test_data', 'mlruns', 'configs', 'scripts', 'docs', 'requirements',
        '.github/workflows'
    ]
    
    for directory in directories:
        create_directory(os.path.join(base_path, directory))
    
    # Create files
    files = [
        'README.md', 'CHANGELOG.md', 'LICENSE', 'setup.py', '.gitignore',
        'Dockerfile', 'pyproject.toml',
        'requirements/requirements.txt', 'requirements/requirements-dev.txt',
        'src/__init__.py', 'tests/__init__.py',
        '.github/workflows/tests.yml', '.github/workflows/deploy.yml'
    ]
    
    for file in files:
        create_file(os.path.join(base_path, file))
    
    # Create __init__.py files in src subdirectories
    for subdir in ['data', 'features', 'models', 'visualization', 'config', 'utils']:
        create_file(os.path.join(base_path, 'src', subdir, '__init__.py'))

def get_project_name():
    while True:
        project_name = input("Enter the name for your ML project: ").strip()
        if project_name:
            if os.path.exists(project_name):
                print(f"Error: A directory named '{project_name}' already exists.")
                overwrite = input("Do you want to overwrite it? (yes/no): ").lower()
                if overwrite == 'yes':
                    return project_name
            else:
                return project_name
        else:
            print("Project name cannot be empty. Please try again.")

if __name__ == '__main__':
    print("Welcome to the ML Project Structure Creator!")
    project_name = get_project_name()
    
    create_project_structure(project_name)
    print(f"\nProject structure created for '{project_name}'")
    print(f"You can find your new project in: {os.path.join(os.getcwd(), project_name)}")