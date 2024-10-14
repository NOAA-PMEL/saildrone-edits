#!/usr/bin/env python
# coding: utf-8

# # purpose: to easily work through a generated xml file for the data served to an ERDDAP

import os
os.environ['HDF5_USE_FILE_LOCKING']='FALSE'
import xml.etree.ElementTree as ET
import sys
import csv


#inputFilename = '/home/users/koukel/tomcat/content/erddap/metaedit_test_xmls/datasets_xmledit_selectvars.xml'#'/home/users/kobrien/erddap/tomcat8/webapps/erddap/WEB-INF/sd1031_hurricane_2024_temp.xml'
#outputFilename = '/home/users/koukel/tomcat/content/erddap/metaedit_test_xmls/datasets_again_check.xml'

#asking for a filename to read and a filename to save out to
inputFilename=sys.argv[1]#input('Enter a filename to read in: ')
outputFilename=sys.argv[2]#input('Enter a filename to be saved out: ')
print('iF',inputFilename)
print('oF',outputFilename)

outputFilename_del = outputFilename.split('.')[0] + '_del' + '.' + outputFilename.split('.')[1]

with open(inputFilename) as inXML, open(outputFilename_del, 'w') as outXML:
    outXML.write('<toplevel>\n')#uncomment this line and the last line of this cell if there is no overhanging xml snippet -- edit_xml_saildrone.ipynb should tell you if there are problems
    for line in inXML.readlines():
        outXML.write(line)
    outXML.write('</toplevel>\n')


#opens xml with new root, using a parser to keep comments
#outputFilename = '/home/users/koukel/tomcat/content/erddap/metaedit_test_xmls/no_metaedit_xmls/datasets_xmledit.xml'
parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))

tree = ET.parse(outputFilename_del, parser)
root = tree.getroot()


inst_name=sys.argv[3]
mission_name=sys.argv[4]
proj_name=sys.argv[5]
year=sys.argv[6]


#opens dictionary of datasetIDs and corresponding titles
title_namedir = '/home/users/koukel/saildrone_metawork/'
title_namefile = 'saildronemeta_datasetIDs_titles.csv'

reader_titlenames = csv.reader(open(title_namedir + title_namefile))
titledatasetdict = {}
for k, v, j in reader_titlenames:
    titledatasetdict[j] = v
    

#edits the trajectory addAttributes attribs (cdm_trajectory_variables and subsetVariables) through searching for saildrone data only
for elemental in root.iter('dataset'):
    for elemencheck in elemental.iter('fileDir'):
        if 'saildrone' in elemencheck.text:
            for elemenkid in elemental.iter('addAttributes'):
                for elemkid in elemenkid.iter('att'):
                    attname = elemkid.get('name')
                    if attname == 'cdm_trajectory_variables':
                        elemkid.text = 'trajectory'
                        #print(elemkid.attrib, ', ', elemkid.text)
                    elif attname == 'subsetVariables':
                        elemkid.text = 'trajectory'
                        #print(elemkid.attrib, ', ', elemkid.text)

#if printing, should have sets of 
#{'name': 'cdm_trajectory_variables'} ,  trajectory
#{'name': 'subsetVariables'} ,  trajectory


#edits the <reloadEveryNMinutes> from some high number to 15
for elemental in root.iter('dataset'):
    for elemencheck in elemental.iter('fileDir'):
        #print(elemencheck.text)
        if 'saildrone' in elemencheck.text:
            for elemenkid in elemental.iter('reloadEveryNMinutes'):
                #print(elemenkid.text)
                elemenkid.text = '15'
                #print(elemenkid.text)

#if printing, should have sets of 
#/home/users/koukel/test/metaedit_test/saildrone2/hawaiian_islands_ocean_chemistry/2023/offset/1091/
#10080
#15


#edits the trajectory dataVariable attrib datatype to be String through searching for saildrone data only
for elemental in root.iter('dataset'):
    for elemencheck in elemental.iter('fileDir'):
        if 'saildrone' in elemencheck.text:
            for elemenkid in elemental.iter('dataVariable'):
                #print('kid ',elemenkid.tag)
                for elemenchild in elemenkid.iter('sourceName'):
                    #print('child ',elemenchild.text)
                    if elemenchild.text == 'trajectory':
                        #print('child ',elemenchild.text)
                        for elemchild in elemenkid.iter('dataType'):
                            elemchild.text = 'String'


for elemental in root.iter('dataset'):
    for elemenkid in elemental.iter('fileDir'):
        #print('fileDir ,', elemenkid.text)
        for elemenchild in elemental.iter('addAttributes'):
            for elemkid in elemenchild.iter('att'):
                attname = elemkid.get('name')
                #print(elemkid.text)
                if attname == 'testOutOfDate':
                    elemkid.text = 'now-2hours'
                    

#GTS_yes = 'y'
GTS_yes=sys.argv[7]#input('Are these GTS data? Type y for yes: ')


#edits datasetID based on fileDir for all saildrone datasets, not changing it for preexisting datasetIDs
    #does this even when title isn't pulled out of attribute comments
for elemental in root.iter('dataset'):
    for elemenkid in elemental.iter('fileDir'):
        print('fileDir ,', elemenkid.text)
        
        #making datasetID, independent of preexisting title            
        if ('high_res' in elemenkid.text) and ('saildrone' in elemenkid.text):
            elemental.attrib['datasetID'] = 'sd' + elemenkid.text.split('/')[-2] + '_' + mission_name + '_' + year + '_' + elemenkid.text.split('/')[8]
            #print('high res saildrone, ', elemental.attrib['datasetID'])
        elif ('ADCP' in elemenkid.text or 'adcp' in elemenkid.text) and ('saildrone' in elemenkid.text):
            elemental.attrib['datasetID'] = 'sd' + elemenkid.text.split('/')[-2] + '_' + mission_name + '_' + year + '_adcp'
            #print('adcp saildrone, ', elemental.attrib['datasetID'])
        elif ('saildrone' in elemenkid.text):
            #print('saildrone')
            #print(elemental.attrib['datasetID'])
            elemental.attrib['datasetID'] = 'sd' + elemenkid.text.split('/')[-2] + '_' + mission_name + '_' + year 
            #print('datasetID, ', elemental.attrib['datasetID'])
        #making new title
        if elemenkid.text[-5] == '-':
            drid = elemenkid.text[-4:-1]
        else:
            drid = elemenkid.text[-5:-1]
        newtitle = str(inst_name + ' ' + proj_name + ' ' + year + ' Saildrone ' + drid)
        if ('ADCP' in elemenkid.text) or ('adcp' in elemenkid.text) and ('hz' in elemenkid.text):
            newtitle = str(inst_name + ' ' + proj_name + ' ' + year + ' High Resolution ' + elemenkid.text.split('/')[-2] + ' ADCP Saildrone ' + drid)
        elif ('ADCP' in elemenkid.text) or ('adcp' in elemenkid.text):
            newtitle = str(inst_name + ' ' + proj_name + ' ' + year + ' ADCP Saildrone ' + drid)
        if ('ek80' in elemenkid.text) or ('EK80' in elemenkid.text) or ('echosounder' in elemenkid.text) or ('Echosounder' in elemenkid.text):
            newtitle = str(inst_name + ' ' + proj_name + ' ' + year + ' Echosounder Saildrone ' + drid)
        if ('wave' in elemenkid.text) or ('wave_spectra' in elemenkid.text):
            newtitle = str(inst_name + ' ' + proj_name + ' ' + year + ' Wave Data Saildrone ' + drid)
        if 'sea-trial' in elemenkid.text:
            newtitle = str(inst_name + ' ' + proj_name + ' ' + year + ' Sea Trial Saildrone ' + drid)
        if ('daily_files' in elemenkid.text) or ('real-time' in elemenkid.text):
            newtitle = str(inst_name + ' ' + proj_name + ' ' + year + ' NRT Saildrone ' + drid)
        if ('delayed' in elemenkid.text) or ('offset' in elemenkid.text):
            newtitle = str(inst_name + ' ' + proj_name + ' ' + year + ' Saildrone ' + drid)
        if 'hz' in elemenkid.text:
            newtitle = str(inst_name + ' ' + proj_name + ' ' + year + ' High Resolution ' + elemenkid.text.split('/')[-2] + ' Saildrone ' + drid)
            if 'hz' in newtitle:
                    newtitle = newtitle.replace('hz','Hz')#this capitalizes Hz to the proper form
        if GTS_yes == 'y':
            newtitle = str(inst_name + ' ' + proj_name + ' ' + year + ' GTS Saildrone ' + drid)
        print('newtitle',newtitle)

        count = 0
        for elemenchild in elemental.iter('addAttributes'):
            #print('elemenchild ', elemenchild.tag)
            try:
                if count == 0:
                    ET.SubElement(elemenchild, 'att', name="title")
                    for elemkid in elemenchild.iter('att'):
                        attname = elemkid.get('name')
                        if attname == 'title':
                            ET.indent(elemkid, '        ')
                            elemkid.text = newtitle
                count = count + 1
            except:
                for elemkid in elemenchild.iter('att'):
                    attname = elemkid.get('name')
                    if attname == 'title':
                        elemkid.text = newtitle
                    #print(attname)
        try:
            if newtitle in titledatasetdict:
                elemental.attrib['datasetID'] = titledatasetdict[newtitle]
                print('same datasetID',elemental.attrib['datasetID'])
        except:
            print('new datasetID',elemental.attrib['datasetID'])

#if printing, should have sets of: (datasetID preexisting, datasetID not preexisting)
#exact title,  NOAA Saildrone Hurricane Monitoring, drone 1031 yesmetaedit
#exact datasetID,  newdatasetID_hurr1031
#/home/users/koukel/test/metaedit_test/saildrone2/hurricane_monitoring/2021/daily_files/1040/
#exact title,  New Hurricane 2021 drone 1040 Title
#saildrone saildrone,  sd1040_metaedit_test_saildrone2

try:
    #finds the dVs of time, lat, lons per dataset
    geckots = []
    geckolas = []
    geckolos =[]
    for elemental in root.iter('dataset'):
        geckot = elemental.findall('./dataVariable[sourceName="time"]')
        geckola = elemental.findall('./dataVariable[sourceName="latitude"]')
        geckolo = elemental.findall('./dataVariable[sourceName="longitude"]')
        geckots.append(geckot)
        geckolas.append(geckola)
        geckolos.append(geckolo)

    for elemental in root.iter('dataset'):
        remt = elemental.findall('./dataVariable[sourceName="time"]')
        remla = elemental.findall('./dataVariable[sourceName="latitude"]')
        remlo = elemental.findall('./dataVariable[sourceName="longitude"]')
        elemental.remove(remt[0])
        elemental.remove(remla[0])
        elemental.remove(remlo[0])

    #this inserts the new time, lat, and lon dVs at the top of the dV list per dataset
    for i,x in enumerate(root.iter('dataset')):
        #print(x,i)
        #print(geckots[i][0])
        #print(geckolas[i][0])
        #print(geckolos[i][0])
        root[i].insert(14,geckots[i][0])
        root[i].insert(15,geckolas[i][0])
        root[i].insert(16,geckolos[i][0])
        
except:
    #finds the dVs of time, lat, lons per dataset                                                         
    geckots = []
    geckolas = []
    geckolos =[]
    for elemental in root.iter('dataset'):
        geckot = elemental.findall('./dataVariable[sourceName="TIME"]')
        geckola = elemental.findall('./dataVariable[sourceName="LAT"]')
        geckolo = elemental.findall('./dataVariable[sourceName="LON"]')
        geckots.append(geckot)
        geckolas.append(geckola)
        geckolos.append(geckolo)
    for elemental in root.iter('dataset'):
        remt = elemental.findall('./dataVariable[sourceName="TIME"]')
        remla = elemental.findall('./dataVariable[sourceName="LAT"]')
        remlo = elemental.findall('./dataVariable[sourceName="LON"]')
        elemental.remove(remt[0])
        elemental.remove(remla[0])
        elemental.remove(remlo[0])
    #this inserts the new time, lat, and lon dVs at the top of the dV list per dataset                    
    for i,x in enumerate(root.iter('dataset')):
        #print(x,i)                                                                                       
        #print(geckots[i][0])                                                                                     #print(geckolas[i][0])                                                                            
        #print(geckolos[i][0])                                                                            
        root[i].insert(14,geckots[i][0])
        root[i].insert(15,geckolas[i][0])
        root[i].insert(16,geckolos[i][0])

#print(ET.tostring(root, encoding='unicode'))


#saves edits out to output file
tree.write(outputFilename_del)


#writes the edited xml to another xml, this time without the added <toplevel> node, back to original form
with open(outputFilename_del) as inXML, open(outputFilename, 'w') as outXML:
    for line in inXML.readlines()[1:-1]:
        outXML.write(line)

        
#deletes the additionally created xml file
os.remove(outputFilename_del)
