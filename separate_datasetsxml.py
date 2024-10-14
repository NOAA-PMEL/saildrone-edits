#!/usr/bin/env python
# coding: utf-8

# # reads in datasets.xml and saves individual datasets as xml files


import os
import xml.etree.ElementTree as ET


#inputFilename = '/home/users/koukel/tomcat/content/erddap/erddap_trials/datasets_publicpmel.xml'
inputFilename = input('Enter a datasets.xml to read in: ')


parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))

tree = ET.parse(inputFilename, parser)
root = tree.getroot()


for elemental in root.iter('dataset'):
    ask = 'not'
    did = elemental.attrib['datasetID']
    for elemencheck in elemental.iter('fileDir'):
        if 'saildrone' in elemencheck.text:
            #print('saildrone')
            print('saildrone','/home/users/koukel/tomcat/content/erddap/erddap_trials/sd_xml/' + did + '.xml')
            with open('/home/users/koukel/tomcat/content/erddap/erddap_trials/sd_xml/' + did + '.xml','w') as f:
                f.write(ET.tostring(elemental, encoding='unicode'))
            ask = 'saildrone'
        else:
            #print(elemental)
            ask = 'not'
    if ask == 'not':
        #print('/home/users/koukel/tomcat/content/erddap/erddap_trials/ds_xml/' + did + '.xml')
        with open('/home/users/koukel/tomcat/content/erddap/erddap_trials/ds_xml/' + did + '.xml','w') as f:
            f.write(ET.tostring(elemental, encoding='unicode'))
