# Developer References:
# https://superuser.com/questions/1560740/reading-live-sensor-information-through-the-commandline-on-windows-10
# https://www.remkoweijnen.nl/blog/2014/07/18/get-actual-cpu-clock-speed-powershell/
# https://www.reddit.com/r/PowerShell/comments/boqh5j/how_to_get_current_cpu_clock_speed_like_in_task/
# https://stackoverflow.com/questions/61802420/unable-to-get-current-cpu-frequency-in-powershell-or-python
# https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-counter?view=powershell-7.1

# How many times to query clockspeed
$count = 100
# Interval in ms
$interval = 1500;
 
 
# Little helper to add colours to output
filter ColorPattern( [string]$Pattern, [ConsoleColor]$Color, [switch]$SimpleMatch ) {
  if( $SimpleMatch ) { $Pattern = [regex]::Escape( $Pattern ) }
 
  $split = $_ -split $Pattern
  $found = [regex]::Matches( $_, $Pattern, 'IgnoreCase' )
  for( $i = 0; $i -lt $split.Count; ++$i ) {
    Write-Host $split[$i] -NoNewline
    Write-Host $found[$i] -NoNewline -ForegroundColor $Color
  }
 
  Write-Host
}
 
#Get Maximum Clock Speed (once because WMI is slow)
$maxClockSpeed = (get-wmiobject Win32_Processor | select-object -first 1).MaxClockSpeed
 
#default color
$highlighColor = 'Green'
 
function GetPerformance(){

	if (!$maxClockSpeed){
		$maxClockSpeed = (Get-CimInstance CIM_Processor).MaxClockSpeed
	}
	write-host ("MaxClockSpeed "+$maxClockSpeed)
	$ProcessorPerformance = (Get-Counter -Counter "\Informações do Processador(_total)\% de Desempenho do Processador").CounterSamples.CookedValue
	write-host ("ProcessorPerformance "+$ProcessorPerformance)
	$CurrentClockSpeed = $maxClockSpeed*($ProcessorPerformance/100)

	Write-Host "Current Processor Speed: " -ForegroundColor Yellow -NoNewLine
	Write-Host $CurrentClockSpeed

}

function GetClockSpeed()
{
	#EN Language HyperV
	#$freq = Get-Counter -Counter "HyperV Hypervisor\Logical Processor\Frequency"
	
	#EN Language
	#$freq = Get-Counter -Counter "\Processor Information(*)\Processor Frequency"
	
	#PT-BR Language HyperV
	#$freq = Get-Counter -Counter "\Processador Lógico do Hipervisor Hyper-V(*)\Frequência"
	
	#PT-BR Language
	$freq = Get-Counter -Counter "\informações do processador(*)\frequência do processador"
	
	$item = New-Object  System.Object
	
	Write-Host $freq

	foreach ($cpu in $freq.CounterSamples)
	{
		#Write-Host ("cpu-path " +  $cpu.Path)
		$procNum = ([RegEx]::Match($cpu.Path, '.+\((\d+,\d+)\).*')).Groups[1].Value
		if ($procNum)
		{
			$item | Add-Member -Type NoteProperty -Name $procNum -Value $cpu.CookedValue
		}
	}
	
	$item
}


for ($i=0 ; $i -lt $count ; $i++)
{
	GetPerformance
	Start-Sleep -Milliseconds $interval
}
function SampleClock(){
	$list = GetClockSpeed 
	#Clear-Host
	
	#Write-Debug -Message "[string]: {0}" $list
	#Write-Host ($list | Format-List | Out-String)
	#Write-Host "objeto :: " ($list | Format-Table -Force | Out-String) "::"
	
	$firstCoreSpeed = ($list | Select-Object -ExpandProperty "0,0")
	#Write-Host ("Core speed:" + $firstCoreSpeed)
	#Write-Host ("MAx Core speed:" + $maxClockSpeed)
	#Write-Debug "end"
	
	# Just some formatting magic, make it green if full speed and red otherwise
	if ($firstCoreSpeed -lt $maxClockSpeed) { $highlighColor = 'Red' } else { $highlighColor = 'Green' }
	
	"Actual: {0} Mhz Maximum: {1} Mhz -> {2:P0}" -f $firstCoreSpeed, $maxClockSpeed, ($firstCoreSpeed / $maxClockSpeed) | ColorPattern -Pattern '\d+ %' -Color $highlighColor
	"Speed per Core:"
	
	$list | Format-Table -AutoSize | Out-String | ColorPattern -Pattern '\d\d+' -Color $highlighColor #-SimpleMatch
	
	
	# Sleep until next interval
	
}
