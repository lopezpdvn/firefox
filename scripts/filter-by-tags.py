#!/usr/bin/env python3
# coding=utf-8

'''filter-by-tag'''

import sys
import json
from argparse import ArgumentParser

def get_tagged_places_iterator(backup_root):
    x = backup_root
    if x.get('type') == 'text/x-moz-place' and x.get('tags'):
        x_ = x.copy()
        x_.pop('children', None)
        x_['tags'] = set(x_['tags'].split(','))
        yield x_

    if 'children' in x and x['children']:
        for child in x['children']:
            yield from get_tagged_places_iterator(child)

parser = ArgumentParser()
parser.add_argument('-i', '--include-tagged', nargs='*', default=())
parser.add_argument('-e', '--exclude-tagged', nargs='*', default=())
args = parser.parse_args()

include_tagged = set(args.include_tagged)
exclude_tagged = set(args.exclude_tagged)

places = tuple(get_tagged_places_iterator(json.load(sys.stdin)))

if include_tagged:
    places = [place for place in places if place['tags'] & include_tagged]

if exclude_tagged:
    places = [place for place in places if not (place['tags'] & exclude_tagged)]

#places = [place for place in places if place['tags']]

places.sort(key=lambda place: place['tags'])

for place in places:
    place['tags'] = ','.join(place['tags'])

json.dump(places, sys.stdout, indent=2)
