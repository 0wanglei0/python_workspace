import os.path
import shutil

path_31AA_apps= "D:\\fb_workspace\\apps"
path_31AA_services= "D:\\r_20\\services\\core"
lst1 = os.walk(path_31AA_apps)
for dirpath, dirname, filename in lst1:

    if dirpath.endswith("\\app\\src\\main\\res\\values"):
        dst_dir = dirpath[dirpath.index("\\apps\\") + 6:dirpath.index("\\app\\"):]
        print(dst_dir)
        out_dir = f"D:\\360Downloads\\string\\{dst_dir}\\chinese\\"
        os.makedirs(out_dir, exist_ok=True)
        shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings.xml")
    elif "\\app\\src\\main\\res\\values-en" in dirpath:
        dst_dir = dirpath[dirpath.index("\\apps\\") + 6:dirpath.index("\\app\\"):]
        out_dir = f"D:\\360Downloads\\string\\{dst_dir}\\english\\"
        print(os.path.exists(out_dir))
        os.makedirs(out_dir, exist_ok=True)
        shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings.xml")


lst2 = os.walk(path_31AA_services)
for dirpath, dirname, filename in lst2:
    if dirpath.endswith("\\src\\main\\res\\values"):
        dst_dir = dirpath[dirpath.index("\\apps\\") + 6:dirpath.index("\\app\\"):]
        print(dst_dir)
        out_dir = f"D:\\360Downloads\\string\\services\\{dst_dir}\\chinese\\"
        os.makedirs(out_dir, exist_ok=True)
        shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings.xml")
    elif "\\src\\main\\res\\values-en" in dirpath:
        dst_dir = dirpath[dirpath.index("\\apps\\") + 6:dirpath.index("\\app\\"):]
        out_dir = f"D:\\360Downloads\\string\\services\\{dst_dir}\\english\\"
        print(os.path.exists(out_dir))
        os.makedirs(out_dir, exist_ok=True)
        shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings.xml")