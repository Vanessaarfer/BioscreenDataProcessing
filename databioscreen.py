# importing pandas as pd
import pandas as pd

#stablish directory path with files and save it in a variable
path = 'YOUR PATH'


# EXTRACT THE BASENAME OF EACH FILE 

#to look for files with certain pattern if you have a directory with other files with same extension
#it depends on your files name ex. (220702_Temp30.xlsx)
name = glob.glob(path + '*' + 'Temp' + '*' + '.xlsx')
#to get the name of each temperature file without the extension
dfnames = []
for x in name:
    n = re.findall('Temp\d\d', x)
    dfnames.append(n)
dfnames= list(numpy.concatenate(dfnames).flat)
#print(dfnames) #to be check that 'dfnames' variable is generated
#To get the path from each file 
path_files = glob.glob(path + '*' + 'Temp' + '*' + '.xlsx')
#print(path_files)
d = 0
datas = [] #empty list
#convert from xlsx to csv 
for n in dfnames:
    for p in path_files:
        f = pd.read_excel(p)
        f.to_csv (n + '.csv', 
                  index = None,
                  header= None)
    #print('This csv are created', n)
    datas.append(f) #save df's in a list
    
  #TO MODIFY OUTPUT FILE THAT BIOSCREEN GIVE US 
  #have 2 rows with no info and python read certain columns with wrong data type
  
 # we have to convert the row we wanto to column header by index
    datas[d]=datas[d].rename(columns=datas[d].iloc[1])
    #print(datas[d].head(2))
    #print(datas[d].head(0)) #just to check the output, 'head' to see the first lines in our data
    #Python count start in 0, so 0 is to indicate the first row
    #Delete first row by index 'cause it's repetitive with the header
    datas[d]=datas[d].drop(datas[d].index[[0,1]])
    print(datas[d].head(1))
    d = d+1 
    #print(datas[d].dtypes)# To check the daya types that we have in each column
#To change DataTypes in certain columns
d=0
str_values = ['Time' , 'Blank']
for data in datas:
    #To convert 'Time' and 'Blank' data to Integer 
    data['Time'] = data['Time'].astype(str).astype(float).astype(int) 
    data['Blank'] = data['Blank'].astype(str).astype(float).astype(int) 
#Now we have in our header numeric values and str values
    float_values = data.columns[~data.columns.isin(str_values)] # create a variable without str values
    float_values = float_values.astype(float).astype(int)#convert numeric values to float

#Create a loop to add str values with numeric values
    for x in float_values:
        str_values.append(x)
   # print(str_values)
    #Change column names with this new values corrected
    datas[d].columns=str_values
    print('data generated', datas[d].head())
    d = d+1 
d=0   
for data in datas:
    for n in dfnames:
        datas[d].to_csv('YOUR PATH' + n + '.csv',
                        index=False)
d = d+1      


