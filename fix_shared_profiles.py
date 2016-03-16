#!/usr/bin/python

import argparse
import plistlib
from Foundation import NSUUID


def change_payloadorg(org, profile):
    profile['PayloadOrganization'] = org
    return profile


def fix_content_level(content):
    for payload in content:
        payload['PayloadUUID'] = new_uuid()
    return content


def fix_profile(file):
    profile = read_profile(file)
    profile['PayloadContent'] = fix_content_level(profile['PayloadContent'])
    new_profile = fix_top_level(profile)
    if args.org:
       change_payloadorg(args.org, new_profile)
    write_new(new_profile, file)


def fix_top_level(profile):
    profile['PayloadUUID'] = new_uuid()
    return profile


def new_uuid():
    return NSUUID.UUID().UUIDString().lower().encode('ascii', 'ignore')


def read_profile(filename):
    return plistlib.readPlist(filename)


def write_new(profile, filename):
    plistlib.writePlist(profile, filename)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate new uuids for shared configuration profiles.')
    parser.add_argument('file', help='One or more configuration profiles to modify.', nargs='+')
    parser.add_argument('-org', help='New string for PayloadOrganization key.', metavar='Organization')
    args = parser.parse_args()

    for file in args.file:
        fix_profile(file)

