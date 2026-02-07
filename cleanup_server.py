import os
import signal
import psutil

print("Scanning for python/uvicorn processes...")
for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        # Check if process is python and running app.main:app
        if proc.info['name'] and 'python' in proc.info['name'].lower():
            cmdline = proc.info['cmdline']
            if cmdline and any('uvicorn' in arg for arg in cmdline):
                print(f"Propably found uvicorn: {proc.info}")
                print(f"Killing PID: {proc.info['pid']}")
                proc.kill()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
print("Cleanup complete.")
