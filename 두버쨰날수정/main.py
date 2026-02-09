from abc import ABC,abstractmethod

class Machine(ABC):
    name :str
    price :int

    def serve(self):
        print(f"{self.name} 자판기")
        f"돈 투입 {self.add_money()}"
        self.action()
        self.done()

    def done(self):
        print("제품 배출 완료")

    def add_money(self):
        user_money = int(input("돈을 넣어주세요"))
        if user_money < self.price:
            print("금액이 부족합니다")
        else: 
            return user_money
    
    @abstractmethod
    def action(self):
        pass
