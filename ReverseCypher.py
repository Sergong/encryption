# Reverse Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

message = raw_input('Enter a message: ')
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
