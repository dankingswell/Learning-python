import string

def encrypt(text,shift):
    text = text.lower()
    alpha = list(string.ascii_lowercase)

    alt = list(alpha[len(alpha)-shift::])
    alt.extend(alpha)
    del([alt[len(alt)-shift::]])

    new_message = ""
    for letter in text:
        if letter == " ":
            new_message += letter
            continue
        new_message += alt[alpha.index(letter)]

    return new_message
    

holder  = encrypt('Get this message to the main server',13)
print(holder)
#'trg guvf zrffntr gb gur znva freire'

def decrypt(text,shift):
    text = text.lower()
    alpha = list(string.ascii_lowercase)

    alt = list(alpha[len(alpha)-shift::])
    alt.extend(alpha)
    del([alt[len(alt)-shift::]])

    new_message = ""
    for letter in text:
        if letter == " ":
            new_message += letter
            continue
        new_message += alpha[alt.index(letter)]

    return new_message

finish = decrypt(holder,13)
print(finish)

def brute_force(message):
    length = len(string.ascii_lowercase)
    for x in range(0,length):
        print(f"using shift value {x} \n message is :\n " +decrypt(message,x))

brute_force(holder)