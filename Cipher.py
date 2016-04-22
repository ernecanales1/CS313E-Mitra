import random
def substitution_encode(strng):
    cipher= [ 'q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']
    new_word=' ' 
    for i in strng:
        if i == ' ':
            new_word += ' '
        else: 
            idx= ord(i) - ord('a')
            new_word += cipher[idx]
        
    return new_word

def substitution_decode(strng):
    cipher= [ 'q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']
    new_word= ' '
    for i in strng:
        if i == ' ':
            new_word += ' '
        else: 
            idx= cipher.index(i) + ord('a')
            new_word += chr(idx)
            
    return new_word
    

def vigenere_encode ( strng, passwd ):
  pass_phrase = ''
  count = 0
  count1 = 0
  encode = ''
  while len(pass_phrase) < len(strng):
    if count >= len(passwd):
      count = 0
    if strng[count1] == ' ':
      pass_phrase += ' '
      count -= 1
    else:
      pass_phrase += passwd[count]
    count += 1
    count1 += 1

  for i in range(len(strng)):
    if strng[i] == ' ':
      ref = ord(' ')
    else:
      ref = ord(pass_phrase[i]) + (ord(strng[i]) - 97)
    if ref <= 122:
      encode += chr(ref)
    else:
      encode += chr(ref - 26)
  return encode

  
    
  ...

def vigenere_decode ( strng, passwd ):
  pass_phrase = ''
  count = 0
  count1 = 0
  decode = ''
  while len(pass_phrase) < len(strng):
    if count >= len(passwd):
      count = 0
    if strng[count1] == ' ':
      pass_phrase += ' '
      count -= 1
    else:
      pass_phrase += passwd[count]
    count += 1
    count1 += 1

  for i in range(len(strng)):

    ref = (ord(strng[i]) - ord(pass_phrase[i])) + 97
    if ref == 97:
      ref = 6
    if ref - 97 >= 0:
      decode += chr(ref)
    else:
      decode += chr(ref + 26)
      
  return decode
  ...

def main():
  # open file for reading
  in_file = open ("cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

main()
