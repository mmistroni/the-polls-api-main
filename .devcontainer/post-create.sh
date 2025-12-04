#!/bin/bash

# Create a virtual environment named .venv in the workspace folder
echo "Creating virtual environment..."
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Check if requirements.txt exists and install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping dependency installation."
fi

# Deactivate the virtual environment (optional, but good practice)
deactivate

echo "Devcontainer setup complete!"