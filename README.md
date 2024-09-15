# ML_Project_Structure
A template repository for automating the creation of a structured machine learning project, including data, notebooks, models, and configuration files.


## Project Structure

```
project-name/
│
├── data/
│   ├── raw/                # Raw, untouched data
│   ├── processed/          # Processed, cleaned data ready for model training
│   ├── external/           # External data sources
│   └── interim/            # Intermediate data for debugging or transformations
│
├── notebooks/              # Jupyter notebooks for exploration, analysis, experiments
│   ├── exploratory/        # Initial data exploration
│   └── reports/            # Final analysis notebooks
│
├── src/
│   ├── __init__.py         # Marks this directory as a Python package
│   ├── data/               # Data ingestion, cleaning, and processing
│   │   ├── __init__.py
│   │   ├── ingestion.py    # Data ingestion from various sources
│   │   ├── cleaning.py     # Data cleaning and validation
│   │   └── pipelines.py    # Pipelines for data processing
│   ├── features/           # Feature engineering
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models/             # Model definition, training, and evaluation
│   │   ├── __init__.py
│   │   ├── base_model.py   # Abstract base class for models
│   │   ├── model_a.py      # Specific model implementation
│   │   ├── model_b.py      # Another model implementation
│   │   ├── train.py        # Model training script
│   │   ├── predict.py      # Model inference script
│   │   ├── evaluate.py     # Evaluation metrics script
│   │   └── save_load.py    # Script for saving/loading models
│   ├── visualization/      # Data and results visualization
│   │   ├── __init__.py
│   │   └── visualize.py
│   ├── config/             # Configuration settings
│   │   ├── __init__.py
│   │   ├── config.py       # Configuration class
│   │   └── logging_config.yaml  # Logging configuration
│   └── utils/              # Utility functions
│       ├── __init__.py
│       ├── logging_utils.py
│       └── ml_utils.py
│
├── tests/                  # Unit and integration tests
│   ├── __init__.py
│   ├── test_data/          # Test data for unit tests
│   ├── test_models.py      # Tests for model training and inference
│   ├── test_features.py    # Tests for feature engineering
│   └── test_utils.py       # Tests for utility functions
│
├── mlruns/                 # MLflow experiment tracking
│
├── configs/                # Configuration files
│   ├── model_config.yaml   # Model hyperparameters
│   └── pipeline_config.yaml # Data pipeline configuration
│
├── scripts/                # Standalone scripts for running the project
│   ├── run_training.sh     # Shell script to run model training
│   ├── run_inference.sh    # Shell script for inference
│   └── setup_env.sh        # Script to set up the development environment
│
├── docs/                   # Documentation
│   ├── architecture.md     # System architecture overview
│   ├── data_dictionary.md  # Descriptions of data fields
│   └── model_card.md       # Model details, use cases, and limitations
│
├── requirements/
│   ├── requirements.txt    # Production dependencies
│   └── requirements-dev.txt # Development dependencies
│
├── Dockerfile              # Docker configuration for reproducibility
│
├── .github/                # CI/CD configurations
│   └── workflows/
│       ├── tests.yml       # GitHub Actions for running tests
│       └── deploy.yml      # Deployment workflow
│
├── .gitignore              # Files to ignore in version control
│
├── README.md               # Project overview, setup instructions, and usage
│
├── CHANGELOG.md            # Document version changes
│
├── LICENSE                 # Project license
│
├── setup.py                # Installation script if your project will be packaged
│
└── pyproject.toml          # Project metadata and build system requirements
```

# About This Repository
This repository serves as a template for creating structured machine learning projects. It provides a standardized directory structure and file organization to streamline the development process and improve project maintainability.
Key features of this structure:

- Clear separation of data, code, and documentation
- Organized source code with modular components
- Dedicated spaces for Jupyter notebooks, tests, and configuration files
- Integration with MLflow for experiment tracking
- CI/CD setup with GitHub Actions
- Docker support for reproducibility

# Getting Started

To use this template:

Clone the repository
Rename the project directory as needed
Customize the structure to fit your specific project requirements

You can also simply run this python file 

```
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
```
