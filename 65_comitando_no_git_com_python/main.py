import sys
import os

os.system("git add .")
os.system(f"git commit -m '{sys.argv[0]}'")
os.system("git push origin master")
