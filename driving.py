driving = input('請問你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('請輸入，有/沒有')
	raise SystemExit    #觸發錯誤，終止程式(raise觸發錯誤)

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age < 18:
		print('未成年偷偷開車攸')
	else:
		print('注意安全')
elif driving == '沒有':
	if age < 18:
		print('乖寶寶')
	else:
		print('快去學吧')

