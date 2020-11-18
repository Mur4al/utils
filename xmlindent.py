#!/usr/bin/env python3

import os
import argparse
from xml.dom import minidom

def is_file(path):
    if os.path.isfile(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"{path} is not a valid file path")

def parse_args():
    parser = argparse.ArgumentParser(description='Indent SOURCE XML and save it as OUTPUT')
    parser.add_argument('SOURCE', type=os.path.abspath,help='XML to indent')
    parser.add_argument('OUTPUT', type=os.path.abspath,help='output name')
    return parser.parse_args()

def indent_xml(xml_file):
    # with open(xml_file, 'r') as xml_string:
    dom=minidom.parse(xml_file)
    return dom.toprettyxml()

def main():
    args=parse_args()
    output_string=indent_xml(is_file(args.SOURCE))
    with open(args.OUTPUT,'w') as output:
        output.write(output_string)


if __name__=='__main__':
    main()