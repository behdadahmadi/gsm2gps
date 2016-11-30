#!/usr/bin/python
#By Behdad Ahmadi
#Twitter: behdadahmadi & MrOplus
#https://logicalcoders.com

import re
import requests
import argparse
def banner():
    dotname = "-" * 16
    print " "
    print dotname.center(16,'-')
    print ".:: " + 'gsmTracker' + " ::.".center(4)
    print "by Behdad Ahmadi".center(18)
    print "Twitter:behdadahmadi".center(18)
    print dotname.center(20,'-')

def main():
    banner()

    parser = argparse.ArgumentParser()
    parser.add_argument('mcc',help='mcc')
    parser.add_argument('mnc',help='mnc')
    parser.add_argument('lac', help='LAC')
    parser.add_argument('cid',help='cellID')

    args = parser.parse_args()
    mcc = args.mcc
    mnc = args.mnc
    lac = args.lac
    cid = args.cid
    print 'Searching for given GSM information...'
    payload = {'mcc':mcc,'mnc':mnc,'lac':lac,'cid':cid}
    page = requests.post('http://cellphonetrackers.org/gsm/gsm-tracker.php',data=payload)
    if 'Error' in page.content:
        err = re.search('Error\d*.+', page.content).group(0)
        print err
    else:
        try:
            lat = re.search('Lat=\d+.\d+', page.content).group(0).replace('Lat=','')
            lon = re.search('Lon=\d+.\d+', page.content).group(0).replace('Lon=', '')
            print '{0},{1}'.format(lat, lon)
        except:
            print 'Nothing found'

if __name__ == '__main__':
    main()
