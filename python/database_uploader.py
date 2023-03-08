import cx_Oracle
from os import listdir
from os.path import isfile, join

# dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL3')
# conn = cx_Oracle.connect(user=r'SYSTEM', password='Oracle123', dsn=dsn_tns)
# c = conn.cursor()
# c.execute('SELECT * FROM Puszki')


files = [f for f in listdir('../tekstWyniki/') if isfile(join('../tekstWyniki/', f))]
print(files)
# for f_name in files:
#     f = open(f'../tekstWyniki/')
# f = open("skladnikiWynik/demofile.txt", "r")
# print(f.read())
#
# for row in c:
#     print(row) # this only shows the first two columns. To add an additional column you'll need to add , '-',
#     # row[2], etc.
# c.execute("INSERT INTO Puszki (firma, kolor, smak, pojemnosc, kofeina, guarana, tauryna, sciezka) VALUES ('RedBull', 'zielony', "
#           "'zielony', 250, 0, 0, 0, 'img/puszki/Redbull/8.png')")
# conn.commit()
# conn.close()
