import os
import ast

def extract_definitions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read())
    
    definitions = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            definitions.append(f"    class {node.name}:")
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    definitions.append(f"        def {item.name}(self):")
        elif isinstance(node, ast.FunctionDef):
            definitions.append(f"    def {node.name}():")
    return definitions

def process_folder(folder_path, output_file):
    output_lines = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.py'):
            file_path = os.path.join(folder_path, file_name)
            output_lines.append(file_name)
            definitions = extract_definitions(file_path)
            output_lines.extend(definitions)
            output_lines.append("")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines))

# Set the folder and output file
folder_path = './'
output_file = 'extracted_defs.txt'

process_folder(folder_path, output_file)
