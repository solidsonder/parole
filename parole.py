from colorama import init, Fore, Back, Style
import argparse
from argparse import RawTextHelpFormatter
import sys
import os
from prettytable import PrettyTable
import re
from lib.guidie import guidie
from core.banner import b2

sefa_dict = guidie()

infox = Fore.LIGHTWHITE_EX+"["+Fore.BLUE+"*"+Style.RESET_ALL+Fore.LIGHTWHITE_EX+"]"+Style.RESET_ALL
warningx = Fore.LIGHTWHITE_EX+"["+Fore.RED+"!"+Style.RESET_ALL+Fore.LIGHTWHITE_EX+"]"+Style.RESET_ALL
unknownx = Fore.LIGHTWHITE_EX+"["+Fore.YELLOW+"?"+Style.RESET_ALL+Fore.LIGHTWHITE_EX+"]"+Style.RESET_ALL

print(b2())


def advanced_hash_type_detector(hash_value):
    hash_length_to_type = {
        32: ['md5', 'md4', 'md2'],
        40: ['sha1'],
        56: ['sha224', 'sha3224'],
        64: ['sha256', 'sha3256', 'blake2s'],
        96: ['sha384', 'sha3384'],
        128: ['sha512', 'sha3512', 'blake2b', 'whirlpool'],
    }

    if len(hash_value) == 40:
        if re.match(r'^\*[a-f0-9]{40}$', hash_value, re.IGNORECASE):
            return ['sha1(sha1_bin)']
    possible_types = hash_length_to_type.get(len(hash_value), [])
    
    if not possible_types:
        return "Unknown or unsupported hash type"
    
    return possible_types

parser = argparse.ArgumentParser(description="Parole v0.032 - 'hashum' (automated hash analysis tool)",
                                 formatter_class=RawTextHelpFormatter)

parser.add_argument("-i","--information", action='store_true', help="find hash information & type")
parser.add_argument("-s","--search", action='store_true', help="search hash on databases (Not Active)")
parser.add_argument("-g","--guidie", action='store_true', help="learn information type about hash and How to crack")
parser.add_argument("hash", type=str, help="hash for information")

if len(sys.argv) == 1:
    parser.print_help()
    parser.exit()
args = parser.parse_args()


if args.information:
    print("\n"+infox+Fore.LIGHTWHITE_EX+" Possible types"+Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX+"---------------------------------------\n"+Style.RESET_ALL)
    tablo = PrettyTable()
    tablo.field_names = ["Type", "Hash"]
    for i in advanced_hash_type_detector(args.hash):
        tablo.add_row([i, args.hash])
    print(str(tablo)+"\n")

if args.search:
    print(warningx+Fore.LIGHTWHITE_EX+' Search module is not active'+Style.RESET_ALL)
if args.guidie:
    print("\n"+infox+Fore.LIGHTWHITE_EX+" Guidie of possible types"+Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX+"---------------------------------------\n"+Style.RESET_ALL)
    tablo2 = PrettyTable()
    tablo2.field_names = ["Type", "Hash","Initialization Vector"]
    for i in advanced_hash_type_detector(args.hash):
        tablo2.add_row([i, args.hash,sefa_dict[i]["Initialization Vector"]])
        print(Fore.YELLOW+i+":"+Style.RESET_ALL+" '"+sefa_dict[i]["Properties"]+"'\n")
    print(tablo2)