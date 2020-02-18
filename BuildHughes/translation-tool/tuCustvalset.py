# Created Date : 15/12/2019
# Created By : Ashin Guha Majumder
# Sub Module of Translation Utility tool to check translation for custom picklist values.

import os
import csv
import xml.etree.ElementTree as ET
from codecs import open

#READING SRC FILE
path = 'C:\\BuildHughes\\translation-tool\\inputs\\source_meta\\objects'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.object' in file:
            files.append(os.path.join(r, file))


path = 'C:\\BuildHughes\\translation-tool\\inputs\\translation_files\\objectTranslations'

transfiles = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for transfile in f:
        if '.objectTranslation' in transfile:
            transfiles.append(os.path.join(r, transfile))

print ("Processing Files >>>>>>>>")

			
for fn in files:
	fnlen = len(fn)
	#fnraw= C:\BuildHughes\translation-tool\inputs\source_meta\standardValueSets\AccountRating.standardValueSet
	       #C:\BuildHughes\translation-tool\inputs\source_meta\objects\Account.object
	fnrawname = fn[59:fnlen-7]
	tree = ET.parse(fn)
	root = tree.getroot()
	#SAVING THE API NAMES AND VALUES OF THE LABELS
	apiname = []
	value = []
	for api in root.findall(".//{http://soap.sforce.com/2006/04/metadata}value/{http://soap.sforce.com/2006/04/metadata}label"):
		#if api.find("/{http://soap.sforce.com/2006/04/metadata}label") is not None:
		if api is not None: 
			apiname.append(api.text)
			#print(api.text)
		#print(api.find("/{http://soap.sforce.com/2006/04/metadata}label").text)
	#for val in root.findall("./{http://soap.sforce.com/2006/04/metadata}fields/{http://soap.sforce.com/2006/04/metadata}"):
					#value.append(api.find("{http://soap.sforce.com/2006/04/metadata}inlineHelpText").text)
	#READING TRANSLATION FILES ONE BY ONE AND STORING SEARCH RESULT IN OUTPUT FILE		
	#print("****************************************************")

	for f in transfiles:
		fi=f[76:]  		#C:\BuildHughes\translation-tool\inputs\translation_files\standardValueSetTranslations\AssetStatus-es_CL.standardValueSetTranslation
		flen=len(fi) 	#C:\BuildHughes\translation-tool\inputs\translation_files\objectTranslations\Account-es_AR.objectTranslation
		transrawname = fi[:flen-24]
		if transrawname == fnrawname:
			with open('./output/Custom Picklist Translations/'+fi+'_TranslationUtilityOutput.csv','w', encoding='utf-8') as f1:
				writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
				header = ["Translation File","API Name","Error"]
				writer.writerow(header)
				tree = ET.parse(f)
				root = tree.getroot()
				#SAVING THE API NAMES AND VALUES OF THE LABELS
				transapinamelist = []
				transvalnamelist = []

				for transapi in root.findall(".//{http://soap.sforce.com/2006/04/metadata}picklistValues"):
					if transapi.find("{http://soap.sforce.com/2006/04/metadata}masterLabel") is not None:	
						if transapi.find("{http://soap.sforce.com/2006/04/metadata}translation") is not None:
						#print(transapi.find("{http://soap.sforce.com/2006/04/metadata}name").text)
							transapinamelist.append(transapi.find("{http://soap.sforce.com/2006/04/metadata}masterLabel").text)
							#print(transapi.find("{http://soap.sforce.com/2006/04/metadata}masterLabel").text)
			#for val in root.findall("./{http://soap.sforce.com/2006/04/metadata}fields/{http://soap.sforce.com/2006/04/metadata}"):
							transvalnamelist.append(transapi.find("{http://soap.sforce.com/2006/04/metadata}translation").text)
							#print(transapi.find("{http://soap.sforce.com/2006/04/metadata}translation").text)

				#for transapi in root.findall('.//{http://soap.sforce.com/2006/04/metadata}name'):
				#	transapiname = transapi.text
				#	transapinamelist.append(transapiname)
				#for transval in root.findall('.//{http://soap.sforce.com/2006/04/metadata}help'):
				#	transvalname = transval.text
				#	transvalnamelist.append(transvalname)

				for api in apiname:
					if api not in transapinamelist:
						str = [fi,api,"API name not found in translation file."]
						writer.writerow(str)
					#Checking commeneted value for label - can be commented api or label
					elif api in transapinamelist: 
						index = transapinamelist.index(api)  #To use same index for finding if Label Value present or not
						#print(index)
						if transvalnamelist[index] is None:
							str = [fi,api,"Value commented/not found in translation file."]
							writer.writerow(str)
print("Translation Utility Comparison CSV created in output folder.")