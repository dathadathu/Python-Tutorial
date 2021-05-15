#dictionay is a key:pair values
#it should be immutable
#it shoud be unique
data = {1:'Datha', 2:'Ram', 4:'Achu'}

data[4]

data[1]

data.get(3)
print(data.get(3))

data.get(1,'Not Found')

data.get(3,'Not Found')

keys = ['Don','Marvel','Shannu']
values = ['Python','Java','C']

data = dict(zip(keys,values))

data['Prasuu'] = 'C#'

del data['Shannu']

prog = {'JS':'Atom','C#':'Visual Studio','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}

prog['Python'][1]

prog['Java']['JSE']