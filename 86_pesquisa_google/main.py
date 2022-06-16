# pip install google
from googlesearch import search

query = "python academy"

for _ in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(_)
