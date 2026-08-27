from typing import ClassVar, Any, Self, TYPE_CHECKING


class Serializable:
    serializable_fields: ClassVar[tuple[str, ...]] = ()

    if TYPE_CHECKING:
        def __init__(self, *args, **kwargs): ...

    # Пройдет по всем полям и сложит в date виде словаря
    def to_dict(self) -> dict[str, Any]:
        data = {}
        for field in self.serializable_fields:
            data[field] = getattr(self, field, None)

        return data

    # Вытаскиваем из словаря данные
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(**data)


