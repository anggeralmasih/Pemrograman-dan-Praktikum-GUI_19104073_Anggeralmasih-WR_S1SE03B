from PyQt5.QtSql import *

def connectdb():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('testdb')
    if db.open():
        print('Koneksi telah dibuat')
        query = QSqlQuery()

        #Create table
        sql = '''Create Table phonebook(
            id integer not null primary key,
            nama varchar(25),
            nohp varchar(15)
            )'''
        query.exec_(sql)
        if(query.exec_):
            print('Berhasil Create Tabel')
        else:
            print('ERROR: ' + db.lastError().text())

connectdb()
