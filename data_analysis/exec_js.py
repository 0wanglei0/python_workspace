import execjs

with open("exec_js.js", "r", encoding="utf-8") as js_file:
    js_code = js_file.read()

data = execjs.compile(js_code).call('main', 'name', "password")
print(data)
