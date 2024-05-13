file_path = "C:\\Users\\Nicholas Armstrong\\Development\\POC_Sem2_Assignments\\10_Functional Programming\\03_File Handling\\assignment.py"

try:
    stream = open(file_path)
    stream.read('1')
    stream.read('2')
    stream.read('3')
    stream.read('4')
    stream.read('5')
    stream.read('6')
    stream.read('7')
    stream.read('8')
    stream.read('9')
    stream.read('10')
    print(stream.read())
    stream.close()
except:
    print(file_path)