from Exercise_KTLT.Ex85.libs.JsonFileFactory import JsonFileFactory
from Exercise_KTLT.Ex85.models.asset import Asset

filename="assets.json"
path=f"../dataset/{filename}"
jff=JsonFileFactory()
assets=jff.read_data(path,Asset)
print("list asset after readjson:")
for a in assets:
    print(a)