student_list = []
max_math = 0
max_chinese = 0
max_english = 0
min_math = 100
min_chinese = 100
min_english = 100
average_math = 0
average_chinese = 0
average_english = 0

print("输入单回车结束。")
try:
    while True:
        student = {}
        print("姓名: ",end='')
        student["name"] = input()
        print("数学: ",end='')
        student["math"] = int(input())
        if student["math"] > max_math:
            max_math = student["math"]
        if student["math"] < min_math:
            min_math = student["math"]
        average_math += student["math"]
        print("语文: ",end='')
        student["chinese"] = int(input())
        if student["chinese"] > max_chinese:
            max_chinese = student["chinese"]
        if student["chinese"] < min_chinese:
            min_chinese = student["chinese"]
        average_chinese += student["chinese"]
        print("英语: ",end='')
        student["english"] = int(input())
        if student["english"] > max_english:
            max_english = student["english"]
        if student["english"] < min_english:
            min_english = student["english"]
        average_english += student["english"]
        student_list.append(student)
        print("-------------------------------------------")
except:
    print("已结束，数据为：")
    print("姓名      数学      语文      英语")
    for i in student_list:
        print(f'''{i["name"]:<10}{i["math"]:<10}{i["chinese"]:<10}{i["english"]:<10}''')
    average_math /= len(student_list)
    average_chinese /= len(student_list)
    average_english /= len(student_list)
    print(f'''{"average":<10}{average_math:<10}{average_chinese:<10}{average_english:<10}''')
    print(f'''{"min":<10}{min_math:<10}{min_chinese:<10}{min_english:<10}''')
    print(f'''{"max":<10}{max_math:<10}{max_chinese:<10}{max_english:<10}''')
