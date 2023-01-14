import os,platform,time                                    
bitt=platform.architecture()[0]

if bitt=="64bit":
    time.sleep(2)
    import r

else:

    print('\n32 BIT NOT SUPPORTED ')
