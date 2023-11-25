# Los Angelas Crime

## Data Set Used
The dataset used for this project is [Crime Data from 2020 to Present](https://datasetsearch.research.google.com/search?src=3&query=crime&docid=L2cvMTFsa3ZiajZjcg%3D%3D)

The dataset (not included in this repo) can be downloaded from the link above.

## Data Mining Task

We wanted to determine when, where, and who is at the highest risk for 
crime in Los Angeles. 

First, I was able to determine what crime CDs correlated to which crimes. 
This was done by data modification, which can be seen in the DataTransformation directory, where the results are also stored. 
The /DataTransformation/crimeCDcorrelation.txt contains the most likely results of each crime cd -> crime correlations, however there is marginal room
for error. These error points can be seen in the /DataTransformation/crimes directory, where every count of the given crime is stored.

Then, models were applied until high accuracy models were obtained. 
Association was ran in a seperate file (association.ipynb), while RFC and NB were rain in max.ipynb. 

## Results

Association didn't yield very strong results, leading to the use of the NB model. This yields a result of 83% model accuracy, with a train-test split of 80-20.