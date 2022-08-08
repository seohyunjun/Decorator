# 메서드(클래스 속성으로 저장되는 함수)
from xml.etree.ElementTree import PI


class Pizza(object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size
        
Pizza.get_size # <function Pizza.get_size at 0x1018b40d0>
Pizza.get_size() # TypeError: get_size() missing 1 required positional argument: 'self'
# 임의의 인스턴스를 메서드에 전달하여 get_size()를 사용할 수 있다.

Pizza.get_size(Pizza(53)) # 53

# get_size()는 어떤 인수를 제공할 필요가 업삳. 바운드 메서드이기 때문에 자체 인수는 자동으로 Pizza 인스턴스로 설정된다. 
m = Pizza(42).get_size
m() # 42

#----- 바인딩된 메서드에 대한 참조가 있는 한 Pizza 객체에 대한 참조를 유지할 필요가 없다.
#----- 메서드에 대한 참조가 있지만 바인딩된 객체를 찾으려면 메서드의 자체 속성을 확인할 수 있다.
m = Pizza(52).get_size
m.__self__ # <__main__.Pizza object at 0x1018c4400>
m == m.__self__.get_size # <bound method Pizza.get_size of <__main__.Pizza object at 0x1018c4400>>

