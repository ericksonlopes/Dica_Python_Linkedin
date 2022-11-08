from time import sleep


def progress(porcent=0, width=50):
    left = width * porcent // 100
    right = width - left

    print('\r[', '#' * left, ' ' * right, ']', f' {porcent}%', sep='', end='', flush=True)


for i in range(101):
    progress(i)
    sleep(0.1)

# [Output]
# [###############################                   ] 63%
