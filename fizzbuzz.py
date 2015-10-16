import sys
## code used when script is executed without any command line arguments
if len(sys.argv) <= 1:
    should_ask_for_input = True
    #### loop to ensure a user entry is a an integer     
    while should_ask_for_input: 
        start_number = raw_input("Pleae enter a start number: ")
        stop_number = raw_input("Pleae enter a stop number: ")
        try:
            int(start_number)
            int(stop_number)
            should_ask_for_input = False
        except ValueError:
            print ('try again')
    ## fizzbuzz code            
    for x in range(int(start_number),int(stop_number)):
        if x % 3 == 0 and x % 5 == 0:
            print "Fizz Buzz"
        elif x % 3 == 0:
            print "Fizz"
        elif x % 5 == 0:
            print "Buzz"
        else:
            print x
            
## code used when script is executed with command line arguments ##            
elif len(sys.argv) > 1:
    command_line_arguments = True
    ## initial error check when script is executed from command line ##    
    try: 
        int(sys.argv[1])
        int(sys.argv[2])
    except ValueError:
        print "Cannot use Letters!"
        check_user_entry = True
        ## loop to ensure a user entry is a an integer after initial error check fails ##        
        while check_user_entry: 
            retry_start = raw_input("Please enter a start number: ")
            retry_stop = raw_input("Please enter a stop number: ")
            try:
                int(retry_start)
                int(retry_stop)
                check_user_entry = False
            except ValueError:
                print "Try Again"
    ## code inspects command line arguments or user input ##         
    if command_line_arguments == True:
        start = int(sys.argv[1])
        stop = int(sys.argv[2])
    else:
        start = int(retry_start)
        stop = int(retry_stop)
    ## fizzbuzz code         
    for x in range(start,stop):
        if x % 3 == 0 and x % 5 == 0:
            print "Fizz Buzz"
        elif x % 3 == 0:
            print "Fizz"
        elif x % 5 == 0:
            print "Buzz"
        else:
            print x
            
            
            
        
    

        
        