#!/usr/bin/env python
# coding: utf-8

# # purpose: to repoint sdig-located saildrone datasets in erddaps to sci-dig


import os
import xml.etree.ElementTree as ET
import csv


#opens dictionary of saildrone file movement, showing where it used to live and where in sci-dig it lives now
move_namedir = '/home/users/koukel/saildrone_metawork/'
move_namefile = 'saildronemeta_mission_movement.csv'

reader_movenames = csv.reader(open(move_namedir + move_namefile))
move_names = {}
for k, v in reader_movenames:
    move_names[k] = v


#editing fileDirs, starting just with sdig -> sci-dig for saildrone datasets
for root, dirs, files in os.walk('/home/users/koukel/tomcat/content/erddap/erddap_trials/sd_xml'):#datasets_trials
    for n in range(len(files)):
        #print(files[n])
        inputFilename = '/home/users/koukel/tomcat/content/erddap/erddap_trials/sd_xml/' + files[n]
        #print(inputFilename)

        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        tree = ET.parse(inputFilename, parser)
        root = tree.getroot()

        for elemental in root.iter('dataset'):
            for elemenkid in elemental.iter('fileDir'):
                print(elemenkid.text)
                if ('sdig' in elemenkid.text):
                    for mission in move_names:
                        if mission in elemenkid.text:
                            elemenkid.text = elemenkid.text.replace('sdig','sci-dig')
                            elemenkid.text = elemenkid.text.replace(mission,move_names[mission])
                            elemenkid.text = elemenkid.text.replace('delayed','offset')#this may pose some problems but it can be dealt with ?? shouldn't be too many cases left
                            #print ('now ',elemenkid.text)
                elif ('data/tomcat' in elemenkid.text) and ('saildrone' in elemenkid.text):
                    for mission in move_names:#if they're saildrone non-sdig files
                        if mission in elemenkid.text:
                            elemenkid.text = elemenkid.text.replace('data/tomcat','mule-external/sci-dig')
                            elemenkid.text = elemenkid.text.replace(mission,move_names[mission])
                            elemenkid.text = elemenkid.text.replace('delayed','offset')#this may pose some problems but it can be dealt with ?? shouldn't be too many cases left
                            #print ('now ',elemenkid.text)

        tree.write(inputFilename)

#if printing, should have sets of 
#/home/mule-external/sdig/saildrone/hurricane_monitoring_2023/delayed/1090/
#now, /home/mule-external/sci-dig/saildrone/hurricane_monitoring/2023/offset/1090
