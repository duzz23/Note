from uuid import UUID

class HasID:
    id: UUID

class Base(HasID):
    def __init__(self, id: UUID):
        self._id: UUID = id if isinstance(id, UUID) else UUID(id)

    @property
    def id(self) -> UUID:
        return self._id

