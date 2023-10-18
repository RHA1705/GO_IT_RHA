message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ord(ch) in range(ord("A"), ord("Z")+1):
        pos = ord(ch) - ord("A")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("A"))
    elif ord(ch) in range(ord("a"), ord("z")):
        pos = ord(ch) - ord("a")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("a"))
    else:
        encoded_message += ch

    encoded_message += new_char