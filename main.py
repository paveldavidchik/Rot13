
def rot13(message):
    rot = ''
    for ch in message:
        if not ch.isalpha():
            rot += ch
        elif 90 < ord(ch) + 13 < 104 or ord(ch) + 13 > 122:
            rot += chr(ord(ch) - 13)
        else:
            rot += chr(ord(ch) + 13)
    return rot


print(rot13('Test'))
