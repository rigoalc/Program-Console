import sys
def program_console(searchtext, filename):
    try:
        f = open(filename)
    except IOError:
        print("Error: Cant't open the file")
        return
    print(filename)
    for line in f:
        if searchtext in line:
            print(line)
if __name__ == '__main__':
    if len(sys.argv) == 3:
        program_console(sys.argv[1],sys.argv[2])
    else:
        print("Error: Missing Arguments")
    
    



    