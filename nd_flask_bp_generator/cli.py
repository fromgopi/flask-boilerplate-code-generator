# Standard library imports
import os
import shutil
from pathlib import Path
from typing import Dict, Any

# Third-party imports
import click
import yaml
from jinja2 import Environment, FileSystemLoader
import subprocess

TEMPLATES_DIR = Path(__file__).parent / "templates"
DEFAULT_CONFIG = {
    "app_name": "flask_app",
    "project_name": "flask_project",
    "author": "Your Name",
    "email": "your.email@example.com",
    "description": "A Flask REST API application",
    "version": "0.1.0",
    "python_version": "3.7",
    "dependencies": {
        "flask": "2.0.1",
        "flask-sqlalchemy": "2.5.1",
        "flask-marshmallow": "0.14.0",
        "marshmallow-sqlalchemy": "0.26.1",
        "python-dotenv": "0.19.0",
        "pytest": "7.0.0",
        "black": "22.3.0",
        "flake8": "4.0.1",
        "isort": "5.10.1",
    }
}

def create_venv(project_path):
    """Create a virtual environment for the project."""
    venv_path = project_path / "venv"
    result = subprocess.run(["python3", "-m", "venv", str(venv_path)], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Failed to create virtual environment: {result.stderr}")
    return venv_path

def create_project_structure(project_path, config):
    """Create the basic project structure."""
    # Create main directories
    (project_path / "app").mkdir(parents=True)
    
    # App structure
    (project_path / "app" / "api").mkdir()
    (project_path / "app" / "api" / "v1").mkdir()
    (project_path / "app" / "api" / "v1" / "endpoints").mkdir()
    (project_path / "app" / "api" / "v1" / "schemas").mkdir()
    
    (project_path / "app" / "core").mkdir()
    (project_path / "app" / "models").mkdir()
    (project_path / "app" / "utils").mkdir()
    
    # Tests structure
    (project_path / "tests").mkdir()
    (project_path / "tests" / "api").mkdir()
    (project_path / "tests" / "api" / "v1").mkdir()
    (project_path / "tests" / "core").mkdir()
    (project_path / "tests" / "models").mkdir()
    
    # Documentation
    (project_path / "docs").mkdir()
    (project_path / "docs" / "api").mkdir()
    
    # Create files
    (project_path / "requirements.txt").touch()
    (project_path / ".env").touch()
    (project_path / ".env.example").touch()
    (project_path / ".gitignore").touch()
    (project_path / "README.md").touch()
    (project_path / "pyproject.toml").touch()
    (project_path / "setup.cfg").touch()
    (project_path / "tox.ini").touch()

def render_templates(project_path, config):
    """Render all template files using Jinja2."""
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    
    # Render main application files
    templates = [
        ("app/__init__.py.j2", "app/__init__.py"),
        ("app/api/__init__.py.j2", "app/api/__init__.py"),
        ("app/api/v1/__init__.py.j2", "app/api/v1/__init__.py"),
        ("app/core/__init__.py.j2", "app/core/__init__.py"),
        ("app/core/config.py.j2", "app/core/config.py"),
        ("app/api/v1/schemas/base.py.j2", "app/api/v1/schemas/base.py"),
        ("app/api/v1/endpoints/health.py.j2", "app/api/v1/endpoints/health.py"),
        ("requirements.txt.j2", "requirements.txt"),
        (".gitignore.j2", ".gitignore"),
        ("README.md.j2", "README.md"),
        ("pyproject.toml.j2", "pyproject.toml"),
        ("setup.cfg.j2", "setup.cfg"),
        ("tox.ini.j2", "tox.ini"),
        ("manage.py.j2", "manage.py"),
    ]

    with click.progressbar(templates, label="Rendering templates") as bar:
        for template_name, output_path in bar:
            template = env.get_template(template_name)
            content = template.render(**config)
            (project_path / output_path).write_text(content)

@click.group()
def cli():
    """Flask boilerplate generator CLI."""
    pass

@cli.command("create")
@click.argument("project_name")
@click.option("--author", prompt="Author name", help="Project author name")
@click.option("--email", prompt="Author email", help="Project author email")
@click.option("--description", prompt="Project description", help="Project description")
def create_project(project_name, author, email, description):
    """Generate a Flask REST API boilerplate project."""
    config = DEFAULT_CONFIG.copy()
    config.update({
        "project_name": project_name,
        "app_name": project_name.lower().replace("-", "_"),
        "author": author,
        "email": email,
        "description": description,
    })

    project_path = Path(project_name)
    if project_path.exists():
        click.echo(f"Error: Directory '{project_name}' already exists.")
        return

    try:
        click.echo(f"Creating project '{project_name}'...")
        project_path.mkdir()
        
        click.echo("Creating project structure...")
        create_project_structure(project_path, config)
        
        click.echo("Rendering templates...")
        render_templates(project_path, config)
        
        click.echo("Creating virtual environment...")
        venv_path = create_venv(project_path)
        
        click.echo(f"\nProject created successfully in '{project_name}'!")
        click.echo("\nTo get started:")
        click.echo(f"1. cd {project_name}")
        click.echo("2. source venv/bin/activate")
        click.echo("3. pip install -r requirements.txt")
        click.echo("4. python -m app")
        
    except FileExistsError as e:
        click.echo(f"Error: Directory or file already exists: {e}")
    except PermissionError as e:
        click.echo(f"Error: Permission denied: {e}")
    except Exception as e:
        click.echo(f"Error: {str(e)}")
        if project_path.exists():
            shutil.rmtree(project_path)

@cli.command("run")
@click.argument("project_name")
@click.option("--host", default="127.0.0.1", help="Host to run the server on")
@click.option("--port", default=5000, help="Port to run the server on")
@click.option("--env", default="development", help="Environment (development/production)")
def run_app(project_name, host, port, env):
    """Run the Flask application."""
    project_path = Path(project_name)
    if not project_path.exists():
        click.echo(f"Error: Project {project_name} not found.")
        return
    
    click.echo(f"Running {project_name} in {env} mode...")
    os.environ["FLASK_APP"] = "manage.py"
    os.environ["FLASK_ENV"] = env
    os.chdir(project_path)
    os.system(f"flask run --host={host} --port={port}")

if __name__ == "__main__":
    cli() 