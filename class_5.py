#  wraps : Dacorator용 Dacorator
import functools

def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

class Store(object):
    @check_is_admin
    def get_food(self,username, food):
        """저장소에서 음식을 가져온다"""
        return self.storage.get(food)

# admin()은 인수로 전달된 함수 f에서 독스트링, 함수 이름, 기타 정보를 복사한다.
# 따라서 Dacorator(get_food() 함수)는 여전히 변경되지 않은 특징이 있다.

store = Store()
store.get_food.__doc__
#'저장소에서 음식을 가져온다'
store.get_food.__name__
'get_food'