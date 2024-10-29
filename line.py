import matplotlib.pyplot as plt
import numpy as np


def generate_line_plot(years,a,b):
    plt.figure(figsize=(10, 6))
    plt.plot(years, a, marker='o', linestyle='-', color='b', label='mean')#改统计类型的，如这里我统计的是均值
    plt.plot(years, b, marker='o', linestyle='-', color='r', label='standard deviation')#同上，这里是标准差
    # 设置标题和标签
    plt.title('Ryde')#改图像标题的，这里是地名
    plt.xlabel('Year')
    plt.ylabel('Sold House price')#改数据名称的，如这里我统计的是房价
    plt.xticks(years, rotation=45 )
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    # 数据是从2021年开始的，每年一个数据点
    years = np.arange(2021, 2024)
    a = [1628483.871, 1584357.29, 1838725.806]  # 对应的数据点
    b = [950440.0227, 908326.182, 886427.2777]  # 对应的数据点
    generate_line_plot(years, a,b)

if __name__ == "__main__":
    main()