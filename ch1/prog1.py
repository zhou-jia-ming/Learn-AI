# -*- encoding: utf-8 -*-
# @FileName: prog1.py
# @Author: Zhou Jiaming
# @Time: 8/25/21 10:36 PM

"""
三个门后边有两个门空的，一个有奖
要求： 选择一个门，争取获得奖品

你选中一个门，还没有打开门。
然后主持人打开另一个空的门。
此时你换一个门会得到更大的概率吗？

"""

import random

def DoorAndPrizeSim(switch, loopNum):
    """
    模拟各种情况下的中奖概率
    :param switch:
    :param loopNum:
    :return:
    """
    win = 0
    total = 0

    for loop in range(loopNum):
        # 初始化奖品和选择的门
        prize = random.randint(0, 2)
        initialChoose = random.randint(0, 2)

        doors = [0,1,2]
        doors.remove(prize) # 移除有奖门

        if initialChoose in doors:
            doors.remove(initialChoose) # 移除选中门

        # 随机打开一个门，改门不是选中门并且是没有奖品的。
        n = len(doors)
        r = random.randint(0, n-1)
        openDoor = doors[r]
        # 计算判断后的门
        if(switch):
            secondChoice = 3 - openDoor - initialChoose
        else:
            secondChoice = initialChoose

        total += 1
        if (secondChoice == prize):
            win +=1
    return win/total


if __name__ == "__main__":
    print("when switching, the winning rate is ",
          DoorAndPrizeSim(True, 1000000))
    print("when not switching, the winning rate is ",
          DoorAndPrizeSim(False, 1000000))
    # 一个可能的输出如下：
    # when switching, the winning rate is  0.666942
    # when not switching, the winning rate is  0.333271
