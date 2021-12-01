#부모 클래스 
class Person(object):
    #초기화 메서드 
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스 
class Student(Person):
    #초기화 메서드를 재정의(덮여쓰기,override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모의 생성자 메서드 호출(super, base키워드가 없다~~)
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드를 재정의(다른 코드를 실행)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(
            self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo() 


