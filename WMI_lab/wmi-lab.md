
# CPU clock monitoring: a case to discover WMI

With the Dynamic frequency Scaling technologies of modern CPU, sometimes in performance requiring situations is useful to know when a CPU is under unadverted trhottling condition. It can be done by checking the current CPU frequency.

On this basic case, the objective is to show the current CPU clock on a Windows Tray Icon. To meed theese needs **Windows Management Instrumentation** has a large API to get Windows system information. This experiment approached the following different implementations:

- Power shell script example  - Used for basic query and console outputs
- Python lab using a particular library - Did the job, but with high cpu usage

Those studies above were important do build the knowlege base for the last implementation that follows

- C# implementation using .net framework built in tools for WMI - Too big memory footprint (25MB) for a tiny app. This is .net


### References

1. PowerShell
- <https://superuser.com/questions/1560740/reading-live-sensor-information-through-the-commandline-on-windows-10>
- <https://www.remkoweijnen.nl/blog/2014/07/18/get-actual-cpu-clock-speed-powershell/>
- <https://www.reddit.com/r/PowerShell/comments/boqh5j/how_to_get_current_cpu_clock_speed_like_in_task/>
- <https://stackoverflow.com/questions/61802420/unable-to-get-current-cpu-frequency-in-powershell-or-python>
- <https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-counter?view=powershell-7.1>

2. Pithon
- <https://www.devdungeon.com/content/dialog-boxes-python>
- <https://www.geeksforgeeks.org/find-average-list-python/>
- <https://www.cac.cornell.edu/wiki/index.php?title=Performance_Data_Helper_in_Python_with_win32pdh#GetCounterInfo>
- <http://timgolden.me.uk/pywin32-docs/win32_modules.html>
- <https://stackoverflow.com/questions/2675028/list-attributes-of-an-object>
- <https://stackoverflow.com/questions/59242582/how-to-destroy-the-icon-tray-when-the-program-ends>
- <https://stackoverflow.com/questions/55381039/dynamic-system-tray-text-python-3>
- <https://stackoverflow.com/questions/61802420/unable-to-get-current-cpu-frequency-in-powershell-or-python>
- <https://github.com/Infinidat/infi.systray/blob/develop/src/infi/systray/traybar.py>
- <https://github.com/Infinidat/infi.systray>
- <https://mail.python.org/pipermail/python-win32/2004-February/001652.html>

3. [Markdown](https://www.markdownguide.org/basic-syntax/)