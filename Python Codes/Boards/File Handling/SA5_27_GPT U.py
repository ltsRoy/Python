def reverse():
    with open("Poem.txt", "r+") as fh:
        lines = fh.readlines()
        fh.seek(0)
        fh.truncate()  # Clear the file before writing the modified lines
        for line in lines:
            reversed_line = line[::-1]
            fh.write(reversed_line)

reverse()
