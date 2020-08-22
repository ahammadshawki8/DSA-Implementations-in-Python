# Caesar_Cipher class

class CaesarCipher:
    
    def __init__(self,shift):
        encoder=["k"]*26
        decoder=["k"]*26
        
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord( "A" ))
            decoder[k] = chr((k - shift) % 26 + ord( "A" ))
            self.forward = "".join(encoder)
            self.backward = "".join(decoder)


    def encrypt(self, message):
        return self. transform(message, self.forward)


    def decrypt(self, secret):
        return self. transform(secret, self.backward)

    def transform(self, original, code):
        msg = list(original)
        
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord( "A" )
                msg[k] = code[j]
                
        return "".join(msg)

if __name__ == "__main__":
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE S."
    coded = cipher.encrypt(message)
    print( "Secret:" , coded)
    answer = cipher.decrypt(coded)
    print( "Message:" , answer)
