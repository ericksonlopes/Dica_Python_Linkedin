import socket
import sys
from geolite2 import geolite2

host = ' '.join(sys.argv[1:])

ip = socket.gethostbyname(host)

reader = geolite2.reader()


def get_ip_location(ip):
    location = reader.get(ip)

    try:
        country = location["country"]["names"]["en"]
    except:
        country = "Unknown"

    try:
        subdivision = location["subdivisions"][0]["names"]["en"]
    except:
        subdivision = "Unknown"

    try:
        city = location["city"]["names"]["en"]
    except:
        city = "Unknown"

    return country, subdivision, city


country, sub, city = get_ip_location(ip=ip)

print(country)
print(sub)
print(city)
