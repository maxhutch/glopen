import globussh as gl
from tempfile import mkstemp, mkdtemp
from os.path import basename, join
from os import fdopen, unlink
from contextlib import contextmanager
from os.path import expanduser
import json

config_file = join(expanduser("~"), ".glopen")
try:
    with open(config_file, "r") as f:
        config = json.load(f)
except:
    raise RuntimeError("Missing '~/.glopen' config file")
  
tdir = mkdtemp(prefix=config["tempdir"])

@contextmanager
def glopen(filename, mode='rb', endpoint = None):
    fo, fn = mkstemp(dir=tdir) 
    if mode == 'rb' or mode == 'r':
        transfer = "{:s}/{:s} {:s}/{:s}".format(endpoint, filename, config["local_endpoint"], fn)
        gl.transfer_sync(transfer, "glopen_read")
    f = fdopen(fo, mode)
    yield f
    f.close()
    if mode == 'wb' or mode == 'w':
        transfer = "{:s}/{:s} {:s}/{:s}".format(config["local_endpoint"], fn, endpoint, filename)
        gl.transfer_sync(transfer, "glopen_write")
    unlink(fn)
