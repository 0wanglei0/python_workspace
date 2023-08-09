words = [
    "龴", "龵", "龶", "龷", "龸", "龹", "龺", "龻",
    "郎",
    "凉",
    "秊",
    "裏",
    "隣",
    "兀",
    "嗀",
    "礼",
    "蘒",
    "",
    "",
    "",
    "",
    "",
    ""]

unicodes = [
"9fb4",
"9fb5",
"9fb6",
"9fb7",
"9fb8",
"9fb9",
"9fba",
"9fbb",
"e81e",
"e826",
"e82b",
"e82c",
"e832",
"e843",
"e854",
"e864"


]

file_object2 = open("unicode.txt", 'r', encoding='utf-8')
file_object = open("unicode_word.txt", 'a', encoding='utf-8')

list = []
try:
    lines = file_object2.readlines()
    prevLine = ''
    for line in lines:
        line.replace("\n", "")



        if "unicode:" in line:
            prevLine = line

        # if "e81e" in prevLine:
            # print(prevLine)

        if "Candidate word: " in line:
            # word = line.split('Candidate word: ')[1:][0]
            # if word in words:
            #     print("word=", word)
            #     print("prevLine=", prevLine)
            #     print("line=", line)
            #     file_object.write(prevLine)
            #     file_object.write("\n")
            #     file_object.write(line)
            #     file_object.write("\n")
                # prevLine=""
                # line = ""
                # print(prevLine)
                # print(line)
                # print("\n")

            unicode = prevLine.split('unicode:')[1:][0]
            unicode = unicode.split("0x")[1:]

            if len(unicode) == 0:
                continue

            unicode = unicode[0].replace("\n", '')

            if unicode in list:
                continue
            print(unicode)
            list.append(unicode)
            print(len(list))
            # file_object.write(unicode[0])
            # if unicode in unicodes:
            #     print(unicode)
            file_object.write(prevLine)
            file_object.write("\n")
            file_object.write(line)
            file_object.write("\n")

finally:
    file_object2.close()
    file_object.close()
