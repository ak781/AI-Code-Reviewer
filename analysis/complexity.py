# analysis/complexity.py

from radon.complexity import cc_visit, cc_rank

def run_radon_complexity(code: str) -> str:
    """
    Analyze the cyclomatic complexity of the given code.

    Args:
        code (str): The source Python code as a string.

    Returns:
        str: A formatted string with function names, complexity scores, and rank.
    """
    try:
        results = cc_visit(code)
        if not results:
            return "No complexity issues found"

        output_lines = [
            f"{res.name} - Complexity: {res.complexity} (Rank: {cc_rank(res.complexity)})"
            for res in results
        ]
        return "\n".join(output_lines)
    except Exception as e:
        return f"Radon error: {str(e)}"
