from Exercise_KTLT.Ex85.libs.JsonFileFactory import JsonFileFactory
from Exercise_KTLT.Ex85.models.employee_asset import Employee_Asset

employee_assets=[]
employee_assets.append(Employee_Asset("E1","AS1","MAIN"))
employee_assets.append(Employee_Asset("E2","AS2","MAIN"))
employee_assets.append(Employee_Asset("E3","AS3","MAIN"))
employee_assets.append(Employee_Asset("E4","AS4","MAIN"))
employee_assets.append(Employee_Asset("E5","AS2","MAIN"))
employee_assets.append(Employee_Asset("E2","AS3","MAIN"))
employee_assets.append(Employee_Asset("E4","AS5","MAIN"))
print("List Employee_Asset:")
for ea in employee_assets:
    print(ea)
#write data into Json:
filename="employee_assets.json"
path=f"../dataset/{filename}"
jff=JsonFileFactory()
jff.write_data(employee_assets,path)