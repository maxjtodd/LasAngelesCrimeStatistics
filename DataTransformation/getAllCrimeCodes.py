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

# open the file to write the data to
file = open("./crimeCDcorrelation.txt", "w")

# loop through all of the unique crimes
for desc in crimeDescColumn:

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

    # add the info to the file
    totals = {}
    for c in allCD.keys():

        for id, count in allCD[c].items():

            nid = int(id)
            
            if nid in totals:
                totals[nid] += count

            else:
                totals[nid] = count


    sorted_totals = sorted_d = dict( sorted(totals.items(), key=operator.itemgetter(1),reverse=True))

    # firstList = totals.keys()
    # print(type(firstList))
    # first = firstList[0]
    first = next(iter(totals))


    file.write(desc + "  :  " + str(first))
    file.write("\n")

