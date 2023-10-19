with open("2.md", "r", encoding="utf-8") as f:
    lines = f.read()

lines = lines.split("\n")
print(lines)

ans = []

for line in lines:
    if line.startswith("- "):
        ans.append("???+ info \"" + line[2:] + "\"")
    elif line.startswith("!"):
        ans.append("    " + line)
    else:
        ans.append(line)

ans = "\n".join(ans)
with open("12.md", "w", encoding="utf-8") as f:
    f.write(ans)