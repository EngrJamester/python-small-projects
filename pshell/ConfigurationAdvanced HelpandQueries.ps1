Get-history
get-history | where-object { $_.CommandLine -like "*history*" }
$w = New-Object -ComObject wscript.shell
$w.popup("All Done")
sysdm.cpl
cmd.exe
appwiz.cpl


get-psdrive

cd function:
dir
Get-Help @PSBoundParameters | more
$x = Get-ChildItem function:c:
$x.definition
$MyInvocation.MyCommand.Name

show-command
show-command

Get-EventLog 

help Get-EventLog

help Get-EventLog -ShowWindow

Get-EventLog -List

get-help get-ChildItem -full

get-help -verb about_*

Get-Service

Get-Service | Select-Object -Property Status,DisplayName | Where-Object { $_.status -eq "Running" }

Get-Service | Select-Object -Property Status,DisplayName | Where-Object { $_.status -eq "Stopped" }

Get-Service | ` 
Select-Object -Property Status,DisplayName ` 
| Where-Object ` 
{ $_.status -eq "Stopped" }

function getMysv{
	Get-Service | `
	Select-Object -Property Status, Name `
	| Where-Object { $_.status -eq "Stopped" }
}

.\getsv.ps1

. C:\scripts\getsv.ps1 
dir function:
