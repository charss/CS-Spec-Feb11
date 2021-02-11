class GradedActivity:
	def __init__(self, letter=' ', score=0.0):
		self._letter = letter
		self._score  = score

	def determineGrade(self):
		if self._score >= 90 and self._score <= 100:
			self._letter = 'A'
		elif self._score >= 80 and self._score <= 89:
			self._letter = 'B'
		elif self._score >= 70 and self._score <= 79:
			self._letter = 'C'
		elif self._score >= 60 and self._score <= 69:
			self._letter = 'D'
		else:
			self._letter = 'F'

	def setScore(self, score):
		self._score = score
		self.determineGrade()

	def getScore(self):
		return self._score

	def getLetterGrade(self):
		return self._letter

	

class CurvedActivity(GradedActivity):
	def __init__(self, rawScore=0.0, percentage=0.0):
		self._rawScore = rawScore
		self._percentage = percentage
		super().__init__()

	def setScore(self, s):
		self._rawScore = s
		super().setScore(self._rawScore * self._percentage)

	def setPercentage(self, c):
		self._percentage = c

	def getPercentage(self):
		return self._percentage

	def getRawScore(self):
		return self._rawScore

exam = CurvedActivity()
raw_score = float(input("Enter the student's raw numeric score: "))
curve_percent = float(input("Enter the curve percentage for this student: "))

exam.setPercentage(curve_percent)
exam.setScore(raw_score)

print(f'The raw score is {exam.getRawScore():.2f}')
print(f'The curved score is {exam.getScore():.2f}')
print('The curved grade is', exam.getLetterGrade())
