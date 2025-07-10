# utils/file_ops.py

import tempfile

def save_code(code: str) -> str:
    """
    Save the given code string to a temporary .py file.

    Args:
        code (str): Python code to save.

    Returns:
        str: Path to the saved temporary file.
    """
    try:
        temp_file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".py")
        temp_file.write(code)
        temp_file.close()
        return temp_file.name
    except Exception as e:
        raise RuntimeError(f"Failed to save code to temp file: {str(e)}")
