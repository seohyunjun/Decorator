## 정적, 클래스, 추상 메서드 혼합하기

# <하위 클래스를 사용하여 상위 추상 메서드의 서명을 확장하기>
import abc
class BasePizza(object, metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def get_ingredients(self):
        """재료를 출력한다."""
def Egg():
    return 'egg'
class Calzone(BasePizza):
    ingredients = ['cheese','dough']
    def get_ingredients(self, with_egg=False):
        egg = Egg() if with_egg else None
        return self.ingredients + [egg]
    
# BasePizza 클래스에서 상속할 Calzone 하위 클래스를 정의한다. BasePizza에서 정의하는 인터페이스를 지원하는 한, Calzone 하위 클래스의 메서드를 원하는 방식으로 정의할 수 있다. 메서드를 클래스 또는 정적 메서드로 구현하는 것이 포함된다. 

# <기본 클래스의 추상 get_gredients() 메서드와 DietPizza 하위 클래스의 정적 get_ingredients() 메서드 정의>
import abc

class BasePizza(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_ingredients(self):
        """재료를 출력한다."""
class DietPizza(BasePizza):
    @staticmethod
    def get_ingredients():
        return None

# 정적 get_ingredients() 메서드가 객체의 상태에 따라 결과를 반환하지 않더라도 추상 BasePizza클래스의 인터페이스를 지원하므로 여전히 유효하다.

## 같은 예시
class BasePizza(object, metaclass=abc.ABCMeta):
    ingredients = ['cheese']
    
    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
        """재료를 출력한다."""
        return cls.ingredients


### 추상 메서드 구현하기
import abc

class BasePizza(object, metaclass=abc.ABCMeta):
    
    default_ingredients = ['cheese']
    
    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
        """재료를 출력한다."""
        return cls.default_ingredients
class DietPizza(BasePizza):
    def get_ingredients(self):
        return [Egg()]+super(DietPizza, self).get_ingredients

# BasePizza에서 상속하는 모든 Pizza(여기서는 DietPizza)는 get_ingredients() 메서드를 재정의해야 하지만 모든 Pizza는 재료 목록을 얻기 위한 기본 클래스의 기본 메커니즘에 super()를 사용하여 액세스할 수 있다.

## ** super -- 사용 주의점
# 파이썬은 항상 개발자가 단일 상속과 다중 상속을 모두 사용하여 클래스를 확장할 수 있게 했지만, 오늘날 많은 개발자가 이러한 메커니즘과 관련된 super() 메서드의 작동 방법을 이해하지 못한다.

# 다중 상속은 많은 곳에서 사용되는데, 특히 mixin(두 개 이상의 다른 클래스 상속) 패턴을 포함하는 코드에서 사용된다.

## class (expression of inheritance)
## 부모 객체 리스트를 지정하기 위한 예시
def parent():
    return object
class A(parent()):
    pass

A.mro()

# .mro()는 속성을 해결하는 데 사용되는 메서드 확인 순서를 반환하며 클래스 간의 상속 트리를 통해 호출할 다음 메서드를 검색하는 방법을 정의

# 부모 클래스에서 메서들르 호출하는 표준 방법은 super() 함수를 사용하는 것이지만 super() 함수는 실제로 생성자이며 호출할 때마다 super 객체를 인스턴스화한다.
# 첫번째 인수는 클래스이고 두 번째 선택적 인수는 하위 클래스 또는 첫 번째 인수의 인스턴스이다.

# 생성자가 반환하는 객체는 첫 번째 인수의 부모 클래스에 대한 프록시로 작동한다. MRO 리스트의 클래스를 반복적으로 검색해서 찾은 첫 번째 일치 속성을 반환하는 고유한 __getatribut__ 메서드가 있다.

## Exp
class A(object):
    bar = 42
    def foo(self):
        pass

class B(object):
    bar = 0

class C(A, B):
    xyz = 'abc'

C.mro() # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

super(C,C()).bar # 42

super(C,C()).foo 

super(B).__self__
super(B,B()).__self__ # <__main__.B object at 0x1050ef340>

# C 인스턴스의 super 객체의 속성을 요청할 때 super() 객체의 __getattribute__ 메서드는 MRO 리스트를 통과하고 super 속성이 있는 첫 번째 클래스의 속서을 반환한다.

super(C) # <super: <class 'C'>, NULL>
# 두 번째 인수로 인스턴스가 제공되지 않아서 super 객체는 인스턴스에 바인딩할 수 없다. 따라서 이 언바운드 객체를 사용하여 클래스 속성에 액세스할 수 없다.

# 액세스를 시도하면 다음과 같은 오류가 발생한다.
super(C).foo 
# AttributeError: 'super' object has no attribute 'foo'
super(C).bar
# AttributeError: 'super' object has no attribute 'bar'
super(C).xyz
# AttributeError: 'super' object has no attribute 'xyz'

# super 클래스가 설명자 프로토콜(descriptor protocol) __get__을 구현하는 방식은 언바운드 super 객체를 클래스 속성으로 유용하게 만든다.

class D(C):
    sup = super(C)

D().sup 
# <super: <class 'C'>, <D object>>
D().sup.foo
# <bound method A.foo of <__main__.D object at 0x1050b8b80>>
D().sup.bar
# 42

# 파이썬 3 이후, super()는 업그레이드되었다. 메서드 내에서 호출할 수 있다. super()에 전달되지 않으면 인수에 대한 스택 프레임을 자동으로 검색한다.
class B(A):
    def foo(self):
        super().foo()

# 하위 클래스에서 부모 속성에 액세스하는 표준 방법은 super()이며, 항상 이것을 사용해야한다.
# 다중 상속을 사용할 때 부모 메서드가 호출되지 않거나, 두 번 호출되는 등 에상치 못한 오류 없이 메서드의 호출을 사용할 수 있다.
