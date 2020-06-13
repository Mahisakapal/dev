
# def ping(host):
#     """
#     Returns True if host responds to a ping request
#     """
#     import subprocess, platform

#     # Ping parameters as function of OS
#     ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
#     args = "ping " + " " + ping_str + " " + host
#     need_sh = False if  platform.system().lower()=="windows" else True

#     # Ping
#     return subprocess.call(args, shell=need_sh) == 0

# # test call

# ping("googelkjkjkj.com")


import subprocess
import platform
import time

starttime=time.time()

 
for var in range(1,20):
    
    operating_sys = platform.system()
    nas = 'google.com' 
    

    def ping(ip ):
        # ping_command = ['ping', ip, '-n', '1'] instead of ping_command = ['ping', ip, '-n 1'] for Windows
        ping_command = ['ping', ip, '-n', '1'] if operating_sys == 'Windows' else ['ping', ip, '-c 1']
        shell_needed = True if operating_sys == 'Windows' else False

        ping_output = subprocess.run(ping_command,shell=shell_needed,stdout=subprocess.PIPE)
        success = ping_output.returncode
        return True if success == 0 else False


    out = ping(nas)  



    
    if out == True:
        print("PLU is connected")
        #var += 1
        
    else:
        print(r"NOT connected with PLU "  +"\n " + "check LAN & IP" ) 
        #var += 1
    time.sleep(2.0 - ((time.time() - starttime) % 2.0))


       

