VERSION = ('0', '0', '6dev')

def get_version(*args, **kwargs):
    return '.'.join(VERSION)

__version__ = get_version()
