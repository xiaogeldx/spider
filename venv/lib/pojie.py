
import zipfile
import random
import time
import sys
from multiprocessing import Process


class MyIterater():
    #密码的匹配
#定义一个单位字符
#从012345里面匹配出我们的5位数密码
    letters = "012345"
#设置一个最大值和最小值
#进行自增
    min_digits = 0
    max_digits = 0
#类似的魔法方法--》类（class声明的自带的）
    def __init__(self,min_digits,max_digits):
    #实例化对象给出密码的范围
#判断我们的最小值和最大值，那么我们的最小值就是最小值，最大值就是最大值
        if min_digits < max_digits:
            self.min_digits= min_digits
            self.max_digits = max_digits
            #最小值大于最大值，最小值就是最大值，最大值就是最小值
        else:
            #self---》是类（class）对象本省，谁使用self，self就是谁
            self.min_digits = max_digits
            self.max_digits = min_digits
            #两个数--》匹配出来的结果---》套正确的密码
            #迭代器访问定义
            def __iter__(self):
                #返回自己本身
                return self

            def __next__(self):
        #密码的生成，随机匹配，按照我们上面定义的规则来匹配
        #空字符
                rst = str()
        #生成随机数
                for item in range(0,random.randrange(self.min_digits,self.max_digits + 1)):
                    rst += random.choice(MyIterater.letters)
                return rst

#定义一个解压缩包的函数
#def定义函数
#def 函数名（）：
def exteact():
    """提取压缩文件"""
    #开始提取的时间
    start_time = time.time()
    #指定文件
    zfile = zipfile.ZipFile("test.zip")
    for p in MyIterater(5,6):
        print(p)
        #把我们的密码一个个去套
        #匹配的密码不正确
        #path---》指定解压后文件的存储位置
        #pwd---》指定zip文件的密码
        #members---》（可选）指定zip文件中要解压的文件
        #当密码不正确时——————》抛出异常，代码会进行执行
        try:
            zfile.extractall(path=".",pwd=str(p).encode("utf-8"))
            print("这是密码{}".format(p))
            #结束时间
            now_time = time.time()
            print("用时{}".format(now_time - start_time))
            sys.exit(0)
        except Exception as e:
            pass
if __name__=="__main__":
    #进程
    t1 = Process(target=exteact)
    t2 = Process(target=exteact)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

exteact()
