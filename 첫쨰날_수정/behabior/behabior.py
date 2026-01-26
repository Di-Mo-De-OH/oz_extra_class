from abc import abstractmethod

class Fly:
    @abstractmethod
    def fly_motion(self):
          raise NotImplementedError()

class FlyStrong(Fly):
     def fly_motion(self):
          print("날개를 힘차게")

class FlyFast(Fly):
     def fly_motion(self):
          print("날개를 빠르게")
          
class FlyGently(Fly):
     def fly_motion(self):
          print("날개를 부드럽게")
          
class FlyWings(Fly):
     def fly_motion(self):
          print("날개를 퍼덕이며")

class FlyNo(Fly):
     def fly_motion(self):
          print("날지 못함")

class Sound:
     @abstractmethod
     def make_sound(self):
          raise NotImplementedError()
     
class ParrotSound(Sound):
     def make_sound(self):
        print("까악")
        

class SparrowSound(Sound):
     def make_sound(self):
        print("쨲쨲")

class PigeonSound(Sound):
     def make_sound(self):
        print("구구")

class ChickenSound(Sound):
     def make_sound(self):
        print("꼬끼오")      

class Rubber_DuckSound(Sound):
     def make_sound(self):
        print("삒삒삒")      