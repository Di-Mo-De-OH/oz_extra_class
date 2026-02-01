from main import Machine     

class CoffeeVendingMachine(Machine):
    name = "커피"
    price = 1000
    
    def action(self):
        print("추출 중...")
        print("컵에 담는 중...")
        
        

class ColaVendingMachine(Machine):
    name = "콜라"
    price = 1500
    
    def action(self):
        print("냉장 상태 확인 중...")
        print("배출구로 이동 중...")
        


class RamenVendingMachine(Machine):
    name = "라면"
    price = 2000
    
    def action(self):
        print("라면 배출")
        print("ㄱ뜨거운 물 주입 중...")
        

a = RamenVendingMachine()

a.serve()