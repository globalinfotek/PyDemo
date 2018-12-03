import os
import socket


class ApplicationDetails:
    def __init__(self):
        self._name = 'demo-python-source'
        self._host_name = socket.gethostname()
        self._version = os.environ.get('SERVICE_VERSION', '?')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def host_name(self):
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        self._host_name = host_name

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version
