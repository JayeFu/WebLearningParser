from bs4 import BeautifulSoup
import xlsxwriter
import os

os.chdir(r"C:\Users\Jaye Fu\Desktop\WebLearningParser")

def main():
    filename = "Web Learning of Tsinghua University.html"
    with open(filename, 'r', errors='ignore') as f:
        html_text = f.read()
    soup = BeautifulSoup(html_text, 'html.parser')
    courses = soup.findAll("a", {"class": "title stu"})
    c_names = list()
    c_nums = list()
    c_seqs = list()
    for course in courses:
        course_str = str(course.string)
        l_bracket_pos = course_str.rfind("(")
        course_name = course_str[:l_bracket_pos]
        course_str = course_str[l_bracket_pos:]
        bar_pos = course_str.rfind("-")
        course_num = course_str[1:bar_pos]
        course_seq = course_str[bar_pos+1:-1]
        try:
            course_seq = int(course_seq)
        except Exception as e:
            print(e)
        c_names.append(course_name)
        c_nums.append(course_num)
        c_seqs.append(course_seq)
    f = xlsxwriter.Workbook("WebLearning.xlsx")
    sheet = f.add_worksheet("courses")
    sheet.set_column(0, 0, 64)
    sheet.set_column(1, 1, 12)
    for i in range(len(c_names)):
        sheet.write(i, 0, c_names[i])
        try:
            c_nums[i] = int(c_nums[i])
        except Exception as e:
            print(e)
            print("{} is not number".format(c_nums[i]))
            sheet.write(i, 1, c_nums[i])
        else:
            sheet.write_number(i, 1, c_nums[i])
        sheet.write_number(i, 2, c_seqs[i])
    f.close()

if __name__ == "__main__":
    main()