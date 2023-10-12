import pandas
import numpy
import operator

# read in the dataframe
dataframe = pandas.read_csv("../Crime_Data_from_2020_to_Present.csv")

# get the crime description columns
crimeDescColumn = pandas.unique(dataframe["Crm Cd Desc"])
crimeDescColumn.sort()

# get the rows that we want
crimeDescRows = ["Crm Cd", "Crm Cd 1", "Crm Cd 2", "Crm Cd 3", "Crm Cd 4"]

print('begin')

# loop through all of the crime columns
for desc in crimeDescColumn:

    # create the file to add output to for the crime description
    fileDesc = desc.replace("/", " (and or) ")
    fileName = ("./crimes/" + fileDesc + ".txt").replace("&"," and ").replace("$"," dollar ")
    file = open(fileName, "w")

    # write the name of the crime to the file and print to get status
    file.write(desc + "\n")
    print(desc)
    
    # set up the counters of crime cds
    allCD = {"Crm Cd" : {}, "Crm Cd 1" : {}, "Crm Cd 2" : {}, "Crm Cd 3" : {}, "Crm Cd 4" : {}}
    
    # loop through the rows of the dataframe that has the crime description
    rowsWithCrimeDesc = dataframe.loc[dataframe["Crm Cd Desc"] == desc]
    for i, row in rowsWithCrimeDesc.iterrows():

        # loop through all of the columns we want
        for c in crimeDescRows:
            # get the cd value
            cd = row[c]

            # cd is valid
            if not numpy.isnan(cd):

                # in the list, incriment
                if cd in allCD[c]:
                    allCD[c][cd] += 1

                # not in the list, add to list
                else:
                    allCD[c][cd] = 1

    # loop through all of the crime code data
    totals = {}
    for c in allCD.keys():

        # write the crime code
        file.write(c + ':\t')

        # get all of the crime cd column info about the crime code
        for id, count in allCD[c].items():

            nid = int(id)
            
            # found, increase the count
            if nid in totals:
                totals[nid] += count

            # not found, set the count
            else:
                totals[nid] = count

            # write the count info to the file
            file.write(str(nid) + ": " + str(count) + ',  ')

        file.write("\n")

    # Write the totals for every code
    sorted_totals = sorted_d = dict( sorted(totals.items(), key=operator.itemgetter(1),reverse=True))

    file.write("\nTOTALS\n\n")
    for id, count in sorted_totals.items():
        file.write(str(id) + ": " + str(count) + "\n")

