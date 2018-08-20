import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def function1():
        print("func1 호출")

    def function2(self):
        print(id(self))
        print("func2 호출")

f = SelfTest()
# print(dir(f))
print(id(f))
# 4364297328
# 4364297328 주소값일치

f.function2()

#인스턴스화 시키지 않고 직접 접근하면 호출된다
print(SelfTest.function1())
