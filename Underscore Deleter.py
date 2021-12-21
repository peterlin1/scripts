import os
d=raw_input("Enter dir path: ")
try:
    a=os.listdir(d)
    d+='/'
    for i in a:
        ni=i.replace('_',' ')
        print 'renaming '+i+' to '+ni
        os.rename(d+i,d+ni)
except:
    print "You might've misspelled your path -.-"
