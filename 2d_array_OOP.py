class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
	def __init__(self, firstName, lastName, idNumber, scores):
		super().__init__(firstName, lastName, idNumber)
		self.scores = scores

	def calculate(self):
		avg = sum(self.scores) / len(self.scores)
		if avg >= 90:
			return 'O'  # Outstanding
		elif avg >= 80:
			return 'E'  # Exceeds Expectations
		elif avg >= 70:
			return 'A'  # Acceptable
		elif avg >= 55:
			return 'P'  # Poor
		elif avg >= 40:
			return 'D'  # Dreadful
		else:
			return 'T'  # Troll
line = input('Enter the line containg First Name, Last Name, ID with space in between: ').split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input('Total No of Sub Scores: ')) # not needed for Python
scores = list( map(int, input('Enter the scores with space in between: ').split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())