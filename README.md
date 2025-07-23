# AI Code Reviewer

A Streamlit-based web application that analyzes Python code for style issues, formatting, complexity, and Big-O estimation using static analysis tools.

## Features

- Upload `.py` file or paste Python code directly.
- Detects style issues using `flake8`.
- Auto-formats code using `black`.
- Analyzes cyclomatic complexity using `radon`.
- Estimates time and space complexity heuristically via AST parsing.

## Project Structure

```bash
ai-code-reviewer/
├── app.py
├── analysis/
| ├── complexity.py # Cyclomatic complexity using radon
│ ├── linter.py # Style checker using flake8
│ ├── formatter.py # Code formatter using black
| |── time_complexity.py # Analyse the time complexity
│ └── complexity_chart.py # Heuristic-based Big-O estimation
└── utils/
└── helpers.py # File reading and validation helpers

## How It Works

- **Style Analysis**: `flake8` checks for PEP8 violations and coding issues.
- **Code Formatting**: `black` reformats code to comply with standard style guidelines.
- **Cyclomatic Complexity**: `radon` analyzes control flow to detect complex functions.
- **Big-O Estimation**: Custom logic parses Python AST to detect recursion, loop nesting, and common patterns to approximate time and space complexity.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-code-reviewer.git
   cd ai-code-reviewer

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the Streamlit app:
    ```bash
    streamlit run app.py

## Requirements

### Python 3.7+

### streamlit

### flake8

### black

### radon

## Install all with:
    ```bash
    pip install streamlit flake8 black radon

