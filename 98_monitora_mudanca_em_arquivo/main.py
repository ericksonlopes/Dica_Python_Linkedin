# pip install watchfiles
from watchfiles import run_process


def warn(a, b, c=None):
    print(f'Warning: {a} {b} {c}')


if __name__ == '__main__':
    print('Starting')
    run_process('teste.txt', target=warn, args=(1, 2), kwargs={"c": "3"})

