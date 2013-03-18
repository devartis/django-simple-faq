VERSION = ('0', '0', '4dev')

def get_version(*args, **kwargs):
    return '.'.join(VERSION)

__version__ = get_version()
