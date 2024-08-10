class Course:
    def __init__(self, name, numbr_of_stdnts, lecturer, hall, department) -> None:
        self.name=name
        self.numbr_of_stdnts=numbr_of_stdnts
        self.lecturer=lecturer
        self.hall=hall
        self.department=department

courses = {
    'course1':Course('debt instroments',16,'Moneyteacher','room 65','economics'),
    'course2':Course('inflation',16,'Hightalker','room 64','economics'),
    'course3':Course,
    'course4':Course,
    'course5':Course
}