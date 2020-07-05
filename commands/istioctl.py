from systems.commands.index import Command
from utility.temp import temp_dir


class Istioctl(Command('istioctl')):

    def exec(self):
        with temp_dir() as temp:
            self.kube_exec(temp, 'istioctl')
