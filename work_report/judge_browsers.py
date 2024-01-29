import winreg  # windows注册表
import os
import psutil


# 取得浏览器的安装路径
def get_path(mainkey, subkey):
    try:
        key = winreg.OpenKey(mainkey, subkey)
    except FileNotFoundError:
        return '未安装'
    value, type = winreg.QueryValueEx(key, "")  # 获取默认值
    full_file_name = value.split(',')[0]  # 截去逗号后面的部分
    [dir_name, file_name] = os.path.split(full_file_name)  # 分离文件名和路径
    return dir_name


def init_edge():
    # 初始化变量
    # ico_ie = r"SOFTWARE\Clients\StartMenuInternet\IEXPLORE.EXE\DefaultIcon"
    # ico_firefox = r"SOFTWARE\Clients\StartMenuInternet\Firefox-308046B0AF4A39CB\DefaultIcon"
    # ico_360js = r"SOFTWARE\Clients\StartMenuInternet\360Chrome\DefaultIcon"
    # install_python = r"Software\Python\PythonCore\3.7\InstallPath"
    # ico_google = r"SOFTWARE\Clients\StartMenuInternet\Google Chrome\DefaultIcon"
    ico_edge = r"SOFTWARE\Clients\StartMenuInternet\Microsoft Edge\DefaultIcon"

    # print("IE : " + get_path(winreg.HKEY_LOCAL_MACHINE, ico_ie))
    # print("火狐 : " + get_path(winreg.HKEY_LOCAL_MACHINE, ico_firefox))
    # print("谷歌 : " + get_path(winreg.HKEY_LOCAL_MACHINE, ico_google))
    # print("360极速: " + get_path(winreg.HKEY_LOCAL_MACHINE, ico_360js))
    # print("edge : " + get_path(winreg.HKEY_LOCAL_MACHINE, ico_edge))
    # print("Python : " + get_path(winreg.HKEY_CURRENT_USER, install_python))
    path = get_path(winreg.HKEY_LOCAL_MACHINE, ico_edge)
    return path != "未安装" or 'MicrosoftEdge' in os.getenv('PATH')


def init_chrome():
    ico_google = r"SOFTWARE\Clients\StartMenuInternet\Google Chrome\DefaultIcon"
    path = get_path(winreg.HKEY_LOCAL_MACHINE, ico_google)
    return path != "未安装"


def is_browser_open(browser_name):
    for process in psutil.process_iter():
        if browser_name.lower() in process.name().lower():
            return True
        return False


# is_browser_open("MicrosoftEdge"):
