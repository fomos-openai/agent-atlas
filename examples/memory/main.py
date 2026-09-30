from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Memory:
    subject: str
    fact: str
    source: str
    confidence: float
    expires: date


class MemoryStore:
    def __init__(self) -> None:
        self._items: list[Memory] = []

    def remember(self, item: Memory) -> None:
        if not item.source or item.confidence < 0.8:
            raise ValueError("长期记忆需要可信来源与至少 0.8 置信度")
        self._items.append(item)

    def recall(self, subject: str, today: date) -> list[Memory]:
        return [item for item in self._items if item.subject == subject and item.expires >= today]


if __name__ == "__main__":
    store = MemoryStore()
    store.remember(Memory("project", "cutoff=2026-09-30", "README", 1.0, date(2027, 9, 30)))
    print(store.recall("project", date(2026, 9, 30)))
