from concurrent.futures import ThreadPoolExecutor
import time
def fn(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    start = time.time()
    # fn(f"第一次")
    # fn(f"第二次")
    #创建线程池
    with ThreadPoolExecutor(50) as t:
           for i in range(100):
            t.submit(fn(f"线程:"))
    # fn("线程:")
    end = time.time()
    print(f"耗时:%f秒" % (end-start))
