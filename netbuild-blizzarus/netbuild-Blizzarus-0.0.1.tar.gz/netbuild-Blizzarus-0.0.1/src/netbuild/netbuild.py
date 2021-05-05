# CAPSTONE Project program - Network Building Tool
# Author: Benjamin C. Lorentson
# This program will take input data on any IPv4 network build topology, and calculate subnetting and IP schema information

def main():

    running = True
    validation = True
    exceed = False

    #IPclean takes in an IPv4 address (as a list) and coverts any octet over 255 by increasing the prior octet, so 192.168.0.256 becomes 192.168.1.0, and 192.256.0.512 becomes 193.0.2.0; it returns the list with the converted values
    def IPclean(addr,exceed):
        if addr[3] > 255:
            iterations = int(addr[3] / 256)
            addr[3] -= iterations * 256
            addr[2] += iterations
        if addr[2] > 255:
            iterations2 = int(addr[2] / 256)
            addr[2] -= iterations2 * 256
            addr[1] += iterations2
        if addr[1] > 255:
            iterations3 = int(addr[1] / 256)
            addr[1] -= iterations3 * 256
            addr[0] += iterations3
        if addr[0] > 255:
            if exceed == False:
                print("WARNING: INVALID IPv4 ADDRESS.  IPv4 addresses cannot exceed 255.255.255.255.\nThe tool will continue subnetting, but all addresses from this point forward are invalid and unusable in a real-world scenario.")
                print()
                exceed = True
        return addr,exceed

    #IPreadable effectively 'un-splits' the list used to contain IPv4 addresses, converting it into the standard readable format for printing purposes
    def IPreadable(addr):
        read1 = str(addr[0])
        read2 = str(addr[1])
        read3 = str(addr[2])
        read4 = str(addr[3])
        readable = read1 + "." + read2 + "." + read3 + "." + read4
        return readable

    #CIDRfind uses pre-defined numbers from the Classless Inter-Domain Routing table, using the provided number of hosts to determine the subnet size and the subsequent netmask, wildcard, and difference from the FA to the LA
    def CIDRfind(subnets):
        if subnets <= 2:
            cidr = '30'
            increase = 1
            netmask = "255.255.255.252"
            wildcard = "0.0.0.3"
        elif subnets <= 6:
            cidr = '29'
            increase = 5
            netmask = "255.255.255.248"
            wildcard = "0.0.0.7"
        elif subnets <= 14:
            cidr = '28'
            increase = 13
            netmask = "255.255.255.240"
            wildcard = "0.0.0.15"
        elif subnets <= 30:
            cidr = '27'
            increase = 29
            netmask = "255.255.255.224"
            wildcard = "0.0.0.31"
        elif subnets <= 62:
            cidr = '26'
            increase = 61
            netmask = "255.255.255.192"
            wildcard = "0.0.0.63"
        elif subnets <= 126:
            cidr = '25'
            increase = 125
            netmask = "255.255.255.128"
            wildcard = "0.0.0.127"
        elif subnets <= 254:
            cidr = '24'
            increase = 253
            netmask = "255.255.255.0"
            wildcard = "0.0.0.255"
        elif subnets <= 510:
            cidr = '23'
            increase = 509
            netmask = "255.255.254.0"
            wildcard = "0.0.1.255"
        elif subnets <= 1022:
            cidr = '22'
            increase = 1021
            netmask = "255.255.252.0"
            wildcard = "0.0.3.255"
        elif subnets <= 2046:
            cidr = '21'
            increase = 2045
            netmask = "255.255.248.0"
            wildcard = "0.0.7.255"
        elif subnets <= 4094:
            cidr = '20'
            increase = 4093
            netmask = "255.255.240.0"
            wildcard = "0.0.15.255"
        elif subnets <= 8190:
            cidr = '19'
            increase = 8189
            netmask = "255.255.224.0"
            wildcard = "0.0.31.255"
        elif subnets <= 16382:
            cidr = '18'
            increase = 16381
            netmask = "255.255.192.0"
            wildcard = "0.0.63.255"
        elif subnets <= 32766:
            cidr = '17'
            increase = 32765
            netmask = "255.255.128.0"
            wildcard = "0.0.127.255"
        elif subnets <= 65534:
            cidr = '16'
            increase = 65533
            netmask = "255.255.0.0"
            wildcard = "0.0.255.255"
        elif subnets <= 131070:
            cidr = '15'
            increase = 131070
            netmask = "255.254.0.0"
            wildcard = "0.1.255.255"
        elif subnets <= 262142:
            cidr = '14'
            increase = 262141
            netmask = "255.252.0.0"
            wildcard = "0.3.255.255"
        elif subnets <= 524286:
            cidr = '13'
            increase = 524285
            netmask = "255.248.0.0"
            wildcard = "0.7.255.255"
        elif subnets <= 1048574:
            cidr = '12'
            increase = 1048573
            netmask = "255.240.0.0"
            wildcard = "0.15.255.255"
        elif subnets <= 2097150:
            cidr = '11'
            increase = 2097149
            netmask = "255.224.0.0"
            wildcard = "0.31.255.255"
        elif subnets <= 4194302:
            cidr = '10'
            increase = 4194301
            netmask = "255.192.0.0"
            wildcard = "0.63.255.255"
        elif subnets <= 8388606:
            cidr = '9'
            increase = 8388605
            netmask = "255.128.0.0"
            wildcard = "0.127.255.255"
        elif subnets <= 16777214:
            cidr = '8'
            increase = 16777213
            netmask = "255.0.0.0"
            wildcard = "0.255.255.255"
        elif subnets <= 33554430:
            cidr = '7'
            increase = 33554429
            netmask = "254.0.0.0"
            wildcard = "1.255.255.255"
        elif subnets <= 67108862:
            cidr = '6'
            increase = 67108861
            netmask = "252.0.0.0"
            wildcard = "3.255.255.255"
        elif subnets <= 134217726:
            cidr = '5'
            increase = 134217725
            netmask = "248.0.0.0"
            wildcard = "7.255.255.255"
        elif subnets <= 268435454:
            cidr = '4'
            increase = 268435453
            netmask = "240.0.0.0"
            wildcard = "15.255.255.255"
        elif subnets <= 536870910:
            cidr = '3'
            increase = 536870909
            netmask = "224.0.0.0"
            wildcard = "31.255.255.255"
        elif subnets <= 1073741822:
            cidr = '2'
            increase = 1073741821
            netmask = "192.0.0.0"
            wildcard = "63.255.255.255"
        elif subnets <= 2147483646:
            cidr = '1'
            increase = 2147483645
            netmask = "128.0.0.0"
            wildcard = "127.255.255.255"
        elif subnets <= 4294967294:
            cidr = '0'
            increase = 4294967293
            netmask = "0.0.0.0"
            wildcard = "255.255.255.255"
        else:
            cidr = 'Error'
            print()
            print("WARNING: The number of hosts in this subnet is invalid.  The tool will proceed as if there were 0 hosts in this subnet.")
            print()
            increase = 0
            netmask = "Invalid"
            wildcard = "Invalid"
        return cidr,netmask,wildcard,increase

    #IPv6input will take in an IPv6 address and perform validation and cleanup, storing it as the fully expanded version of the string
    def IPv6input():
        validation = True
        while validation:
            inputAddress = input("Enter an IPv6 address, separating each hextet with a colon --> ")
            inputAddress = inputAddress.lower()
            colonCount = inputAddress.count(":")
            if inputAddress.count("::") > 1 or inputAddress.count(":::") > 0 or inputAddress.count("::::") > 0 or inputAddress.count(":::::") > 0 or inputAddress.count("::::::") > 0 or inputAddress.count(":::::::") > 0:
                print()
                print("ERROR: Only one double-colon can be used.  Please input a valid IPv6 address.")
                print()
                continue
            elif colonCount > 7:
                print()
                print("ERROR: Too many colons.  Please input a valid IPv6 address.")
                print()
                continue
            elif inputAddress.startswith(":") == True and inputAddress.startswith("::") == False:
                print()
                print("ERROR: Cannot start address with a single colon.  Please input a valid IPv6 address.")
                print()
                continue
            elif inputAddress.count("::") == 1:
                doublecolon = True
            elif inputAddress.count("::") == 0:
                doublecolon = False

            if doublecolon == True:
                if inputAddress.endswith("::"):
                    missing = 9 - colonCount
                    zeroStr = (":0000" * missing)
                    inputAddress = inputAddress.replace("::",zeroStr)
                    address = inputAddress.split(":")
                elif inputAddress.startswith("::"):
                    missing = 9 - colonCount
                    zeroStr = ("0000:" * missing)
                    inputAddress = inputAddress.replace("::",zeroStr)
                    address = inputAddress.split(":")
                else:
                    missing = 8 - colonCount
                    zeroStr = (":")
                    zeroStr += ("0000:" * missing)
                    inputAddress = inputAddress.replace("::",zeroStr)
                    address = inputAddress.split(":")
            elif colonCount != 7:
                print()
                print("ERROR: There should be 8 hextets.  Please input a valid IPv6 address.")
                print()
                continue
            else:
                address = inputAddress.split(":")

            validation = False
            for x in range(0, len(address)):
                if len(address[x]) > 4 or address[x].isalnum() == False:
                    validation = True
                address[x] = address[x].zfill(4)
            if validation == True:
                print()
                print("ERROR: All hextets must consist of 4 characters or less, and can only include numbers and letters (a-f)")
                print()
                continue
            validation = False
            return address

    #IPv6calc will take in an IPv6 address as a list and ask the user for a prefix length.  It will then use that data to find the number of /64 networks, the IP range, and whether the address is a special IPv6 address
    def IPv6calc(address):
        validation = True
        while validation:
            print()
            print("Please select a prefix length...")
            print()
            print("1. /16")
            print("2. /32")
            print("3. /48")
            print("4. /64")
            print("5. /80")
            print("6. /96")
            print("7. /112")
            print("8. /128")
            print()
            prefixChoice = input("Choose a prefix length: ")
            prefixChoice = prefixChoice.lstrip("/")
            if prefixChoice == '1' or prefixChoice == '16':
                prefix = '/16'
                validation = False
            elif prefixChoice == '2' or prefixChoice == '32':
                prefix = '/32'
                validation = False
            elif prefixChoice == '3' or prefixChoice == '48':
                prefix = '/48'
                validation = False
            elif prefixChoice == '4' or prefixChoice == '64':
                prefix = '/64'
                validation = False
            elif prefixChoice == '5' or prefixChoice == '80':
                prefix = '/80'
                validation = False
            elif prefixChoice == '6' or prefixChoice == '96':
                prefix = '/96'
                validation = False
            elif prefixChoice == '7' or prefixChoice == '112':
                prefix = '/112'
                validation = False
            elif prefixChoice == '8' or prefixChoice == '128':
                prefix = '/128'
                validation = False
            else:
                print()
                print("ERROR: Please select a valid option.")
                print()

        special = ""
        if address[0] == '2001' and address[1] == '0db8' and prefix == '/32':
            special = "This is a Documentation IPv6 Address"
        elif address[0] == '0000' and address[1] == '0000' and address[2] == '0000' and address[3] == '0000' and address[4] == '0000' and address[5] == '0000' and address[6] == '0000' and address[7] == '0001' and prefix == '/128':
            special = "This is the loopback IPv6 address."
        elif address[0] == '0000' and address[1] == '0000' and address[2] == '0000' and address[3] == '0000' and address[4] == '0000' and address[5] == 'ffff' and prefix == '/96':
            special = "This address is in the IPv4 mapped-address range."
        else:
            special = "This is not a special IPv6 Address."
            
        lowIP = address.copy()
        highIP = address.copy()
        if prefix == '/128':
            SFnets = '0'
            if special == "This is not a special IPv6 Address.":
                special = "This is a single-address network, since the entire address is the prefix; it is highly unlikely you would use this address in a real-world scenario."
        elif prefix == '/112':
            SFnets = '0'
            lowIP[7] = '0000'
            highIP[7] = 'ffff'
        elif prefix == '/96':
            SFnets = '0'
            lowIP[6] = lowIP[7] = '0000'
            highIP[6] = highIP[7] = 'ffff'
        elif prefix == '/80':
            SFnets = '0'
            lowIP[5] = lowIP[6] = lowIP[7] = '0000'
            highIP[5] = highIP[6] = highIP[7] = 'ffff'
        elif prefix == '/64':
            SFnets = '1'
            lowIP[4] = lowIP[5] = lowIP[6] = lowIP[7] = '0000'
            highIP[4] = highIP[5] = highIP[6] = highIP[7] = 'ffff'
        elif prefix == '/48':
            SFnets = '65536'
            lowIP[3] = lowIP[4] = lowIP[5] = lowIP[6] = lowIP[7] = '0000'
            highIP[3] = highIP[4] = highIP[5] = highIP[6] = highIP[7] = 'ffff'
        elif prefix == '/32':
            SFnets = '4,294,967,296'
            lowIP[2] = lowIP[3] = lowIP[4] = lowIP[5] = lowIP[6] = lowIP[7] = '0000'
            highIP[2] = highIP[3] = highIP[4] = highIP[5] = highIP[6] = highIP[7] = 'ffff'
        elif prefix == '/16':
            SFnets = '281,474,976,710,656'
            lowIP[1] = lowIP[2] = lowIP[3] = lowIP[4] = lowIP[5] = lowIP[6] = lowIP[7] = '0000'
            highIP[1] = highIP[2] = highIP[3] = highIP[4] = highIP[5] = highIP[6] = highIP[7] = 'ffff'
        else:
            print()
            print("ERROR: Invalid Prefix.")
            SFnets = '0'
        return prefix, special, SFnets, lowIP, highIP
        


    #IPv6expanded will unsplit an IPv6 address stored as a list and return a string with colon separators, but will NOT display the compressed version of the IPv6 address
    def IPv6expanded(addr):
        read1 = str(addr[0])
        read2 = str(addr[1])
        read3 = str(addr[2])
        read4 = str(addr[3])
        read5 = str(addr[4])
        read6 = str(addr[5])
        read7 = str(addr[6])
        read8 = str(addr[7])
        expanded = read1 + ":" + read2 + ":" + read3 + ":" + read4 + ":" + read5 + ":" + read6 + ":" + read7 + ":" + read8
        return expanded

    #IPv6compressed will unsplit an IPv6 address stored as a list and return a string with colon separators, and WILL compress it into the correct shorthand version of the address
    def IPv6compressed(addr):
        for x in range (0,8):
            addr[x] = addr[x].lstrip('0')
            if addr[x] == '':
                addr[x] = '0'

        if addr.count('0') == 2:
            addrCopy = addr.copy()
            pos1 = addrCopy.index('0')
            addrCopy[pos1] = 'nil'
            pos2 = addrCopy.index('0')
            if pos1+1 == pos2:
                addr[pos1] = ''
                addr[pos2] = ''
        elif addr.count('0') == 3:
            addrCopy = addr.copy()
            pos1 = addrCopy.index('0')
            addrCopy[pos1] = 'nil'
            pos2 = addrCopy.index('0')
            addrCopy[pos2] = 'nil'
            pos3 = addrCopy.index('0')
            if pos1+1 == pos2:
                if pos2+1 == pos3:
                    addr[pos1] = ''
                    addr[pos2] = ''
                    addr[pos3] = ''
                else:
                    addr[pos1] = ''
                    addr[pos2] = ''
            elif pos2+1 == pos3:
                addr[pos2] = ''
                addr[pos3] = ''
        elif addr.count('0') == 4:
            addrCopy = addr.copy()
            pos1 = addrCopy.index('0')
            addrCopy[pos1] = 'nil'
            pos2 = addrCopy.index('0')
            addrCopy[pos2] = 'nil'
            pos3 = addrCopy.index('0')
            addrCopy[pos3] = 'nil'
            pos4 = addrCopy.index('0')
            if pos1+1 == pos2:
                if pos2+1 == pos3:
                    if pos3+1 == pos4:
                        addr[pos1] = ''
                        addr[pos2] = ''
                        addr[pos3] = ''
                        addr[pos4] = ''
                    else:
                        addr[pos1] = ''
                        addr[pos2] = ''
                        addr[pos3] = ''
                else:
                    addr[pos1] = ''
                    addr[pos2] = ''
            elif pos2+1 == pos3:
                if pos3+1 == pos4:
                    addr[pos2] = ''
                    addr[pos3] = ''
                    addr[pos4] = ''
                else:
                    addr[pos2] = ''
                    addr[pos3] = ''
            elif pos3+1 == pos4:
                addr[pos3] = ''
                addr[pos4] = ''
        elif addr.count('0') == 5:
            addrCopy = addr.copy()
            pos1 = addrCopy.index('0')
            addrCopy[pos1] = 'nil'
            pos2 = addrCopy.index('0')
            addrCopy[pos2] = 'nil'
            pos3 = addrCopy.index('0')
            addrCopy[pos3] = 'nil'
            pos4 = addrCopy.index('0')
            addrCopy[pos4] = 'nil'
            pos5 = addrCopy.index('0')
            if pos1+1 == pos2 and pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5:
                addr[pos1] = ''
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
            elif pos1+1 == pos2 and pos2+1 == pos3 and pos3+1 == pos4:
                addr[pos1] = ''
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
            elif pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5:
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
            elif pos1+1 == pos2 and pos2+1 == pos3:
                addr[pos1] = ''
                addr[pos2] = ''
                addr[pos3] = ''
            elif pos2+1 == pos3 and pos3+1 == pos4:
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
            elif pos3+1 == pos4 and pos4+1 == pos5:
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
            elif pos1+1 == pos2:
                addr[pos1] = ''
                addr[pos2] = ''
            elif pos2+1 == pos3:
                addr[pos2] = ''
                addr[pos3] = ''
            elif pos3+1 == pos4:
                addr[pos3] = ''
                addr[pos4] = ''
            elif pos4+1 == pos5:
                addr[pos4] = ''
                addr[pos5] = ''
        elif addr.count('0') == 6:
            addrCopy = addr.copy()
            pos1 = addrCopy.index('0')
            addrCopy[pos1] = 'nil'
            pos2 = addrCopy.index('0')
            addrCopy[pos2] = 'nil'
            pos3 = addrCopy.index('0')
            addrCopy[pos3] = 'nil'
            pos4 = addrCopy.index('0')
            addrCopy[pos4] = 'nil'
            pos5 = addrCopy.index('0')
            addrCopy[pos5] = 'nil'
            pos6 = addrCopy.index('0')
            if pos1+1 == pos2 and pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5 and pos5+1 == pos6:
                addr[pos1] = ''
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
                addr[pos6] = ''
            elif pos1+1 == pos2 and pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5:
                addr[pos1] = ''
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
            elif pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5 and pos5+1 == pos6:
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
                addr[pos6] = ''
            elif pos1+1 == pos2 and pos2+1 == pos3 and pos3+1 == pos4:
                addr[pos1] = ''
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
            elif pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5:
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
            elif pos3+1 == pos4 and pos4+1 == pos5 and pos5+1 == pos6:
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
                addr[pos6] = ''
            elif pos1+1 == pos2 and pos2+1 == pos3:
                addr[pos1] = ''
                addr[pos2] = ''
                addr[pos3] = ''
            elif pos2+1 == pos3 and pos3+1 == pos4:
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
            elif pos3+1 == pos4 and pos4+1 == pos5:
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
            elif pos4+1 == pos5 and pos5+1 == pos6:
                addr[pos4] = ''
                addr[pos5] = ''
                addr[pos6] = ''
            elif pos1+1 == pos2:
                addr[pos1] = ''
                addr[pos2] = ''
        elif addr.count('0') == 7:
            addrCopy = addr.copy()
            pos1 = addrCopy.index('0')
            addrCopy[pos1] = 'nil'
            pos2 = addrCopy.index('0')
            addrCopy[pos2] = 'nil'
            pos3 = addrCopy.index('0')
            addrCopy[pos3] = 'nil'
            pos4 = addrCopy.index('0')
            addrCopy[pos4] = 'nil'
            pos5 = addrCopy.index('0')
            addrCopy[pos5] = 'nil'
            pos6 = addrCopy.index('0')
            addrCopy[pos6] = 'nil'
            pos7 = addrCopy.index('0')
            if pos1+1 == pos2 and pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5 and pos5+1 == pos6 and pos6+1 == pos7:
                addr[pos1] = ''
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
                addr[pos6] = ''
                addr[pos7] = ''
            elif pos1+1 == pos2 and pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5 and pos5+1 == pos6:
                addr[pos1] = ''
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
                addr[pos6] = ''
            elif pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5 and pos5+1 == pos6 and pos6+1 == pos7:
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
                addr[pos6] = ''
                addr[pos7] = ''
            elif pos1+1 == pos2 and pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5:
                addr[pos1] = ''
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
            elif pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5 and pos5+1 == pos6:
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
                addr[pos6] = ''
            elif pos3+1 == pos4 and pos4+1 == pos5 and pos5+1 == pos6 and pos6+1 == pos7:
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
                addr[pos6] = ''
                addr[pos7] = ''
            elif pos1+1 == pos2 and pos2+1 == pos3 and pos3+1 == pos4:
                addr[pos1] = ''
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
            elif pos2+1 == pos3 and pos3+1 == pos4 and pos4+1 == pos5:
                addr[pos2] = ''
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
            elif pos3+1 == pos4 and pos4+1 == pos5 and pos5+1 == pos6:
                addr[pos3] = ''
                addr[pos4] = ''
                addr[pos5] = ''
                addr[pos6] = ''
            elif pos4+1 == pos5 and pos5+1 == pos6 and pos6+1 == pos7:
                addr[pos4] = ''
                addr[pos5] = ''
                addr[pos6] = ''
                addr[pos7] = ''


        read1 = str(addr[0])
        read2 = str(addr[1])
        read3 = str(addr[2])
        read4 = str(addr[3])
        read5 = str(addr[4])
        read6 = str(addr[5])
        read7 = str(addr[6])
        read8 = str(addr[7])
        compressed = read1 + ":" + read2 + ":" + read3 + ":" + read4 + ":" + read5 + ":" + read6 + ":" + read7 + ":" + read8
        while compressed.count(":::") >= 1:
            compressed = compressed.replace(':::', '::')
            
        return compressed
        
        
            
            

    #Walkthrough Mode - Will give the user detailed explanations of data to enter and what the program is doing at each step, and explain the process of subnetting an IPv4 network build along the way
    def walkthrough():
        print("\n" * 5)
        print("====== Beginning Walktrhough Mode ======")
        print("\n" * 5)
        print("------ WALKTHROUGH MODE: STEP 1 - Count your Subnets")
        print("\n")
        print('Let’s get started!  First, we’ll collect some data from your network build.')
        print()
        print('First, we need to know how many separate subnetworks are in the build.')
        print('Every  COLLISION DOMAIN comprises a single subnetwork, so you’ll need to count the')
        print('number of collision domains in your network.  To find this, look for the ROUTERS on your')
        print('network topography; each uniuqe connection from a router to a set of other devices is one')
        print('collision domain, regardless of how many other devices it connects to.  In short, you')
        print('will have one subnet for each port on a router that connects to something.')
        print()
        print("Count your subnets, and remember the number.  Next, you'll count any Point-to-Point connections.")
        print()
        print('Point-to-Point connections are links DIRECTLY from one router to another.  Each PtP connection')
        print('counts as one subnet.  For example, if there are two routers in your build, with a link between them, then')
        print('you have one PtP subnet.  If there is only one router, there will be no PtP connections.')
        print()
        print('Count the number of PtP subnets, and add that to the number of subnets you counted before.')
        print('Type the TOTAL number of subnets, including the PtP subnets, below.')
        #Get subnet count and validate
        print()
        print("<INPUT>")
        print()
        validation = True
        while validation:
            subnetCount = input("Total number of Subnets (type a number): ")
            if subnetCount.isnumeric() == False:
                print()
                print("ERROR: Please type a positive number for the subnet count.")
                print()
                validation = True
            else:
                validation = False
            
        
        subnetInt = int(subnetCount)
        if subnetInt < 1:
            print("WARNING: Subnet Count is less than 1.  No subnet information will be generated - use only for tutorial purposes.")
            print()
        print()
        print("\n" * 5)
        print("------ WALKTHROUGH MODE: STEP 2")
        print("\n")
        print('Secondly, we need to determine the size of each subnet.  We’ll assign a name to each')
        print('subnet so it will be easier to read later. Your network build will likely show groups of')
        print('hosts using a computer or laptop icon, with a name like “ACCOUNTING” or “SALES” by it.')
        print('Next to this name there will be a number, telling you how many HOSTS (devices) will be on')
        print('that network.  When prompted below, type the name of the largest subnet first (or, the one with')
        print('the most hosts).  After typing the names, type in the number of hosts the correspond to each name.')
        print()
        print('If there are any point-to-point connections, there may not be a name on the network build, so')
        print('you can call them something simple like "p2p" or "ptp."  Just make sure, if there are multiple')
        print('point-to-point connections, that each one has a different name.  Each PtP subnet has exactly 2')
        print('hosts on it, so when prompted for a number of hosts, type "2."')
        #Get names and host counts for each subnet
        validation = True
        while validation:
            print()
            print("<INPUT>")
            print()
            subnetNames = []
            for i in range (0, subnetInt):
                j = i+1
                counter = str(j)
                name = input("Name for subnet #" + counter + ": ")
                subnetNames.append(name)

            subnets = []
            for i in range (0, subnetInt):
                validate = True
                while validate:
                    if i == 0:
                        hosts = input("Number of hosts in the " + subnetNames[i] + " subnet (type a number): ")
                    else:
                        hosts = input("Number of hosts in the " + subnetNames[i] + " subnet: ")
                    if hosts.isnumeric() == False:
                        print("ERROR: Number of hosts must be an integer value and cannot be negative.  Please enter a valid number of hosts.")
                        print()
                        continue
                    else:
                        validate = False
                    hostInt = int(hosts)
                    subnets.append(hostInt)

            if subnets != sorted(subnets, reverse=True):
                print()
                print("ERROR: You have inputted your subnets in a non-descending order.  Subnetting should always start with the largest subnet and work downwards from there.")
                print("Please re-enter your subnet information, making sure to input the largest subnet first and the smallest last")
                print("Note that subnets of equal size, such as point-to-point networks, can be entered in any order.")
                print()
                validation = True
            else:
                validation = False
        
        print("\n" * 5)
        print("------ WALKTHROUGH MODE: STEP 3")
        print("\n")
        print('Third, let’s determine the starting address.  This is the address that we can begin subnetting')
        print('from, and should be provided with your network build.  In a business scenario, this would')
        print('represent the first address that is not already being used somewhere else in the business.  If')
        print('there is no address provided, or if you are just building on your own, it is recommended you use')
        print('the standard Class C private address range, starting at 192.168.0.0.')
        print()
        print('NOTE: Type the IP address carefully; make sure the numbers are right, and that each octet is')
        print('separated by a “.” just like in the address above.  Otherwise, the program may misread it.')
        print()
        print("<INPUT>")
        print()
        #get starting IP address
        validation = True
        while validation:
            startAddress = input("Starting IP address: ")
            address = startAddress.split(".")
            if len(address) != 4:
                print("ERROR: IP address must be four positive numerals with periods separating them.  Please enter a valid IP address.")
                print()
                continue
            elif address[0].isnumeric() == False or address[1].isnumeric() == False or address[2].isnumeric() == False or address[3].isnumeric() == False:
                print("ERROR: IP address must be four positive numerals with periods separating them.  Please enter a valid IP address.")
                print()
                continue
            else:
                validation = False
            map_object = map(int, address)
            listAddress = list(map_object)
            if listAddress[0] > 255 or listAddress[1] > 255 or listAddress[2] > 255 or listAddress[3] > 255:
                print("ERROR: IP address must consist of four octets with values between 0 and 255.  Please enter a valid IP address.")
                print()
                continue
            else:
                validation = False
        print("\n" * 5)
        print("------ WALKTHROUGH MODE: STEP 4")
        print("\n")
        print('Now that we have the data needed, let’s start subnetting!  First, let’s determine the IP Address')
        print('Class you’re using, and whether it’s a private or public address.  For Private addresses, the tool')
        print('will also tell you if it’s one of the standard private IP ranges (RFC1918), if it is an Automatic')
        print('Private IP Address (APIPA), or if it is in the loopback address block (localhost).  You might not')
        print('need all this information for every build, but it’s always good to know what you’re working with…')
        print()
        print("<OUTPUT>")
        print()
        #Calculate data for output
        
        exceed = False
        listAddress,exceed = IPclean(listAddress,exceed)
        #Determine address class
        if listAddress[0] >= 0 and listAddress[0] <= 127:
            addressClass = 'A'
        elif listAddress[0] >= 128 and listAddress[0] <= 191:
            addressClass = 'B'
        elif listAddress[0] >= 192 and listAddress[0] <= 223:
            addressClass = 'C'
        elif listAddress[0] >= 224 and listAddress[0] <= 239:
            addressClass = 'D'
        elif listAddress[0] >= 240 and listAddress[0] <= 255:
            addressClass = 'E'
        else:
            print("WARNING: You are using an invalid IPv4 address.  Valid IPv4 addresses must have a value between 0 and 255 in EVERY octet.")
            print("If you wish to start again with a valid IPv4 address, restart the Network Building Tool.  If you wish to continue, the tool will proceed using the invalid address.")
            print()
            addressClass = 'Invalid'

        #Check if address is private (Localhost, APIPA, or one of the standard RFC 1918 private IP ranges) or public
        if listAddress[0] == 10:
            privacy = "Private (RFC 1918)"
        elif listAddress[0] == 127:
            privacy = "Private (Localhost)"
        elif listAddress[0] == 169 and listAddress[1] == 254:
            privacy = "Private (APIPA)"
        elif listAddress[0] == 172 and listAddress[1] >= 16 and listAddress[1] <= 31:
            privacy = "Prviate (RFC 1918)"
        elif listAddress[0] == 192 and listAddress[1] == 168:
            privacy = "Private (RFC 1918)"
        elif addressClass == 'Invalid':
            privacy = "Public (INVALID)"
        else:
            privacy = "Public"

        print("Starting IP address: ", end =" ")
        print(IPreadable(listAddress))
        print("Address Class: " + addressClass)
        print("This is a " + privacy + " IP Address")
        print()
        pause = input("Press enter to continue...")
        
        print("\n" * 5)
        print("------ WALKTHROUGH MODE: STEP 5")
        print("\n")
        print('Next we’ll calculate the info you need for each subnet.  The key to subnetting is using the')
        print('Classless Inter-Domain Routing (CIDR) table.  Each subnet will have a CIDR notation, like “/24”')
        print('or “/30”, which corresponds to the size of the subnet.  Each CIDR notation corresponds to a')
        print('certain number of available addresses, as well as a certain subnet mask.')
        print()
        print('This is the key information you need for subnetting.  You’ll need each subnet’s Network Address')
        print('(NA), First Available Address (FA), Last Available Address (LA), and Broadcast Address (BA). ')
        print('You’ll also need the aforementioned Subnet Mask (SM).')
        print()
        print('The tool will determine, based on the number of hosts you provided, which CIDR notation is')
        print('used for each subnet.  This tells it the subnet mask, and how many addresses will be allocated')
        print('to the subnet, allowing it to calculate the NA, FA, LA, and BA, as follows…')
        print()
        print('The NA is the very first address of the subnet.  The FA is the next address after the NA.  The LA')
        print('is equal to the NA + the number of hosts that CIDR notation supports.  The BA is the next')
        print('address after the LA.  Then, the following address is the NA of the next subnet.')
        print()
        print()
        print('Here is the subnetting information for each of the subnets you inputted.  The wildcard mask is')
        print('also displayed; this is essentially the inverse of the subnet mask.  You may need this for some')
        print('network builds, but you can ignore it for the basic subnetting part.')
        print()
        print('Remember, those /30 subnets that have only two hosts are most likely your point-to-point')
        print('connections that directly connect two routers.  The first available address should be one router,')
        print('and the last available is the other router.')
        print()
        pause = input("Press enter to show output...")
        print()
        print("<OUTPUT>")
        print()
        
        #Loop to display subnetting information for each host group
        for x in range(0, subnetInt):
            y = x+1
            counter = str(y)
            hostCount = str(subnets[x])

            #determine CIDR using the CIDRfind function
            cidr,netmask,wildcard,increase = CIDRfind(subnets[x])

            
            print(subnetNames[x] + " Subnet (" + hostCount + " hosts)...")
            print()
            print("CIDR Notation = /" + cidr)
            print()
            print("Subnet Mask: " + netmask)
            print()
            print("Wildcard Mask: " + wildcard)
            print()
            print()
            print("Network Address: ", end=" ")
            print(IPreadable(listAddress))
            listAddress[3] += 1
            listAddress,exceed = IPclean(listAddress,exceed)
            print("First Available Host Address: ", end=" ")
            print(IPreadable(listAddress))
            listAddress[3] += increase
            listAddress,exceed = IPclean(listAddress,exceed)
            print("Last Available Host Address: ", end=" ")
            print(IPreadable(listAddress))
            listAddress[3] += 1
            listAddress,exceed = IPclean(listAddress,exceed)
            print("Broadcast Address: ", end=" ")
            print(IPreadable(listAddress))
            print()
            print()
            listAddress[3] += 1
            listAddress,exceed = IPclean(listAddress,exceed)
            
        print("\n" * 5)
        pause = input("All done!  Press enter to bring up the main menu again (your output will not be cleared)...")
        print()
            

    #Quickstart Mode - Will take in the basic information of a network build and provide a quick and simple ouput page, for automated subnetting or error checking
    def quickstart():
        print("\n" * 5)
        print("====== Beginning Quick Start Mode ======")
        print("\n" * 5)
        print("------ QUICK START MODE: INPUT DATA")
        print()
        

        #Get number of subnets and the hosts count for each one, and validate
        print()
        print('Enter the following data.  Type IP addresses correctly, with a period "." separating the octets (ex. "192.168.0.0" or "10.0.0.0")')
        print()
        
        validation = True
        while validation:
            subnetCount = input("No. of Subnets (type a number): ")
            if subnetCount.isnumeric() == False:
                print()
                print("ERROR: Please type a positive number for the subnet count.")
                print()
                validation = True
            else:
                validation = False

        subnetInt = int(subnetCount)
        if subnetInt < 1:
            print("WARNING: Subnet Count is less than 1.  No subnet information will be generated - use only to check address classes.")
            print()

        
        subnets = []
        for i in range (0, subnetInt):
            j = i+1
            counter = str(j)
            validation = True
            while validation:
                if i == 0:
                    hosts = input("No. of hosts in subnet " + counter + " (largest first): ")
                else:
                    hosts = input("No. of hosts in subnet " + counter + ": ")
                if hosts.isnumeric() == False:
                    print("ERROR: Number of hosts must be an integer value and cannot be negative.  Please enter a valid number of hosts.")
                    print()
                    continue
                else:
                    validation = False
                hostInt = int(hosts)
                subnets.append(hostInt)

        #check that user inputted the largest subnet first.  If not, offer to sort the subnets correctly.
        if subnets != sorted(subnets, reverse=True):
                    print("WARNING: Subnets not entered in proper order.  It is recommended that you subnet using the largest subnet first.")
                    validation = True
                    while validation:
                        sortChoice = input("Would you like to sort your subnets to use the largest first? [Y/N]")
                        if sortChoice == 'Y' or sortChoice == 'y':
                            print()
                            print("Confirmed.  Subnets will be sorted in order from largest to smallest.")
                            subnets = sorted(subnets, reverse=True)
                            validation = False
                        elif sortChoice == 'N' or sortChoice == 'n':
                            print()
                            print("Confirmed.  Subnetting will occur in the order the subnets were entered; note that this scenario may not be realisitc or correct.")
                            validation = False
                        else:
                            print()
                            print("Invalid selection.  Please enter a valid option.")
                            print()
                            validation = True   
        print()

        #get starting IP address and validate
        validation = True
        while validation:
            startAddress = input("Starting IP address: ")
            address = startAddress.split(".")
            if len(address) != 4:
                print("ERROR: IP address must be four positive numerals with periods separating them.  Please enter a valid IP address.")
                print()
                continue
            elif address[0].isnumeric() == False or address[1].isnumeric() == False or address[2].isnumeric() == False or address[3].isnumeric() == False:
                print("ERROR: IP address must be four positive numerals with periods separating them.  Please enter a valid IP address.")
                print()
                continue
            else:
                validation = False
            map_object = map(int, address)
            listAddress = list(map_object)
            if listAddress[0] > 255 or listAddress[1] > 255 or listAddress[2] > 255 or listAddress[3] > 255:
                print("ERROR: IP address must consist of four octets with values between 0 and 255.  Please enter a valid IP address.")
                print()
                continue
            else:
                validation = False
        #address = exploded string of startAddress with four fields, one for each octet
        #map_object and listAddress used to map and create a list of integer values, so that numeric operations can be performed on each octet and values over 255 can be converted
        print("\n" * 5)
        print("------ QUICK START MODE: OUTPUT")
        print()
        print("Here's a summary of your network build...")
        print()
        #Use IPclean function to convert numbers over 255 into proper IPv4 address format; pass and return the 'exceed' Boolean so that the warning message only triggers once
        exceed = False
        listAddress,exceed = IPclean(listAddress,exceed)
        #Determine address class
        if listAddress[0] >= 0 and listAddress[0] <= 127:
            addressClass = 'A'
        elif listAddress[0] >= 128 and listAddress[0] <= 191:
            addressClass = 'B'
        elif listAddress[0] >= 192 and listAddress[0] <= 223:
            addressClass = 'C'
        elif listAddress[0] >= 224 and listAddress[0] <= 239:
            addressClass = 'D'
        elif listAddress[0] >= 240 and listAddress[0] <= 255:
            addressClass = 'E'
        else:
            print("WARNING: You are using an invalid IPv4 address.  Valid IPv4 addresses must have a value between 0 and 255 in EVERY octet.")
            print("If you wish to start again with a valid IPv4 address, restart the Network Building Tool.  If you wish to continue, the tool will proceed using the invalid address.")
            print()
            addressClass = 'Invalid'

        #Check if address is private (Localhost, APIPA, or one of the standard RFC 1918 private IP ranges) or public
        if listAddress[0] == 10:
            privacy = "Private (RFC 1918)"
        elif listAddress[0] == 127:
            privacy = "Private (Localhost)"
        elif listAddress[0] == 169 and listAddress[1] == 254:
            privacy = "Private (APIPA)"
        elif listAddress[0] == 172 and listAddress[1] >= 16 and listAddress[1] <= 31:
            privacy = "Prviate (RFC 1918)"
        elif listAddress[0] == 192 and listAddress[1] == 168:
            privacy = "Private (RFC 1918)"
        elif addressClass == 'Invalid':
            privacy = "Public (INVALID)"
        else:
            privacy = "Public"


        
            
        print("Starting IP address: ", end =" ")
        print(IPreadable(listAddress))
        print("Address Class: " + addressClass)
        print("This is a " + privacy + " IP Address")
        print()
        print()


        #Loop to display subnetting information for each host group
        for x in range(0, subnetInt):
            y = x+1
            counter = str(y)
            hostCount = str(subnets[x])

            #determine CIDR using the CIDRfind function
            cidr,netmask,wildcard,increase = CIDRfind(subnets[x])

            
            print("Subnet #" + counter + " (" + hostCount + " hosts)...")
            print()
            print("CIDR Notation = /" + cidr)
            print("Netmask: " + netmask)
            print("Wildcard: " + wildcard)
            print()
            print("NA: ", end=" ")
            print(IPreadable(listAddress))
            listAddress[3] += 1
            listAddress,exceed = IPclean(listAddress,exceed)
            print("FA: ", end=" ")
            print(IPreadable(listAddress))
            listAddress[3] += increase
            listAddress,exceed = IPclean(listAddress,exceed)
            print("LA: ", end=" ")
            print(IPreadable(listAddress))
            listAddress[3] += 1
            listAddress,exceed = IPclean(listAddress,exceed)
            print("BA: ", end=" ")
            print(IPreadable(listAddress))
            print()
            print()
            listAddress[3] += 1
            listAddress,exceed = IPclean(listAddress,exceed)

        print("\n" * 5)
        pause = input("All done!  Press enter to bring up the main menu again (your output will not be cleared)...")
        print()
            
        # Loop: For each value of Subnets[x], print the CIDR notation, netmask and wildcard.  Then increase the listAddress and print the Network Address, First Available, Last Available, and Broadcast Address
        # CIDR is calculated first to determine the increase variable (increase is 1 less than that CIDR's maximum # of hosts, so a /25 would be 125

        # 1st NA is start address, FA is NA +1, LA is FA + increase by CIDR (max hosts - 1), BA = FA +1; then the next NA for the next Subnet is the last BA+1
        # After each increase, run the address array through a function that will ask if any number is over 255, and if it is, subtract 256 [NOT 255] and add 1 to the prior field



    #IPv6 Mode - This will allow the user to compress or expand IPv6 addresses, and provides a basic IPv6 subnetting tutorial
    def v6():
        #Begin with IPv6 addressing basics and examples
        print("\n" * 5)
        print("====== Beginning IPv6 Guide Mode ======")
        print("\n" * 5)
        print("------ IPv6 MODE: IPv6 ADDRESSING GUIDE")
        print()
        print("IPv6 is a newer method for managing IP addresses, which avoids the (relatively speaking) small address")
        print("space available with IPv4 addresses.  Where an IPv4 address has only 32 bits, and IPv6 address has 128.")
        print("This drastically increases the number of possible addresses, so much so that it is pretty much impossible")
        print("to run out, no matter how many devices we use.  For reference, there are 3.4 x 10^38 IPv6 addresses that")
        print("can be used, or 340,282,366,920,938,000,000,000,000,000,000,000,000 unique addresses.")
        print()
        print("So, safe to say, we probably won't be running out of addresses... ever.  This makes subnetting a little")
        print("easier in some ways, as we don't need to worry about things like subnet masks or running out of addresses,")
        print("and there is little math that really needs to be done.  You can do it very easily just by understanding the format")
        print("of an IPv6 address, and how hexadecimals work.")
        print()
        pause = input("Press enter to continue...")
        print("\n" * 5)
        print("Hexadeciamls work like this: instead of the base 10 system we normally use for numbers, they use a base 16 system.")
        print("Each 'digit' can be a number from 0 to 9, or a letter from a to f.  'a' represents 10, 'f' represents 15.  This")
        print("gives us 16 total options.  Each hexadecimal digit is equal to 4 bits in binary.")
        print()
        print("Looking at an IPv6 address, there are 128 bits, meaning there are 32 digits in the address.  They are separated into")
        print("blocks of four, called 'hextets,' and these are divided into three sections.  The first section is the site prefix,")
        print("the second is the subnet ID, and the third is the interface ID.")
        print()
        print("The typical IPv6 address format uses 48 bits for the site prefix; this is called a /48 address (you can think of this as")
        print("the IPv6 version of the CIDR /24, /30, etc. used in IPv4.  48 bits means three hextets, so a /48 IPv6 address has three hextets")
        print("of site prefix.  The Subnet ID is 16 bits, represented by the fourth hextet; this is used for subnetting with IPv6, so there is.")
        print("no need for as subnet mask.  Finally, the last 64 bits (and thus the final four hextets) represent the Interface ID, which")
        print("is where individual addresses for each device are assigned, usually automatically via DHCP.")
        print()
        print("Example IPv6 address ---> 2001:0db8:85a3:0000:0000:8a2e:0370:7334")
        print("                          [            ] [  ] [                 ]")
        print("                           Site Prefix  Subnet   Interface ID")
        print()
        pause = input("Press enter to continue...")
        print("\n" * 5)
        print("When writing IPv6 addresses, the hextets are separated by colons ':', and leading 0s are removed from each hextet.  This")
        print("means that in the example above, the '0db8' in the second hextet would be written as just 'db8'.  In addition, if there are")
        print("multiple hextets of all zeroes right next to each other, you can remove all the zeroes entirely and write them as just two colons")
        print("side by side, like this '::'.  So, the example above would be written as '2001:db8:85a3::8a2e:370:7334', where the double colon")
        print("signifies two hextets of all zeroes.  Note that you can only do this in ONE place, even if there are multiple sets of all zeroes.")
        print()
        print("Take the following ---> 2001:0db8:00a3:0000:0000:8203:0000:0000")
        print("We can't change this address to 2001:db8:a3::8203:: because then, how do we know where the omitted zeroes are?  Instead, we omit")
        print("only one set of all zeroes, and shorten the other by removing LEADING zeroes, so it becomes 2001:db8:a3::8203:0:0 instead.")
        print("Notice that the leading zeroes are removed from each hextet, but non-leading zeroes are left in.")
        print()
        pause = input("Press enter to continue...")
        print("\n" * 5)
        print("This calculator will show you both the fully expanded and the fully compressed version of any IPv6 address you")
        print("enter.  It will also provide you the number of /64 networks, as well as the full IP range of the associated subnet.")
        print("You needn't type in a prefix length; the tool will ask yyou for one after typing in the address.")
        print()

        #use IPv6input function to get a user-inputted IPv6 address, perform validation, and convert to usable values
        address = IPv6input()

        #use the IPv6calc function to get a prefix length from the user and find the IP range, check if the address is a special address, and find the number of /64 networks,
        prefix,special,SFnets,lowIP,highIP = IPv6calc(address)
        network = []
        network = lowIP.copy()
        
        print("\n" * 5)
        print("------ IPv6 MODE: OUTPUT")
        print()
        print("Expanded IPv6 Address: ", end="")
        print(IPv6expanded(address))
        print()
        print("Compressed IPv6 Address: ", end="")
        print(IPv6compressed(address))
        print()
        print(special)
        print()
        print()
        print("Network: ", end="")
        print(IPv6compressed(network))
        print()
        print("Number of /64 subnets: ", end="")
        print(SFnets)
        print()
        print("IP Address Range: ", IPv6expanded(lowIP), " - ", IPv6expanded(highIP))
        print("\n" * 5)
        pause = input("Press enter to bring up the main menu again (your output will not be cleared)...")
        print()

    #v6quickstart will skip the guide information for IPv6 mode and bring the user directly to the data input and output section
    def v6quickstart():
        print("\n" * 5)
        print("====== Beginning IPv6 Quickstart Mode ======")
        print("\n" * 5)
        print("Enter an IPv6 address, and select a prefix length when prompted.  The tool will provide the fully expanded and fully compressed versions")
        print("of the address, as well as the number of /64 networks and the full IP range of the associated subnet.  You do not need to type a prefix.")
        print()

        #use IPv6input function to get a user-inputted IPv6 address, perform validation, and convert to usable values
        address = IPv6input()

        #use the IPv6calc function to get a prefix length from the user and find the IP range, check if the address is a special address, and find the number of /64 networks,
        prefix,special,SFnets,lowIP,highIP = IPv6calc(address)
        network = []
        network = lowIP.copy()
        
        
        print("\n" * 5)
        print("------ IPv6 MODE: OUTPUT")
        print()
        print("Expanded IPv6 Address: ", end="")
        print(IPv6expanded(address))
        print("Compressed IPv6 Address: ", end="")
        print(IPv6compressed(address))
        print(special)
        print()
        print("Network: ", end="")
        print(IPv6compressed(network))
        print("Number of /64 subnets: ", end="")
        print(SFnets)
        print("IP Address Range: ", IPv6expanded(lowIP), " - ", IPv6expanded(highIP))
        print("\n" * 5)
        pause = input("Press enter to bring up the main menu again (your output will not be cleared)...")
        print()
        
        
    
    print()
    print("====== Welcome to the Network Building Tool! ======")
    while running:
        print()
        print("1. Begin in Walkthrough Mode")
        print("2. Begin in Quick Start Mode")
        print("3. IPv6 Addressing & Subnetting Guide w/ Calculator")
        print("4. IPv6 Calculator Only")
        print("5. Exit the Program")
        
        menuChoice = input("Please select an option: ")
        
        if menuChoice == '1':
            walkthrough()

        elif menuChoice == '2':
            quickstart()

        elif menuChoice == '3':
            v6()

        elif menuChoice == '4':
            v6quickstart()

        elif menuChoice == '5':
            running = False

        else:
            print()
            print("Please enter a valid selection (type a number and press enter)...")

main()
