#! /usr/bin/env python
#
# Converts an INI-style config file to a map of maps, and returns that
# in JSON format. The output is a two-level map, indexed by section
# name, with a nested map that contains the key/val pairs for each
# section entry.

import configparser
import json
import sys

if len(sys.argv) < 2:
    print('Need input file as only argument')
    sys.exit(1)

parser = configparser.RawConfigParser()
parser.read(sys.argv[1])

d = {}

for name, sect in parser.items():
    content = {}
    for key, val in sect.items():
        content[key] = val
    d[name] = content

print(json.dumps(d))
