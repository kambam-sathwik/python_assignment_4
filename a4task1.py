
try:
    with open("sample.txt") as f:
        content = f.readlines()
        print("Reading file content")
        for i in range(len(content)):
            print(f"Line {i+1}: {content[i].strip()}")
except FileNotFoundError:
    print("Error:The file 'sample.txt' was not found.")