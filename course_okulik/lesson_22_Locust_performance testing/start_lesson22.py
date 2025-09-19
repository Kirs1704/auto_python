import requests
from datetime import datetime

start = datetime.now()

response = requests.get('')
print(response)
end = datetime.now()
result = end - start
print(result)