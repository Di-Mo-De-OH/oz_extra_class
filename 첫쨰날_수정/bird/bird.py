from behabior.behabior import Fly,FlyStrong,FlyFast,FlyGently,FlyNo,FlyWings,Sound,SparrowSound,ParrotSound,PigeonSound,ChickenSound,Rubber_DuckSound

class Bird:
    NAME:str = "이름없음"
    CRY: Sound
    FLY:Fly
    distance_m: 0

    def __init__(self):
        self.name = self.NAME
        self.cry = self.CRY()
        self.fly = self.FLY()
        self.distance_m = self.distance_m

    def play(self):
        print(f"{self.name} 출발!!!")
        print("새 소리: ", end="")
        self.cry.make_sound()
        print("나는 방식: ", end="")
        self.fly.fly_motion()
        print(f"결과는 {self.distance_m}m입니다.")
   
class Parrot(Bird):
    NAME="앵무새"
    CRY= ParrotSound
    FLY= FlyStrong
    distance_m= 2


class Sparrow(Bird):
    NAME=str = "참새"
    CRY= SparrowSound
    FLY=FlyFast
    distance_m= 8


class Pigeon(Bird):
    NAME=str = "비둘기"
    CRY= PigeonSound
    FLY=FlyGently
    distance_m= 12

class Chicken(Bird):
    NAME=str = "치킨"
    CRY= ChickenSound
    FLY=FlyWings
    distance_m= 1

class Rubber_Duck(Bird):
    NAME=str = "러버덕"
    CRY= Rubber_DuckSound
    FLY=FlyNo
    

