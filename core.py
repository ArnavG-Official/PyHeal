class _SkipContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc:
            print(f"[pyheal] Ignored error: {exc}")
            return True
        return False


class _StrictContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


def skip():
    return _SkipContext()


def strict():
    return _StrictContext()
