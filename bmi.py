body_height = input('請輸入你的身高(cm): ')
body_weight =  input('請輸入你的體重(kg): ')
body_weight =  float(body_weight)
body_height = float(body_height)
body_height = body_height / 100 # 換成公尺
bmi = body_weight / (body_height ** 2)

if bmi < 18.5:
	print('你的BMI值為: ', bmi , '你的體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('你的BMI值為: ', bmi , '你的體重在正常範圍')
elif bmi >= 24 and bmi < 27:
	print('你的BMI值為: ', bmi , '你的體重過重')
elif bmi >= 27 and bmi < 30:
	print('你的BMI值為: ', bmi , '你的體重已到輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('你的BMI值為: ', bmi , '你的體重已到中度肥胖')
else:
	print('你的BMI值為: ', bmi , '你的體重已到重度肥胖')