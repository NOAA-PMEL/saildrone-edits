#!/usr/bin/env python
# coding: utf-8

# # python notebook that copies an xml file and removes unwanted variables


import os
import xml.etree.ElementTree as ET


for root, dirs, files in os.walk('/home/users/koukel/tomcat/content/erddap/erddap_trials/sd_xml'):
    for n in range(len(files)):
        #print(files[n])
        inputFilename = '/home/users/koukel/tomcat/content/erddap/erddap_trials/sd_xml/' + files[n]
        print(inputFilename)

        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        tree = ET.parse(inputFilename, parser)
        root = tree.getroot()

        #finds all dataVariables not in varskeep and removes them
        for dT in root.iter('dataset'):
            no_time = dT.findall('./dataVariable[sourceName="time"]')
            no_lat = dT.findall('./dataVariable[sourceName="latitude"]')
            no_lon = dT.findall('./dataVariable[sourceName="longitude"]')
            no_traj = dT.findall('./dataVariable[sourceName="trajectory"]')
            no_sog = dT.findall('./dataVariable[sourceName="SOG"]')
            no_sfm = dT.findall('./dataVariable[sourceName="SOG_FILTERED_MEAN"]')
            no_sfs = dT.findall('./dataVariable[sourceName="SOG_FILTERED_STDDEV"]')
            no_sfmx = dT.findall('./dataVariable[sourceName="SOG_FILTERED_MAX"]')
            no_sfmn = dT.findall('./dataVariable[sourceName="SOG_FILTERED_MIN"]')
            no_cog = dT.findall('./dataVariable[sourceName="COG"]')
            no_cfm = dT.findall('./dataVariable[sourceName="COG_FILTERED_MEAN"]')
            no_cfs = dT.findall('./dataVariable[sourceName="COG_FILTERED_STDDEV"]')
            no_hdg = dT.findall('./dataVariable[sourceName="HDG"]')
            no_hfm = dT.findall('./dataVariable[sourceName="HDG_FILTERED_MEAN"]')
            no_hfs = dT.findall('./dataVariable[sourceName="HDG_FILTERED_STDDEV"]')
            no_rfm = dT.findall('./dataVariable[sourceName="ROLL_FILTERED_MEAN"]')
            no_rfs = dT.findall('./dataVariable[sourceName="ROLL_FILTERED_STDDEV"]')
            no_rfp = dT.findall('./dataVariable[sourceName="ROLL_FILTERED_PEAK"]')
            no_pfm = dT.findall('./dataVariable[sourceName="PITCH_FILTERED_MEAN"]')
            no_pfs = dT.findall('./dataVariable[sourceName="PITCH_FILTERED_STDDEV"]')
            no_pfp = dT.findall('./dataVariable[sourceName="PITCH_FILTERED_PEAK"]')
            no_hdgw = dT.findall('./dataVariable[sourceName="HDG_WING"]')
            no_whfm = dT.findall('./dataVariable[sourceName="WING_HDG_FILTERED_MEAN"]')
            no_whfs = dT.findall('./dataVariable[sourceName="WING_HDG_FILTERED_STDDEV"]')
            no_wrfm = dT.findall('./dataVariable[sourceName="WING_ROLL_FILTERED_MEAN"]')
            no_wrfs = dT.findall('./dataVariable[sourceName="WING_ROLL_FILTERED_STDDEV"]')
            no_wrfp = dT.findall('./dataVariable[sourceName="WING_ROLL_FILTERED_PEAK"]')
            no_wpfm = dT.findall('./dataVariable[sourceName="WING_PITCH_FILTERED_MEAN"]')
            no_wpfs = dT.findall('./dataVariable[sourceName="WING_PITCH_FILTERED_STDDEV"]')
            no_wpfp = dT.findall('./dataVariable[sourceName="WING_PITCH_FILTERED_PEAK"]')
            no_wa = dT.findall('./dataVariable[sourceName="WING_ANGLE"]')
            no_wfm = dT.findall('./dataVariable[sourceName="WIND_FROM_MEAN"]')
            no_wfs = dT.findall('./dataVariable[sourceName="WIND_FROM_STDDEV"]')
            no_wsm = dT.findall('./dataVariable[sourceName="WIND_SPEED_MEAN"]')
            no_wss = dT.findall('./dataVariable[sourceName="WIND_SPEED_STDDEV"]')
            no_uwm = dT.findall('./dataVariable[sourceName="UWND_MEAN"]')
            no_uws = dT.findall('./dataVariable[sourceName="UWND_STDDEV"]')
            no_vwm = dT.findall('./dataVariable[sourceName="VWND_MEAN"]')
            no_vws = dT.findall('./dataVariable[sourceName="VWND_STDDEV"]')
            no_wwm = dT.findall('./dataVariable[sourceName="WWND_MEAN"]')
            no_wws = dT.findall('./dataVariable[sourceName="WWND_STDDEV"]')
            no_gwm = dT.findall('./dataVariable[sourceName="GUST_WND_MEAN"]')
            no_gws = dT.findall('./dataVariable[sourceName="GUST_WND_STDDEV"]')
            no_wmhm = dT.findall('./dataVariable[sourceName="WIND_MEASUREMENT_HEIGHT_MEAN"]')
            no_wmhs = dT.findall('./dataVariable[sourceName="WIND_MEASUREMENT_HEIGHT_STDDEV"]')
            no_tam = dT.findall('./dataVariable[sourceName="TEMP_AIR_MEAN"]')
            no_tas = dT.findall('./dataVariable[sourceName="TEMP_AIR_STDDEV"]')
            no_rhm = dT.findall('./dataVariable[sourceName="RH_MEAN"]')
            no_rhs = dT.findall('./dataVariable[sourceName="RH_STDDEV"]')
            no_bpm = dT.findall('./dataVariable[sourceName="BARO_PRES_MEAN"]')
            no_bps = dT.findall('./dataVariable[sourceName="BARO_PRES_STDDEV"]')
            no_tiswum = dT.findall('./dataVariable[sourceName="TEMP_IR_SEA_WING_UNCOMP_MEAN"]')
            no_tiswus = dT.findall('./dataVariable[sourceName="TEMP_IR_SEA_WING_UNCOMP_STDDEV"]')
            no_wdp = dT.findall('./dataVariable[sourceName="WAVE_DOMINANT_PERIOD"]')
            no_wsh = dT.findall('./dataVariable[sourceName="WAVE_SIGNIFICANT_HEIGHT"]')
            no_tdhm = dT.findall('./dataVariable[sourceName="TEMP_DEPTH_HALFMETER_MEAN"]')
            no_tdhs = dT.findall('./dataVariable[sourceName="TEMP_DEPTH_HALFMETER_STDDEV"]')
            no_tsm = dT.findall('./dataVariable[sourceName="TEMP_SBE37_MEAN"]')
            no_tsd = dT.findall('./dataVariable[sourceName="TEMP_SBE37_STDDEV"]')
            no_ssm = dT.findall('./dataVariable[sourceName="SAL_SBE37_MEAN"]')
            no_sss = dT.findall('./dataVariable[sourceName="SAL_SBE37_STDDEV"]')
            no_csm = dT.findall('./dataVariable[sourceName="COND_SBE37_MEAN"]')
            no_css = dT.findall('./dataVariable[sourceName="COND_SBE37_STDDEV"]')
            no_wcsm = dT.findall('./dataVariable[sourceName="WATER_CURRENT_SPEED_MEAN"]')
            no_wcdm = dT.findall('./dataVariable[sourceName="WATER_CURRENT_DIRECTION_MEAN"]')
    
            noremlist = no_time + no_lat + no_lon + no_traj + no_sog + no_sfm + no_sfs + no_sfmx + no_sfmn + no_cog + no_cfm + no_cfs + no_hdg + no_hfm + no_hfs + no_rfm + no_rfs + no_rfp + no_pfm + no_pfs  + no_pfp + no_hdgw + no_whfm + no_whfs + no_wrfm + no_wrfs + no_wrfp + no_wpfm + no_wpfs + no_wpfp + no_wa + no_wfm + no_wfs + no_wsm + no_wss + no_uwm + no_uws + no_vwm + no_vws + no_wwm + no_wws + no_gwm + no_gws + no_wmhm + no_wmhs + no_tam + no_tas + no_rhm + no_rhs + no_bpm + no_bps + no_tiswum + no_tiswus + no_wdp + no_wsh + no_tdhm + no_tdhs + no_tsm + no_tsd + no_ssm + no_sss + no_csm + no_css + no_wcsm + no_wcdm
        
            rem = dT.findall('./dataVariable')
            for x in range(len(rem)):    
                if rem[x] not in noremlist:
                    #print('rem[x]',rem[x])
                    #remx.append(rem[x])
                    dT.remove(rem[x])

        tree.write(inputFilename)
