import fire
import subprocess
import os
from importlib import import_module

def call(file):
    
    mod = import_module(file)
    try:
        
        
        os.chdir(file.split(".")[0])
        subprocess.run(r"proc.bat")
        
    except Exception as e:
        rs = os.getcwd()
        os.chdir("..")
        os.chdir("internal")
        
        subprocess.run(r"env.bat")
        print("Done setting up environment")
        cwd = os.getcwd()
        os.chdir("..")
        os.chdir(file.split(".")[0])
        subprocess.run(r"proc.bat")
        
    return 

if __name__ == '__main__':
    call("Plots_from_nD_data.script")
    fire.Fire(call)