def isPhoneNUmber(text):
  if len(text) != 12:
    return False
  for i in range(0, 3):
    if not text[i].isdecimal():
      return False
  if text[3] != '-':
    return False
  for i in range(4, 7):
    if not text[i].isdecimal():
      return False
  if text[7] != '-':
    return False
  for i in range(8, 12):
    if not text[i].isdecimal():
      return False
  return True

#print('Is 415-55-4242 a phone number?')
#print(isPhoneNUmber('415-555-4242'))
#print('Is Moshi moshi a phone number?')
#print(isPhoneNUmber('Moshi moshi'))

message = 'Call me at 415-55-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
  chunk = message[i:i+12]
  if isPhoneNUmber(chunk):
    print('Phone number found: ' + chunk)
print('Done')


