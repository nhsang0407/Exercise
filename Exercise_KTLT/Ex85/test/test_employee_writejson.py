from Exercise_KTLT.Ex85.libs.JsonFileFactory import JsonFileFactory
from Exercise_KTLT.Ex85.models.employee import Employee

employees=[]
employees.append(Employee("E1","John","john","123"))
employees.append(Employee("E2","Tom","tom","456"))
employees.append(Employee("E3","Peter","peter","789"))
employees.append(Employee("E4","Bean","bean","bean1"))
employees.append(Employee("E5","Cafe","cafe","1134"))
print("List Employees: ")
for e in employees:
    print(e)
#write data into Json:
filename="employees.json"
path=f"../dataset/{filename}"
jff=JsonFileFactory()
jff.write_data(employees,path)