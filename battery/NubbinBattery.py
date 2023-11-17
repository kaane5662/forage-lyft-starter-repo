from Battery import Battery

class NubbinBattey(Battery):
    def __init__(self, current_date, last_service_date):
        # super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_date - self.last_service_date > 4