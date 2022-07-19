# Windows 7/10 setup tips

### Disable hibernate function (and fast startup so)

	powercfg.exe /hibernate off

### Install all updates in a contatining folder

```
for %h in (*x64*.msu) do start /wait wusa "%cd%\%h" /quiet /norestart
# with logs:
for %h in (*x64*.msu) do start /wait  wusa "%cd%\%h" /quiet /norestart /log:"%cd%\logs\%h.log"
```


### Reset filesystem permissions
	icacls "C:\Users\..." /reset /t

		