from abc import ABC,abstractmethod

#========추상 클래스==========
class Interface(ABC):
    @abstractmethod
    def storage(self):
        pass

    @abstractmethod
    def thumbnail(self):
        pass

    @abstractmethod
    def metadata(self):
        pass

    @abstractmethod
    def createurl(self):
        pass
#========인터페이스==========

#======제품군============

class Enterprise(Interface):
    def storage(self):
        return "AWS S3"

    def thumbnail(self):
        return "AWS Lambda Image Processor"

    def metadata(self):
        return "AWS MediaConvert"

    def createurl(self):
        return "CloudFront Signed URL"

class Startup(Interface):
    def storage(self):
        return "Local Storage"

    def thumbnail(self):
        return "Pillow 기반 서버 처리"

    def metadata(self):
        return "FFmpeg"

    def createurl(self):
        return "lStatic URL Builder"

class Privacy(Interface):
    def storage(self):
        return "Private Object Storage"

    def thumbnail(self):
        return "내부 폐쇄망 처리 서버"

    def metadata(self):
        return "내부 분석 서비스"

    def createurl(self):
        return "Token 기반 임시 URL"

#======제품군============

#======실행=========

# 아래 클래스를 어떻게 작성해야 할지 잘 모르겠습니다.
class Create(ABC):
    @abstractmethod
    def fctory(self):
        pass


class EnterpriseCreate(Create):
    def fctory(self):
        return Enterprise()


class StartupCreate(Create):
    def fctory(self):
        return Startup()
    
class PrivacyCreate(Create):
    def fctory(self):
        return Privacy()


#======실행=========


