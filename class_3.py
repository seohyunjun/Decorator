# update_wrapper Decorator로 원래 속성 검색
from doctest import Example
from sys import exec_prefix


def is_admin(f):
    def wrapper(self,*args,**kwargs):
        if kwargs.get('username')!='admin':
            raise Exception("This user is not allowed get food")
        return f(*args, **kwargs)
    return wrapper


def foobar(username="someone"):
    """구현할 메서드 내용"""
    pass

foobar.__doc__  #'구현할 메서드 내용'
foobar.__name__ # 'foobar'

@is_admin
def foobar(username="someone"):
    """구현할 메서드 내용"""
    pass

foobar.__doc__  #
foobar.__name__ #'wrapper'


