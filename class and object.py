number1=int(input("enter a mumber"));
number2=int(input("enter a number"));
print("1-add");
print("2-subtract");
print("3-multiply");
print("4-division");

while choice !=5:
    if choice==1:
        result=number1 + number2;
    elif choice==2:
        result = number1 - number2;
    elif choice == 3:
        result = number1 * number2;
    elif choice == 4:
        result = number1 / number2;
    else:
         result=("Thank you");

    choice = int(input("choice operation:"));
    print(result);




'''i=0;
while i<10:
    print(i,end=" ");
    i=i+1;'''