# corpus_mk.py
# function: make corpus for chatterbot
# author: jack-lio
# github: https://github.com/Jack-Lio
# date: 2019.12.27
# 马上就期末考试了，快点做完啊啊啊啊啊~~~~~~

from data import get_teacher_info,get_content

# 预料库存储位置
corpus = "./corpus"

# 生成南开大学教师基本学院相关信息问答语料库
def create_teacher_info_corpus():
    info = get_teacher_info()
    print(info)
    teacher = open("./corpus/teacher.yml",'w',encoding='utf-8')
    teacher.write("categories:\n")
    teacher.write("- teacher\n")
    teacher.write("conversations:\n")
    xueyuan = open("./corpus/xueyuan.yml",'w',encoding='utf-8')
    xueyuan.write("categories:\n")
    xueyuan.write("- xueyuan\n")
    xueyuan.write("conversations:\n")
    for key in info.keys() :
        teacher.write("- - "+info[ key]["name"] +"\n  - "+info[key]["name"]+"老师是"+info[key]["xueyuan"]+"的\n")
        teacher.write("- - " + info[key]["name"] + "是哪个学院的\n  - " + info[key]["name"] + "老师是" + info[key]["xueyuan"] + "的\n")
        teacher.write("- - " + info[key]["name"] + "在哪个学院\n  - " + info[key]["name"] + "老师是" + info[key]["xueyuan"] + "的\n")
        teacher.write(
            "- - 我想去" + info[key]["name"] + "老师主页看一下\n  - 这是" + info[key]["name"] + "的主页链接" + info[key]["url"] + "\n")
        teacher.write(
            "- - " + info[key]["name"] + "老师主页\n  - 这是" + info[key]["name"] + "的主页链接" + info[key]["url"] + "\n")
        teacher.write(
            "- - " + info[key]["name"] + "主页链接\n  - 这是" + info[key]["name"] + "的主页链接" + info[key]["url"] + "\n")
        teacher.write(
            "- - 你知道" + info[key]["name"] + "老师吗\n  - 当然知道，" + info[key]["name"] + "是"+info[key]["xueyuan"]+"的，这是她的主页链接" + info[key]["url"] + "，想知道更多的信息可以点击一下\n")

        xueyuan.write("- - 我想去" + info[key]["xueyuan"] + "主页看一下\n  - 这是" + info[key]["xueyuan"] + "的主页链接" + info[key]["parentUrl"] )
        xueyuan.write(
            "- - " + info[key]["xueyuan"] + "主页\n  - 这是" + info[key]["xueyuan"] + "的主页链接" + info[key]["parentUrl"] )
        xueyuan.write(
            "- - " + info[key]["xueyuan"] + "\n  - 这是" + info[key]["xueyuan"] + "的主页链接" + info[key]["parentUrl"] )
        xueyuan.write(
            "- - 你知道" + info[key]["xueyuan"] + "吗\n  - 我当然知道，这是" + info[key]["xueyuan"] + "的主页链接" + info[key]["parentUrl"] )
    teacher.close()
    xueyuan.close()
    return 0

# 生成计算机学院教师信息对话语料库
def create_cc_info():
    info = get_teacher_info()
    cc = open("./corpus/cc.yml", 'w', encoding='utf-8')
    cc.write("categories:\n")
    cc.write("- cc\n")
    cc.write("conversations:\n")
    titles = ['性别','所属部门''行政职务','职称','学历','所学专业','办公电话','电子邮件','研究方向']
    for key in info.keys() :
        if info[key]['xueyuan'] != "南开大学计算机学院":
            continue
        t_f_path = get_content(info[key]['xueyuan'],info[key]['name'])
        t_f = open(t_f_path,'r',encoding='utf-8')
        for line in t_f :
            tt = line.split("：")
            print(tt)
            if tt[0] in titles:
                cc.write("- - " + info[key]["name"]+"的"+tt[0] + "是什么\n  - " + info[key]["name"] + "老师的"+tt[0]+ "是"+
                    tt[1].strip('\n')+ "\n")
        t_f.close()
    cc.close()
    return 0

if __name__ == "__main__":
    create_teacher_info_corpus()
    create_cc_info()