# coding=utf-8

import Queue
import threading

task_queue = Queue.Queue()  # 任务队列

for i in xrange(5):  # 把任务放到任务队列
    task_queue.put(i)


def do_job():
    """
    干活的函数
    """
    while True:
        task = task_queue.get()   # 从任务队列中取任务
        print "Task:{task}, Thread:{thread}".format(task=task, thread=threading.current_thread)  # 做任务，输出一下做任务的是哪个线程
        task_queue.task_done()  # 告诉他我任务做完了


def main():
    thread_nums = 3  # 线程数
    for i in range(thread_nums):
        t = threading.Thread(target=do_job)    # 创造一个线程去干活 do_job
        t.daemon = True   # 设为守护线程的话，mainThread结束带着我就结束了。不然mainThread就得等我。
        t.start()   # 开始干活吧

    task_queue.join()  # Queue.join()函数 要等队列中所有任务都被获取并处理


if __name__ == '__main__':
    main()
