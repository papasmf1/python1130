# DemoFile2.py 

#서식지정
print("{0:b}".format(10))
print("{0:x}".format(10))
print("{0:,}".format(15000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

#파일에 읽기와 쓰기 
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("한글\nabcd\n세번째\n")
f.close()

