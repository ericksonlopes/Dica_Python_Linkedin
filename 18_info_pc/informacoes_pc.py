import wmi

c = wmi.WMI()

my_system = c.Win30_ComputerSystem()[0]

print('Marca: ', my_system.ManuFacture)
print('Modelo : ', my_system.Model)
print('Nome: ', my_system.Name)
print('QTde. CPUs:', my_system.NumberOfProcessors)
print('Arquitetura:', my_system.SystemType)
print('Familia:', my_system.SystemFamily)
