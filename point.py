import matplotlib.pyplot as plt
import numpy as np


def generate_scatter_plot(x_data, y_data, x_label, y_label, title, colors):
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, color=colors, label='Data Points')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

x_data = [2113200,1011736.408,1667361.867,950440.0227,908326.182,886427.2777,665806.1823,1065746.976,896673.6228
]  #更改这里的数值，如现在是房屋价格均值
y_data = [199.229712,163.8008884,172.7721178,264.0457959,241.6995836,309.4186722,39.38027104,53.34176298,54.40555457
]
#更改这里的数值，注意与x的值对应，如第一个x是2021年A区的房价均值,第一个y就是2021年A区的房屋面积
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'orange']
#一个颜色对应一个地区一年的状态，3个地区3年有9个

generate_scatter_plot(x_data, y_data, 'house price', 'Landscape Value', 'standard deviation', colors)
#这里可以更改x轴和y轴的名称，以及图表的名称