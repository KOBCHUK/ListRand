strings = ["sport", "crossfit", "jogging", "running", "box"]
substring = "r"
new_strings = []

for string in strings:
    if string.startswith(substring):
        new_strings.append(string)
print(strings)
print(new_strings)
