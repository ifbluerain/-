import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import xlrd
def ShowFinaInfo():
    def Count(l):
        num=len(re.findall('([\u4e00-\u9fa5])',l))
        return num
    fp = open('FinanceInfo.csv','r')
    data=fp.readlines()
    for line in data:
        for li in line.split(','):
            li = li.replace('\n','')
            if Count(li) == 1:
                print('{:^7}'.format(li), end='')
            elif Count(li) == 2:
                print('{:^6}'.format(li), end='')
            elif Count(li) == 3:
                print('{:^5}'.format(li), end='')
            elif Count(li) == 4:
                print('{:^4}'.format(li), end='')
            else:
                print('{:^8}'.format(li), end='')
        print('')

def AddFinaInfo():
    fo = open("FinanceInfo.csv","a+")
    finas = []
    for finalinfo in fo:
        finalinfo = finalinfo.replace("\n","")
        finas.append(finalinfo)
    a = input("请输入您想添加的费用类型：")
    finalInfo = []
    finalInfo.append(a)
    for i in range(2,14):
        b = input("请输入{}月此类型的花费：".format(str(i-1)))
        finalInfo.append(b)
    finas.append(finalInfo)
    for item in finas:
        fo.seek(0,2)
        fo.write(','.join(item) + '\n')
    fo.close()


def DelFinaInfo():
    fo = "FinanceInfo.csv"
    """删除财务记录"""
    df = pd.read_csv(fo, index_col=[0], encoding='gbk')
    index = input("请输入要删除的财务记录内容: ")
    try:
        df.drop(index, inplace=True)
        print("已删除{}".format(index))
    except Exception as e:
        print(e)
        print("请输入正确的财务记录内容")
    df.to_csv(fo, encoding='gbk')


def ModFinaInfo():
    """修改财务记录"""
    fo = "FinanceInfo.csv"
    df = pd.read_csv(fo, index_col=[0], encoding='gbk')
    index = input("请输入要修改的财务记录内容: ")
    col = input("请输入要修改的财务记录的时间: ")
    try:
        val = input("请输入新的值: ")
        df.loc[index, col] = val
        print("已修改{}的{}为{}".format(col, index, val))
    except Exception as e:
        print(e)
        print("请输入正确的要修改的财务内容、时间、值")
    df.to_csv(fo, encoding='gbk')

def AnalyFinaInfo():
    data = pd.read_csv("FinanceInfo.csv", encoding='gbk')

    col_1 = data["月份"]
    data_1 = np.array(col_1)
    col_2 = data["一年总数"]
    data_2 = np.array(col_2)

    fig = plt.figure()
    sub = fig.add_subplot(111)
    sub.pie(data_2, labels=data_1, rotatelabels=False, labeldistance=1, autopct='%.1f%%')

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    sub.legend()
    fig.suptitle('pies', fontsize=16)
    fig.tight_layout()
    plt.show()


def ShowUI():
    os.system("cls")
    print(' '*18+"& &",end='\n\n')
    print(' '*5+'||{:-^20}||'.format('家庭财务分析系统'))
    print('     [{:^24}]'.format('1*显示财务记录*'))
    print('~--2*添加财务记录*        3*删除财务记录*--~')
    print('~~----4*修改财务记录*  5*分析财务记录*----~~')
    print('~~~{:-^32}~~~'.format('6*退出系统*'))
    while True:
        n = eval(input("选择你的操作（1-6）："))
        if n==1:
            ShowFinaInfo()
        elif n==2:
            AddFinaInfo()
        elif n==3:
            DelFinaInfo()
        elif n==4:
            ModFinaInfo()
        elif n==5:
            AnalyFinaInfo()
        elif n==6:
            break
        else:
            print('请输入1-6之间的整数')
if __name__ == '__main__':
    ShowUI()