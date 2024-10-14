#!/usr/bin/env python
# coding: utf-8


import os
import xml.etree.ElementTree as ET
import sys


inputFilename=sys.argv[1]#input('Enter a filename to read in: ')
#inputFilename = '/home/users/koukel/tomcat/content/erddap/erddap_trials/sd_xml/sd1031_hurricane_monitoring_2021_nrt_indiv.xml'
parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
tree = ET.parse(inputFilename, parser)
root = tree.getroot()


for elemental in root.iter('dataset'):
    for elemenkid in elemental.iter('fileDir'):
        print(elemental.attrib['datasetID'])



