import math

number_dict = {'0':1,'1':2,'2':3,'3':4,'4':5,'5':6,'7':8,'8':9,'9':10}

word_dict= {'A':11,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'H':18,'I':19,'J':20,'K':21,'L':22,'M':23,'N':24,'O':25,'P':26,'Q':27,'R':28,'S':29,'T':30,'U':31,'V':32,'W':33,'X':34,'Y':35,'Z':36,
            'a':37,'b':38,'c':39,'d':40,'e':41,'f':42,'g':43,'h':44,'i':45,'j':46,'k':47,'l':48,'m':49,'n':50,'o':51,'p':52,'q':53,'r':54,'s':55,'t':56,'u':57,'v':58,'w':59,'x':60,'y':61,'z':62,' ':63}

word_dict.update(number_dict)

def encrypt_subs(plain_text,key):
    pt_len = len(plain_text)
    key_len = len(key)
    string = ""
    c=0
    for i in range(0,pt_len):
        if(i%key_len == 0):
            c=0
        val1 = word_dict[plain_text[i]]
        val2 = word_dict[key[c]]
        avg_val = (val1+val2)/2
        check_val = math.ceil(avg_val) - math.floor(avg_val)
        if(check_val):
            string += '$'+ str(list(word_dict.keys())[list(word_dict.values()).index(math.floor(avg_val))])+ str(list(word_dict.keys())[list(word_dict.values()).index(math.ceil(avg_val))]) + '$'
        else:
            string +=  str(list(word_dict.keys())[list(word_dict.values()).index(math.floor(avg_val))])
        c= c+1
    return string

def decrypt_subs(cipher_text,key):
    cipher_len = len(cipher_text)
    key_len = len(key)
    c = 0
    string = ""
    i=0
    try:   
        while(i<cipher_len):
            if(c%key_len == 0):
                c=0
            if(cipher_text[i] == '$'):
                val1 = word_dict[cipher_text[i+1]]
                val2 = word_dict[cipher_text[i+2]]
                final_val = val1 + val2 - word_dict[key[c]]
                string += str(list(word_dict.keys())[list(word_dict.values()).index(final_val)])
                i=i+4
            else:
                val1 = 2*word_dict[cipher_text[i]]
                final_val = val1 - word_dict[key[c]]
                string += str(list(word_dict.keys())[list(word_dict.values()).index(final_val)])
                i=i+1
            c = c+1
    except:
        print('Access denied, Please enter the right key')
        string = ""
    return string
    
plain_text = str(input('Enter the plain text: '))
key = str(input('Enter the key: '))
print(encrypt_subs(plain_text,key))
cipher_text = str(input('Enter the cipher text: '))
key = str(input('Enter the key: '))
print("plain text:",decrypt_subs(cipher_text,key))
