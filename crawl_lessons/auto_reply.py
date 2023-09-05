import pandas as pd
import numpy as np

from uiautomation import WindowControl, MenuControl

wx = WindowControl(Name="微信")

wx.SwitchToThisWindow()
hw = wx.ListControl(Name="会话")
df = pd.read_csv("auto_reply.csv", encoding="utf-8")

while True:
    we = hw.TextControl(searchDepth=4)
    while not we.Exists(0):
        pass
    if we.Name:
        we.Click(simulateMove=False)
        last_msg = wx.ListControl(Name="消息").GetChildren()[-1].Name
        print(last_msg)

        if "@Hynex李文超 文超老师，开始OTA了各" in last_msg:
            continue
        msg = df.apply(lambda x: x['回复内容'] if x['关键词'] in last_msg else None, axis=1)
        msg.dropna(axis=0, how="any", inplace=True)
        ar = np.array(msg).tolist()
        print(ar)
        if len(ar) != 0:
            wx.SwitchToThisWindow()
            wx.SendKeys(ar[0], waitTime=0)
            wx.SendKeys('{Enter}', waitTime=0)
            print("enter")

            # wx.ButtonControl(SubName="发送(S)").Click()
        else:
            # wx.SendKeys("稍等，一会回复", waitTime=0)
            # wx.SendKeys('{Enter}', waitTime=0)
            # wx.TextControl().RightClick()
            print("pass")
            pass
