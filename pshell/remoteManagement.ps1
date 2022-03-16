#Manipulating the command Pipeline
get-service | select-object -property status,name -expandproperty name | group-object -property status | format-list
get-service | select-object -property status,name | gm
gcm -verb *out


#DOT Syntax and Powershell ISE
$wrm = get-Service -Name WinRm
$wrm.start

#Sorting Pipeline output
Get-Process | Sort-object ws -Descending

#understanding remoting architecture

#powershell remoting architecture
Enter-PSSession -ComputerName nomad01
Enable-PSRemoting
enter-pssession -ComputerName nomad01
enter-pssession -ComputerName nomad02
exit-pssession
get-command -noun enter-pssession
$nomad01 = new-pssession -ComputerName nomad01
enter-pssession -id 2


#serial vs parallel remoting
Enable-PSRemoting -SkipNetworkProfileCheck # Modify [CmdletBinding()] to [CmdletBinding(SupportsShouldProcess=$true, DefaultParameterSetName='Path')]
Get-WmiObject -ComputerName nomad01,nomad02 -Class win32_bios | fl
Get-ExecutionPolicy
Enter-PSSession -ComputerName nomad01 

Invoke-Command -ComputerName nomad01,nomad02 -ScriptBlock { Get-EventLog -LogName Security -Newest 5 }
Set-ExecutionPolicy -ExecutePolicy Unrestricted -Scope
Invoke-Command -ComputerName localhost,nomad01 { Get-ExecutionPolicy }
Connect-WSman
Get-PSProvider
set-item .\trustedHosts -value nomad01^C


$paths = @()
if ($psCmdlet.ParameterSetName -eq 'Path') {
    foreach ($aPath in $Path) {
        if (!(Test-Path -Path $aPath)) {
            $ex = New-Object System.Management.Automation.ItemNotFoundException "Cannot find path '$aPath' because it does not exist."
            $category = [System.Management.Automation.ErrorCategory]::ObjectNotFound
            $errRecord = New-Object System.Management.Automation.ErrorRecord $ex,'PathNotFound',$category,$aPath
            $psCmdlet.WriteError($errRecord)
            continue
        }
    
        # Resolve any wildcards that might be in the path
        $provider = $null
        $paths += $psCmdlet.SessionState.Path.GetResolvedProviderPathFromPSPath($aPath, [ref]$provider)
    }
}
else {
    foreach ($aPath in $LiteralPath) {
        if (!(Test-Path -LiteralPath $aPath)) {
            $ex = New-Object System.Management.Automation.ItemNotFoundException "Cannot find path '$aPath' because it does not exist."
            $category = [System.Management.Automation.ErrorCategory]::ObjectNotFound
            $errRecord = New-Object System.Management.Automation.ErrorRecord $ex,'PathNotFound',$category,$aPath
            $psCmdlet.WriteError($errRecord)
            continue
        }
    
        # Resolve any relative paths
        $paths += $psCmdlet.SessionState.Path.GetUnresolvedProviderPathFromPSPath($aPath)
    }
}

foreach ($aPath in $paths) {
    if ($pscmdlet.ShouldProcess($aPath, 'Operation')) {
        # Process each path
        
    }
}