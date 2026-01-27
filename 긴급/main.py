from abc import ABC,abstractmethod

class Serve(ABC):
    
    def create(self):
        print(f"돈 투입 {self.add_money}")
        money = self.money_valid()
        print(self.action)
        print("제품배출 완료")
        print({self.add_money-self.product})
        
    def add_money(self):
        user_money = int(input("돈을 넣어주세요"))
        return user_money
    
    def money_valid(self):
        if self.add_money < self.product:
            print("금액이 부족합니다")
        else:
            return self.add_money

    @abstractmethod
    def product(self):
        pass
    @abstractmethod
    def action(self):
        pass

    
        
        
