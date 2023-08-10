 #!/usr/bin/python3
def uppercase(string):
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            upper_case = ord(char) - 32
            print("{}".format(chr(upper_case)), end='')
        else:
            print("{}".format(char), end='')
    return \n
        
