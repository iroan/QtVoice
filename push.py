import os
import time
comment = input("comment:")
os.system("git add .")
os.system(''' git commit -m "%s" ''' %comment)
os.system("git push origin master")
