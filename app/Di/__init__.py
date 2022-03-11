from app.Exceptions import NotRegisteredServiceException, DuplicatedServiceException


class SimplyDi:
    _services = {}

    def registry_service(self, service_name: str, service_obj):
        if service_name in self._services:
            raise DuplicatedServiceException("Duplicate service: {}".format(service_name))

        self._services[service_name] = service_obj
        pass

    def get_service(self, service_name):
        if service_name in self._services:
            return self._services[service_name]
        else:
            raise NotRegisteredServiceException("Unable find service {}".format(service_name))

    pass
