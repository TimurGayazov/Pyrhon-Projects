import subprocess
import wmi

# Запустить команду WMIC и сохранить результат в переменную output
output = subprocess.check_output("wmic bios get smbiosbiosversion", shell=True)

# Разбить вывод на строки и сохранить первую строку (версию BIOS)
bios_version = output.decode().split('\n')[1].strip()

print("Версия BIOS:", bios_version)

# Создать объект WMI для работы с системными данными
c = wmi.WMI()

# Получить объект класса Win32_ComputerSystem, содержащий информацию о системе
system = c.Win32_ComputerSystem()[0]

# Получить модель компьютера из свойства Model
model = system.Model

print("Модель компьютера:", model)
