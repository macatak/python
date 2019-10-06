import random
import string

def randomStringwithDigitsAndSymbols(stringLength=10):
    """Generate a random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

def randomStringwithDigits(stringLength):
    # this os just for alphanmeric
    password_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(password_characters) for i in range(stringLength))


print("Generating Random String password with letters, digits and special characters ")
#print ("First Random String ", randomStringwithDigitsAndSymbols() )
#print ("Second Random String", randomStringwithDigitsAndSymbols(10) )
#print ("Third Random String", randomStringwithDigitsAndSymbols(30) )

#print(random.choice(string.punctuation))

# this is for MD5
for x in range(100):
    print(randomStringwithDigits(32))
