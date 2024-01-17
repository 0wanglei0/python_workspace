import os.path
import re
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='demo')

    # add argument
    parser.add_argument('--path', type=str, help='root path', default="")
    # parse args
    args = parser.parse_args()
    # use arg
    return args.path

path_31AA_others = parse_args()

if not path_31AA_others.endswith("\\"):
    # python3
    # path_31AA_others = f"{path_31AA_others}\\"
    # python2
    path_31AA_others = "{path_31AA_others}\\".format(path_31AA_others=path_31AA_others)

print(path_31AA_others)
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

path_list = []
for dst_dir in dir_lst:
    temp_dir = dst_dir
    if "-" in dst_dir:
        if "mirror-link" in dst_dir:
            temp_dir = dst_dir.replace("-", "\\", 1)
        else:
            temp_dir = dst_dir.replace("-", "\\")
    add_path = "{path_31AA_others}{temp_dir}".format(path_31AA_others=path_31AA_others, temp_dir=temp_dir)
    path_list.append(add_path)
print(path_list)

coverage_statistics = []
filter_pattern = r"testReleaseUnitTest|testDebugUnitTest"
retain_pattern = r"TEST-*"

for path in path_list:
    dst_dir = ""
    dir_list = os.walk(path)

    for dir_path, dirname, filename in dir_list:
        match = re.findall(filter_pattern, dir_path.replace("\\", "\\\\"))
        if len(match) == 0:
            continue

        print("pass")
        print(filename)
        tests_total = 0
        tests_failures = 0
        tests_success_rate = ""
        tests_package_name = ""
        if dir_path.endswith("testReleaseUnitTest"):
            dest_path = dir_path + "\\index.html"
            if os.path.exists(dest_path):
                print(dest_path)

                with open(dest_path, "r") as f:
                    lines = f.readlines()
                    tests_total = lines[22].split('<div class="counter">')[1].split('</div>')[0]
                    tests_failures = lines[28].split('<div class="counter">')[1].split('</div>')[0]
                    tests_success_rate = lines[50].split('<div class="percent">')[1].split('</div>')[0]
                    tests_package_name = lines[82].split('<a href="packages/com.mxnavi.user.html">')[1].split('</a>')[0]
                item = "package: {tests_package_name}\ttests:{tests_total}\tfailures:{tests_failures}\tsuccess rate:{tests_success_rate}"\
                        .format(tests_package_name=tests_package_name, tests_total=tests_total,
                                tests_failures=tests_failures, tests_success_rate=tests_success_rate)
                coverage_statistics.append(item)
        elif dir_path.endswith("testDebugUnitTest"):
            if len(filename) == 1 and filename[0].endswith("xml"):
                dest_path = dir_path + "\\{filename}".format(filename=filename[0])
                print(dest_path)
                if os.path.exists(dest_path):
                    with open(dest_path, "r") as f:
                        lines = f.readlines()
                        line = lines[1].split(" ")
                        print(line)
                        tests_total = eval(line[2].split('tests=')[1])
                        tests_failures = eval(line[4].split('failures=')[1])
                        print(tests_total)
                        rate = "%.2f" % ((float(tests_total) - float(tests_failures)) / float(tests_total) * 100)
                        tests_success_rate = '{rate}%'.format(rate=rate)
                        packages = line[1].split('name="')[1].split('.')
                        tests_package_name = "com.{packages_1}.{packages_2}".format(packages_1=packages[1], packages_2=packages[2])
                item = "package: {tests_package_name}\ttests:{tests_total}\tfailures:{tests_failures}\tsuccess rate:{tests_success_rate}"\
                        .format(tests_package_name=tests_package_name, tests_total=tests_total,
                                tests_failures=tests_failures, tests_success_rate=tests_success_rate)
                coverage_statistics.append(item)

print(coverage_statistics)
with open("results.txt", 'w+') as f:
    for item in coverage_statistics:
        f.write(item)
        f.write('\n')

print("end")