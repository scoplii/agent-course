def open_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return content
file_path = "./backend/python_test.py"
content = open_file(file_path)
print(content)