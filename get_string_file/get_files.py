import os.path
import shutil
import re

path_31AA_apps = "D:\\fb_workspace\\apps"
path_31AA_services = "D:\\fb_workspace\\services\\core"


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

def get_dst_dir(dirpath, dst_dir=""):
    dirpath_list3 = dirpath.split("\\")

    for index in range(len(dirpath_list3)):
        if index == 0 or index == 1:
            continue
        if dst_dir == "":
            dst_dir = f"{dirpath_list3[index]}"
        else:
            c_path = dirpath_list3[index]
            if c_path == "src" or c_path == "main" or c_path == "res" or c_path == "core" \
                    or c_path == "values" or c_path == "values-en" or c_path == "values-zh-rCN" or c_path == "values-zh":
                continue
            dst_dir = f"{dst_dir}.{dirpath_list3[index]}"
    return dst_dir


path_31AA_others = "D:\\r_20\\"
lst3 = os.walk(path_31AA_others)
dst_name = "31AA"
# path_T31A_others= "D:\\r_20\\"
# lst3 = os.walk(path_T31A_others)
# dst_name = "T31A"

# pattern = r".repo|.git|.PVS|build"
pattern = r"\.repo*|\.git|\.PVS|build|\.idea|\.gradle"

app_name = ""
app_names = []
for dirpath, dirname, filename in lst3:
    match = re.findall(pattern, dirpath)
    if len(match) != 0:
        continue
    # print(dirpath)
    dst_dir = ""
    if "\\app\\" in dirpath:
        dir_steps = dirpath.split("\\")
        # print(dir_steps)
        app_name = dir_steps[dir_steps.index("app") - 1]
        app_names.append(app_name)
        # print(app_name)
        if app_name == "android":
            print(dirpath)
        out_dir = f"D:\\360Downloads\\string\\{dst_name}\\{app_name}\\"
        os.makedirs(out_dir, exist_ok=True)
        # print(out_dir)

    for name in app_names:
        if name in dirpath:
            app_name = name
            print("app_name", app_name)
            break
    if "\\VR\\" in dirpath or "\\VREngine\\" in dirpath or "\\tts\\" in dirpath:
        app_name = "VRUI"
        if "VRUI" not in app_names:
            app_names.append("VRUI")
    if "\\tamllgenie\\" in dirpath:
        app_name = "tmallgenie"
        if "tmallgenie" not in app_names:
            app_names.append("tmallgenie")

    if "\\BTPhone\\" in dirpath:
        app_name = "btphone"
        if "btphone" not in app_names:
            app_names.append("tmallgenie")

    if "\\services\\core\\ecall" in dirpath:
        dst_dir = get_dst_dir(dirpath, dst_dir)
        out_dir = f"D:\\360Downloads\\string\\{dst_name}\\ecall\\{dst_dir}."
        if not os.path.exists(f"D:\\360Downloads\\string\\{dst_name}\\ecall"):
            os.makedirs(f"D:\\360Downloads\\string\\{dst_name}\\ecall", exist_ok=True)
        if dirpath.endswith("\\src\\main\\res\\values"):
            if os.path.exists(dirpath + "\\strings.xml"):
                shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-en.xml")
                if os.path.exists(dirpath + "\\strings_other.xml"):
                    shutil.copyfile(dirpath + "\\strings_other.xml", f"{out_dir}strings_other-en.xml")
        elif dirpath.endswith("\\src\\main\\res\\values-zh"):
            if os.path.exists(dirpath + "\\strings.xml"):
                shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-zh.xml")
        continue
    if dirpath.endswith("\\src\\main\\res\\values"):
        dst_dir = get_dst_dir(dirpath, dst_dir)
        if app_name != "":
            out_dir = f"D:\\360Downloads\\string\\{dst_name}\\{app_name}\\{dst_dir}."
            if not os.path.exists(f"D:\\360Downloads\\string\\{dst_name}\\{app_name}"):
                os.makedirs(f"D:\\360Downloads\\string\\{dst_name}\\{app_name}", exist_ok=True)
        else:
            print(dirpath)
            out_dir = f"D:\\360Downloads\\string\\{dst_name}\\{dst_dir}\\"
            os.makedirs(out_dir, exist_ok=True)
        if os.path.exists(dirpath + "\\strings.xml"):
            shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-zh.xml")
        elif os.path.exists(dirpath + "\\strings_tts.xml"):
            shutil.copyfile(dirpath + "\\strings_tts.xml", f"{out_dir}strings_tts-zh.xml")
            shutil.copyfile(dirpath + "\\strings_other.xml", f"{out_dir}strings_other-zh.xml")
            shutil.copyfile(dirpath + "\\helplist.xml", f"{out_dir}helplist-zh.xml")
    elif dirpath.endswith("\\src\\main\\res\\values-en"):
        dst_dir = get_dst_dir(dirpath, dst_dir)

        if app_name != "":
            out_dir = f"D:\\360Downloads\\string\\{dst_name}\\{app_name}\\{dst_dir}."
            if not os.path.exists(f"D:\\360Downloads\\string\\{dst_name}\\{app_name}"):
                os.makedirs(f"D:\\360Downloads\\string\\{dst_name}\\{app_name}", exist_ok=True)

        else:
            print(dirpath)

            out_dir = f"D:\\360Downloads\\string\\{dst_name}\\{dst_dir}\\"
            os.makedirs(out_dir, exist_ok=True)
        if os.path.exists(dirpath + "\\strings.xml"):
            shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-en.xml")
    elif dirpath.endswith("\\src\\main\\res\\values-zh-rCN"):
        dst_dir = get_dst_dir(dirpath, dst_dir)

        if app_name != "":
            out_dir = f"D:\\360Downloads\\string\\{dst_name}\\{app_name}\\{dst_dir}."
            if not os.path.exists(f"D:\\360Downloads\\string\\{dst_name}\\{app_name}"):
                os.makedirs(f"D:\\360Downloads\\string\\{dst_name}\\{app_name}", exist_ok=True)

        else:
            print(dirpath)
            out_dir = f"D:\\360Downloads\\string\\{dst_name}\\{dst_dir}\\"
            os.makedirs(out_dir, exist_ok=True)
        if os.path.exists(dirpath + "\\strings.xml"):
            if os.path.exists(out_dir + "\\strings-zh.xml") or os.access(f"{out_dir}strings-zh.xml", os.F_OK):
                shutil.copyfile(out_dir + "strings-zh.xml", f"{out_dir}strings-en.xml")
                shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-zh.xml")
            elif os.path.exists(out_dir + "\\strings_tts-zh.xml") or os.path.exists(out_dir + "strings-zh.xml"):
                shutil.copyfile(out_dir + "strings_tts-zh.xml", f"{out_dir}strings_tts-default.xml")
                shutil.copyfile(out_dir + "strings_other-zh.xml", f"{out_dir}strings_other-default.xml")
                shutil.copyfile(out_dir + "helplist-zh.xml", f"{out_dir}helplist-default.xml")
                shutil.copyfile(dirpath + "\\strings.xml", f"{out_dir}strings-zh.xml")
    app_name = ""
