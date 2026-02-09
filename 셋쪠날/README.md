## 팩토리 메서드

### 1. 사용이유
- 생성 로직이 흩어지는걸 막기 위해 사용
  - 조건문이 여기저기 퍼지고 제품 타입이 추가 변경될떄 수정 범위가 많이 늘어난다   
- 확장에 유리하게 만들기 위함
  - 기존 사용코드를 건드리지 않고 생성 쪽만 확장 하는 구조를 만들 수 있다
  
### 2. 장단점
#### 장점
- 변경에 강하다: 어떤 객체를 만들지 규칙이 바뀌어도 팩토리 쪽만 수정하면 되는 경우가 많음
- 결합도 감소: 사용 코드는 구체 클래스에 덜 의존
- 확장성이 좋아짐: 제품군이 늘어나도 구조적으로 받아들이기 쉬움

#### 단점
- 구조가 복잡해질 수 있음: 작은 프로젝트에서는 오히려 손해
- 코드 추적이 어려워질 수 있음: 객체가 어디서 생성되는지 한눈에 안 보일 떄가 있음

```python
from abc import ABC,abstractmethod
# 객체가 기본적으로 가지게될 행동에 대해서 정의 및 각각의 객체가 무조건 달라져야하면 추상메서드로 뺼 수 도 있음
class ObjectAction(ABC):
    def action1(self):
        print("action1")
    @abstractmethod
    def action2(self):
        pass
    def action3(self):
        print("action3")
    def action4(self):
        print("action4")

#  객체들을 정의
class Object1(ObjectAction):
    def action2(self):
        print("action222")
#  객체들을 정의
class Object2(ObjectAction):
    def action2(self):
        print("action22")

#각 객체의 알고리즘 생성
class ObjectAlgorithm(ABC):
    def algorithm(self,obj_type):
        objectaction = self.create_action(obj_type)
        objectaction.action1()
        objectaction.action2()
        objectaction.action3()
        objectaction.action4()

    # 어떤 객체를 사용할지에 대한 함수를 추상메서드로 생성
    @abstractmethod
    def create_action(self,obj_type):
        pass

# 어떤 객체를 사용할지에 대한 클라스 정의(초기엔 조건문으로 했는데 gpt에 검사 해달라 했을떄 dict형태가 더 낫다 라고해서 dict 형식으로 수정)
class WhichObject(ObjectAlgorithm):
    mapping = {"1": Object1, "2": Object2}
    def create_action(self,obj_type):
       try:
          return mapping["obj_type"]()
       except KeyError:
          raise ValueError()
        

