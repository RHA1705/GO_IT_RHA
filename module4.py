def is_valid_password(password):
    if len(password) != 8:
        return False
    
    for i in password:
        if ord(i) not in range(65, 90) :
            return True
    
    return True

print(is_valid_password('RomkoH47'))