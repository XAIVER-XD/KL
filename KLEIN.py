import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

bit = platform.architecture()[0]
if bit == '64bit':
    import fk                                                                                                                                 
elif bit == '32bit':
    import 32fk
else:
    import fk
