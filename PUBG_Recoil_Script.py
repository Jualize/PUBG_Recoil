import psutil

print(psutil.pids()) # Print all pids

p = psutil.Process(1245)  # The pid of desired process
print(p.name()) # If the name is "python.exe" is called by python
print(p.cmdline()) # Is the command line this process has been called with

#If you use psutil.pids() on a for, you can verify all if this process uses python, like: \/
for pid in psutil.pids():
    p = psutil.Process(pid)
    if p.name() == "python.exe":
        print("Called By Python:"+ str(p.cmdline())
