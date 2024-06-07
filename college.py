print("WELCOME TO XYZ COLLEGE")
print("----------------------")
print("Dear student fill the details below based on your percentage course will offered")
Student_name=input("Enter your name:")
Year_Of_Passing=int(input("Enter passout year:"))
Qualification=input("Enter your qualification:")
percentage=int(input("Enter your percentage:"))
course=input("Enter your interested field: ")
if (course=="Engg" or course=="Arts and science"):
    if(percentage >=90 and percentage <=100 and course=="Engg"):
        print("Congratulations!,You are eligible for BE CSE")
    elif(percentage >=80 and percentage <=90 and course=="Engg"):
        print("Congratulations!,You are eligible for BE ECE")
    elif(percentage >=70 and percentage <=80 and course=="Engg"):
        print("Congratulations!,You are eligible for BE MECHANICAL")
    elif(percentage >=60 and percentage <=70 and course=="Engg"):
        print("Congratulations!,you are eligible for BE CIVIL")
    elif(percentage <=50 and course=="Engg"):
        print("Oops!,You are not eligible")
    elif(percentage >=90 and percentage <=100 and course=="Arts and science"):
        print(",You are eligible for BSC CHEMISTRY")
    elif(percentage >=80 and percentage <=90 and course=="Arts and science"):
        print(",You are eligible for BSC CS")
    elif(percentage >=70 and percentage <=80 and course=="Arts and science"):
        print(",You are eligible for BSC PHYSICS")
    elif(percentage >=60 and percentage <=70 and course=="Arts and science"):
        print(",You are eligible for B.Com")
    elif(percentage <50 and course=="Arts and science"):
        print("Oops!,You are not eligible")
else:
    print("Sorry,we not have the field that you selected")