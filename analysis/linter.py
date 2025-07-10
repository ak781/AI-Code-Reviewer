# analysis/linter.py

import subprocess

def run_flake8(filepath: str) -> str:
    """
    Run flake8 linter on the given file path.

    Args:
        filepath (str): Path to the Python file.

    Returns:
        str: flake8 output or 'No style issues found'.
    """
    try:
        result = subprocess.run(
            ["flake8", filepath],
            text=True,
            capture_output=True
        )
        return result.stdout.strip() or "No style issues found"
    except Exception as e:
        return f"Flake8 error: {str(e)}"
