# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

string = 'не очень хочется купаться, да и не люлблю, я это дело'
x = 'н'
string = string.split()
result = [item for item in string if x not in item]
print(*result)