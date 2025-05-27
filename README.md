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



## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

If you have Anaconda or Miniconda installed run the following code in your terminal:

```bash
# Clone or download this repository
cd llm_business_analytics_tutorials

# Run the automated setup script
chmod +x setup_environment.sh
./setup_environment.sh
```

This creates a complete `llm_analytics` environment with all dependencies.

### Option 2: Manual Setup: run the following code in your terminal

1. **Create virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📋 Prerequisites

### Required Software
- **Python 3.9+** ([Download](https://www.python.org/downloads/))
- **VS Code** or **Cursor** with Python/Jupyter extensions
  - [VS Code Download](https://code.visualstudio.com/)
  - [Cursor Download](https://cursor.sh/) (Recommended)

### Knowledge Requirements
- **Basic Python**: Variables, functions, loops
- **Optional**: Basic understanding of neural networks


## 📖 Detailed Setup Instructions

<details>
<summary>🖥️ Platform-Specific Python Installation</summary>

### Windows
1. Download from [python.org](https://www.python.org/downloads/windows/)
2. ✅ **Important**: Check "Add Python to PATH" during installation
3. Verify: Open Command Prompt → `python --version`

### macOS
```bash
# Using Homebrew (recommended)
brew install python

# Or download from python.org
```
Verify: Open Terminal → `python3 --version`

### Linux (Ubuntu/Debian)
```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv
```
Verify: `python3 --version`

</details>

<details>
<summary>🔧 VS Code/Cursor Setup</summary>

1. **Open the project folder**: `File > Open Folder...` → Select `llm_business_analytics_tutorials`
2. **Select Python interpreter**:
   - Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
   - Type "Python: Select Interpreter"
   - Choose: `.venv/bin/python` (or your conda environment)
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


## 🛠️ Troubleshooting

<details>
<summary>❓ Common Issues & Solutions</summary>

### "conda not found"
- Install [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Restart terminal after installation

### "Module not found" errors
```bash
# Ensure environment is activated
conda activate llm_analytics  # or source .venv/bin/activate

# Reinstall packages
pip install -r requirements.txt
```

### "Jupyter kernel not found"
```bash
# Install jupyter kernel for your environment
python -m ipykernel install --user --name llm_analytics
```

### Training seems slow
- ✅ This is normal for CPU training
- ✅ Reduce `max_iters` for faster experimentation
- ✅ Consider smaller `batch_size` if memory issues

### VS Code not recognizing environment
- Use Command Palette → "Python: Select Interpreter"
- Choose the correct environment path
- Restart VS Code if needed

</details>


## 📄 License

MIT License - Feel free to use and modify for educational purposes!


---

**Happy Learning!** 🎓✨

*These tutorials are designed to be your first step into the exciting world of Large Language Models. Take your time, experiment freely, and don't hesitate to explore beyond the provided examples!* 