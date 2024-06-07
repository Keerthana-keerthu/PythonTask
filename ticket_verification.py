print("Welcome to INDIGO Airlines")
print("Please,Finish the verifications first")
list_verified=[]
def Ticket_checking():
    Ticket_check=input("Enter if your ticket is valid or not: ")
    if Ticket_check=="valid":
        print("Ticket verified, Now you can go inside")
        list_verified.append("Ticket checking:verified")
        print(list_verified)
    else:
        print("Oops, Ticket not valid, you are not allowed to go inside")
def covid_checking():
    covid_check=input("Enter your result of covid-19: ")
    if covid_check=="negative":
        print("Result negative, You can travel now")
        list_verified.append("covid_check:verified")
        print(list_verified)
    else:
        print("Oops, your results are positive, you won't allow to travel")
def immigration_checking():
    immigration_check=input("Enter whether verification satisfy or not: ")
    if immigration_check=="satisfy":
        print("Verified, Get the boarding pass ")
        list_verified.append("immigration_check:satified")
        print(list_verified)
    else:
        print("Not satisfied, you are not allowed")
def bagweight_checking():
    bagweight_check=int(input("Enter your bag weight: "))
    bagweight_amount=1000
    if bagweight_check<=20:
        print("you can travel")
        list_verified.append("bagweight_checking:verified")
        print(list_verified)
    else:
        print("Please, Reduce some bagweight or you should pay extra fees")
        total_bill=((bagweight_check - 20)*1000)
        print(f"your bagweight {bagweight_check} , you sholud pay {total_bill} for your extra bagweight")
print("The list of verification")
check1=print("\tcheck1:Ticket_checking()")
check2=print("\tcheck2:covid_checking()")
check3=print("\tcheck3:immigration_checking()")
check4=print("\tcheck4:bagweight_checking()")
user_details=input("\nEnter your details you need form this verification process:")
list=["check1","check2","check3","check4"]
if user_details in list:
    if user_details=="check1":
        Ticket_checking()
        user_details1=input("\nEnter your details you need form this verification process:")
        if user_details1 in list :
            if user_details1=="check2":
                covid_checking()
                user_details2=input("\nEnter your details you need form this verification process:")
                if user_details2=="check3":
                    immigration_checking()
                    user_details3=input("\nEnter your details you need form this verification process:")
                    if user_details3=="check4":
                        bagweight_checking()
else:
    print("Enter details not in list")