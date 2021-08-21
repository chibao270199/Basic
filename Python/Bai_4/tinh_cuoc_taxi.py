print(("Nguyễn Chí Bảo").center(78,'-'))
a = int(input("Loại Xe (Chỉ nhập 4 hoặc 7): \n"))
b = int(input("Số km di chuyển: \n"))
c = int(input("Thời Gian Chờ(làm tròn theo phút): \n"))
d = (c -5)*750
if a == 4 and b==1:
    print ("Tiền Chờ = ",d)
    print ("Tiền di chuyển = 11000")
    print ("Tiền Cước = ",11000+d)
elif a==4 and 1<b<31 :
    print ("Tiền Chờ = ",d)
    print ("Tiền di chuyển = ",11000+(b-1)*15300)
    print ("Tiền Cước = ",11000+(b-1)*15300+d)
elif a==4 and b>30:
    print ("Tiền Chờ = ",d)
    print ("Tiền di chuyển = ",11000+(30-1)*15300+(b-30)*12100)
    print ("Tiền Cước = ",11000+(30-1)*15300+(b-30)*12100+d)
if a == 7 and b==1:
    print ("Tiền Chờ = ",d)
    print ("Tiền di chuyển = 12000")
    print ("Tiền Cước = ",12000+d)
elif a==7 and 1<b<31 :
    print ("Tiền Chờ = ",d)
    print ("Tiền di chuyển = ",12000+(b-1)*16100)
    print ("Tiền Cước = ",12000+(b-1)*16100+d)
elif a==7 and b>30:
    print ("Tiền Chờ = ",d)
    print ("Tiền di chuyển = ",12000+(30-1)*16100+(b-30)*13800)
    print ("Tiền Cước = ",12000+(30-1)*16100+(b-30)*13800+d)