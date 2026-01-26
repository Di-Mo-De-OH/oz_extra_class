from bird.bird import Parrot,Pigeon,Chicken,Sparrow,Rubber_Duck,Bird


BIRD = {
    "앵무새": Parrot,
    "참새": Sparrow,
    "비둘기": Pigeon,
    "닭": Chicken,
    "러버덕": Rubber_Duck,
}

name = input("새 이름을 입력하세요 (앵무새/참새/비둘기/닭/러버덕): ").strip()

bird = BIRD.get(name)
if not bird:
    print("지원하지 않는 새입니다.")
else:
    bird = bird()
    bird.play()
    
