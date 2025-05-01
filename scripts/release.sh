#!/bin/bash

# Exit on error
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Function to print colored messages
print_message() {
    echo -e "${2}${1}${NC}"
}

# Check if version is provided
if [ -z "$1" ]; then
    print_message "Please provide a version number (e.g., 0.1.0)" "$RED"
    exit 1
fi

VERSION=$1

# Clean up old builds
print_message "Cleaning up old builds..." "$YELLOW"
rm -rf build/ dist/ *.egg-info/

# Update version in setup.py
print_message "Updating version in setup.py..." "$YELLOW"
sed -i '' "s/version=\".*\"/version=\"$VERSION\"/" setup.py

# Build the package
print_message "Building package..." "$YELLOW"
if command -v python3 &> /dev/null; then
    PYTHON=python3
elif command -v python &> /dev/null; then
    PYTHON=python
else
    print_message "Python is not installed!" "$RED"
    exit 1
fi

$PYTHON setup.py sdist bdist_wheel

# Check if twine is installed
if ! command -v twine &> /dev/null; then
    print_message "Installing twine..." "$YELLOW"
    pip install twine
fi

# Upload to PyPI
print_message "Uploading to PyPI..." "$YELLOW"
twine upload dist/*

# Clean up
print_message "Cleaning up..." "$YELLOW"
rm -rf build/ dist/ *.egg-info/

print_message "Release $VERSION completed successfully!" "$GREEN"
print_message "You can now install the package using: pip install nd-flask-bp-generator==$VERSION" "$GREEN" 