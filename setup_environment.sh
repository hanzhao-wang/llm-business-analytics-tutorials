#!/bin/bash

# LLM Business Analytics Environment Setup Script
# This script creates a conda environment with all required packages.
# It explicitly uses Python 3.11 to ensure compatibility with data science
# libraries like PyTorch, which may not yet support the latest Python releases.

set -e  # Exit on any error

echo "🚀 Setting up LLM Business Analytics Environment..."

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "❌ Error: conda is not installed or not in PATH"
    echo "Please install Anaconda or Miniconda first"
    exit 1
fi

# Environment name
ENV_NAME="GenAI"

# Check if environment already exists
if conda info --envs | grep -q "^${ENV_NAME}"; then
    echo "⚠️  Environment '${ENV_NAME}' already exists"
    read -p "Do you want to remove and recreate it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🗑️  Removing existing environment..."
        conda env remove -n $ENV_NAME -y
    else
        echo "✅ Using existing environment"
        conda activate $ENV_NAME
        exit 0
    fi
fi

echo "📦 Creating conda environment with Python 3.11..."
conda create -n $ENV_NAME python=3.11 -y

echo "🔧 Activating environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate $ENV_NAME

echo "📋 Installing packages from requirements.txt..."
pip install -r requirements.txt

echo "🧪 Testing installation..."
python -c "
import torch
import transformers
import datasets
import numpy
import sklearn
import matplotlib
import pandas
import seaborn
import sys
print('✅ All packages imported successfully!')
print(f'🐍 Using Python {sys.version.split(" ")[0]}')
print(f'📦 PyTorch version: {torch.__version__}')
print(f'📦 Transformers version: {transformers.__version__}')
"

echo ""
echo "🎉 Environment setup complete!"
echo ""
echo "To activate this environment in the future, run:"
echo "  conda activate $ENV_NAME"
echo ""
echo "To deactivate when done:"
echo "  conda deactivate"
echo ""
echo "To use in Jupyter/VS Code, select the Python interpreter at:"
echo "  $(conda info --base)/envs/$ENV_NAME/bin/python" 