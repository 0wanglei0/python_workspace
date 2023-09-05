import pandas as pd
import re
# df dataFrame类型，第一行为key
# df = pd.read_csv("auto_reply.csv", encoding="utf-8")
# print(df.get("序号")[0])
compileX = re.compile("\S")
regexName = re.compile("\S") if "\S" else None
print(regexName.match("穿"))