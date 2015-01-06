with open("text.txt", "r+") as my_file:
    my_file.write("Use with ... as to write data.")

print my_file.closed

if not my_file.closed:
    my_file.close()

print my_file.closed