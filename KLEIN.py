import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

bit = platform.architecture()[0]
if bit == '64bit':
    import jk                                                                                                                                 
elif bit == '32bit':
    import 32jk
else:
    import jk
