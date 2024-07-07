# 2023 Console Cowboys Python Smart Contract Hacking Course
# @author Olie Brown @ficti0n
# http://cclabs.io 

# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


import re, requests
from colorama import Fore

bytecode = "6080604052348015600e575f80fd5b506101438061001c5f395ff3fe608060405234801561000f575f80fd5b5060043610610034575f3560e01c80632e64cec1146100385780636057361d14610056575b5f80fd5b610040610072565b60405161004d919061009b565b60405180910390f35b610070600480360381019061006b91906100e2565b61007a565b005b5f8054905090565b805f8190555050565b5f819050919050565b61009581610083565b82525050565b5f6020820190506100ae5f83018461008c565b92915050565b5f80fd5b6100c181610083565b81146100cb575f80fd5b50565b5f813590506100dc816100b8565b92915050565b5f602082840312156100f7576100f66100b4565b5b5f610104848285016100ce565b9150509291505056fea26469706673582212209a0dd35336aff1eb3eeb11db76aa60a1427a12c1b92f945ea8c8d1dfa337cf2264736f6c634300081a0033"
signatures = "D:\project\/4_metamask\latihan\signaturesDB.txt"

#--------------Start Signature Loop-----------------------------#
for signature in open(signatures, 'r'):
    signature = str(signature.strip())
 
 #Does this signature Exist in Bytecode, if so do a lookup
    if signature in bytecode:
        r = requests.get('https://api.etherface.io/v1/signatures/hash/all/'+signature+"/1", verify=False)
        # print(r.text)



        matches = re.findall(r'(?<="text":")(.*?)(?=",)', r.text)
        
 #Print things out and do error checks       
        if r.status_code == 200 and matches :
            print(f' {Fore.GREEN}Signature found:')
            print(f'{Fore.WHITE}Possible Function Values for {signature}:')
            for match in matches:   
                print(f'{Fore.YELLOW}            - {match}')
                
        elif r.status_code != 200:
            print(f'{Fore.RED}Signature Not Found: {signature} returned {r.status_code} (Might be False Positive)')
#--------------END Signature Loop-----------------------------#

print(Fore.WHITE)