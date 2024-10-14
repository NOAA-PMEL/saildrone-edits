#!/usr/bin/env python
# coding: utf-8

# # python script that edits saildrone xml and only keeps GTS vars


import os
import xml.etree.ElementTree as ET


for root, dirs, files in os.walk('/home/users/koukel/tomcat/content/erddap/erddap_trials/sd_xml'):#pointing towards the saildrone dir since this only applies there
    for n in range(len(files)):
        #print(files[n])
        inputFilename = '/home/users/koukel/tomcat/content/erddap/erddap_trials/sd_xml/' + files[n]
        print(inputFilename)

        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        tree = ET.parse(inputFilename, parser)
        root = tree.getroot()

        for dT in root.iter('dataset'):
            no_time = dT.findall('./dataVariable[sourceName="time"]')
            no_lat = dT.findall('./dataVariable[sourceName="latitude"]')
            no_lon = dT.findall('./dataVariable[sourceName="longitude"]')
            no_traj = dT.findall('./dataVariable[sourceName="trajectory"]')
            no_tam = dT.findall('./dataVariable[sourceName="TEMP_AIR_MEAN"]')
            no_rm = dT.findall('./dataVariable[sourceName="RH_MEAN"]')
            no_bpm = dT.findall('./dataVariable[sourceName="BARO_PRES_MEAN"]')
            no_tsm = dT.findall('./dataVariable[sourceName="TEMP_SBE37_MEAN"]')
            no_wfm = dT.findall('./dataVariable[sourceName="WIND_FROM_MEAN"]')
            no_wsm = dT.findall('./dataVariable[sourceName="WIND_SPEED_MEAN"]')
            no_ssm = dT.findall('./dataVariable[sourceName="SAL_SBE37_MEAN"]')
            no_wcsm = dT.findall('./dataVariable[sourceName="WATER_CURRENT_SPEED_MEAN"]')
            no_wcdm = dT.findall('./dataVariable[sourceName="WATER_CURRENT_DIRECTION_MEAN"]')
            no_wdp = dT.findall('./dataVariable[sourceName="WAVE_DOMINANT_PERIOD"]')
            no_wsh = dT.findall('./dataVariable[sourceName="WAVE_SIGNIFICANT_HEIGHT"]')
            
            noremlist = no_time + no_lat + no_lon + no_traj + no_tam + no_rm + no_bpm + no_tsm + no_wfm + no_wsm + no_ssm + no_wcsm + no_wcdm + no_wdp + no_wsh
        
            rem = dT.findall('./dataVariable')
            for x in range(len(rem)):    
                if rem[x] not in noremlist:
                    #print('rem[x]',rem[x])
                    #remx.append(rem[x])
                    dT.remove(rem[x])

        tree.write(inputFilename)
