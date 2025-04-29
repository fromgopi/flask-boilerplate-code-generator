# Flask Boilerplate Generator

A CLI tool to generate Flask REST API boilerplate code with SQLAlchemy, Marshmallow, and Jinja2 templates.

## Features

- Generates a complete Flask REST API project structure
- Includes SQLAlchemy ORM setup
- Marshmallow serialization/deserialization
- Blueprint-based architecture
- Environment-based configuration
- Virtual environment setup
- Git integration

## Installation

```bash
pip install -e .
```

## Usage

### Creating a New Project

```bash
nd_bp create <project_name> --author "Your Name" --email "your.email@example.com" --description "Project description"
```

The generator will:
1. Create a new project directory
2. Set up the project structure
3. Create a virtual environment
4. Generate all necessary files
5. Initialize a Git repository

### Running Your Project

```bash
# Run with default settings (localhost:5000, development mode)
nd_bp run <project_name>

```
project_name/
├── app/
│   ├── __init__.py
│   ├── config/
│   │   └── config.py
│   ├── models/
│   │   └── base.py
│   ├── schemas/
│   │   └── base.py
│   └── routes/
│       └── __init__.py
├── tests/
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 