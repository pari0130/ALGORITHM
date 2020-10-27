
msg = "It is Time"
print(msg.upper())

tmp = msg.upper()

print(tmp.find("T"))  # 문자열 index 찾기
print(tmp.count("T"))  # 문자열 count

# 대문자 문자열 찾아서 찾기 isupper
for x in msg:
    if x.isupper():
        print(x, end='')
print()

# 소문자 문자열 찾아서 찾기 islower
for x in msg:
    if x.islower():
        print(x, end='')
print()

# 알파벳 찾기 isalpha
for x in msg:
    if x.isalpha():
        print(x, end='')
print()

# 아스키 넘버 출력 ord
tmp = "AZ"
for x in tmp:
    print(ord(x))

# 아스키 번호로 문자 찾기
tmp = 90
print(chr(tmp))
