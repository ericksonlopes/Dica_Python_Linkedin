# pip install watchfiles

"""
Se você quiser refazer automaticamente um processo quando um arquivo for alterado
"""

from watchfiles import run_process


def warn(a):
    print('Warning: This is a warning' + a)


if __name__ == '__main__':
    print('Starting')
    run_process('main.py', target=warn, args=('test',))
