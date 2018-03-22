#! /usr/bin/python

import os, sys
from stat import *
import argparse
from lxml import etree

parser = argparse.ArgumentParser(description='This program adds the location metadata to the images')

parser.add_argument('-i', '--input-directory', help='Name of the input directory containing the images', required=True)
parser.add_argument('-f', '--file-gpx', help='Name of the file containing GPS coordinates in the GPX format', required=True)

args=vars(parser.parse_args())

input_dir=args['input_directory']
file_gpx=args['file_gpx']

tree = etree.parse(file_gpx)
nsmap = {k if k is not None else 'default':v for k,v in tree.getroot().nsmap.items()}

trkpts = tree.xpath('/default:gpx/default:trk/default:trkseg/default:trkpt', namespaces=nsmap)
for trkpt in trkpts:
    print(trkpt.get('lat'))
    print(trkpt.get('lon')) 
    time = trkpt.find('default:time', nsmap)
    print(time.text)
    ele = trkpt.find('default:ele', nsmap)
    print(ele.text)
