def read_next_line(filename):
    file = open(filename, "r")

    file.seek(20)

    line = file.readline()
    print("Line:", line.strip())

    file.close()

read_next_line("lyrics.txt")