from typing import List, Dict, Any, Callable
import datetime

class Event:
    def __init__(self, name: str, payload: Dict[str, Any]):
        self.name = name
        self.payload = payload
        self.timestamp = datetime.datetime.now().isoformat()

class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}
        self.log: List[Event] = []

    def subscribe(self, event_name: str, callback: Callable):
        if event_name not in self.subscribers:
            self.subscribers[event_name] = []
        self.subscribers[event_name].append(callback)
        
    def dispatch(self, event: Event):
        self.log.append(event)
        print(f"[EventBus] Dispatched: {event.name}")
        callbacks = self.subscribers.get(event.name, [])
        for cb in callbacks:
            cb(event)
