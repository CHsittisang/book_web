from dataclasses import dataclass , field
from typing import Optional
from account import admin, customer

@dataclass
class System:
    admin: Optional[list] = field(default_factory=list)
    customer: Optional[list] = field(default_factory=list)

    def add_admin(self, admin):
        self.admin.append(admin)

    def add_customer(self, customer):
        self.customer.append(customer)

server = System(admin=[], customer=[])
admin1 = admin(id="admin", password="admin", name="admin", email="admin", phone="admin", permission="admin")
admin2 = admin(id="admin2", password="admin2", name="admin2", email="admin2", phone="admin2", permission="admin2")

server.add_admin(admin1)
server.add_admin(admin2)
print(server.admin)

