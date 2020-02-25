class Analyzer:

	Result_FILE = r'C:\Users\1\PycharmProjects\SMC_result.txt'
	Data_FILE = r'C:\Users\1\PycharmProjects\my_first_project\test.txt'
	Time_FILE = r'C:\Users\1\PycharmProjects\SMC_time.txt'
	server = []
	System = dict()

	__overload_file = r'Output\Task2\overload.txt'

	def __init__(self):
		self.__res = open(self.Result_FILE, 'w')
		# ДЛЯ SMC
		self.__smc = AppClass.AppClass()
		self.__data = open(self.Data_FILE, 'r')

	def __del__(self):
		self.__data.close()
		self.__res.close()

	def check_strings(self):
		f_time = open(self.Time_FILE, 'w')
		start_time = time.perf_counter()
		count = 0
		for line in self.__data:
			res = self.__smc.CheckString(line)
			if not res[0]:
				self.__f.write(line + ' - no' + '\n')
			else:
				count += 1
				self.__f.write(line + ' - yes' + '\n')
				if line in self.System:
					self.System[line] = 1
				else:
					self.System[line] += 1
		f_time.write(str(time.perf_counter() - start_time)+'\n')
		f_time.close()
		print(count)

	def get_file_content(self):
		try:
			self.__f = open(self.Result_FILE)
		except IOError as e:
			self.check_strings()
			self.__f = open(self.Result_FILE)

		nf = self.__f.read()
		self.__A = nf.split('\n')

		self.__f.close()
		return self.__A

	def analyze_overload(self):
		f_overload = open(self.__overload_file, 'w')
		for key in self.System:
			if self.System.get(key) > 1:
				f_overload.write(str(key) + ' ' + str(self.System.get(key)) + '\n')
		f_overload.close()


if __name__ == "__main__":

	machine = Analyzer()
	machine.check_strings()
	machine.analyze_overload()
