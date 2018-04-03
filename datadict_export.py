import pandas as pd 

df = pd.read_csv('./data/sog2_datadict.csv')
    #print('Loading data from '%sys.argv[0])
df.describe()
ndf = df.drop_duplicates(['object_name', 'field_name'])
    #print('Removing dupplicated column')
    
ndf.to_csv('./data/sog2_datadict.csv')
ndf.describe()
print('dictionary export end')