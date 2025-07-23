# analysis/time_complexity.py

import ast

class TimeComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.loop_depth = 0
        self.recursive_calls = 0
        self.current_function = None

    def visit_FunctionDef(self, node):
        self.current_function = node.name
        self.loop_depth = 0
        self.recursive_calls = 0
        self.generic_visit(node)
        complexity = "O(1)"
        if self.loop_depth == 1:
            complexity = "O(N)"
        elif self.loop_depth >= 2:
            complexity = f"O(N^{self.loop_depth})"
        if self.recursive_calls > 0:
            complexity += " + Recursion"
        return f"{node.name} - Estimated Time Complexity: {complexity}"

    def visit_For(self, node):
        self.loop_depth += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.loop_depth += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == self.current_function:
            self.recursive_calls += 1
        self.generic_visit(node)

def estimate_time_complexity(code: str) -> str:
    try:
        tree = ast.parse(code)
        visitor = TimeComplexityVisitor()
        results = []
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                results.append(visitor.visit_FunctionDef(node))
        return "\n".join(results) if results else "No functions detected."
    except Exception as e:
        return f"Time Complexity Estimation Error: {str(e)}"
