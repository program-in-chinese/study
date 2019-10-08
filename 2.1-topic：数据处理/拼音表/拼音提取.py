from openpyxl import load_workbook

开始行 = 3
结束行 = 205

所有拼音 = []

def 遍历表格(文件名):
    工作簿 = load_workbook(文件名)
    表单 = 工作簿.active
    for 行 in range(开始行, 结束行):
        for 拼音序号 in range(0, 2):
            拼音所在列 = 拼音序号 * 6 + 1
            拼音 = 表单.cell(row = 行, column = 拼音所在列).value.lower()

            for 列 in range(拼音所在列 + 1, 拼音所在列 + 6):
                对应字 = 表单.cell(row = 行, column = 列).value
                if 对应字 != None:
                    所有拼音.append(拼音 + str(列 - 拼音所在列 - 1))


遍历表格("汉语拼音四声大全.xlsx")
所有拼音.sort()
print(len(所有拼音))
for 拼音 in 所有拼音:
    print(拼音)