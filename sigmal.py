import mysql.connector    
from datetime import date, datetime, timedelta

def buildQuery(signature, name):
    print 'building query..'
    qstring = "INSERT INTO signatures "
    qstring += "(id, offsets, data) "
    qstring += "VALUES ("
    qstring += "'" + name + "' "
    qstring += "'" + str(signature[0]) + "' "
    qstring += "'" + signature[1] + "') "
    
    return qstring
    
def readFile(path):
    return ''
def generateOffsets():
    return '0,1,3'

def readAtOffsets(fileText):
    return '43,13,2'
    
def registerMalware(query):
    #add_employee = ("INSERT INTO signatures "
     #          "(id, offsets, data) "
      #         "VALUES ('TrojanVir', '15,26,37', '08,e8,e2')")

    print 'registering malware signature in database..'
    cnx = mysql.connector.connect(user='root', password='killer4',
                              host='localhost',
                              database='malware')
    cursor = cnx.cursor()

    # execute command against databse
    cursor.execute(query)

    # flush to make sure changes were sent
    cnx.commit()

    # close connection
    cnx.close()

def analyze(file_path):
    print 'analyzing file at' + file_path + '..'
    fileText = readFile(file_path)
    offset_list = generateOffsets()
    offset_data = readAtOffsets(fileText)
    signatureList = list()
    signatureList.append(offset_list)
    signatureList.append(offset_data)
    print 'returning signatures..'
    return signatureList
    
if __name__ == '__main__':
    signature = analyze('path')
    query = buildQuery(signature, 'test')
    #registerMalware(query)
