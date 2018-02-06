# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
import numpy as np 


def built_in_sampling(mean_x, mean_y, rho, sigma_x, sigma_y, sample_num):
    """
    Numpy built-in multivariate normal distribution.
    """
    x, y = np.random.multivariate_normal([mean_x, mean_y], 
        [[sigma_x ** 2, rho * sigma_x * sigma_y], [rho * sigma_x * sigma_y, sigma_y ** 2]], sample_num).T
    plt.plot(x, y, 'x')
    plt.axis('equal')
    plt.show()


def Gibbs_sampling(mean_x, mean_y, rho, sigma_x, sigma_y, sample_num, show_line):
    """
    Gibbs sampling for 2-dimensional gaussian distribution.
    """
    
    # 随机初始化 y
    x = np.random.rand() * 10
    y = np.random.rand() * 10

    # 采样结果
    sample_x = []
    sample_y = []

    # 自定义画布大小
    plt.axis([-15, 15, -15, 15])  
    plt.ion()  

    # 循环采样
    for i in range(sample_num):
        # 采样新的x
        new_x = np.random.normal(mean_x + sigma_x * rho * (y - mean_y) / sigma_y, sigma_x ** 2 * (1 - rho ** 2))

        if show_line:
            plt.plot([x, new_x], [y, y])
        else:
            plt.scatter(new_x, y)

        plt.pause(0.15)

        x = new_x

        # 采样新的y
        new_y = np.random.normal(mean_y + sigma_y * rho * (x - mean_x) / sigma_x, sigma_y ** 2 * (1 - rho ** 2))

        if show_line:
            plt.plot([x, x], [y, new_y])
        else:
            plt.scatter(x, new_y)
        plt.pause(0.15)

        y = new_y


if __name__ == '__main__':
    # 均值
    mean_x = 0
    mean_y = 0
    # 相关系数
    rho = 0
    # 标准差
    sigma_x = 1
    sigma_y = 2 
    # 样本数
    sample_num = 1000

    # 是否显示生成路线
    SHOW_LINE = True 

    built_in_sampling(mean_x, mean_y, rho, sigma_x, sigma_y, sample_num)

    # Gibbs_sampling(mean_x, mean_y, rho, sigma_x, sigma_y, sample_num, SHOW_LINE)
