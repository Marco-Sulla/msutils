import os
import errno
import shutil

def mkdirP(path, *args, **kwargs):
    path_real = str(path)
    kwargs.setdefault("mode", 0o700)
    
    try:
        os.makedirs(path_real, *args, **kwargs)
    except OSError as e:
        if not (e.errno == errno.EEXIST and os.path.isdir(path_real)):
            raise


def rmFile(path):
    try:
        try:
            os.remove(path)
        except TypeError:
            os.remove(str(path))
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise


def _singleOverwrite(path):
    filename = os.path.basename(path)
    dest_path = os.path.join(dest_dir, filename)

    mkdirP(dest_dir)
    rmFile(dest_path)
    shutil.move(path, dest_dir)

def overwrite(paths, dest_dir):
    if isinstance(paths, Iterable):
        for path in paths:
            _singleOverwrite(path)
    else:
        path = paths
        _singleOverwrite(path)

def tail(filepath):
    """
    @author Marco Sulla (marcosullaroma@gmail.com)
    @date May 31, 2016
    """

    try:
        filepath.is_file
        fp = str(filepath)
    except AttributeError:
        fp = filepath

    with open(fp, "rb") as f:
        size = os.stat(fp).st_size
        start_pos = 0 if size - 1 < 0 else size - 1

        if start_pos != 0:
            f.seek(start_pos)
            char = f.read(1)

            if char == b"\n":
                start_pos -= 1
                f.seek(start_pos)

            if start_pos == 0:
                f.seek(start_pos)
            else:
                char = ""

                for pos in range(start_pos, -1, -1):
                    f.seek(pos)

                    char = f.read(1)

                    if char == b"\n":
                        break

        return f.readline()

__all__ = (mkdirP.__name__, rmFile.__name__, overwrite.__name__, tail.__name__)
