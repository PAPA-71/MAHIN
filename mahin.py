import platform
import os
arc = str(platform.uname().machine)
if 'arm' in arc:
    __import__("nothung")._login()
elif 'aarch' in arc:
    __import__("MAHIN").licenseone()
else:
    exit(f'unknow device machine {arc}')
