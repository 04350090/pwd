password = 'a123456'
n = 3
while n > 0:
	n = n - 1
	login = input('請輸入密碼：')
	if login == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤！')
		if n > 0:
			print('還有',n,'次機會')
		else:
			print('沒機會嘗試了')

