from typing import Protocol


class StorageProtocol(Protocol):
    def save(self) -> None: ...
    def load(self) -> None: ...

