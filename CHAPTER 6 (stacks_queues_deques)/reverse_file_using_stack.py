from stack_class import *
def reverse_file(path):
    """Overwrite given file using its context line-by-line reversed"""
    s=ArrayStack()
    with open(path,"r") as original:
        for line in original:
            s.push(line.rstrip("\n")) # removing newline characters

    # overwrite the contents in LIFO order
    with open(path,"w") as new:
        while not s.is_empty():
            new.write(s.pop()+"\n") # re-insert newline characters.

    return "Reversed"

print(reverse_file("sample.txt"))
