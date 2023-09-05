import pandas as pd
import numpy as np
import uiautomation as auto
# import autoit


from uiautomation import WindowControl, MenuControl, PaneControl, ControlType

fs = PaneControl(searchDepth=1, Name='美行科技')

fs.SwitchToThisWindow()
# print(fs.GetChildren())
# hwnd = auto.GetForegroundWindow()
#
# auto.WaitWindowTitleChange(hwnd, "美行科技")
# unread_messages = auto.GetChildWindow(hwnd, auto.GetWindowText(hwnd).split(" ")[0])
# 获取当前窗口句柄
# hwnd = autoit.win_get_window(autoit.SW_HIDE)
#
# # 监听窗口标题变化事件
# autoit.win_wait(hwnd, "飞书")
#
# # 获取未读消息列表
# unread_messages = autoit.control_get(hwnd, "", "List", "")
# print(unread_messages)


# print(fs.GroupControl(searchDepth=14).GetParentControl().GetChildren())
# control_list = fs.PaneControl(searchDepth=1).GetParentControl().GetChildren()
# print(len(control_list))
# for index, value in enumerate(control_list):
#     print(value)
# print(fs.GroupControl(searchDepth=18).GetChildren())
# print(fs.GroupControl(searchDepth=20).TextControl(searchDepth=21))
# print(fs.GroupControl(searchDepth=21, Name="丁茄元").GetParentControl().GetChildren()[2].Name)
# print(fs.GetF(searchDepth=21))


# for i in range(3):
# print(fs.TextControl(Depth=21).GetChildren())
# 只能单个找到对话回复
we = fs.TextControl(searchDepth=21, Name="飞书助手").GetParentControl()
children = we.GetChildren()
msg = children[len(children) - 1].Name
print(msg)
if msg:
    we.Click(simulateMove=False)

    df = pd.read_csv("auto_reply.csv", encoding="utf-8")
    reply = df.apply(lambda x: x['回复内容'] if x['关键词'] in msg else None, axis=1)
    reply.dropna(axis=0, how="any", inplace=True)
    ar = np.array(reply).tolist()

    if ar:
        fs.SendKeys(ar[0].replace("{br}", '{shift}{Enter}'), waitTime=0)
        fs.SendKeys('{Enter}', waitTime=0)
        fs.TextControl(SubName=ar[0][:5]).RightClick()
    else:
        fs.SendKeys("稍等，一会回复", waitTime=0)
        fs.SendKeys('{Enter}', waitTime=0)
        fs.TextControl().RightClick()
