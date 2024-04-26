def cipher(str):
  changestr = ''
  for i in str:
    
      
    if ord(i) - ord('a') >= 0 & ord(i) - ord('a') < 26:
      changestr += chr(219 - ord(i))
    else:
      changestr += i
  return changestr
encrypt = cipher('CuSO4')
decrypt = cipher(encrypt)
print('原文: CuSO4')
print('暗号化:',encrypt)
print('復号化:',decrypt)
