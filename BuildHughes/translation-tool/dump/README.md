#=====================================================
#<================== READ ME FILE ===================>
#<============= Translation Utility =================>
##====================================================

#Created By : Ashin Guha Majumder 
#Email : <aguhamajumder@deloitte.com>
#Personal Email : <agmajumder@gmail.com>
#Company : Deloitte USI
#Created Date : 28/10/2019

#Current Version : v1.1
#Version Release Date : 6/11/2019


#Notes to start working with Translation Utility Tool->
##Tool Aim > To provide insights on - 
1. Translation Value not updated due to not updating API names in Translation File.
2. New Translation Values which are not updated in Translation Language/File due to not adding API names in translation File.
3. Translation Values which are commented in Translation File hence Translation not available in Client's Translation Language.

#How to Install/Use the tool ?
install node.js
npm install node-xml-stream --save
1. git clone ---- TO ADD MY REPO BRANCH LINK//////////////
1. Install node from https://nodejs.org/en/
1. npm install
1. Tool will work only for following metadata types in -> customLabels, .///////... TO ADD (Can be enhanced as per client requirement)
1. Place your source meta in : translation-tool\inputs\source_meta (Place exact metadata folder of above type unaltered) Eg: "labels" folder
1. Place your translation files in : translation-tool\inputs\translation_files (Place exact translation metadata folder of above type unaltered) Eg : "translations" foler
1. Click on main.bat in C:\BuildHughes\translation-tool -> Enter inputs and Wait for tool to run
1. Translation Search Errors are saved in : C:\BuildHughes\translation-tool\output\Translation_Search_Errors.xls
1. Review Issues in Excel and update the translations accordingly

#Note: 
1. In some cases output might be showing undefined in some columns - which means there is no data for that metadata
1. In rare cases the value / API name might be having some characters which might mess up the tabbing in the xml, but nothing to worry - please check the next row - data about the error will be present in two rows in these cases instead of one.

#======================================================
