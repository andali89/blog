import re
import shutil
import sys
import os

# read the bibfile

def read_bib(filepath):
    with open(filepath, "r", encoding="utf8") as f:
        bib_info = f.read()
    return bib_info

def get_bib_set(bib_info: str):
    # divide the bib_info into list
    if is_illegal(bib_info):
        print("more @ in each reference")
        return False
    bibs = bib_info.split("@")   
    bib_set = []
    for bib in bibs:
        if str.strip(bib) != "":
            bib_set.append(get_name_info(bib))
    
    # sort based on reference name
    key = get_key(bib_set, 1)
    bib_set = sorted(bib_set, key=key)    
    # sort based on reference type
    key = get_key(bib_set, 0)
    bib_set = sorted(bib_set, key=key)  
    return bib_set

def is_illegal(bib_info):
    pat = r"@([^\n]*?){([^}]*?),(\s*?)\n"
    match = re.findall(pat, bib_info)
    l1 = len(match)
    pat = r"@"
    match = re.findall(pat, bib_info)
    if len(match) != l1:
        return True
    return False
            
def output_bibfile(bib_set, bib_info, filepath):
    out_str = ""  
    for bib in bib_set:
        out_str += bib[2] + "\n\n"
    if out_str == bib_info:
       print("The order of bibfile is up to date, do not need to update again!") 
       return
    with open(filepath, "w", encoding="utf8") as f:
        f.write(out_str)
    print("Successfully output sorted bibfile!")        
            
def get_key(bib_set, idx):
    key = []
    for bib in bib_set:
        key.append(bib[idx])
    
def get_name_info(bib):
    info = "@" + str.strip(bib)
    # get the name of this reference
    pat = r"^@(.*?){([^}]*?),"
    math_info = re.match(pat, info)
    return math_info[1].lower(), math_info[2], info
    
if __name__ == "__main__":
    filepath = sys.argv[1]
    #filepath = "E:/OneDrive/科研/写作/论文17-NSGAII_QP/Writing/bibtest.bib"
    if str.strip(filepath) != "" and os.path.exists(filepath):
        shutil.copyfile(filepath, filepath + "bak")
        bib_info = read_bib(filepath=filepath)
        bib_set = get_bib_set(bib_info)
        if bib_set==False:
            print("Do not sort and out put bib")
        else:
            output_bibfile(bib_set, bib_info, filepath)
    print("The sortBib processed normally!")
            
         