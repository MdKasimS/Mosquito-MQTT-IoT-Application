import subprocess
import os
import signal
import psutil
from time import sleep


def initBroker(server):
    subprocess.Popen(server, shell=True)
    return "success"

def closeBroker(pid):
    sleep(0.5)
    try:
        os.kill(pid, signal.SIGTERM)
        print(f"Broker terminated : {pid}")
    except OSError as e:
        print(f"Error terminating process with PID {pid}: {e}") 

def get_pid_by_name(process_name):
    sleep(0.025)
    for process in psutil.process_iter(['pid', 'name']):
        if process_name.lower() in process.info['name'].lower():
            return process.info['pid']
    return None

def acknowledgeAllClients():
    pass

