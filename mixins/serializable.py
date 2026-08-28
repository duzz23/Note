from typing import ClassVar, Any, Self, TYPE_CHECKING


class Serializable:
    serializable_fields: ClassVar[tuple[str, ...]] = ()

    if TYPE_CHECKING:
        def __init__(self, *args, **kwargs): ...
    """Кастомная серелизация и десериализация"""

    # сереалтзаьтор по имени поля
    def _serialize_field(self, field_name: str) -> Any:
        if serialize := getattr(self, f"serialize_{field_name}", None):
            return serialize()
        return getattr(self, field_name, None)

    # Пройдет по всем полям и сложит в date виде словаря
    def to_dict(self) -> dict[str, Any]:
        data = {}
        for field in self.serializable_fields:
            data[field] = self._serialize_field(field)
        return data

    # десереальзатор по имени поля
    @classmethod
    def _deserialize_field(cls, field_name: str, value: Any) -> Any:
        if deserialize := getattr(cls, f"deserialize_{field_name}", None):
            return deserialize(value)
        return value

    # Вытаскиваем из словаря данные
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        for field, value in data.items():
            data[field] = cls._deserialize_field(field, value)
        return cls(**data)
