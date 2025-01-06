from Exercise_KTLT.Ex31.function_ex31 import extract_url

url = input("Enter: ") #http://www.mywebsite.com/apparel/skirt.php?sku=123&lang=en&sect=silk
result = extract_url(url)
for key, value in result.items():
    print(f"{key}: {value}")
