# analysis/complexity_chart.py

import ast
import numpy as np

def generate_big_o_curve(complexity: str, max_n: int = 100):
    n_values = np.arange(1, max_n + 1)

    if complexity == "O(1)":
        return n_values, np.ones_like(n_values)
    elif complexity == "O(N)":
        return n_values, n_values
    elif complexity == "O(N^2)":
        return n_values, n_values ** 2
    elif complexity == "O(N^3)":
        return n_values, n_values ** 3
    elif complexity == "O(log N)":
        return n_values, np.log2(n_values)
    elif complexity == "O(N log N)":
        return n_values, n_values * np.log2(n_values)
    elif complexity == "O(2^N)":
        return n_values, 2 ** n_values
    else:
        return n_values, n_values  # fallback linear


def estimate_big_o(code: str):
    try:
        tree = ast.parse(code)
        results = []

        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                depth = _estimate_loop_depth(node)
                is_recursive = _is_recursive(node, func_name)

                # Default complexity
                time = "O(1)"
                space = "O(1)"

                # Heuristic Time Complexity
                if is_recursive and depth >= 2:
                    time = f"O(N^{depth}) + recursion"
                    space = "O(N)"
                elif is_recursive:
                    time = "O(N)"
                    space = "O(N)"
                elif depth == 1:
                    time = "O(N)"
                elif depth == 2:
                    time = "O(N^2)"
                elif depth >= 3:
                    time = f"O(N^{depth})"

                results.append({
                    "Function": func_name,
                    "Best": "O(1)",  # Conservative assumption
                    "Average": time,
                    "Worst": time,
                    "Space": space
                })

        return results
    except Exception as e:
        return f"Complexity chart error: {str(e)}"


def _estimate_loop_depth(node):
    """
    Count the maximum nesting level of loops in a function.
    """
    max_depth = 0
    current_depth = 0

    def helper(n, depth):
        nonlocal max_depth
        if isinstance(n, (ast.For, ast.While)):
            depth += 1
            max_depth = max(max_depth, depth)
        for child in ast.iter_child_nodes(n):
            helper(child, depth)

    helper(node, 0)
    return max_depth


def _is_recursive(node, name):
    """
    Check if the function calls itself (recursion).
    """
    for n in ast.walk(node):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
            if n.func.id == name:
                return True
    return False
