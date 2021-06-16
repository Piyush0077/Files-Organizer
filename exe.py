import cx_Freeze
import sys
import os

base = None 
if sys.platform =='win64':
    base = "Win64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Python39\tcl\tcl8.6" 
os.environ['TK_LIBRARY'] = r"C:\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("Files Organizer.py", base=base, icon="folder.ico")]


cx_Freeze.setup(
    name ="Files Organizer",
    options = {"build_exe": {"packages":["tkinter","os", "sys","shutil"], "include_files":['tcl86t.dll','tk86t.dll', 'folder.ico','images']}},
    version="1.0",
    description = "FILES ORGANISER | Developed by Piyush and Amar",
    executables = executables
    )