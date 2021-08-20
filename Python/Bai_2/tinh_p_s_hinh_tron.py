print (("Nguyễn Chí Bảo").center(78,"*"))
a = eval(input("Nhập bán kính: \n"))
p = 2 * 3.14 *a
s = 3.14 * a * a
print("P = 2 * 3.14 * %s = %.2f "%(a,p))
print("P = 3.14 * %s * %s = %.2f "%(a,a,s))