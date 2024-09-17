import string
# 创建一个Python脚本，用于生成从aaaa到zzzz的所有四位英文字母组合，并保存到txt文档中

# 打开一个文件用于写入
with open('four_letter_combinations.txt', 'w') as file:
    # 遍历所有小写字母的组合
    for first_letter in string.ascii_lowercase:
        for second_letter in string.ascii_lowercase:
            for third_letter in string.ascii_lowercase:
                for fourth_letter in string.ascii_lowercase:
                    for fifth_letter in string.ascii_lowercase:
                    # 生成四位字母组合
                        combination = first_letter + second_letter + third_letter + fourth_letter + fifth_letter
                    # 写入文件，每个组合占一行
                        file.write(combination + '\n')

