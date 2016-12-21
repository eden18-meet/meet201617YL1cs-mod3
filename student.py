class Student:
    def __init__(self,name,hometown,age,height,favorite_ice_cream):
        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.favorite_ice_cream=favorite_ice_cream

    def print_summary(self):
        print(self.name)
        print(self.hometown)
        print(self.age)
        print(self.height)
        print(self.favorite_ice_cream)

    def get_giraffe_gap(self):
        giraffe=500
        return(giraffe-self.height)
    
        
        
##from student import student
##my_student=student("may","hifa","15","160","vanilla cookies")
##my_student.get_giraffe_gap("160")
