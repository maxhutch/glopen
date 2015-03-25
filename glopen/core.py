import globussh as gl
from tempfile import mkstemp, mkdtemp
from os.path import basename, join
from os import fdopen, unlink
from contextlib import contextmanager
from os.path import expanduser
from io import BufferedReader, TextIOWrapper
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
    if endpoint is None:
        f = open(filename, mode)
        yield f
        f.close()
    else:
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

@contextmanager
def glopen_many(filenames, mode='rb', endpoint = None):
    if endpoint is None:
        fs = []
        for fn in filenames:
          fs.append(open(fn, mode))
        yield fs
        for f in fs:
          f.close()
    else:
        temps = []
        for fn in filenames:
          ti, tn = mkstemp(dir=tdir) 
          temps.append((ti, tn))
        if mode == 'rb' or mode == 'r':
            transfer = ""
            for i in range(len(filenames)):
              transfer += "{:s}/{:s} {:s}/{:s}\n".format(endpoint, filenames[i], 
                                                      config["local_endpoint"], temps[i][1])
            gl.transfer_sync(transfer, "glopen_read")
        fs = []
        for i in range(len(filenames)):
          fs.append(fdopen(temps[i][0], mode))
        yield fs
        for f in fs:
          f.close()
        if mode == 'wb' or mode == 'w':
            transfer = ""
            for i in range(len(filenames)):
              transfer += "{:s}/{:s} {:s}/{:s}\n".format(config["local_endpoint"], temps[i][1],
                                                         endpoint, filenames[i]
                                                        )
            gl.transfer_sync(transfer, "glopen_write")
        for i in range(len(filenames)):
          unlink(temps[i][1])
