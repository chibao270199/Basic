print (("Nguyễn Chí Bảo").center(78,'-'))
a = int(input("Nhập X: \n"))
S = 1 + a + (a**3)/3 + (a**5)/5
print ("S = 1 + %s + %s^3/3 + %s^5/5 = %.1f"%(a,a,a,S))