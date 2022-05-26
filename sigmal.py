#import mysql.connector    
from datetime import date, datetime, timedelta
import sys

def buildQuery(signature, name):
    print('building query..')
    qstring = "INSERT INTO signatures "
    qstring += "(id, offsets, data) "
    qstring += "VALUES ("
    qstring += "'" + name + "' "
    qstring += "'" + str(signature[0]) + "' "
    qstring += "'" + signature[1] + "') "
    
    return qstring

def generateOffsets():
    return (631,2231,5123)

def readAtOffsets(path, offsets):
    byts = []

    f = open(path, 'rb')
    content = f.read()

    for offset in offsets:
        f.seek(offset)
        r = f.read(1)
        byts.append(r)
        print('read byte {} at offset {}'.format(r.hex(), offset))

    f.close()

    
def registerMalware(query):
    #add_employee = ("INSERT INTO signatures "
     #          "(id, offsets, data) "
      #         "VALUES ('TrojanVir', '15,26,37', '08,e8,e2')")

    print('registering malware signature in database..')
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
    print('analyzing file at {}..'.format(file_path))
    offset_list = generateOffsets()
    offset_data = readAtOffsets(file_path, offset_list)
    signatureList = list()
    signatureList.append(offset_list)
    signatureList.append(offset_data)
    print('returning signatures..')
    return signatureList
    
if __name__ == '__main__':
    if len(sys.argv) != 2 :
        print('missing filename - exiting')
        sys.exit(-1)

    file_path = sys.argv[1]
    signature = analyze(file_path)
    #query = buildQuery(signature, 'test')
    #registerMalware(query)
