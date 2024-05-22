import pandas as pd

class Store:
    def __init__(self, emps, slots) -> None:
        self.emps = emps
        self.slots = slots

class Employee:
    def __init__(self) -> None:
        pass

employees = pd.read_excel('employees.xlsx')
# position = positions['sandwiches'][0]
# positions['sandwiches'][0]=False
# print(positions)
# positions.to_excel('positions.xlsx', index=False)