class SimplyDi:
    _services = {}

    def registry_service(self, service_name: str, service_obj):
        self._services[service_name] = service_obj
        pass

    def get_service(self, service_name):
        return self._services[service_name]

    pass
