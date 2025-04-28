from setuptools import setup, find_packages

setup(
    name="nd-flask-bp-generator",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
        "jinja2>=3.0.0",
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "nd_bp=nd_flask_bp_generator.cli:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to generate Flask REST API boilerplate code",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/nd-flask-bp-generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 