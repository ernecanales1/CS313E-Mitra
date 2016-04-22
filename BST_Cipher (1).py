
class Node (object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None
    
    
    def __str__(self):
        return str(self.data)

class Tree (object):
    def __init__(self, encrypt_str):
      self.root = None
      self.string = encrypt_str
      self.encrypt_tree()
      
    def search(self, key):
      encr_str = ''
      key = ord(key)
      #Tree is empty
      if self.root == None:
          return (encr_str)
      current = self.root
      

      while (current != None) and (current.data != key):
          if (key < current.data):
            current = current.lChild
            encr_str += '<'
          else:
            current = current.rChild
            encr_str += '>'

      if key == self.root.data:
          encr_str += '*'
      if current.data == key:
          encr_str += '!'
      return (encr_str)

    def encrypt(self, st):
        final_str = ''
        #convert to lower case
        st.lower()

        for i in st:
            if ord('a')<= ord(i) <= ord('z') or ord(i) == ord(' '):
                final_str += self.search(i)
            else:
                pass
        
        return (final_str[:-1])

    def encrypt_tree(self):
        #convert to lower case
        self.string.lower()
        l1 = []
        for i in self.string:
            if ord('a')<= ord(i) <= ord('z') or ord(i) == ord(' '):
                if i in l1:
                    pass
                else:
                    self.insert(i)
                l1.append(i)
            else:
                pass

    def insert(self, val):
        val = ord(val)
        newnode = Node(val)

        if (self.root == None):
            self.root = newnode
        else:
            current = self.root
            parent = self.root
            while current != None:
                parent = current
                if val < current.data:
                    current = current.lChild
                else:
                    current = current.rChild
            if val < parent.data:
                parent.lChild = newnode
            else:
                parent.rChild = newnode

    def traverse(self, st):
        string = st.split('!')
        str_re = ''

        for char in string:
            current = self.root
            for j in char:
                if j == '<':
                    current = current.lChild
                elif j == '>':
                    current = current.rChild
            if current == None:
                return ''
            else:
                str_re += chr(current.data)
        
        return str_re

    def decrypt(self, st):
        return (self.traverse(st))
                
def main():
    f = open('input.txt')
    s=0
    while(s<8):
        key = f.readline()
        encode = f.readline()
        decode = f.readline()
        skip = f.readline()
        s+=1
	
        t = Tree(key)
        t.encrypt_tree()
        print(t.encrypt(encode))
        print(t.decrypt(decode))
        print('')
	
    """key = input('Enter encryption key: ')
    print('\n')
    t1 = Tree(key)
    s = t1.encrypt_tree()
    string = input('Enter string to be encrypted: ')
    print('Encrypted string: ', t1.encrypt(string))
    print('\n')
    d_string = input('Enter string to be decrypted: ')
    print('Decrypted string: ', t1.decrypt(d_string))"""
main()
    
    
