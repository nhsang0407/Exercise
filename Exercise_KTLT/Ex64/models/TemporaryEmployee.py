from Exercise_KTLT.Ex64.models.Employee import Employee


class TemporaryEmployee(Employee):
    def __init__(self, id=None, idcard=None, name=None, birthday=None,workingday=0):
        super().__init__(id,idcard,name,birthday)
        self.workingday=workingday
    def cal_salary(self):
        return self.workingday*300000