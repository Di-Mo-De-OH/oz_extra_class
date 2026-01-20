class Bird:
    def __init__(self,name,twit,flyingsound,meter):
        self.name = name
        self.twit = twit
        self.meter = meter
        self.flyingsound = flyingsound

    def flying(self):
        print(f"{self.name} 출발!!!!")
        print(f"{self.twit}")
        print(f"날개를 {self.flyingsound} 날았습니다.")
        print(f"결과는 {self.meter} m 입니다.")

parrot = Bird("앵무새","까악","힘차게",2)
sparrow = Bird("참새","짹짹","빠르게",8)
pigeon = Bird("비둘기","구구","부드럽게",12)
chiken = Bird("닭","꼬끼오","퍼덕이며",1)
rubberduck = Bird("러버덕","삑삑삑","날지 못함",0)

user_input = input("앵무새,참새,비둘기,닭,러버덕 중 하나를 골라주세요")

if user_input == "앵무새":
    parrot.flying()
elif user_input == "참새":
    sparrow.flying()
elif user_input == "비둘기":
    pigeon.flying()
elif user_input == "닭":
    chiken.flying()
elif user_input == "러버덕":
    rubberduck.flying()
else:
    print("당신의 답은 틀렸습니다,앵무새,참새,비둘기,닭,러버덕 중 하나를 골라주세요")
