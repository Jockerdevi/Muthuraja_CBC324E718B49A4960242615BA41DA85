year=int(input("enter the year"))
if(year%4==0)and(year%100!=0):
   print(f" the given year{year} is leap year")
else:
   print(f"the given year{year} is not a leap year")