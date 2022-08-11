# 추상 메서드
# 추상 메서드는 구현 자체를 제공하지 않을 수 있는 추상 기본 클래스에서 정의된다.
# 클래스에 추상 메서드가 있다면 인스턴스화할 수 없다.
# 따라서 추상 클래스(하나 이상의 추상메서드가 있는 클래스로 정의)를 다른 클래스에서 부모 클래스로 사용해야 한다.
# 이 하위 클래스는 추상 메서드를 구현하여 부모 클래스를 인스턴스화할 수 있도록 한다.

# 추상 기본 클래스를 사용하여 기본 클래스에서 파생된 다른 연결된 클래스 간의 관계를 명확히 할 수 있지만, 추상 기본 클래스 자체를 인스턴스화하는 것은 불가능핟.
# 추상 기본 클래스를 사용하여 기본 클래스에서 파생된 클래스는 기본 클래스에서 특정 메서드를 구현하도록 보장하거나 예외를 발생시킨다.

# <기본 메서드 구현>
class Pizza(object):
    @staticmethod
    def get_radius():
        raise NotImplementedError

# 이 정의를 사용하면 Pizza에 상속되는 모든 클래스는 get_radius() 메서드를 구현하고 재정의해야한다.
# 그렇지 않고 메서드를 호출하면 예외가 발생한다.
# Pizza의 각 하위 클래스가 자체적인 컴퓨팅 방법을 구현하고 get_radius()를 반환하는 데 유용하다.

# 추상 메서드를 구현하는 이 방법에는 단점이 있다. Pizza에서 상속하지만 get_radius()를 구현하는 것을 잊어버린 클래스를 작성하면, 런타임에 해당 메서드를 사용하려는 경우에만 오류가 발생한다. 
Pizza()
# <__main__.Pizza object at 0x102875b20>
Pizza().get_radius()
# # Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 4, in get_radius
# NotImplementedError

# Pizza는 직접 인스턴트화할 수 있기 때문에 이런 일을 방지할 방법이 없다. 메서드를 구현하고 재정의하는 것을 잊거나 추상 메서드로 객체를 인스턴스화하는 것에 대한 조기 경고를 받는 한 가지 방법은 Python에서 제공하는 추상 기본 클래스 모듈을 사용하는 것이다.

# <추상 메서드 구현>
import abc

class BasePizza(object, metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def get_radius(self):
        """구현할 메서드 내용"""
        
BasePizza()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Can't instantiate abstract class BasePizza with abstract methods get_radius

# BasePizza 클래스를 인스턴스화하려고 하면, 즉시 할 수 없다는 피드백을 받는다.
# 추상 메서드를 사용한다고 해서 사용자가 메서드를 구현하는 것이 보장되지는 않지만 이 데커레이터를 통해 오류를 더 일찍 잡는 데 도움이 된다.

