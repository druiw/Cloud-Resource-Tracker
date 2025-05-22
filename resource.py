import uuid
from datetime import datetime

class Resource:
    def __init(self, name, rtype):
        self.id = str(uuid.uuid4())
        self.name = name
        self.type = rtype
        self.status = "running"
        self.created_at = datetime.now().isoformat()

    # Function to map resource value
    def to_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "rtype": self.type,
            "status": self.status,
            "created_at": self.created_at
        }