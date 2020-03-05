import arrow
from pathlib import Path

iso_fmt_file = "YYYY-MM-DDTHH-mm-ssZ"

def uniquePath(path, tz=None, prefix=True, dateformat=iso_fmt_file):
    now = arrow.now()
    path = Path(path)

    if tz is not None:
        now = now.to(tz)

    iso_str = now.format(dateformat)
    add_str = ""
    already_exists = True
    add_num = 0
    base_dir = path.parent
    extension = path.suffix
    stem = path.stem

    while already_exists:
        if prefix:
            new_filename = "{0}_{1}{2}{3}".format(iso_str, stem, add_str,
                                                  extension)
        else:
            new_filename = "{0}_{1}{2}{3}".format(stem, iso_str, add_str,
                                                  extension)

        new_path = base_dir / new_filename

        already_exists = new_path.exists()

        if already_exists:
            add_num += 1
            add_str = "_" + str(add_num)

    return new_path

__all__ = (uniquePath.__name__, "iso_fmt_file")
