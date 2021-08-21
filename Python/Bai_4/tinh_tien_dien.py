print (("Nguyên Chí Bảo").center(78,'-'))
a = int(input("Số kw tiêu thụ: \n"))
if a < 51:
    print("Tiền điện phải trả = ",50*1484)
elif 50 < a <101:
    print("Tiền điện phải trả = ",50*1484+50*1533)
elif 100<a<201:
    print("Tiền điện phải trả = ",50*1484+50*1533+100*1786)
elif 200<a<301:
    print("Tiền điện phải trả = ",50*1484+50*1533+100*1786+100*2242)
elif 300<a<401:
    print("Tiền điện phải trả = ",50*1484+50*1533+100*1786+100*2242+100*2503)
elif 400<a:
    print("Tiền điện phải trả = ",50*1484+50*1533+100*1786+100*2242+100*2503+(a-400)*2587)