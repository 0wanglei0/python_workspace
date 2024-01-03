import os.path
import shutil
import re
import subprocess

path_31AA_others = "D:\\r_20\\"
lst3 = os.walk(path_31AA_others)
dst_name = "31AA"

dir_lst = ["apps-appstore", "apps-btphone", "apps-cabincontrol", "apps-clock", "apps-CNRradio", "apps-diagnose",
           "apps-inputmethod", "apps-messagecenter", "apps-music", "apps-onlinefm", "apps-peccancy",
           "apps-personality", "apps-policy", "apps-setting", "apps-tmallgenie", "apps-user",
           "apps-VRUI", "apps-weather", "misc", "provider-onlineFM", "provider-user", "provider-violation",
           "provider-VR", "provider-weather", "sal-car", "sal-mirror-link", "sal-moustache", "services-mxserver",
           "services-dmc", "services-core-appstore", "services-core-audiomanager", "services-core-BTPhone",
           "services-core-cabincontrol", "services-core-CNRradio", "services-core-ecall", "services-core-messagecenter",
           "services-core-music", "services-core-onlineFM", "services-core-settings", "services-core-peccancy",
           "services-core-tamllgenie", "services-core-tts", "services-core-user", "services-core-VREngine",
           "services-core-weather"
           ]

# a = "1x"
a = "2x"
# branch_a_left = "r_1x_2210"
# branch_a_right = "r_1x_2306"
branch_a_left = "r_3x_2210"
branch_a_right = "r_2x_2306"
# filename_a = "log_r_1x_2210-r_1x_2306.txt"
filename_a = "log_r_3x_2210-r_2x_2306.txt"
for dst_dir in dir_lst:
    out_dir = f"D:\\360Downloads\\brances\\{a}\\{dst_dir}\\"
    os.makedirs(out_dir, exist_ok=True)
    temp_dir = dst_dir
    if "-" in dst_dir:
        if "mirror-link" in dst_dir:
            temp_dir = dst_dir.replace("-", "\\", 1)
        else:
            temp_dir = dst_dir.replace("-", "\\")
    print(f"{path_31AA_others}{temp_dir}")
    os.chdir(f"{path_31AA_others}{temp_dir}")
    result = subprocess.run(['git', 'log', '--left-right', f'origin/{branch_a_left}...origin/{branch_a_right}'],
                            stdout=subprocess.PIPE)

    # 将命令输出写入文件
    with open(f'{out_dir}{filename_a}', 'wb') as f:
        f.write(result.stdout)

print("-" in 'misc')