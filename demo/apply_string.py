s = "<string>message</string>"

index_start = s.index(">")
index_end = s.rindex("<")
print(index_end)


result_lst = list()
i = 0

with open("result_file.txt", "w", encoding="utf8") as f:
    with open("vr_string.txt", "r", encoding="utf8") as fp:
        for response in fp.readlines():
            if response == "\n":
                continue

            if "<" not in response:
                print(response, end="", file=f)
            else:
                index_start = response.index(">")
                index_end = response.rindex("<")
                if i < 2:
                    end_with = "\t"
                    i+=1
                else:
                    i = 0
                    end_with = "\n"
                print(response[index_start + 1:index_end], end=end_with, file=f)
