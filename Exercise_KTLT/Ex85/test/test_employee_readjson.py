from Exercise_KTLT.Ex85.libs.JsonFileFactory import JsonFileFactory
from Exercise_KTLT.Ex85.models.employee import Employee

filename="employees.json"
path=f"../dataset/{filename}"
jff=JsonFileFactory()
employees=jff.read_data(path,Employee)
print("list employee after readjson")
for e in employees:
    print(e)