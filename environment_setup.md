# Setting Up Your Environment for the GenAI Course

Welcome to the GenAI course! This brief guide will walk you through setting up a clean Python environment where you'll run all your codes for the course assignments and examples.


## Why create a virtual Python environment? 

A virtual Python environment is simply a folder that contains its own copy of Python and any libraries you install. This setup keeps the packages for this course separate from everything else on your computer, ensures that everyone in the class uses the exact same package versions, and allows you to delete the entire setup with a single command when the semester ends.


## What is `uv`?

`uv` is a modern, lightweight command-line tool that streamlines the process of creating virtual environments and installing Python packages into one fast and efficient workflow. Traditionally, Python projects require tools like `venv` for setting up environments and `pip` for installing packages, `uv` combines both steps into a single, easy-to-use interface. If you've used `conda`, you may already be familiar with managing environments and packages together. Compared to `conda`, `uv` is focused on Python-only workflows, and is faster in most cases.


## Installing `uv`

Follow the tutorial that matches your operating system.

### Windows

First, install **Python 3.10 or newer** from the official website:  
<https://www.python.org/downloads/>. During installation, make sure to check the box that says **"Add Python to PATH"**.

After installing Python, open **PowerShell** and run the following command to install `uv`:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```


### macOS

Install **Python 3.10 or newer** using [Homebrew](https://brew.sh/). Open the Terminal and run:

```bash
brew install python@3.10
```

Then install `uv`:

```bash
brew install uv
```

Alternatively, you can use the installer script:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sudo sh
```


### Linux (Ubuntu/Debian example)

Start by installing Python and essential development tools:

```bash
sudo apt update
sudo apt install -y build-essential curl python3 python3-venv python3-pip
```

Check your Python version with:

```bash
python3 --version
```

Make sure it’s at least **3.10**. Then install `uv` with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sudo sh
```

Finally, run:

```bash
uv --version
```

to confirm that `uv` is installed and working correctly.

## Creating and activating the environment

In your workplace folder, open the termial and run the following commands:

```bash
mkdir GenAI_LLM
cd GenAI_LLM
uv venv GenAI           # make the environment
```

This creates a virtual environment named `GenAI` in the `GenAI_LLM` folder. To activate the environment, first `cd` into the folder in the terminal, then run the appropriate command for your operating system:

* macOS / Linux: `source GenAI/bin/activate`  
* Windows (Command Prompt): `GenAI/Scripts/activate`  
* Windows (PowerShell):    `GenAI/Scripts/Activate.ps1`

Your terminal prompt will now display `(GenAI)` to indicate that you are working inside the virtual environment.



## Installing the core packages

Inside the active environment, install the essential Python libraries:

```bash
uv pip install numpy pandas scikit-learn matplotlib jupyter notebook
```

## Installing PyTorch (with Optional GPU Support)

### Step 1: Check if Your Computer Has a GPU

To see if your machine has a dedicated NVIDIA GPU (required for CUDA), run:

```bash
nvidia-smi
```

- If you see information about your GPU (e.g., model name, driver version), then you have an NVIDIA GPU.
- If the command is not found or shows an error, your system likely doesn’t have an NVIDIA GPU or the driver isn’t installed.

Alternatively, on Windows:

- Open Device Manager → Expand "Display Adapters" to check for NVIDIA hardware.


### Step 2: Install PyTorch

**If you do NOT have a GPU**, install the CPU-only version:

```bash
uv pip install torch torchvision torchaudio
```

**If you have a GPU**, install the PyTorch version that includes precompiled CUDA support. You can select the appropriate version from [PyTorch's official site](https://pytorch.org/get-started/locally/), or use a common version like CUDA 12.1:

```bash
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

This installs a version of PyTorch that includes the necessary CUDA libraries—**you do not need to install CUDA manually**.


### Step 3: Verify the Installation

Run the following Python code (in a Jupyter notebook or a temporary python script) to verify that PyTorch is installed correctly and check if a GPU is available:
```python
import torch
print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU device:", torch.cuda.get_device_name(0))
```



## Launching Jupyter

Start a notebook server (still inside the `(GenAI)` environment and `cd` into the target folder, i.e., the folder that contains the notebook) by the following command:

```bash
jupyter notebook
```

A browser tab will open; create or open notebooks there. Whenever you come back to coursework, remember to activate `(GenAI)` first and then start Jupyter.



### You’re fully set to explore machine‑learning code in a neat and comfortable environment. Happy learning!
