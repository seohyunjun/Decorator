# Class Decorator 사용하기
# --- Class Decorator는 함수 Decorator와 동일한 방식으로 작동하지만 함수가 아닌 클래스에서 작동

from msvcrt import kbhit
import uuid

def set_class_name_and_id(klass):
    klass.name = str(klass)
    klass.random_id = uuid.uuid4()
    return klass

@set_class_name_and_id
class SomeClass(object):
    pass

SomeClass.name # <class '__main__.SomeClass'>
SomeClass.random_id # UUID('4dcf4088-5bf0-4b04-a2d3-b6009f144e59')

# 함수 Decorator와 마찬가지로 클래스를 조작하는 공통 코드를 팩터링하는 데 유용하다.
# Class Decorator의 또 다른 용도는 함수 또는 Class를 Class로 래핑하는 것이다. 