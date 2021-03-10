# text to image : Pillow (https://pillow.readthedocs.io/en/latest/handbook/tutorial.html - simple code sample:  https://code-maven.com/create-images-with-python-pil-pillow)
# icon in systray : infi.systray (https://github.com/Infinidat/infi.systray and https://stackoverflow.com/a/54082417/3154274)

# inspired by https://www.reddit.com/r/learnpython/comments/a7utd7/pystray_python_system_tray_icon_app/

# This piece of code is based on above referrences
#
# Current Developer references:
# https://www.devdungeon.com/content/dialog-boxes-python
# https://www.geeksforgeeks.org/find-average-list-python/
# https://www.cac.cornell.edu/wiki/index.php?title=Performance_Data_Helper_in_Python_with_win32pdh#GetCounterInfo
# http://timgolden.me.uk/pywin32-docs/win32_modules.html
# https://stackoverflow.com/questions/2675028/list-attributes-of-an-object
# https://stackoverflow.com/questions/59242582/how-to-destroy-the-icon-tray-when-the-program-ends
# https://stackoverflow.com/questions/55381039/dynamic-system-tray-text-python-3
# https://stackoverflow.com/questions/61802420/unable-to-get-current-cpu-frequency-in-powershell-or-python
# https://github.com/Infinidat/infi.systray/blob/develop/src/infi/systray/traybar.py
# https://github.com/Infinidat/infi.systray
# https://mail.python.org/pipermail/python-win32/2004-February/001652.html


# install PIL :  pip install Pillow
# install infi.systray : pip install infi.systray
# instal win32PDH: pip install pywin32

from infi.systray import SysTrayIcon
from PIL import Image, ImageDraw,ImageFont
import win32ui
import time
import wmi

CPU_CLOCK = 0.0
def update_cpu_clock(c_max,c_wmi):
    """
    TLDR: To find the Current Processor Frequency, you have to use the % Processor Performance performance counter
    """
    c_perf = get_cpu_perf(c_wmi)
    CPU_CLOCK = c_max*(c_perf/100)
    return CPU_CLOCK

def get_cpu_perf(c_wmi):
    processor_perf = [int(cpu.PercentProcessorPerformance) for cpu in c_wmi.Win32_PerfFormattedData_Counters_ProcessorInformation()]    
    return sum(processor_perf)/len(processor_perf)

def get_cpu_max(c_wmi):
    cpu_max = [cpu.MaxClockSpeed for cpu in c_wmi.Win32_Processor()][0]
    print (f"max CPU: {cpu_max}")
    return cpu_max

def on_quit_callback(systra):
    print (str(systra))
    try:
        SysTrayIcon.shutdown(systra)
        systra.shutdown()
    except Exception as err:
        print ("FALHA: " + str(err))
    finally:
        print ("Exit called")
        raise SystemExit

def show_messagebox(a):
    print (str(a.cpu_clock))
    message = "   {:.1f} Ghz".format(CPU_CLOCK)
    title = "CPU Speed"
    win32ui.MessageBox(message, title)
    print("[Dialog] {} - {}".format(title,message))

def print_log(a):
    print("Menu pushed: log")

image="pil_text.ico"
n=1

def generate_icon(cpu_clock):
    # create image
    img = Image.new('RGBA', (50, 50), color = (255, 255, 0, 0))  # color background =  white  with transparency
    d = ImageDraw.Draw(img)
    d.rectangle([(0, 40), (50, 50)], fill=(39, 112, 229), outline=None)  #  color = blue

    #add text to the image
    font_type  = ImageFont.truetype("arial.ttf", 36)
    d.text((0,0), "{:.1f}".format(cpu_clock), fill=(0,0,255), font = font_type)
    img.save(image)

if True:
   
    #menu
    menu_options = (("CPU Speed",None,show_messagebox),("Log",None,print_log))
    c = wmi.WMI()
    c_max = get_cpu_max(c)
    # display image in systray 
    with SysTrayIcon(image, "CPU Clock", menu_options, on_quit=on_quit_callback, default_menu_index=0) as systray:
        while True:
            cpu_clock = update_cpu_clock(c_max, c)/1000
            generate_icon(cpu_clock)
            systray.update(icon=image)
            systray.update(hover_text="{:.1f}Ghz".format(cpu_clock))
            time.sleep(2)

exit(0)

#DEPRECATED
#######################################################################################################################
#    if n==1:
#        systrayX = SysTrayIcon(image, "CPU Clock", menu_options, on_quit=on_quit_callback, default_menu_index=0)
#        systrayX.start()
#    else:
#        systrayX.update(icon=image)
#        systrayX.update(hover_text="{:.1f}Ghz".format(a))
#    time.sleep(2)
#    n+=1
#systrayX.shutdown()

# def get_windows_counter():
#     """deprecated method
#     """
#     path = win32pdh.MakeCounterPath((None,"Informações do Processador", "_Total", None, -1, "\% de Desempenho do Processador"))
#     base = win32pdh.OpenQuery()
#     counter = win32pdh.AddCounter(base, path)
#     win32pdh.GetCounterInfo(counter, 0)
#     # Traceback (most recent call last):
#     #   File "<interactive input>", line 1, in ?
#     # error: (-2147481646, 'GetCounterInfo for size', 'No error message is 
#     # available')

#     win32pdh.CollectQueryData(base)
#     win32pdh.CollectQueryData(base)
#     win32pdh.GetFormattedCounterValue(hc,win32pdh.PDH_FMT_LONG)
#     # (558957824, 6)
    #So my counter is "well formed".