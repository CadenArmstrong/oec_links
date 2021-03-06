#!/usr/bin/python
import hashlib
import xml.etree.ElementTree as ET
import xmltools
import time
from os import listdir
from os.path import isfile

catalogues = ["open_exoplanet_catalogue", "exoplaneteu", "exoplanetarchive"]

hashfilename = "hashes/systemhashes.xml"
hashes = ET.parse(hashfilename).getroot()

html = ET.Element("html")
head = ET.SubElement(html,"head")
link = ET.SubElement(head,"link")
link.attrib["rel"] ="stylesheet"
link.attrib["type"]="text/css"
link.attrib["href"]="style.css"
body = ET.SubElement(html,"body")
table = ET.SubElement(body,"table")
tr = ET.SubElement(table,"tr")
ET.SubElement(tr,"th").text = "systemid"
for cat in catalogues:
    ET.SubElement(tr,"th").text = cat


for system in hashes.findall("./system"):
    tr = ET.SubElement(table,"tr")
    th = ET.SubElement(tr,"th")
    th.text = system.findtext("./id")
    newestdate = ""
    for cat in catalogues:
        catinfo = system.find("./catalogue[name='"+cat+"']")
        if catinfo is not None:
            date = catinfo.findtext("./date")
            if date > newestdate:
                newestdate = date
    for cat in catalogues:
        td = ET.SubElement(tr,"td")
        catinfo = system.find("./catalogue[name='"+cat+"']")
        if catinfo is not None:
            date = catinfo.findtext("./date")
            if date == newestdate:
                td.attrib["class"] = "newest"
            else:
                td.attrib["class"] = "notnewest"
            dl = ET.SubElement(td,"dl")
            ET.SubElement(dl,"dt").text = "last updated"
            ET.SubElement(dl,"dd").text = catinfo.findtext("./date")
            ET.SubElement(dl,"dt").text = "filename"
            ET.SubElement(dl,"dd").text = catinfo.findtext("./filename")
            ET.SubElement(dl,"dt").text = "hash"
            ET.SubElement(dl,"dd").text = catinfo.findtext("./hash")[0:8]
        else:
            td.attrib["class"] = "missing"



    
xmltools.indent(html)
ET.ElementTree(html).write("status.html")
