import time
from threading import * 


class Hello(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            time.sleep(0.2)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print('hi')
            time.sleep(0.2)


def main():
    o1 = Hello()
    o2 = Hi()
    o1.start()
    time.sleep(0.1)
    o2.start()
    o1.join()
    o2.join()
    print('end')

if __name__ == '__main__':
    main()
