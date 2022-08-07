## 파이썬 표준라이브러리 functools 모듈은 래퍼 자체에 손실된 원래 함수의 속성을 복사하는 update_wrapper() 함수로 이 문제를 해결

import functools

WRAPPER_ASSIGNMENTS = ('__module__','__name__','__qualname__','__doc__','__annotations__')
WRAPPER_UPDATES = ('__dict__',)

def update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updates=WRAPPER_UPDATES):
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)
    for attr in updates:
        getattr(wrapper, attr).update(getattr(wrapped, attr,{}))
        
    
    # 이슈 #17482: __dict__를 업데이트할 때 래핑된 함수에서
    # 실수로 복사하지 않도록 __wrapped__를 설정한다.
    wrapper.__wrapped__ = wrapped
    # 래퍼를 돌려주고 partial() 함수를 통해 Decorator로 사용할 수 있다.    
    return wrapper 

def foobar(username='someone'):
    """구현할 메서드 내용"""
    pass

def is_admin(f):
    def wrapper(self,*args,**kwargs):
        if kwargs.get('username')!='admin':
            raise Exception("This user is not allowed get food")
        return f(*args, **kwargs)
    return wrapper

foobar = functools.update_wrapper(is_admin, foobar)

foobar.__name__ # 'foobar'
foobar.__doc__ # '구현할 메서드 내용'
