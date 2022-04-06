class Class:
	__students_count = 22

	def __init__(self, name):
		self.name = name
		self.grades = []
		self.students = []
		self.average_grade = 0

	def add_student(self, name, grade):
		self.grades.append(float(grade))
		self.students.append(name)

	def get_average_grade(self):
		self.average_grade = sum(self.grades) / len(self.students)
		return f"{self.average_grade:.2f}"

	def __repr__(self):
		self.average_grade = sum(self.grades) / len(self.students)
		return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.average_grade:.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 3.20)
a_class.add_student("George", 5.48)
a_class.add_student("Amy", 4.32)
a_class.add_student("Ico", 3.32)
a_class.add_student("Ani", 2.32)
a_class.add_student("Pepa", 5.32)
print(a_class)
