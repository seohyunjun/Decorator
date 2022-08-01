# ---- 단일 함수를 사용해 하나 이상의 Decorator 사용 테스트
from os import O_NONBLOCK


def check_user_is_not(username):
    def user_check_decorator(f):
        def wrapper(*args, **kwargs):
            if kwargs.get('username') == username:
                raise Exception("This user is not allowed to get food")
            return f(*args, **kwargs)
        return wrapper
    return user_check_decorator

class Store(object):
    @check_user_is_not("admin")
    @check_user_is_not("user123")
    def get_food(self, username, food):
        return self.storage.get(food)

#--- 결과 : Decorator는 위에서 아래로 적용되므로 def 키워드에 가장 가까운 Decorator가 먼저 적용되고 마지막으로 실행
