Format-table
Format-list

get-service | get-member
get-command -noun service
get-service -name spooler
get-service -name spooler | stop-service
get-service -name spooler | start-service
get-command -noun process
notepad spooler.txt
get-content -path .\spooler.txt
get-content -path .\spooler.txt
get-hep stop-service -Parameter
get-content -path .\spooler.txt | gm #get-member


import-csv .\data.csv | gm 
help restart-service -Parameter *


import-csv .\data.csv | restart-service -Force

get-module -ListAvailable | Select-object -Property name

get-command -verb export

get-module -ListAvailable | Select-object -Property name | export-csv path modules.csv
notepad .\modules.csv

get-module -ListAvailable | Select-object -Property name | convertto-xml

get-module -ListAvailable | Select-object -Property name | export-clixml -path modules.xml

start wordpad .\modules.xml

get-module -ListAvailable | select-object -property name | convertTo-Html | out-file module.html
get-module -name activedirectory | gm

dir env:\psmodulepath

dir env:\psmodulepath | fl

$profile

new-item -path $profile -force

notepad $profile

get-psdrive


#EXERCISE
get-process | Format-table Autosize
get-service | Format-List 
get-pssnapin
get-module -ListAvailable


