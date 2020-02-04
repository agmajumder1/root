@echo off
cls
echo Welcome to SALESFORCE TRANSLATION UTILITY !
echo Select From the following Metadata Types : 
echo 1. Custom Labels
echo 2. Others
set /p id=Enter Option: 

IF /i "%id%"=="1" goto customlabels
IF /i "%id%"=="2" goto others

echo "Invalid!"
goto commonexit

:customlabels
echo Starting TRANSLATION UTILITY for Custom Labels
cd C:\BuildHughes\translation-tool
CALL node translationUtilityLabels.js
echo Output successfully created !
goto commonexit

:others
echo Starting TRANSLATION UTILITY for Others
echo Under Constr.
goto commonexit
cd C:\BuildHughes\translation-tool
CALL node translationUtility.js
echo Output successfully created !
goto commonexit

:commonexit
PAUSE

