import pandas


def write_to_excel(log, detail_datas, analysis_datas):
    log.info_out("写入文件")
    rows_num = len(detail_datas["日期"]) + 3
    df0 = pandas.DataFrame(detail_datas)
    df1 = pandas.DataFrame(analysis_datas)
    # print(df0)

    df0.convert_dtypes()
    df1.convert_dtypes()
    with pandas.ExcelWriter("work_report.xlsx", engine='xlsxwriter') as writer:
        df0.to_excel(writer, sheet_name="work_report", index=False, startrow=0)
        df1.to_excel(writer, sheet_name="work_report", index=False, startrow=rows_num)


def write_to_file(calculate_header, calculate_value):
    with open("work_report.xlsx", "w+", encoding="utf8") as wr:
        # wr.write(print_lst.replace(",", "\t"))
        # for string in print_lst:
        #     wr.write(string)

        wr.write("\n")
        wr.write("\n")
        wr.write("\n")
        for header in calculate_header:
            wr.write(header + "\t")
        wr.write("\n")

        for c_value in calculate_value:
            wr.write(str(c_value) + "\t")
        wr.write("\n")
