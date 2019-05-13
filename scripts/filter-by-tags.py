#!/usr/bin/env python3
# coding=utf-8

'''filter-by-tag'''

import sys
import json
from pprint import pprint


def get_places_iterator(backup_root):
    x = backup_root
    if x.get('type') == 'text/x-moz-place' and x.get('tags'):
        x_ = x.copy()
        x_.pop('children', None)
        yield x_

    if 'children' in x and x['children']:
        for child in x['children']:
            yield from get_places_iterator(child)

backup = json.load(sys.stdin)

for i in get_places_iterator(backup):
    pprint(i)
