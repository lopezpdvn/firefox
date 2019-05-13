#!/usr/bin/env python3
# coding=utf-8

'''filter-by-tag'''

import sys
import json
from pprint import pprint


def get_places_iterator(backup_root):
    x = backup_root
    if 'type' in x and x['type'] == 'text/x-moz-place' and 'tags' in x and x['tags']:
        x_ = x.copy()
        x_.pop('children', None)
        yield x_

    if 'children' in x and x['children']:
        for child in x['children']:
            yield from get_places_iterator(child)

backup = json.load(sys.stdin)

for i in get_places_iterator(backup):
    pprint(i)
