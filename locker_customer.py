from customer import Customer


class LockerCustomer(Customer):

    def __new__(cls, location, locker, package_demand=1):
        obj = object.__new__(cls)
        return obj

    def __init__(self, location, store, package_demand=1):
        super().__init__(location, package_demand)
        self.store = store

    def __repr__(self):
        return "{index: " + str(self.index) + ", location: " + str(self.location) + ", store: " + str(self.store) +\
               "}"
