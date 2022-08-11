# 클래스 메서드(class method)
# 인스턴스가 아닌 클래스 바인딩
# 클래스 메서드는 객체의 상태에 액세스할 수 없고 클래스의 상태 및 메서드만 액세스할 수 있다. 

# <클래스 메서드를 클래스에 바인딩하기>
class Pizza(object):
    radius = 42
    @classmethod
    def get_radius(cls):
        return cls.radius
    
Pizza.get_radius # <bound method Pizza.get_radius of <class '__main__.Pizza'>

Pizza().get_radius # <bound method Pizza.get_radius of <class '__main__.Pizza'>

Pizza.get_radius is Pizza().get_radius # False

Pizza.get_radius() # 42

# get_radius() 클래스 메서드에 다양한 방법이 있지만 어떻게 접속하든 메서드는 항상 연결된 클래스에 바인딩 된다.
# 첫번째 인수는 클래스 자체여야 한다. 클래스 = 객체(object)!


# 클래스 메서드는 주로 __init__보다 다른 signature(서명)를 사용하여 객체를 인스턴스화하는 팩터리 메서드를 만드는 데 유용하다.
class Pizza(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())
    
# @classmethod 대신에 @staticmethod를 사용하면 Pizza에서 상속받은 클래스가 자체 목적으로 팩터리를 사용할 수 없게 되어 Pizza 클래스 이름을 하드코딩해야 한다.
# 그러나 이 경우 Fridge 객체를 전달할 수 있는 from_fridge() 팩터리 메서드를 제공한다.
# 우리가 pizza.from_fridge(myfridge)와 같은 것으로 이 메서드를 호출하면 myfridge에서 사용할 수 있는 재료와 함께 아주 새로운 Pizza를 반환한다.
# 객체의 상태에 대한 것이 아니라 객체의 클래스에만 관심이 있는 메서드를 작성할 때마다 클래스 메서드로 선언해야 한다.

Pizza.from_fridge is Pizza.from_fridge # False