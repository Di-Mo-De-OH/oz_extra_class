from abc import ABC,abstractmethod
# 피자의 기본 값들을 설정
class Pizza(ABC):

    def prepaer(self):
        print("준비중")
    def bake(self):
        print("만드는중")
    def cut(self):
        print("자르는 중")
    def box(self):
        print("박스에 담는중")

#  객체 즉 피자들을 정의
class NYStylePizza(Pizza):
    def bake(self):
        print("햄 넣는중")

class NYExtraToppingPizza(Pizza):
    def bake(self):
        print("햄+고기 넣는중 ")

#피자를 만들떄 기본 알고리즘을 생성
class PizzaStore(ABC):
    def order_pizza(self,pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepaer()
        pizza.bake()
        pizza.cut()
        pizza.box()
    # 어떤 가게에서(PizzaStore을 상속받는 가게) 어떤 피자를 만들지 설정(기본적으로 만들어 놓은 피자들 NyStylePizza,WestStylePizza)
    @abstractmethod
    def create_pizza(self,pizza_type):
        pass
# 피자 가게에서 어떤 스타일의 피자를 사용할지 결정 
class NYPizzaStore(PizzaStore):
    def create_pizza(self,pizza_type):
        if pizza_type == "nomal":
            return NYStylePizza()
        elif pizza_type =="extra":
            return NYExtraToppingPizza()
        else:
            raise ValueError("no pizza")
        
store = NYPizzaStore()

store.order_pizza("nomal")

store.order_pizza("extra")