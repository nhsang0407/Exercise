from Exercise_KTLT.Ex85.libs.JsonFileFactory import JsonFileFactory
from Exercise_KTLT.Ex85.models.employee_asset import Employee_Asset

filename="employee_assets.json"
path=f"../dataset/{filename}"
jff=JsonFileFactory()
employee_assets=jff.read_data(path,Employee_Asset)
print("list employee-asset after readjson")
for ea in employee_assets:
    print(ea)