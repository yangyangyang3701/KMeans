# -*- coding: utf-8 -*-
import csv
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
import random
import math


def random_points():
    print("*======================================================*")
    n = int(input("请输入数字N，表示您想生成N个数："))
    x_list = []
    y_list = []
    for i in range(n):
        # 1.随机生成n个点的坐标
        x_list.append(math.ceil(random.random() * 10))
        y_list.append(math.ceil(random.random() * 10))

    # 2.把数据写入文件
    file = open('data_coordinate.csv', 'w', newline='', encoding='utf-8')
    csv_write = csv.writer(file)
    csv_write.writerow(["X坐标", "Y坐标"])
    for i in range(n):
        csv_write.writerow([x_list[i], y_list[i]])
    file.close()


def process_data():
    # 3.读取数据
    data = pd.read_csv('data_coordinate.csv', encoding='utf-8')
    x_train = data[["X坐标", "Y坐标"]]
    df = pd.DataFrame(x_train)

    # 4.数据归一化（样本数据均衡时，可不写）
    normal = preprocessing.MinMaxScaler()
    x_train = normal.fit_transform(x_train)

    # 5.KMeans
    k_number = int(input("请输入数字K,代表聚类数:"))
    print("*======================================================*")
    kmeans = KMeans(n_clusters=k_number).fit(x_train)
    y_pred = kmeans.predict(x_train)

    result = pd.concat((data, pd.DataFrame(y_pred)), axis=1)
    result.rename({0: '聚类结果'}, axis=1, inplace=True)
    print(result)


if __name__ == "__main__":
    random_points()
    process_data()






