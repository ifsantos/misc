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


### W10 setup
slmgr/dlv
slmgr/upk


comando para verificar arquivos do sistema: sfc /scannow

Comando de ativação e Seriais


cscript slmgr.vbs /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH

cscript slmgr.vbs /skms kms.lotro.cc

cscript slmgr.vbs /ato

==================================================================
Home/Core                            TX9XD-98N7V-6WMQ6-BX7FG-H8Q99
Home/Core (Country Specific)         PVMJN-6DFY6-9CCP6-7BKTT-D3WVR
Home/Core (Single Language)          7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH
Home/Core N                          3KHY7-WNT83-DGQKR-F7HPR-844BM
Professional       (Windows 10 pro)                  W269N-WFGWX-YVC9B-4J6C9-T83GX
Professional N     (Windows 10 pro N)                  MH37W-N47XK-V7XM9-C7227-GCQG9
Enterprise                           NPPR9-FWDCX-D2C8J-H872K-2YT43
Enterprise N                         DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4
Education                            NW6C2-QMPVW-D7KKK-3GKT6-VCFB2
Education N                          2WH4N-8QGBV-H22JP-CT43Q-MDWWJ
Enterprise 2015 LTSB                 WNMTR-4C88C-JK8YV-HQ7T2-76DF9
Enterprise 2015 LTSB N               2F77B-TNFGY-69QQF-B8YKP-D69TJ
Enterprise 2016 LTSB                 DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ
Enterprise 2016 LTSB N               QFFDN-GRT3P-VKWWX-X7T3R-8B639

