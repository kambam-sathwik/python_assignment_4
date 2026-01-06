
with open("output.txt","wt") as f:
    content=input("Enter text to write to the file:")
    f.write(content+'\n')
    print("Data successfully written to output.txt")

with open("output.txt","at") as f:
    content=input("Enter additional text to append :")
    f.write(content)
    print("Data successfully appended")

with open("output.txt","rt") as f:
    content=f.read()
    print("final content of output.txt")
    print(content)
