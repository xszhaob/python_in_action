from urllib.request import urlopen
from io import StringIO
import csv

url = "http://pythonscraping.com/files/MontyPythonAlbums.csv"

data = urlopen(url).read().decode('ascii', 'ignore')
data_file = StringIO(data)
csv_reader = csv.reader(data_file)

# for row in csv_reader:
# 	print(row[0] + '---------->' + row[1])

csv_reader = csv.DictReader(data_file)

print(csv_reader.fieldnames)

for reader in csv_reader:
	print(reader['Name'] + '--->' + reader['Year'])