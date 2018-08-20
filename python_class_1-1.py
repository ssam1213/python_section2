import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스선언

class UserInfo:
    #메소드로 안하고 init
    #초기화될떄 단한번 실행
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("name : " + self.name)
        print("phone : " + self.phone)
    
    def __del__(self):
        print("delete")


#인스턴스화 => 메모리에 올리는
user1 = UserInfo("kim", "010-1111-1234")
user2 = UserInfo("park", "010-1234-1234")

print(id(user1)) #4501861768 ref address
print(id(user2)) #4501861824

# user1.set_info("kim", "010-1111-1234")
# user2.set_info("park", "010-1234-1234")

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone)
print(user2.name)