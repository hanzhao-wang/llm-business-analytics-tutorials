# LLM Tutorials for Business Analytics

Welcome to these introductory tutorials on (toy) Large Language Models (LLMs) training!



These tutorials provide practical experience with training toy language models for two fundamental tasks: **text generation** and **arithmetic learning**. Everything is designed to run efficiently on standard laptop CPUs.

> 💡 **Based on**: These tutorials build upon the excellent work from [karpathy/minGPT](https://github.com/karpathy/minGPT) and [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

## 📚 What You'll Learn

- **Fundamentals**: How transformer models work under the hood
- **Data Preparation**: Tokenization, vocabulary building, and dataset creation
- **Model Training**: Complete training loops, loss functions, and optimization
- **Text Generation**: Sampling strategies and creative text generation
- **Problem Solving**: Applying Transformer to structured tasks like arithmetic



## 🚀 Quick Start (Assume Python has been installed, see Prerequisites)

### Option 1: Automated Setup

If you have Anaconda or Miniconda installed run the following code in your terminal:

```bash
# Clone or download this repository
cd llm_business_analytics_tutorials

# Run the automated setup script
chmod +x setup_environment.sh
./setup_environment.sh
```

This creates a complete `GenAI` conda environment with all dependencies. The script automatically installs a compatible Python version (3.11), so you don't need to check your system's Python version beforehand.

### Option 2: Manual Setup

These steps assume you have already cloned or downloaded the repository and are in the `llm_business_analytics_tutorials` directory. Open your Terminal on MacOS or Command Prompt on Windows and type:

1. **Navigate to the project directory (if you haven't already)**:
   ```bash
   cd path/to/llm_business_analytics_tutorials-main
   ```

2. **Set up or Activate the `GenAI` Virtual Environment**:
   First, check your default `python3` version by running `python3 --version`.
   - **If your version is 3.11 or older**, you can create the environment directly:
     ```bash
     python3 -m venv GenAI
     ```
   - **If your version is 3.12 or newer**, you must use a specific, compatible version (like 3.11).
     - **If you do not have a compatible version installed**, please first follow the guide in the "Platform-Specific Python Installation" section below to install one.
     - Once you have a compatible version (e.g., 3.11), create the virtual environment with that specific version:
       ```bash
       python3.11 -m venv GenAI # Or python3.10, etc.
       ```

   Once the `GenAI` directory is created, activate it:
   ```bash
   source GenAI/bin/activate  # On Windows: GenAI\Scripts\activate
   ```
   (If the `GenAI` directory already exists from a previous attempt, you can just activate it.)

3. **Install dependencies**:
   (Ensure `pip` is available with your Python installation. It's usually included with Python 3.9+ and in virtual environments.)
   ```bash
   pip install -r requirements.txt
   ```

## 📋 Prerequisites

### Required Software
- **Python 3.9, 3.10, or 3.11**
  - **Important**: Python 3.12+ may have compatibility issues with key libraries like PyTorch. We strongly recommend using Python 3.9, 3.10, or 3.11 for a smooth installation.
  - To check your default Python version, open your terminal and type:
    ```sh
    python3 --version
    ```
    (On some systems, you might need to use `python --version`.)
  - If you need to install a specific version, please see the "Platform-Specific Python Installation" guide below.
- **VS Code** or **Cursor** with Python/Jupyter extensions
  - [VS Code Download](https://code.visualstudio.com/)
  - [Cursor Download](https://cursor.sh/) 

### Knowledge Requirements
- **Basic Python**: Variables, functions, loops
- **Optional**: Basic understanding of neural networks


## 📖 Detailed Setup Instructions

<details>
<summary>🖥️ Platform-Specific Python Installation</summary>

Here's how to install a compatible version of Python on different operating systems.

### Windows
1. Download a specific version (e.g., Python 3.11) from the [official Python website](https://www.python.org/downloads/windows/).
2. ✅ **Important**: Check "Add Python to PATH" during installation.
3. Verify in a new Command Prompt → `python --version`.

### macOS
Using [Homebrew](https://brew.sh/) is the recommended way to manage multiple Python versions.
```bash
# Install Python 3.11
brew install python@3.11

# After installation, you can use `python3.11` to run it
python3.11 --version
```
If you don't have Homebrew, you can download the installer from [python.org](https://www.python.org/downloads/macos/).

### Linux (Ubuntu/Debian)
```bash
sudo apt update && sudo apt install python3.11 python3.11-venv
```
Verify: `python3.11 --version`

</details>

<details>
<summary>🔧 VS Code/Cursor Setup</summary>

1. **Open the project folder**: `File > Open Folder...` → Select `llm_business_analytics_tutorials`
2. **Select Python interpreter**:
   - Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
   - Type "Python: Select Interpreter"
   - Choose: `GenAI/bin/python` (or your conda environment)
3. **Install recommended extensions** (if prompted):
   - Python
   - Jupyter

</details>

## 🎓 Running the Tutorials

1. **Open your preferred editor** (VS Code/Cursor)
2. **Navigate to tutorial folders**:
   - `nanogpt_tutorial/nanogpt_tutorial.ipynb`
   - `adder_tutorial/adder_tutorial.ipynb`
3. **Run cells sequentially** - each tutorial is self-contained!

### 💡 Pro Tips
- Start with Tutorial 1 (nanoGPT) for foundational concepts
- Read the markdown cells carefully - they explain the "why" behind the code
- Experiment with hyperparameters to see how they affect training
- Don't worry if training takes a few minutes - grab a coffee! ☕

## 📊 Tutorial Details

### Tutorial 1: nanoGPT - Text Generation 📝
**File**: `nanogpt_tutorial/nanogpt_tutorial.ipynb`

**What you'll build**: A word-level language model that generates Shakespeare-style text


### Tutorial 2: GPT-Adder - Arithmetic Learning 🧮
**File**: `adder_tutorial/adder_tutorial.ipynb`

**What you'll build**: A model that learns to perform addition (e.g., "2+3=" → "5")

```
Input: "7+3=" → Output: "10" ✅
```