import os
import subprocess as sp

from abc import ABC, abstractmethod
from pathlib import Path


class BaseServer(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def url(self) -> str:
        pass
    
    @property
    def usr(self) -> str:
        username = os.environ.get(f'{self.name}_USERNAME')
        if username is None:
            raise RuntimeError(f"Environment variable '{self.name}_USERNAME' is not defined")
        return username

    @property
    def pwd(self) -> str:
        password = os.environ.get(f'{self.name}_PASSWORD')
        if password is None:
            raise RuntimeError(f"Environment variable '{self.name}_PASSWORD' is not defined")
        return password

    def login(self) -> None:
        sp.run(f"sshpass -p {self.pwd} ssh {self.usr}@{self.url}", shell=True)

    def download(self, file: Path, dl_dir: Path = Path.home().joinpath('Downloads')) -> None:
        sp.run(f"sshpass -p {self.pwd} rsync {self.usr}@{self.url}:{file} {dl_dir}", shell=True)

    def upload(self, file: Path, dl_dir: Path) -> None:
        sp.run(f"sshpass -p {self.pwd} rsync {file} {self.usr}@{self.url}:{dl_dir}", shell=True)


class ComputeCanadaServer(BaseServer):
    name = 'COMPUTE_CANADA'


class BelugaServer(ComputeCanadaServer):
    url = "beluga.computecanada.ca"


class NarvalServer(ComputeCanadaServer):
    url = "narval.computecanada.ca"


SERVERS = {
    'beluga': BelugaServer,
    'narval': NarvalServer,
}
