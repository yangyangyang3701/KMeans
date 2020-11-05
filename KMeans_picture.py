# -*- coding: utf-8 -*-
"""利用KMeans对颜色进行聚类。输出仅由k中颜色组成的输入图片
"""
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
import PIL.Image as image  # 仍然使用PIL的写法


# load图片,便利得到其所有像素点
def load_picture(path):
    f = open(path, 'rb')
    data_list = []
    img_object = image.open(f)
    width, height = img_object.size
    for x in range(width):
        for y in range(height):
            pix1_tuple, pix2_tuple, pix3_tuple = img_object.getpixel((x, y))
            data_list.append([pix1_tuple, pix2_tuple, pix3_tuple])
    f.close()
    # 数据归一化
    mm = preprocessing.MinMaxScaler()
    data = mm.fit_transform(data_list)
    return np.mat(data), width, height


if __name__ == "__main__":
    # 1.load图片
    img, width, height = load_picture('box.jpg')

    # 2.调用KMeans进行聚类
    kmeans = KMeans(n_clusters=4).fit(img)
    label_index = kmeans.predict(img)
    label = label_index.reshape([width, height])
    # 3.save新图片
    pic_new = image.new("P", (width, height), color=(111, 111, 111))
    for x in range(width):
        for y in range(height):
            # 4.更改灰度值，根据类别数生成相同数目的灰度值
            pic_new.putpixel((x, y), int(256/(label[x][y]+1))-1)
    pic_new.save("box_new.jpg", "BMP")
