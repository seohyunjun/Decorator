# Decorator는 함수를 중심으로 반복되는 코드를 리팩터링할 때 자주 사용 


#-----비효율 적인 예시 
import re


class Store(object):
    def get_food(self, username, food):
        if username!='admin':
            raise Exception("This user is not allowed to get food") #---> 반복
        return self.storage.get(food)
    
    def put_food(self, username, food):
        if username!='admin':
            raise Exception("This user is not allowed to put food") #---> 반복
        self.storage.put(food)
    
#----- 리팩터링 사용 조금 더 효율적  
def check_is_admin(username): #1
    if username!='admin':
        raise Exception('This user is not allowed to put food')

class Store(object):
    def get_food(self, username, food):
        check_is_admin(username)
        return self.storage.get(food)

    def put_food(self, username, food):
        check_is_admin(username)
        return self.storage.put(food)

#-----Decorator 사용 코드 더 깔끔
def check_is_admin(f): 
    def wrapper(*args, **kwargs): #1
        if kwargs.get('username')!='admin':
            raise Exception('This user is not allowed to put food')
        return f(*args, **kwargs)
    return wrapper



class Store(object):
    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)
    
    @check_is_admin
    def put_food(self, username, food):
        self.storage.put(food)
        
# 1과 같이 check)is_admin Decorator를 정의하고 액세스 권한을 확인해야 할 때마다 호출, Decorator는 
# kwargs 변수를 사영해 함수에 전달된 인수를 검사하고 username을 검색
