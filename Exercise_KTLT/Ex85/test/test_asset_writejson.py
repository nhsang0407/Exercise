#write data into Json:
from Exercise_KTLT.Ex85.libs.JsonFileFactory import JsonFileFactory
from Exercise_KTLT.Ex85.models.asset import Asset

assets=[]
assets.append(Asset("A1","Led Monitor",2019,200))
assets.append(Asset("A2","Laptop 1",2015,10))
assets.append(Asset("A3","Projector 1",208,8))
assets.append(Asset("A4","Laptop 2",2010,11))
assets.append(Asset("A5","Car 1",2017,700))
print("List of Assets:")
for a in assets:
    print(a)

filename="assets.json"
path=f"../dataset/{filename}"
jff=JsonFileFactory()
jff.write_data(assets,path)