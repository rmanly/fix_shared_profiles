#!/usr/bin/python

import argparse
import plistlib
from Foundation import NSUUID

def new_uuid():
    return NSUUID.UUID().UUIDString().lower().encode('ascii', 'ignore')


def read_profile(filename):
    return plistlib.readPlist(filename)


def fix_top_level(profile):
    profile['PayloadUUID'] = new_uuid()
    return profile


def fix_content_level(content):
    '''
    fix_content_level(list) -> list

    Return a modified list with new uuids for use in PayloadContent section
    of a configuration profile.
    '''
    for payload in content:
        payload['PayloadUUID'] = new_uuid()
    return content


def fix_profile(file):
    profile = read_profile(file)
    profile['PayloadContent'] = fix_content_level(profile['PayloadContent'])
    new_profile = fix_top_level(profile)
    write_new(new_profile, file)


def write_new(profile, filename):
    plistlib.writePlist(profile, filename)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate new uuids for shared configuration profiles.')
    parser.add_argument('file', help='one or more configuration profiles', nargs='+')
    args = parser.parse_args()

    for file in args.file:
       fix_profile(file) 
