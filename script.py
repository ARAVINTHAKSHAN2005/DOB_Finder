# Define Function that finds DOB.
def magic_date_find(num = 'int'):
    '''
    DOCSTRING: Returns your date of birth
    '''
    #Conditional statemnts to validate user input
    if num.isdigit() == True:
        num = int(num) 
        date   = num - 250
        date_of_birth = date%100
        month_of_birth = date//100
        month = '{m:1.0f}'.format(m = month_of_birth)
        #Defining refrence dictionery with corresponding numbers and months
        mydictionery = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

        #User Output 
        if date_of_birth < 32 and date_of_birth >= 1 and int(month) <=12:
            value = f"Your date of birth is {mydictionery[str(month)]} " + str(date_of_birth)
            return value
        #Input Validation 
        elif int(month) > 12:
            value = "Enter a valid number \n Or follow the instructions carefully.\nThe month value is invalid"
            return value 
        #Input Validation 
        else:
            value = "Enter a valid number \n Or follow the instructions carefully.\nThe date value is invalid"
            return value 
    else:
        value = "Enter a number not any other character"
        return value     