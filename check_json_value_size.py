#!/usr/bin/env python
"""
A Python script of Nagios plugin for checking json validity and value of size.
"""

import os
import sys
import json
import argparse
from urllib2 import urlopen, URLError


NAGIOS_OK = 0
NAGIOS_WARNING = 1
NAGIOS_CRITICAL = 2


def retrieve_json_size(args):
    """Using Urllib2 to request target url and retrieve
    value size of json
    """
    try:
        connect = urlopen(args.url)

        if connect.getcode() != 200:
            print "HTTP response status code is NOT 200!"
            sys.exit(NAGIOS_CRITICAL)

        data = json.loads(connect.read())

        if data.get("validate") == True:
            return data.get("size")
        else:
            print "Invalid data"
            sys.exit(NAGIOS_CRITICAL)

    except URLError, error:
        print "URLError:", error
        sys.exit(NAGIOS_CRITICAL)


def main():
    """
    e.g.
    $ python check_json_value_size.py -l "http://validate.jsontest.com/?json=[1,2,3,5,8]"
    $ python check_json_value_size.py -l "http://validate.jsontest.com/?json=[2,4,3,5,8,9]" -w 8 -c 2
    """

    parser = argparse.ArgumentParser(epilog=main.__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-l", "--url", required=True,
                        help="Please input the target url.")
    parser.add_argument("-w", "--warning", type=int, default=4,
                        help="Please define the warning threshold size.")
    parser.add_argument("-c", "--critical", type=int, default=2,
                        help="Please define the critical threshold size.")

    args = parser.parse_args()
    size = retrieve_json_size(args)

    if size >= args.warning:
        print "OK: the size is %s. Equal or greater than %s" % (size, args.warning)
        return NAGIOS_OK
    elif args.critical <= size < args.warning:
        print "WARNING: the size is %s. Less than %s but equal or greater than %s" % \
              (size, args.warning, args.critical)
        return NAGIOS_WARNING
    else:
        print "CRITICAL: the size is %s. Less than %s" % (size, args.critical)
        return NAGIOS_CRITICAL


if __name__ == '__main__':
    sys.exit(main())