import bz2

__all__ = ["tinyCrypt"]


class tinyCrypt:
    secret = ""
    version = "1.0"


    def __init__(self, key = None):
        if key == None:
            key = "steganocryptosaurus"
        self.secret = key

    def crypt(self, message):
        """encode message to byteArray

        Args:
            message (str): message to crypt

        Returns:
            byteArray, byteArray: message encoded, byteArray-encoded length of message
        """
        coded = bz2.compress(bytes(message, 'utf-8'))
        bkey = self.getBytesKey(coded)

        bMess = bytearray()
        for i in range(len(coded)):
            car = ((coded[i] + bkey[i]) % 256)
            bMess.append(car)
        
        bMessage = []
        expandBytes(bMessage, bMess)
        
        return bMessage, self.cryptLength(len(bMessage))

    def checksum(self, array) -> int :
        chk = 0
        for i in reversed(array) :
            chk = ((chk *7) + i) % 97

        chk = chk % 49
        if chk % 10 > 5 : 
            chk = chk - 5


        return chk

    def cryptLength(self, length):
        bytes = length.to_bytes(3, byteorder='big')
        ress = []
        expandBytes(ress,bytes)

        chk = self.checksum(ress)
        
        unit = chk % 10
        diz  = chk//10

        ress.insert(0, unit)
        ress.append( diz)

        return ress

    def decryptLength(self, tabBytes):
        """decode length 

        Args:
            tabBytes (byteArray): encoded length of message

        Returns:
            int: length
        """
        
        # first chek data validity
        if len(tabBytes) != 14:
            return -1
        siz = tabBytes[1:-1]
        chk = tabBytes[0] + (10*tabBytes[-1])
        # verify checksum
        if self.checksum(siz) != chk:
            return -1


        tb = shrinkBytes(siz)

        return int.from_bytes(tb, byteorder='big')

    def getBytesKey(self, coded) :
        key = bz2.compress(bytes(self.secret,'utf-8'))

        if (len(key) < len(coded)):
            mult = len(coded)/len(key)
            key = key *int(mult+1)
        
        return key


    def decrypt(self, tabBytes):
        """decode message from byteArray

        Args:
            tabBytes (byteArray): encoded message

        Returns:
            str: human readable message
        """
        coded = shrinkBytes(tabBytes)

        bkey = self.getBytesKey(coded)
        bMess = bytearray()
        for i in range(len(coded)):
            car = ((coded[i] + 256 - bkey[i]) % 256)
            bMess.append(car)
        
        message = str(bz2.decompress(bMess), encoding='utf-8')

        return message

def expandBytes(tab, bmess):
    for val in bmess:
        tab.append(val % 4)
        tab.append((val >>2) %4)
        tab.append((val >>4) %4)
        tab.append((val >>6) %4)

def shrinkBytes( tabBytes):
    coded = bytearray()
    for v in range(0,len(tabBytes), 4):
        t = 0
        for w in range(4):
            t *= 4
            t += tabBytes[v+(3-w)]
        coded.append(t)
    
    return coded

def main():

    coder = tinyCrypt()

    orig = "un petit texte, sans prétention qui doit être encodé"
    b, lon = coder.crypt(orig)
    print(b, '  -  ' , lon)
    mess = coder.decrypt(b)
    print("------------------------------------")
    print(len(orig), " => ",len(b))
    print()
    print(mess[:150])





    # coder = tinyCrypt()
    # for val in (12,124,255,4512,100_000):
    #     t = coder.cryptLength(val)
    #     tot = coder.checksum(t[1:-1])
    #     print (val, " => ", t, " checksum : ", tot, 'decryptée : ', coder.decryptLength(t))    

    # val = 147
    # t = coder.cryptLength(val)
    # t[4] = 5
    # tot = coder.checksum(t[1:-1])
    # print (val, " => ", t, " checksum : ", tot, 'decryptée : ', coder.decryptLength(t))    

if __name__ == "__main__":
    # execute only if run as a script
    main()
