l = ["hallo", "welt", "wie", "geht", "es", "dir"]

sort_len = lambda v: (
    sorted(v, key=lambda x: len(x))
)

for _ in sort_len(l):
    print(_)
