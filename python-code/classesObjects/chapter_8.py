class Student:
    school_name="High Lakes";
    @classmethod
    def school_property(cls):
        print(f"Name of the School {cls.school_name}");
    
Student.school_property();