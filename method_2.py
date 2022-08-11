## 정적 메서드
## 정적 메서드는 클래스의 인스턴스가 아니라 클래스 속하므로 실제 클래스 인스턴스에서 작동하거나 영향을 주지 않는다.
# ** 정적 메서드는 일반적으로 클래스 또는 해당 객체의 상태에 의존하지 않기 때문에 유틸리티 함수를 만드는 데 사용된다.

from os import O_NONBLOCK


class Pizza(object):
    @staticmethod 
    def mix_ingredients(x, y):
        return x + y
    
    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)

# 정적 mix_ingredients() 메서드는 Pizza 클래스 속하지만, 클래스와 상관 없이 mix_gredients() 메서드를 사용할 수 있다.
# Staticmethod를 사용하면 좋은점 
# 1. 속도가 빠르다 ~ Pizza 객체에 대한 바인딩된 메서드를 인스턴스화할 필요가 없다. 바인딩된 메서드도 객체이며, CPU와 메모리 비용이 발생한다. 정적 메서드를 사용하면 이를 피할 수 있다.
# 2. 정적 메서드는 코드 가독성을 향상시킨다. @staticmethod를 보면 메서드가 객체 상태에 의존하지 않는다는 것을 알 수 있다.
# 3. 정적 메서드는 하위 클래스에서 재정의할 수 있다. 정적 메서드 대신 모듈의 최상위 수준에 정의된 mix_ingredients() 함수를 사용하면, pizza에서 상속된 클래스가 cook() 메서드 자체를 재정의하지 않고 피자의 재료를 혼합하는 방식을 변경할 수 없다. 정적 메서드를 사용하면 하위 클래스가 자체 목적을 위해 메서드를 재정의할 수 있다.
# ** 파이썬은 메서드가 정적인지 아닌지 항상 자체적으로 감지할 수 있는 것은 아니다. 한 가지 가능한 패턴을 감지하고 flake8을 사용하여 경고를 발생하는 검사를 추가하는 방법이다.


Pizza().cook is Pizza().cook # False # 바인딩 생성
Pizza().mix_ingredients is Pizza.mix_ingredients # True
Pizza().mix_ingredients is Pizza().mix_ingredients # True 바인딩 생성 x
