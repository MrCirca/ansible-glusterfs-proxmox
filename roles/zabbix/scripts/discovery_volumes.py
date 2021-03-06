#!/usr/bin/python
import json
import subprocess
import xml.etree.ElementTree as ET
import sys

gluster_volumes_xml = subprocess.check_output('gluster --xml volume status all detail', shell=True)

#print(gluster_volumes_xml)
root  = ET.fromstring(gluster_volumes_xml)

def volumeNames():
    volumes = root.find('volStatus').find('volumes').findall('volume')
    gluster_volume_info = []

    for volume_name in volumes:
        gluster_volume_name = volume_name.find('volName').text
        gluster_volume_info.append({"#VOLUME_NAME": gluster_volume_name})

    return json.dumps({'data': gluster_volume_info})

test = sys.argv[1]

if test == "volumes":
    print(volumeNames())


