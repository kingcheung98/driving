country = input('請問你是哪國人')
age = input('Age:')
age = int(age)
if country == 'China':
	if age >= 18:
		print('你可以考駕照')
	else:
			print('你不能考駕照')
elif country == 'USA':
	if age >= 16:
		print('你可以考駕照')
	else:
			print('你不能考駕照')

