import winsound
import time
import sys
CODE = {'A': '.-',   'B': '-...',  'C': '-.-.', 
    'D': '-..',  'E': '.',   'F': '..-.',
    'G': '--.',  'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',  'L': '.-..',
    'M': '--',   'N': '-.',   'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
     'S': '...',  'T': '-',   'U': '..-',
    'V': '...-',  'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.' 
    }
#单位时间t=50毫秒,频率为800mhz
t = 0.075
freq = 900
a = "Today we are going to talk about the best ways to learn English Does anyone learn English by watching videos No It is too hard to understand spoken English"
str1 = a.split(" ")
#按空格分隔单词i
for i in str1:
  #分隔单个字母j
  for j in i:
    #根据字母取出字典中对应的摩斯码
    k = CODE[j.upper()]  
    g = 0
    #按摩斯码点横发声
    while g < len(k):
      #如果与上个点横不一致，则间隔1t
      sys.stdout.flush()
      print(k[g],end='')
      if g > 0 and k[g-1] != k[g]:
        time.sleep(t)
      if k[g] == '.':
        winsound.Beep(freq,int(t*1000))
      else:
        #横3个时间单位
        winsound.Beep(freq,int(t*3000))
      #点横之间间隔1T
      time.sleep(t)
      g += 1
    #字符之间间隔3t
    print(' ',end='')
    time.sleep(3*t)
  #单词之间间隔7t
  print('\\')
  time.sleep(t*7)