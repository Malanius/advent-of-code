from dataclasses import dataclass, field


@dataclass
class LensBox:
    id: int
    lenses: dict[str, int] = field(default_factory=dict)

    @property
    def focusing_power(self) -> int:
        lens_power = 0
        for posistion, focal_lenght in enumerate(self.lenses.values(), start=1):
            lens_power += (1 + self.id) * posistion * focal_lenght
        return lens_power

    @property
    def is_empty(self) -> bool:
        return len(self.lenses) == 0

    def add_lens(self, lens_type: str, focal_lenght: int) -> None:
        self.lenses[lens_type] = focal_lenght

    def remove_lens(self, lens_type: str) -> None:
        self.lenses.pop(lens_type, None)

    def __str__(self) -> str:
        return f"Box {self.id}: {self.lenses}"
