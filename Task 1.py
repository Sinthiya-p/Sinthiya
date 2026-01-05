import pandas as pd
a = [5,10,15,20]
s = pd.Series(a)
print(s)
s = pd.Series(a,index=['w','x','y','z'])
print(s)
Mame={'Name':['Ravi','Kiran','Meena'],'Age':[22,25,28],'City':['Chennai','Bangalore','Hyderabad']}
Th=pd.DataFrame(Mame)
print(Th)
print(Th['Name'])
print(Th[['Name','City']])
print(Th.loc[1])
print(Th.iloc[1])
print(Th[0:2])
print(Th[Th['Age']>23])
Th['Salary'] = [30000,40000,50000]
print(Th)
Th['Age'] = Th['Age']+1
print(Th)
Th.loc[Th['Name'] == 'Kiran','Age']+=1
print(Th)
