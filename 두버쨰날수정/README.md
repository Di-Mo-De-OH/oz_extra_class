## 템플릿 메서드

### 1. 탬플릿 메서드를 사용하는 이유
- 부모 클래스에서 정의된 구조를 그대로 유지하면서 자식 클래스들에 의해 쉽게 확장될 수 있다
- 코드의 중복을 방지할 수 있다
- 확장 시 제어의 역전(부모가 자식을 호출)구조로 일관된 워크플로를 보장한다
- 부모가 알고리즘의 제어권을 갖고, 자식은 일부 단계만 구현 제공한다


### 2. 기본구조 
- 부모 클래스에 알고리즘의 순서 흐름을 정의
- 자식이 반드시 구현해야 하는 추상 메서드 단계를 만듦
- 각각의 자식에서 추상메서드 들을 정의
```python
from abc import ABC,abstractmethod

class TemplateMethod(ABC):

    def template_method(self):
        self.action()
        self.action2()
        self.action3()
        self.action4()

    def action():
        print("action1")
    def action2():
        print("action2")
    def action3():
        print("action3")
    @abstractmethod
    def required_action():
        pass


class  TemplateMethodChild(TemplateMethod):
    def required_action(self):
        print("action4")
```
위와 같은 방식으로 기본구조를 만들 수 있다.

### 3. 장 단점
####1. 장점
- 중복 코드 감소
- 일관된 워크플로 보장
- 확장 용이
- 변경 영향 범위 축소
#### 2. 단점
- 상속 의존: 유연성이 떨어지고 구조가 경직될 수 있음
- 클래스 폭증 가능: 변형이 많아지면 하위 클래스가 많이 생겨 관리가 어려워짐
- 부모-자식 결합도 증가: 자식이 부모 구현 세부에 영향을 많이 받음
- 단계 설계 난이도: 어디를 추상으로 할지 잘못 지정하면 확장이 불편하거나 과도하게 복잡해짐
