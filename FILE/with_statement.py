"""
`with` statement automatically close the file after compleating the work.
"""

try:
    with open("./data.txt", "r") as f:
        print(f.read())

except Exception as e:
    print("Exception Occured:", e)
    exit()
print("File Finished...")
print("File Closed:", f.closed)
