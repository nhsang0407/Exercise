from Exercise_KTLT.Ex85.libs.JsonFileFactory import JsonFileFactory
from Exercise_KTLT.Ex85.models.employee import Employee


class DataConnector:
    def load_all_employees(self):
        filename = "employees.json"
        path = f"../dataset/{filename}"
        jff = JsonFileFactory()
        employees = jff.read_data(path, Employee)
        return employees
    def login(self,username,password):
        employees=self.load_all_employees()
        for emp in employees:
            if emp.UserName==username and emp.Password==password:
                return emp
        return None