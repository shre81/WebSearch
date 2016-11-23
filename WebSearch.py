import os
import webbrowser as wb
import re

filenames = []
folnames = []
tabs = 0
while True:
    try:
        userpth = input("\n Enter the folder that needs to be searched (for e.g. C:\Documents): ")
        flist = os.listdir(path = userpth)
        break
    except FileNotFoundError:
        print('Not a valid file path; please try again')
#flist = os.listdir(path = 'C:\\Users\\shreyasgopinath')
userip = int(input("\n\nSelect from three options below \n 1.File Names only \n 2.Folder Names only \n 3.Both Files and Folders \n Default will search for both \n "))
if userip not in (1,2,3):
    userip = 3

def gosearch(searchlst): #searchstring need to be a list of strings
    global tabs
    for j in range(len(searchlst)):
        if(len(searchlst)==0):
            continue
        else:
            if (tabs >= 10):
                userip = input("\n\sContinue with next ten results (y/n)?: ")
                if (userip=='y'):
                    tabs = 0
                    #continue
                else:
                    print ('Have a Good Day, Bye!')
                    break
            else:
                search_term = searchlst[j][0]
                print('\nSearching on the web for:', search_term )
                url = "https://www.google.com/search?q={}".format(search_term)    
                wb.open(url)
                #print(type(search_term))
                #print(search_term)
                tabs+=1

for i in range(len(flist)):
    if(re.findall('^[a-zA-Z0-9].+\.',flist[i])): #filenames
        filenames.append(re.findall('^[a-zA-Z0-9].+(?=\.)', flist[i]))
    elif(re.findall('^[a-zA-Z0-9].+',flist[i])):
        folnames.append(re.findall('^[a-zA-Z0-9].+', flist[i]))
    else:
        continue
        
if(userip==3):
    gosearch(filenames)
    gosearch(folnames)
elif(userip==1):
    gosearch(filenames)
else:
    gosearch(folnames)    