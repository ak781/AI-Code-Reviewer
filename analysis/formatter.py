# analysis/formatter.py

import black

def run_black_format(code: str) -> str:
    """
    Format the given Python code using Black.

    Args:
        code (str): The source Python code as a string.

    Returns:
        str: Formatted code, or an error message if formatting fails.
    """
    try:
        formatted_code = black.format_str(src_contents=code, mode=black.Mode())
        return formatted_code
    except Exception as e:
        return f"Black formatting error: {str(e)}"
