import ast

def chunk_python_code(code:str):
    chunks = []

    tree = ast.parse(code)
    lines = code.splitlines()

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            start_line = node.lineno
            end_line = node.end_lineno

            function_code = "\n".join(lines[start_line-1:end_line])

            chunk = {
                "type": "function",
                "name": node.name,
                "start_line": start_line,
                "end_line": end_line,
                "code": function_code
            }

            chunks.append(chunk)

    return chunks    
