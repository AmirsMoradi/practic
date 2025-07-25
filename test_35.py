#import math



#def sq(number):
   #try:
     #if number < 0 :
      #   print("cant sqrt in - ")
     #else:
     #  v =   math.sqrt(number)
    #   print(v)
   #    return v
  # except ValueError:
 #      return "number in valid"

#number =float(input("Enter a number: "))
#print(sq(number))



import re
print(re.findall(r"\d+","من 3 سیب و 15 پرتقال دارم"))
print(re.findall(r"[\w\.-]+@[\w\.-]+\.\w+","برای اطلاعات بیشتر با ما تماس بگیرید: info@example.com یا support123@domain.ir و یا test.email@company.co"))
print(re.sub(r"[مخفی شده]","لطفاً با شماره‌های 09123456789 یا 021-12345678 تماس بگیرید. شماره پشتیبانی: 09351234567 است."))