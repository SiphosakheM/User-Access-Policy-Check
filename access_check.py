import datetime

role = input("Enter your role: ").strip().lower()
has_token = input("Do you have a token, yes or no? ").strip().lower()
current_hour = datetime.datetime.now().hour
opening_time = datetime.time(9 , 0)
closing_time = datetime.time(17 , 0)

def access_check(role, has_token):
    if role == "admin" and has_token == "yes":
        print("ACCESS GRANTED")
    elif role == "editor" and has_token == "yes":
        if opening_time <= current_hour <= closing_time:
            print("ACCESS GRANTED")
        elif not (opening_time <= current_hour <= closing_time):
            print("ACCSS DENIED out of office hours")
        else:
            print("ACCESS DENIED missing credentails")
    elif role == "guest" and has_token == "yes" or role == "guest" and has_token == "no":
        print("ACCESS DENIED Uauthorized role")
    else:
        print("ACCESS DINIED Missing credentials")
        
access_check(role,has_token)