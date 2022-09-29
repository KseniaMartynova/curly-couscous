#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #импортируем код в модуль
import numpy #поддержка больших массивов и матриц
import matplotlib.pyplot as mpp # визуализация функции

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': #указывает на область видимости, где будет выполняться код
    arguments = numpy.arange(0, 200, 0.1) #задание промежутка
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments] #рисует график
    )
    mpp.show() #показывает график 
