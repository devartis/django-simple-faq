VERSION = ('0', '0', '2dev')

def get_version(*args, **kwargs):
    return '.'.join(VERSION)

__version__ = get_version()
