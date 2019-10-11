# 密码转换
s = input()  # 输入一串字符串，本题较难
t = ""
for c in s:
    if 'a' <= c <= 'z':
        t += chr(ord('a') + ((ord(c) - ord('a')) + 3) % 26)
    elif 'A' <= c <= 'Z':
        t += chr(ord('A') + ((ord(c) - ord('A')) + 3) % 26)
    else:
        t += c
print(t)
