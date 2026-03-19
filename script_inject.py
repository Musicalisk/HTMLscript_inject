import os
import glob
import tkinter
from tkinter import filedialog
# Opens Pop-up that allows user to select folder that contains html files.
def folder_select():
    r=tkinter.Tk()
    r.withdraw()
    f=filedialog.askdirectory(title="Select Folder:")
    r.destroy()
    return f
# Opens Pop-up that allows user to select markdown file that contains script.
def script_select():
    r=tkinter.Tk()
    r.withdraw()
    s=filedialog.askopenfilename(title="Select Script:",filetypes=(("Markdown Files","*.md"), ("Markdown Files","*.MD")))
    r.destroy()
    return s
# Turns script file into usable string.
def define_script(s):
    if not s:
        return "Error: No file selected."
    try:
        with open(s,'r',encoding='utf-8') as f:
            m=f.read()
        return m
    except FileNotFoundError:
        return "Error: File was not found!"
    except Exception as e:
        return f"Error: An error occurred: {e}"
# Counts HTML files in folder
def count_folder(f):
    c=0
    for root,dirs,files in os.walk(f):
        for file in files:
            if file.endswith(".html"):
                c+=1
    return c
# Injects script into </body> only if </body> exists and script does not exist.
def inject_script(f, s):
    if not f or s.startswith("Error"):
        print(s if s.startswith("Error") else "Error: No folder selected.")
        return
    os.chdir(f)
    tf=count_folder(f)
    uc=0
    sc=0
    for filepath in glob.glob("*.html"):
        with open(filepath,'r',encoding="utf-8") as fl:
            fc=fl.read()
        if "</body>" in fc:
            if s in fc:
                print(f"Skipped: {filepath} (Script already exists)")
                sc+=1
            else:
                nf=fc.replace("</body>",f"{s}</body>")
                with open(f"Output-{filepath}",'w',encoding="utf-8") as nc:
                    nc.write(nf)
                uc+=1
        else:
            print(f"Skipped: {filepath} (No </body> tag found)")
    print(f"Total HTML files found: {tf}")
    print(f"Files updated: {uc}")
    print(f"Files skipped: {sc}")
inject_script(folder_select(),define_script(script_select()))