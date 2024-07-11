#shutil.copy
#shutil.copyfile
import shutil
import time
time.sleep(2)
shutil.copy(".hushlogin","$HOME")
print("Succes!")