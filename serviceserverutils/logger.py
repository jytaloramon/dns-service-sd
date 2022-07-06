from typing import Dict, List, Tuple


class LoggerService:

    def __init__(self) -> None:

        self._data: Dict[int, List[Tuple[str, any]]] = {}

    def push_event(self, k: int, e_name: str, e_data: any) -> None:

        d = self._data.get(k)

        if d is None:
            self._data[k] = []
            d = self._data[k]

        d.append((e_name, e_data))

    def pop_show_event(self, k: int) -> None:

        events = self._data.get(k)

        if events is None:
            return

        self._data.pop(k)

        print(f'Event {k}:')

        for e in events:
            print(f' - {e[0]} => {e[1]}')

        print('\n')
