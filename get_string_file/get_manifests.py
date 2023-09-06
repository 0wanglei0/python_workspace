import os.path
import shutil

# path_31AA_apps= "D:\\fb_workspace\\apps"
# path_31AA_services= "D:\\fb_workspace\\services\\core"
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

# path_31AA_others= "D:\\fb_workspace\\"
# lst3 = os.walk(path_31AA_others)
# dst_name = "31AA"
path_T31A_others= "D:\\r_20\\"
lst3 = os.walk(path_T31A_others)
# dst_name = "r_1x_2210"
# dst_name = "r_2x_2210"
# dst_name = "r_3x_2210"
# dst_name = "r_31"
# dst_name = "r_32"
# dst_name = "r_41"
# dst_name = "r_51"
# dst_name = "r_61"
dst_name = "r_71"



for dirpath, dirname, filename in lst3:
    dst_dir = ""

    if dirpath.endswith("\\src\\main"):
        dest_path = dirpath + "\\AndroidManifest.xml"
        # print(dest_path)
        if os.path.exists(dest_path):
            dirpath_list3 = dirpath.split("\\")
            print(dirpath_list3)
            for index in range(len(dirpath_list3)):
                if index == 0 or index == 1:
                    continue
                if dst_dir == "":
                    dst_dir = f"{dirpath_list3[index]}"
                else:
                    c_path = dirpath_list3[index]
                    if c_path == "src" or c_path == "main" :
                        continue
                    dst_dir = f"{dst_dir}.{dirpath_list3[index]}"
            out_dir = f"D:\\360Downloads\\manifest\\{dst_name}"
            os.makedirs(out_dir, exist_ok=True)
            if os.path.exists(dirpath + "\\AndroidManifest.xml"):
                shutil.copyfile(dirpath + "\\AndroidManifest.xml", f"{out_dir}\\{dst_dir}_AndroidManifest.xml")
