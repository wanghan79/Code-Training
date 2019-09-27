##!/usr/bin/python3
import threading
import time

"""
  Author:  Sheng Yang
  Purpose: Adding exception handling to ensure that calling multithreaded classes 
    can get corresponding results
  Created: 27/9/2019
"""


class mythread:
    """
    Create multithreaded tasks, including the number of threads.
    """

    def create(self, job, m):
        """
        :param job:Target job name
        :param m:Number of threads created
        :return:
        """
        self.job = job
        self.m = m
        for _ in range(m):
            threading.Thread(target=self.job, args=()).start()


def job1():
    """
    create a job
    :return:
    """

    f = open('test.txt', mode='a', encoding='gb2312')
    f.write('job1 begin   ' + time.ctime(time.time()) + '\n')
    f.close()
    time.sleep(0.1)
    f = open('test.txt', mode='a', encoding='gb2312')
    f.write('job1 running  ' + time.ctime(time.time()) + '\n')
    f.close()
    time.sleep(0.1)
    f = open('test.txt', mode='a', encoding='gb2312')
    f.write('job1 finish  ' + time.ctime(time.time()) + '\n')
    f.close()


def job2():
    """
    create a job
    :return:
    """
    f = open('test.txt', mode='a', encoding='gb2312')
    f.write('job2 begin   ' + time.ctime(time.time()) + '\n')
    f.close()
    time.sleep(0.1)
    f = open('test.txt', mode='a', encoding='gb2312')
    f.write('job2 running  ' + time.ctime(time.time()) + '\n')
    f.close()
    time.sleep(0.2)
    f = open('test.txt', mode='a', encoding='gb2312')
    f.write('job2 finish  ' + time.ctime(time.time()) + '\n')
    f.close()


def job3():
    """
    create a job
    :return:
    """
    f = open('test.txt', mode='a', encoding='gb2312')
    f.write('job3 begin   ' + time.ctime(time.time()) + '\n')
    f.close()
    time.sleep(0.1)
    f = open('test.txt', mode='a', encoding='gb2312')
    f.write('job3 running  ' + time.ctime(time.time()) + '\n')
    f.close()
    time.sleep(0.3)
    f = open('test.txt', mode='a', encoding='gb2312')
    f.write('job3 finish  ' + time.ctime(time.time()) + '\n')
    f.close()


if __name__ == '__main__':
    try:
        thread1 = mythread()
        thread1.create(job1, 1)
        thread1.create(job2, 1)
        thread1.create(job3, 1)
    except NameError:
        print('请指定正确的线程任务')
    except TypeError:
        print('参数格式不对，请输入正确的线程任务名及需要启动线程的个数')
    else:
        print('程序正常运行')
