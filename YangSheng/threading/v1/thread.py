import threading
import time

#m表示线程数，n表示每个线程工作的执行次数
class mythread:
    def create(self, job, m, n):
        """
        :param job:
        :param m:
        :param n:
        :return:
        """
        self.job = job
        self.m = m
        self.n = n
        for _ in range(m):
            threading.Thread(target=self.job, args=(n,)).start()


def job1(n):
    for _ in range(n):
        f = open('test.txt', mode='a', encoding='gb2312')
        f.write('job1   ' + time.ctime(time.time()) + '\n')
        f.close()
        time.sleep(1)


def job2(n):
    for _ in range(n):
        f = open('test.txt', mode='a', encoding='gb2312')
        f.write('job2   ' + time.ctime(time.time()) + '\n')
        f.close()
        time.sleep(2)


if __name__ == '__main__':
    thread1 = mythread()
    thread1.create(job1, 3, 4)
    thread1.create(job2, 3, 4)