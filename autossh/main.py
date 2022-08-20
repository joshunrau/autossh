import argparse
import shutil

from pathlib import Path

from .servers import SERVERS


def check_sshpass_installed():
    if shutil.which("sshpass") is None:
        raise RuntimeError("Cannot find sshpass in path, make sure it is installed on system.")


def parse_args():
    parser = argparse.ArgumentParser(prog="autossh")
    parser.add_argument('server', choices=SERVERS.keys())
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('-l', action='store_true')
    mode.add_argument('-d', type=Path, metavar='FILE_TO_DOWNLOAD')
    mode.add_argument('-u', type=Path, nargs=2, metavar=('FILE_TO_UPLOAD', 'UPLOAD_DIR'))
    return parser.parse_args()


def main():
    check_sshpass_installed()
    args = parse_args()

    server = SERVERS[args.server]()

    if args.l:
        server.login()
    elif args.d:
        server.download(args.d)
    elif args.u:
        server.upload(args.u[0], args.u[1])
