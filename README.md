# Flask Boilerplate Generator CLI

A command-line tool to generate Flask boilerplate code with best practices and modern project structure.

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
pip install nd-flask-bp-generator
```

## Usage

### Create a new project

```bash
nd-flask-bp create my_project
```

### Run the project

```bash
nd-flask-bp run my_project
```

## Project Structure

```
my_project/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── health.py
│   │       └── routes.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/
│   │   └── __init__.py
│   └── __init__.py
├── tests/
│   └── __init__.py
├── .env
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## Development

### Setup Development Environment

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nd-flask-bp-generator.git
cd nd-flask-bp-generator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Releasing a New Version

1. Update the version in `setup.py`
2. Run the release script:
```bash
./scripts/release.sh <version>
```

For example:
```bash
./scripts/release.sh 0.1.0
```

The script will:
- Clean up old builds
- Update the version in setup.py
- Build the package
- Upload to PyPI
- Clean up build artifacts

## License

MIT License 