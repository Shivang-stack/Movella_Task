import re
passw = input("Enter Your Password! = ")

def check_pass(password):
    count = 1
    startDif_c=0
    Digit_c =0
    Spl_c=0
    
    to_arr = list(password)
    
    if len(password) == 0:
        print('password cannot be Blank')
    if len (password) < 4:
        print('Password Strength LOW')
    if len(password) >8:
        count+=1    
    
    if re.search("[0-9]",to_arr[0]):
        startDif_c-=1

    for char in password:
            if re.search("[0-9]",char):
                Digit_c +=1
            if re.search("[@#$%&]",char):
                Spl_c+=1
    
    count += startDif_c+Digit_c+Spl_c
    
    if count < 5:
        print('Password Strength LOW')
    elif count >= 5 and count < 7.5:
        print('Password Strength AVERAGE')
    elif count >= 7.5 and count < 9:
        print('Password Strength GOOD')
    else :
        print('Password Strength VERY GOOD')
    print(count)



check_pass(passw)