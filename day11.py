
def check_pwd (s):

    if any([l in s for l in ["i", "o", "l"]]):
        return False

    for i in range(len(s)-2):
        if ord(s[i+1]) == ord(s[i])+1 and ord(s[i+2]) == ord(s[i])+2:
            break
    if not (ord(s[i+1]) == ord(s[i])+1 and ord(s[i+2]) == ord(s[i])+2): return False


    i = 0
    c1 = " "
    c2 = " "
    while i<len(s)-1 and c2 == " ":
        if s[i] == s[i+1]:
            if c1 == " ": c1 = s[i]
            elif not s[i] == c1:
                c2 = s[i]
            i+=2
        else:
            i+=1

    return not c2 == " "

def next_pwd (s):
    i = len(s)-1
    carry = 1
    while carry and i > 0:
        if s[i] == "z":
            s = s[:i]+'a'+s[i+1:]
            i -= 1
        else:
            s = s[:i]+chr(ord(s[i])+1)+s[i+1:]
            carry = 0
    return s


pwd = "hxbxwxba"

while not check_pwd(pwd):
    pwd = next_pwd(pwd)

print (pwd)

pwd = next_pwd(pwd)

while not check_pwd(pwd):
    pwd = next_pwd(pwd)

print (pwd)