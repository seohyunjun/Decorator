# 검사를 통해 관련 정보 추출
# Dacorator 함수 활용 극대화

import functools
import inspect

def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs) # 함수 인수의 이름과 값을, 키/쌍으로 포함하여 {'username':'admin','type':'chocolate'} 반환 
        if func_args.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

@check_is_admin
def get_food(username, type='chocolate'):
    return type + " nom nom nom!"

get_food('admin') # 'chocolate nom nom nom!'
get_food('min') # Exception: This user is not allowed to get food 
