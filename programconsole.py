
# KVCC 
# CIS-226-23199
# Advanced Python Programming
import sys
def program_console(searchtext, filename):#create function
    counter = 0 #initialize in 0 
    try:#attemp to open the file
        f = open(filename)#open the file and assign to "f"
    except IOError:#in Out error
        print("Error: Cant't open the file")#output the error
        return#return to end
    print(filename)#output
    for line in f:#read lines in file open
        if searchtext in line:#search input in lines
            print(line)#output if searchtext is in lines
            counter += 1 #add one to counter
    return counter     
if __name__ == '__main__':#compare name and file of the first argument input
    if len(sys.argv) == 3:#requires 3 arguments as input
        program_console(sys.argv[1],sys.argv[2])#assign arguments 
    else:#with not enough arguments 
        print("Error: Missing Arguments")#output

      

        



    
    



    