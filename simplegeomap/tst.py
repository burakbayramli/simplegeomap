import zipfile, csv, io

def find_city(name,country):
    zip_file    = zipfile.ZipFile('cities.zip')
    items_file  = zip_file.open('cities.csv')
    items_file  = io.TextIOWrapper(items_file)
    rd = csv.reader(items_file)
    headers = {k: v for v, k in enumerate(next(rd))}
    res = []
    for row in rd:
        if name in row[headers['name']].lower() and \
           country==row[headers['country_name']].lower(): res.append(row)

    return res

res = find_city('lyman','ukraine')
print (res)
