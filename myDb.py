import sys
# �������� ���� ������ ��� �������
sys.path.append('./classes/import')
sys.path.append('./classes/commands')

# ���������� ������
from importData import ImportData
from command import Command

# ����������� ������ �� �����
i = ImportData('./data/input/testDb.txt')
i.importFromTxt()

# ������� ������ ��� ��������� ������
cmd = Command(i.getDbs())

# �������
req = {
    "command" : "find",
    "table" : "sales"
    
}
# ��������� �������
cmd.doCommand(req)

req = {
    "command" : "remove",
    "table" : "sales",
    "condition" : {
        "=" : ['city', 'London']  
    }
    
}
cmd.doCommand(req)

print()
req = {
    "command" : "find",
    "table" : "sales"
    
}
# ��������� �������
cmd.doCommand(req)

req = {
     "command" : "insert",
     "table" : "sales",
     "values" : { 'snum' : 1008,
                   'city' : 'Kiyv',
                'sname' : "John"
                 }
}

cmd.doCommand(req)
print()
req = {
    "command" : "find",
    "table" : "sales"
    
}
# ��������� �������
cmd.doCommand(req)