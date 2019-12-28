##############################
# get data from source files
# filename:init.py
# author:  liwei
# StuID:   1711350
# date:    2019.12.5
##############################

import os
from shutil import copyfile
from sys import exit
import sys
import numpy as np
import re

# 学院
xy_dict = {
    "南开大学商学院":"bs",
    "南开大学计算机学院":"cc",
    "南开大学经济学院":"ec",
    "南开大学历史学院":"ht",
    "南开大学法学院":"law",
    "南开大学文学院":"lt",
    "南开大学哲学院":"phi",
}

# 资源文档目录
file_path = './docs'


# 获取某一人员的快照文件路径,相对于查询是的路由地址而言
def get_html(xueyuan,name):
    if os.path.exists("/snapshots/%s/%s.html"%(xy_dict[xueyuan],name)):
        return "/snapshots/%s/%s.html"%(xy_dict[xueyuan],name)
    else:
        return "/snapshots/%s/%s.html"%(xy_dict[xueyuan],str(name).replace(" ",""))


# 获取某一人员的内容文件路径
def get_content(xueyuan,name):
    if  os.path.exists( "./docs/%s/%s.txt"%(xy_dict[xueyuan],name)):      # 锚文本存储文件夹
        return "./docs/%s/%s.txt"%(xy_dict[xueyuan],name)
    else:
        return "./docs/%s/%s.txt"%(xy_dict[xueyuan],str(name).replace(" ",""))


# 获取某一人员的锚文本保存路径
def get_mtext(xueyuan,name):
    if  os.path.exists("./docs/%s/m_text/%s_m.txt"%(xy_dict[xueyuan],name)):      # 锚文本存储文件夹
        return "./docs/%s/m_text/%s_m.txt"%(xy_dict[xueyuan],name)
    else:
        return "./docs/%s/m_text/%s_m.txt"%(xy_dict[xueyuan],str(name).replace(" ",""))

# 获取某一人员的照片保存路径
def get_img(xueyuan,name):
    if  os.path.exists("./docs/%s/imgs/%s.jpg"%(xy_dict[xueyuan],str(name).replace(" ",""))):      # 锚文本存储文件夹
        return "./docs/%s/imgs/%s.jpg" % (xy_dict[xueyuan], name)
    elif  os.path.exists("./docs/%s/imgs/%s.png"%(xy_dict[xueyuan],str(name).replace(" ",""))):      # 锚文本存储文件夹
        return "./docs/%s/imgs/%s.png" % (xy_dict[xueyuan], name)
    elif os.path.exists("./docs/%s/imgs/%s.bmp"%(xy_dict[xueyuan],str(name).replace(" ",""))):      # 锚文本存储文件夹
        return "./docs/%s/imgs/%s.bmp" % (xy_dict[xueyuan], name)
    else:
        return "#"

# 获取所有的教师信息的index.txt 文件内容
def get_teacher_info():
    info = dict()
    # 遍历根目录对索引文本内容构建索引
    for root, dirs, files in os.walk(file_path, topdown=True):
        for file in files:
            path_t = os.path.join(root, file)
            if  path_t.split('\\')[-1] != 'index.txt':
                continue
            print("=======>" + path_t, file)
            f = open(path_t, 'r', encoding='UTF-8')
            for line in f:
                item_list = line.split(",")
                #print(item_list)
                #assert(item_list[0]+item_list[1] not in info.keys())     # 检验条件
                if item_list[0] in [x.split('-')[0] for x in   info.keys()]:
                    print("$$$$"+item_list[0]+item_list[1])                 # 存在同一个人，在不同的页面出现个人主页，且内容完全一样,只要链接不同，则视同为不同的人
                                                                            # 也有不同学院同名的，如果是同学院的同名情况则目前无法解决
                if item_list[0]+'-'+item_list[1] in info.keys():
                    print("####"+item_list[0]+item_list[1] )
                    pc = info[item_list[0]+'-'+item_list[1]]["pageRefer"]     # 同样的连接有两条指向存在，说明指向其锚文本数量为2，可用于连接分析
                    info[item_list[0] + '-' + item_list[1]]["pageRefer"]=pc+1
                    continue
                info[item_list[0]+'-'+item_list[1]] = {                      # 建立字典项
                    "name":item_list[0],
                    "url":item_list[1],
                    "xueyuan":item_list[2],
                    "parentUrl":item_list[3],
                    "pageRefer":1,
                }
    return info

# 转移图片
def move_img():
    # 遍历根目录将所有的图片转移到查询flask系统的静态目录下
    for root, dirs, files in os.walk(file_path, topdown=True):
        for file in files:
            path_t = os.path.join(root, file)
            if path_t.split('\\')[-2] != 'imgs':
                continue
            print("=======>" + path_t, file)
            source= path_t
            target = "./static/images/%s/%s"%(path_t.split('\\')[-3],path_t.split('\\')[-1])
            if not os.path.exists("./static/images/%s"%(path_t.split('\\')[-3])):
                os.makedirs("./static/images/%s"%(path_t.split('\\')[-3]))
            # adding exception handling
            try:
                copyfile(source, target)
            except IOError as e:
                print("Unable to copy file. %s" % e)
                exit(1)
            except:
                print("Unexpected error:", sys.exc_info())
                exit(1)


# 处理南开大学信息文本，通过一些截断词对文本进行划分，得到很多的小段文本，存储到list格式中用于之后训练
def get_text():
    file = open(file_path+"/nankai.txt",'r',encoding="UTF-8")
    text_list = []
    for line in file:
        # print(line)
        line_sent = re.findall(r'[^，。:是]*|“[^“”]*”',line.strip("\r\n").strip("\u3000"))
        # print(line_sent)
        for item in line_sent:
            if len(str(item)) >= 4 and len(str(item)) < 20:
                text_list.append(item)
    return text_list


# 拷贝图片
# move_img()
# print(get_text())