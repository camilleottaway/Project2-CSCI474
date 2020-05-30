import csv
import re
import pandas

fields = ('R0', 'HospitalLag', 'profileName', 'Dead', 'Susceptible', 'Hospital', 'RecoveredMild', 'RecoveredSevere', 'RecoveredTotal', 'Infected', 'Exposed', 'Sum')
modelfields = ('Time', 'R0', 'HospitalLag', 'Dead', 'Susceptible', 'Hospital', 'RecoveredMild', 'RecoveredSevere', 'RecoveredTotal','Infected', 'Exposed', 'Sum')

with open("resultsmini.txt", "r") as myfile, open("parsedresults",'w', newline='') as fw:
    writer = csv.DictWriter(fw, fields, delimiter='|')

    record = {}

    for line in myfile:
        
        #writer.writerow(params)
        #params = {}
        #continue

        record=line.split('}', 1)
        params = record[0]+'}'
        print(params)
        runs = record[1]
        runs = runs.split('}')
        print(runs[1])

        rundf = pandas.DataFrame(columns=('Time', 'R0', 'HospitalLag', 'Dead', 'Susceptible', 'Hospital', 'RecoveredMild', 'RecoveredSevere', 'RecoveredTotal','Infected', 'Exposed', 'Sum'))

        for run in runs:
            fields = run.split(':')
            print (fields)
            # for field in fields:
            #     modelfield = field.split(': ', 1)
            #     print(field)
            #     field = modelfield[0]
            #     #field = modelfield[1]
            # rundf[modelfield.partition('/')[-1].strip()] = value.stripS()
        

        

        
        #print(runs)

        #print(line)
        #field, value = line.split(': ', 1)
        #runsdf[field.partition('/')[-1].strip()] = value.stripS()
        #print(params)

    #if record:
        # handle last record
        #writer.writerow(record)