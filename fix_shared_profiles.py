#!/usr/bin/python

import argparse
import plistlib
from Foundation import NSUUID

profiles = []

def new_uuid():
    return NSUUID.UUID().UUIDString().lower().encode('ascii', 'ignore')

def read_profile(profile):
    return plistlib.readPlist(profile)

parser = argparse.ArgumentParser(description='Generate new uuids for shared configuration profiles.')
parser.add_argument('file', help='one or more configuration profiles', nargs='+')
args = parser.parse_args()

#for profile in profiles:
#    new_profile = read_profile(profile)
#    new_profile['PayloadUUID'] = new_uuid()
#    
