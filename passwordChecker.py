import re

def check_pass(password):
    #Rules Array
    rules=[ 'Password should have atleast 8 characters',
            'Password should contains atleast 2 special characters',
            'Password should contains atleast 2 numbers',
            'Password should not start with any number'
            ]

    #validation for blank input
    if len(password) ==0:
        print("Password can't be blank")
        return

    #Rule Flags
    rule1=rule2=rule3=rule4 = True
    
    #Counters
    total_mark=0
    passlen = 0
    startDif_c=0
    Digit_c =0
    Spl_c=0
    
    #checking for length of password
    if len(password) >8:
        rule1=  False
        passlen+=2
    
    #checking is first character is Digit
    to_arr = list(password)
    if re.search("[0-9]",to_arr[0]):
        startDif_c-=1
    else:
        startDif_c+=2
        rule4=False

    #checking for no of digits and special characters
    for char in password:
            if re.search("[0-9]",char):
                Digit_c +=1
                
            if re.search("[@#$%&]",char):
                Spl_c+=1
                
    
    if Digit_c >=2:
        Digit_c=2
        rule3 = False
    if Spl_c>= 2:
        Spl_c= 3
        rule2 = False


    total_mark += startDif_c+Digit_c+Spl_c+passlen
    
    #Printing Response
    if total_mark < 5:
        print('Password Strength LOW')
        prerule=0
        if rule1 and prerule<2:
            print(rules[0]) 
            prerule+=1
        if rule2 and prerule<2:
            print(rules[1])
            prerule+=1
        if rule3 and prerule<2:
            print(rules[2])
            prerule+=1
        if rule4 and prerule<2:
            print(rules[3])
            prerule+=1
    elif total_mark >= 5 and total_mark < 7.5:
        print('Password Strength AVERAGE')
        prerule=0
        if rule1 and prerule<2:
            print(rules[0]) 
            prerule+=1
        if rule2 and prerule<2:
            print(rules[1])
            prerule+=1
        if rule3 and prerule<2:
            print(rules[2])
            prerule+=1
        if rule4 and prerule<2:
            print(rules[3])
            prerule+=1
    elif total_mark >= 7.5 and total_mark < 9:
        print('Password Strength GOOD')
    else :
        print('Password Strength VERY GOOD')
    
    
if __name__ == '__main__':
    #Input
    passw = input("Enter Your Password =")
    check_pass(passw)