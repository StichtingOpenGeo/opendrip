#!/usr/bin/env python2

# Technolution DRIP to PNG exporter

import simplejson as json
import urllib2
import sys

if len(sys.argv) < 2:
    drip = '3083c455-8528-4ae5-95c6-792426699b30'
else:
    drip = sys.argv[1]

req = urllib2.Request('http://opendata.technolution.nl/opendata/displaydata/v1/dynamic/' + drip)
opener = urllib2.build_opener()
f = opener.open(req)

obj = json.load(f)

with open(drip + '.png', 'wb') as png:
    png.write(bytearray((x & 0xff) for x in obj['displayDynamicInformation']['facilityActualStatus']['image']))
