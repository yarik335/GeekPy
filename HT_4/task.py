import re
import os
import csv


def ensure_dir(file_path):# checking if directory alredy exist argument=path to new folder
    if not os.path.exists(file_path):
        os.makedirs(file_path) #creating new folder

def write_to_csv(filewr,item,counter=0):#to make main code less repeatable
        filewr.writerow([str(counter),str(item[1]),str(item[0]),str(item[2])])
     
    
def uniq_elements(list):#make new list of unique elements of args list
    seen = set()
    result = []
    for item in list:
        if item[2] not in seen:
            result.append(item)
            seen.add(item[2])
    return result

file1 = open("openerp-server.log")#open file in working dir

file1s = file1.readlines()#read every line list of lines
pat = re.compile(r"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}).+(WARNING|ERROR|CRITICAL).+(werkzeug.+|openerp.+)")#pattern which gets all required data
all_matches = []
errors = []
warnings = []
criticals = []
for lineid,line in enumerate(file1s):#passing all strings and get its ids
    if(pat.match(line)):#if find a match
        matchh = pat.findall(line) #returns a tuple in a list
        if(matchh[0][1] == "ERROR"): # if match is error then append it to errors
            errors.append(matchh[0])
        elif(matchh[0][1] == "WARNING"):# if match is error then append it to warnings
            warnings.append(matchh[0])
        elif(matchh[0][1] == "CRITICAL"):# if match is error then append it to criticals
            criticals.append(matchh[0])
        else:
            print("ERROR")
        
        matchh[0] = matchh[0]+(str(lineid),)#add lineid to the tuple    
        all_matches.append(matchh[0])#add all tuples with line id    
  
 
err_uniq = uniq_elements(errors)#getting unique elements
war_uniq = uniq_elements(warnings)
cr_uniq = uniq_elements(criticals)
all_uniq = uniq_elements(all_matches)

ensure_dir(os.getcwd()+"/result") #checking is there result directory in working directory

with open('result/all_data.csv', 'w') as csvfile: #open or create if don't exists cvs file
    fnames = ['line_id', 'marker','date_time','description']#set column names as a first raw
    filewriter = csv.writer(csvfile, delimiter=',')#set writer object
    filewriter.writerow(fnames)#call the columns
    for item in all_matches:#pass all matches 
        filewriter.writerow([item[3],item[1],item[0],item[2]])#everithing in its order
                                                #lineid,marker,datetime,description
with open('result/unique.csv', 'w') as csvfile: #open or create cvs file for unique elements
    fnames = ['count', 'marker','date_time','description'] #set column names
    filewriter = csv.writer(csvfile, delimiter=',')#writer object
    filewriter.writerow(fnames) #call the columns
    count = 0 #counter of unique elements
    
    for item in err_uniq: #for every ERROR
        count += 1 #not from zero
        write_to_csv(filewriter, item, count)#write everything in its order
     
    for item in war_uniq:#same for warnings
        count += 1
        write_to_csv(filewriter, item, count)
      
    for item in cr_uniq:#same for criticals
        count += 1
        write_to_csv(filewriter, item, count)
"""unique cvs made like this because i wanted elements to be ordered,but it works fine for unordered"""