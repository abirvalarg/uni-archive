class Archiver:
    def append_data(self, data: bytes):
        raise NotImplemented()

    def dump(self) -> bytes:
        raise NotImplemented()
