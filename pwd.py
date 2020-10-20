password = 'a123456'
n = 3
while True:
	login = input('請輸入密碼：')
	if login == password:
		print('登入成功')
		break
	else:
		n = n-1
		if n != 0:
			print('密碼錯誤！還有',n,'次機會')
		else:
				print('錯誤過多次，密碼已經鎖住')
				break

