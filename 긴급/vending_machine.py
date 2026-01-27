from main import Serve     

class CoffeeVendingMachine(Serve):
    def product(self):
        coffee = {
            "아메리카노":500,
            "라뗴":1000
        }
        return coffee
    
    def action(self):
        print("추출 중...")
        print("컵에 담는 중...")
        

class ColaVendingMachine(Serve):
    def product(self):
        drink = {
            "콜라":1000,
            "사이다":1500
        }
        return drink
    
    def action(self):
        print("냉장 상태 확인 중...")
        print("배출구로 이동 중...")
        


class RamenVendingMachine(Serve):
    def product(self):
        noodle = {
            "신라면":1000,
            "진라면":1500
        }
        return noodle
    def action(self):
        print("추출 중...")
        print("컵에 담는 중...")
        