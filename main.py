#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021.7.2
# @Author : JackuXL
# @Version：v0.1
# @File : main.py
# @desc :快查成绩 API 调用工具
# 仅供学习使用
import functools
import json
import requests

names = [
    "梁宇轩",
    "万弈新",
    "包容先",
    "刘嘉瑞",
    "王培宇",
    "李子杰",
    "杨嘉昊",
    "罗钧译",
    "蒲家琦",
    "范钧奕",
    "赵鸿铮",
    "高子桐",
    "金子喆",
    "戴承霖",
    "张祐嘉",
    "卫晨",
    "杨云聪",
    "陈奕霖",
    "张依山",
    "陈孙可",
    "纪伽阳",
    "刘祺",
    "田博豪",
    "王嘉宸",
    "许凯瑞",
    "叶子麟",
    "张煜民",
    "邹启贤",
    "孙夕晰",
    "蔺一迪",
    "刘怡辰",
    "吴佩祺",
    "黄紫睿",
    "周璟雯",
    "王一帆",
    "张子越",
    "郭语格",
    "张琦煊",
    "张茜子",
    "李怡静",
    "吕瑗辰",
    "袁新婷",
    "周可欣",
    "罗清戈",
    "陈玉晗",
    "张枢淳",
    "王悦悦",
    "戈子源",
    "金熙真",
    "孟芮希",
    "王晨宇",
    "郇云迪",
    "余蜀豫",
    "杨雨轩",
    "杨易男",
    "王奕霏",
    "任奕成",
    "董力玮"
]


class Person:
    def __init__(self, uid, name, score, num):
        self.uid = uid
        self.name = name
        self.score = score
        self.num = num

    def getNum(self):
        return self.num


def score_cmp(self, other):
    try:
        tmp1 = int(self.num)
        tmp2 = int(other.num)
        if tmp1 < tmp2:
            return -1
        elif tmp1 == tmp2:
            return 0
        else:
            return 1
    except:
        return -1


def inquire(uid, name):
    return requests.get(
        f"http://www.sales1.top/score/interface/search_exam_all_score.jsp?student_name={name}&student_num={uid}&course=%E5%85%A8%E9%83%A8"
    ).text


def simple():
    try:
        name = input("请输入学生姓名: ")
        uid = int(input("请输入学号: "))
        result = json.loads(inquire(uid, name))
        exam_scores = result
        for i in range(len(exam_scores)):
            if exam_scores[i]['course'] == "班级排名" or exam_scores[i]['course'] == "总分":
                print(exam_scores[i]['course'], str(exam_scores[i]['score']))
            else:
                print(exam_scores[i]['course'], str(exam_scores[i]['score']) + "/" + str(exam_scores[i]['paper_score']))
    except:
        print("查询异常")


def total(type):
    # type=0 按学号排列
    # type=1 按分数排列
    people = [Person(0, "", 0, 59)] * 60
    if type == 0:
        for i in range(58):
            result = json.loads(inquire(i + 1, names[i]))
            exam_scores = result
            try:
                print(i + 1, names[i], "总分", str(exam_scores[7]['score']), "排名", str(exam_scores[8]['score']))
            except:
                print(i + 1, names[i], "总分", "未录入", "排名", "未录入")
    else:
        for i in range(58):
            result = json.loads(inquire(i + 1, names[i]))
            exam_scores = result
            try:
                people[i] = Person(i + 1, names[i], exam_scores[7]['score'], exam_scores[8]['score'])
            except:
                people[i] = Person(i + 1, names[i], 0, 59)
        sorted_people = sorted(people, key=functools.cmp_to_key(score_cmp))
        for i in range(58):
            try:
                print(sorted_people[i].num, sorted_people[i].name, "总分", sorted_people[i].score, "学号",
                      sorted_people[i].uid)
            except:
                print(sorted_people[i].num, sorted_people[i].name, "总分", "未录入", "学号", sorted_people[i].uid)


if __name__ == '__main__':
    total(type=1)
