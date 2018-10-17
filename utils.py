import hashlib


def _hash_from_dict(o):
    sha1 = hashlib.sha1()

    def _update(v):
        if isinstance(v, str):
            sha1.update(v.encode())
        elif isinstance(v, (int, float)):
            _update(str(v))
        elif isinstance(v, (tuple, list)):
            for e in v:
                _update(e)
        elif isinstance(v, dict):
            keys = v.keys()
            for k in sorted(keys):
                _update(k)
                _update(v[k])

    _update(o)
    return sha1.hexdigest()


def try_or(fn, default):
    try:
        return fn()
    except:
        return default
