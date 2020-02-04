import os
import csv
import xml.etree.ElementTree as ET
from codecs import open

#READING CUSTOM LABELS FILE
path = 'C:\\BuildHughes\\translation-tool\\inputs\\source_meta\\labels'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.labels' in file:
            files.append(os.path.join(r, file))
			
for f in files:
	tree = ET.parse(f)
	root = tree.getroot()
	#SAVING THE API NAMES AND VALUES OF THE LABELS
	apiname = []
	value = []
	for api in root.findall("./{http://soap.sforce.com/2006/04/metadata}labels/{http://soap.sforce.com/2006/04/metadata}fullName"):
		apiname.append(api.text)
	for val in root.findall("./{http://soap.sforce.com/2006/04/metadata}labels/{http://soap.sforce.com/2006/04/metadata}value"):
		value.append(val.text)

#READING TRANSLATION FILES ONE BY ONE AND STORING SEARCH RESULT IN OUTPUT FILE
path = 'C:\\BuildHughes\\translation-tool\\inputs\\translation_files\\translations'

print ("Processing Translation Files >>>>>>>>")

transfiles = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for transfile in f:
        if '.translation' in transfile:
            transfiles.append(os.path.join(r, transfile))
			
for f in transfiles:
	fi=f[70:]
	with open('./output/Custom Label Translations/'+fi+'_TranslationUtilityOutput.csv','w') as f1:
		writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
		header = ["Translation File","API Name","Error"]
		writer.writerow(header)
		tree = ET.parse(f)
		root = tree.getroot()
		#SAVING THE API NAMES AND VALUES OF THE LABELS
		transapinamelist = []
		transvalnamelist = []
		for transapi in root.findall('.//{http://soap.sforce.com/2006/04/metadata}name'):
			transapiname = transapi.text
			transapinamelist.append(transapiname)
		for transval in root.findall('.//{http://soap.sforce.com/2006/04/metadata}label'):
			transvalname = transval.text
			transvalnamelist.append(transvalname)
		for api in apiname:
			if api not in transapinamelist:
				str = [fi,api,"API name not found in translation file."]
				writer.writerow(str)
			#Checking commeneted value for label - can be commented api or label
			elif api in transapinamelist: 
				index = transapinamelist.index(api)  #To use same index for finding if Label Value present or not
				if transvalnamelist[index] is None:
					str = [fi,api,"Value commented/not found in translation file."]
					writer.writerow(str)

print("Translation Utility Comparison CSV created in output folder.")