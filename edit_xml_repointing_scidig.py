#!/usr/bin/env python
# coding: utf-8

# # purpose: to repoint sdig-located erddaps to sci-dig, plus other updates


import os
import xml.etree.ElementTree as ET
import csv


for root, dirs, files in os.walk('/home/users/koukel/tomcat/content/erddap/erddap_trials/ds_xml'):
    for n in range(len(files)):
        #print(files[n])
        inputFilename = '/home/users/koukel/tomcat/content/erddap/erddap_trials/ds_xml/' + files[n]
        #print(inputFilename)

        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        tree = ET.parse(inputFilename, parser)
        root = tree.getroot()

        for elemental in root.iter('dataset'):
            for elemenkid in elemental.iter('fileDir'):
                #print(elemenkid.text)
                if ('sdig' in elemenkid.text) and ('Argo' in elemenkid.text):#special argo exception since put argo files in superdir
                    #print('sdig-argo')
                    elemenkid.text = elemenkid.text.replace('sdig','sci-dig/argo')
                elif ('sdig' in elemenkid.text) and ('saildrone' not in elemenkid.text):#normal way for files in sdig to easily change over
                    #print('sdig')
                    elemenkid.text = elemenkid.text.replace('sdig','sci-dig')
                    #print('newloc, ',elemenkid.text)

        #print(ET.tostring(root, encoding='unicode'))
        tree.write(inputFilename)
