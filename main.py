import keyword
# 读取原文件
with open("random_int.py", "r") as file:
    content = file.readlines()

# 处理每一行内容
processed_lines = []
for line in content:
    new_line = []
    for word in line.split():
        # 如果不是保留字，将小写字母转为大写
        if not keyword.iskeyword(word):
            word = word.upper()
        new_line.append(word)
    processed_lines.append(" ".join(new_line) + "\n")

# 将处理后的内容写入新文件
with open("converted_random_int.py", "w") as file:
    file.writelines(processed_lines)
