# pip install markitdown

import os
from markitdown import MarkItDown

input_folder = "./in"
output_folder = "./out"

md = MarkItDown()

for root, dirs, files in os.walk(input_folder):
    for filename in files:
        input_path = os.path.join(root, filename)
        relative_path = os.path.relpath(root, input_folder)
        output_dir = os.path.join(output_folder, relative_path)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.md")
        
        try:
            result = md.convert(input_path)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result.text_content)
            print(f"結果が {output_path} に書き込まれました。")
        except Exception as e:
            print(f"{filename} を変換できませんでした: {e}")