# Library regex 
# Day 4 practice

import re

texto = "IDs: A12 B777 C9"
texto1 = "abc123xyz456"
texto2 = "hola   adios"
texto3 = "Mi número es 912345678"
texto4 = "Correos: ana@gmail.com, pepe_luis@hotmail.com, juan.carlos123@hotmail.com"
texto5 = "IPs: 192.168.1.1 y 10.0.0.25"
texto6 = """
ERROR 404
INFO 200
ERROR 500
"""


print(re.findall(r"\d+", texto))
print(re.findall(r"\d", texto1))
print(re.findall(r"\s", texto2))
print(re.findall(r"\d+", texto3))
print(re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", texto4))
print(re.findall(r"\d+\.\d+\.\d+\.\d+", texto5))
print(re.findall(r"ERROR\s\d+", texto6))

# log file data
log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 192.168.190.178 \narutley 2022-05-12 17:00:59 1923.1689.3.24 \nrjensen 2022-05-11 0:59:26 192.168.213.128 \naestrada 2022-05-09 19:28:12 1924.1680.27.57 \nasundara 2022-05-11 18:38:07 192.168.96.200 \ndkot 2022-05-12 10:52:00 1921.168.1283.75 \nabernard 2022-05-12 23:38:46 19245.168.2345.49 \ncjackson 2022-05-12 19:36:42 192.168.247.153 \njclark 2022-05-10 10:48:02 192.168.174.117 \nalevitsk 2022-05-08 12:09:10 192.16874.1390.176 \njrafael 2022-05-10 22:40:01 192.168.148.115 \nyappiah 2022-05-12 10:37:22 192.168.103.10654 \ndaquino 2022-05-08 7:02:35 192.168.168.144"

pattern = "\d+\.\d+\.\d+\.\d+"

valid_ip_addresses = re.findall(pattern, log_file)

for i in valid_ip_addresses:
    print(i)
