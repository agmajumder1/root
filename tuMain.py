import os

print("====================================================================================")
print("===================  Welcome to Translation Utility Accelerator  ===================")
print("====================================================================================")
print("==                                                                                ==")
print("== Tranlation Utility is a tool / accelerator that helps in comparing translatable==")
print("== Salesforce metadata and checking them against the respective translation files ==")
print("== in the local repository. The outputs are in csv format files giving details of ==")
print("== translation filename, the API name of the metadata and the Error which gives   ==")
print("== clarity by stating whether the API name itself is missing from the translation ==")
print("== file or with the value, commented in the translation file. 	\t	  ==")                
print("==                                                                                ==")
print("====================================================================================")
print("====================================================================================")
print("\n \nPlease choose one from the following options : ")
print("\t1. Custom Labels Translation")
print("\t2. Standard Value Sets Translation")
print("\t3. Validation Error Message Translation")
print("\t4. Help Message Translation")
print("\t5. Custom Picklist Translation")

a = input("\nYour Choice = ")
print("\nYou have chosen Option "+a+"\n")

if a == '1':
	os.system('python tuLabels.py')
elif a == '2':
	os.system('python tuStdvalset.py')
elif a == '3':
	os.system('python tuValerrmssg.py')
elif a == '4':
	os.system('python tuHelpmssg.py')
elif a == '5':
	os.system('python tuCustvalset.py')
else:
	print("\nInvalid Input! Please contact Admin @agmajumder1 Github")





