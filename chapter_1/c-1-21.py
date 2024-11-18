
lines = []
try:
    while True:
        line = input()
        lines.append(line)
except EOFError:
    print("End of file")
except Exception as e:
    print(e.__cause__)
finally:
    for i in range(len(lines) - 1, -1, -1):
        print(lines[i])


