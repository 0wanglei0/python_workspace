import os.path
import shutil

path_31AA_apps= "D:\\fb_workspace\\apps"
path_31AA_services= "D:\\fb_workspace\\services\\core"
# lst1 = os.walk(path_31AA_apps)
# for dirpath, dirname, filename in lst1:
#
#     if dirpath.endswith("\\app\\src\\main\\res\\values"):
#         dst_dir = dirpath[dirpath.index("\\apps\\"):dirpath.index("\\app\\"):].replace("\\", ".")
#         print(dst_dir)
#         out_dir = f"D:\\360Downloads\\string\\{dst_dir}\\"
#         os.makedirs(out_dir, exist_ok=True)
#         shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-zh.xml")
#     elif "\\app\\src\\main\\res\\values-en" in dirpath:
#         dst_dir = dirpath[dirpath.index("\\apps\\"):dirpath.index("\\app\\"):].replace("\\", ".")
#         out_dir = f"D:\\360Downloads\\string\\{dst_dir}\\"
#         print(os.path.exists(out_dir))
#         os.makedirs(out_dir, exist_ok=True)
#         shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-en.xml")
#     elif "\\app\\src\\main\\res\\values-zh-rCN" in dirpath:
#         dst_dir = dirpath[dirpath.index("\\apps\\"):dirpath.index("\\app\\"):].replace("\\", ".").replace("\\", ".")
#         out_dir = f"D:\\360Downloads\\string\\{dst_dir}\\"
#         print(os.path.exists(out_dir))
#         os.makedirs(out_dir, exist_ok=True)
#         shutil.copyfile(out_dir + "strings-zh.xml", f"{out_dir}strings-en.xml")
#         shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-zh.xml")
#
#
# lst2 = os.walk(path_31AA_services)
# for dirpath, dirname, filename in lst2:
#     if dirpath.endswith("\\src\\main\\res\\values"):
#         dirpath_list3 = dirpath.split("\\")
#         dst_dir = f"{dirpath_list3[4]}.{dirpath_list3[5]}"
#         out_dir = f"D:\\360Downloads\\string\\{dst_dir}\\"
#         os.makedirs(out_dir, exist_ok=True)
#         shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-zh.xml")
#     elif "\\app\\src\\main\\res\\values-en" in dirpath:
#         dirpath_list3 = dirpath.split("\\")
#         dst_dir = f"{dirpath_list3[4]}.{dirpath_list3[5]}"
#         out_dir = f"D:\\360Downloads\\string\\{dst_dir}\\"
#         os.makedirs(out_dir, exist_ok=True)
#         shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-en.xml")
#     elif "\\app\\src\\main\\res\\values-zh-rCN" in dirpath:
#         dirpath_list3 = dirpath.split("\\")
#         dst_dir = f"{dirpath_list3[4]}.{dirpath_list3[5]}"
#         out_dir = f"D:\\360Downloads\\string\\{dst_dir}\\"
#         os.makedirs(out_dir, exist_ok=True)
#         shutil.copyfile(out_dir + "strings-zh.xml", f"{out_dir}strings-en.xml")
#         shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-zh.xml")
#

path_31AA_others= "D:\\fb_workspace\\"
lst3 = os.walk(path_31AA_others)
dst_name = "31AA"
# path_T31A_others= "D:\\r_20\\"
# lst3 = os.walk(path_T31A_others)
# dst_name = "T31A"

for dirpath, dirname, filename in lst3:
    dst_dir = ""
    if dirpath.endswith("\\src\\main\\res\\values"):
        dirpath_list3 = dirpath.split("\\")
        for index in range(len(dirpath_list3)):
            if index == 0 or index == 1:
                continue
            if dst_dir == "":
                dst_dir = f"{dirpath_list3[index]}"
            else:
                c_path = dirpath_list3[index]
                if c_path == "src" or c_path == "main" or c_path == "res" or c_path == "core"\
                    or c_path == "values" or c_path == "values-en" or c_path == "values-zh-rCN":
                    continue
                dst_dir = f"{dst_dir}.{dirpath_list3[index]}"
        out_dir = f"D:\\360Downloads\\string\\{dst_name}\\{dst_dir}\\"
        os.makedirs(out_dir, exist_ok=True)
        if os.path.exists(dirpath + "\\strings.xml"):
            shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-zh.xml")
        elif os.path.exists(dirpath + "\\strings_tts.xml"):
            shutil.copyfile(dirpath + "\\strings_tts.xml", f"{out_dir}strings_tts-zh.xml")
            shutil.copyfile(dirpath + "\\strings_other.xml", f"{out_dir}strings_other-zh.xml")
            shutil.copyfile(dirpath + "\\helplist.xml", f"{out_dir}helplist-zh.xml")
    elif dirpath.endswith("\\src\\main\\res\\values-en"):
            dirpath_list3 = dirpath.split("\\")
            for index in range(len(dirpath_list3)):
                if index == 0 or index == 1:
                    continue
                if dst_dir == "":
                    dst_dir = f"{dirpath_list3[index]}"
                else:
                    c_path = dirpath_list3[index]
                    if c_path == "src" or c_path == "main" or c_path == "res" or c_path == "core" \
                            or c_path == "values" or c_path == "values-en" or c_path == "values-zh-rCN":
                        continue
                    dst_dir = f"{dst_dir}.{dirpath_list3[index]}"
            out_dir = f"D:\\360Downloads\\string\\{dst_name}\\{dst_dir}\\"
            os.makedirs(out_dir, exist_ok=True)
            if os.path.exists(dirpath + "\\strings.xml"):
                shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-en.xml")
    elif dirpath.endswith("\\src\\main\\res\\values-zh-rCN"):
        dirpath_list3 = dirpath.split("\\")

        for index in range(len(dirpath_list3)):
            if index == 0 or index == 1:
                continue
            if dst_dir == "":
                dst_dir = f"{dirpath_list3[index]}"
            else:
                c_path = dirpath_list3[index]
                if c_path == "src" or c_path == "main" or c_path == "res" or c_path == "core"\
                    or c_path == "values" or c_path == "values-en" or c_path == "values-zh-rCN":
                    continue
                dst_dir = f"{dst_dir}.{dirpath_list3[index]}"
        out_dir = f"D:\\360Downloads\\string\\{dst_name}\\{dst_dir}\\"
        os.makedirs(out_dir, exist_ok=True)
        if os.path.exists(dirpath + "\\strings.xml"):
            if os.path.exists(out_dir + "\\strings-zh.xml"):
                shutil.copyfile(out_dir + "strings-zh.xml", f"{out_dir}strings-en.xml")
                shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-zh.xml")
            elif os.path.exists(out_dir + "\\strings_tts-zh.xml"):
                shutil.copyfile(out_dir + "strings_tts-zh.xml", f"{out_dir}strings_tts-default.xml")
                shutil.copyfile(out_dir + "strings_other-zh.xml", f"{out_dir}strings_other-default.xml")
                shutil.copyfile(out_dir + "helplist-zh.xml", f"{out_dir}helplist-default.xml")
                shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-zh.xml")