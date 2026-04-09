# Documentation used in code: https://docs.python.org/3/
import os
import glob
import tkinter
from tkinter import filedialog
# Opens Pop-up that allows user to select folder that contains html files.
def folder_select():
    root=tkinter.Tk()
    root.withdraw()
    folder=filedialog.askdirectory(title="Select Folder:")
    root.destroy()
    return folder
# Opens Pop-up that allows user to select markdown file that contains script.
def script_select():
    root=tkinter.Tk()
    root.withdraw()
    script=filedialog.askopenfilename(title="Select Script:",filetypes=(("Markdown Files","*.md"), ("Markdown Files","*.MD")))
    root.destroy()
    return script
# Turns script file into usable string.
def define_script(script):
    if not script:
        return "Error: No file selected."
    try:
        with open(script,'r',encoding='utf-8') as file:
            markdown=file.read()
        return markdown
    except FileNotFoundError:
        return "Error: File was not found!"
    except Exception as error:
        return f"Error: An error occurred: {error}"
# Counts HTML files in folder
def count_folder(folder):
    count=0
    for root,dirs,files in os.walk(folder):
        for file in files:
            if file.endswith(".html"):
                count+=1
    return count
# Injects script into </body> only if </body> exists and script does not exist.
def inject_script(folder,markdown):
    if not folder or markdown.startswith("Error"):
        print(markdown if markdown.startswith("Error") else "Error: No folder selected.")
        return
    os.chdir(folder)
    totalfiles=count_folder(folder)
    updatedcount=0
    skippedcount=0
    for filepath in glob.glob("*.html"):
        with open(filepath,'r',encoding="utf-8") as file:
            filecheck=file.read()
        if "</body>" in filecheck:
            if markdown in filecheck:
                print(f"Skipped: {filepath} (Script already exists)")
                skippedcount+=1
            else:
                newfile=filecheck.replace("</body>",f"{markdown}</body>")
                with open(f"Output-{filepath}",'w',encoding="utf-8") as newchange:
                    newchange.write(newfile)
                updatedcount+=1
        else:
            print(f"Skipped: {filepath} (No </body> tag found)")
    print(f"Total HTML files found: {totalfiles}")
    print(f"Files updated: {updatedcount}")
    print(f"Files skipped: {skippedcount}")
inject_script(folder_select(),define_script(script_select()))