from typing import Any
from datetime import datetime
import time

class Item:
    def __init__(self, value: str, lifetime: datetime):
        self.value = value
        self.lifetime = lifetime

class MemoryStorage:

    storage: dict[str, Item]

    def __init__(self):
        self.storage = {}

    def set(self, key, value, lifetime: datetime = None):
        self.storage[key] = Item(value, lifetime) 
    
    def get(self, key):
        item = self.storage.get(key)
        if item:
            if item.lifetime and self.expired(key, item.lifetime):
                del self.storage[key]
                return None
            return item.value
        return None
        
    def delete(self, key):
        if key in self.storage:
            del self.storage[key]
            return 1
        return 0
    
    def expired(self, key, item_lifetime: Item):
        if item_lifetime < datetime.now():
            self.set(key, None)
            return True
        return False
    

    def exists(self, key):
        return key in self.storage
    
    def keys(self):
        return self.storage.keys()
    
    def flush(self):
        self.storage.clear()
    