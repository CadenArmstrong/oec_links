#!/usr/bin/python
import urllib
import os
import xml.etree.ElementTree as ET 
import exoplaneteu
import exoplanetarchive

#####################
# Configuration
#####################

	
exoplaneteu.get()
exoplaneteu.parse()

exoplanetarchive.get()
exoplanetarchive.parse()


