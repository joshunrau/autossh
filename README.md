# AutoSSH

## About

This is a simple program I wrote to facilitate access to Compute Canada via sshpass. You can also extend it to an arbitrary number of servers of your choice (see advanced usage). I thought I’d put it up here in case it is useful to anyone else.

## Install

First, make sure sshpass is installed (for Mac, you will have to build it from [source](https://github.com/kevinburke/sshpass)). Then, you can download and install this package:

    git clone https://github.com/joshunrau/autossh.git
    pip install autossh/
    rm -rf autossh

## Usage

For this app to work, the following enviroment variables must be defined: 

    export COMPUTE_CANADA_USERNAME=FOO
    export COMPUTE_CANADA_PASSWORD=FOO

Then, you can use the command-line interface:

    usage: autossh [-h] (-l | -d FILE_TO_DOWNLOAD | -u FILE_TO_UPLOAD UPLOAD_DIR) {beluga,narval,cic}

    positional arguments:
      {beluga,narval}

    options:
      -h, --help            show this help message and exit
      -l
      -d FILE_TO_DOWNLOAD
      -u FILE_TO_UPLOAD UPLOAD_DIR

## Advanced Usage

It is very easy to add additional servers to the program. For example, if the following environment variables are defined: 

    export SERVER_USERNAME=FOO
    export SERVER_PASSWORD=FOO

In servers.py, simply define a new class inheriting from BaseServer and implement the abstract properties “name” and “url”, corresponding to the prefix of the associated environment variables and endpoint respectively. Then, add it to the dictionary of servers available.

    class ServerAtMyWorkplace(BaseServer):
        name = 'SERVER'
        url = 'subdomain.server.com'
    
    SERVERS = {
        'beluga': BelugaServer,
        'narval': NarvalServer,
        'work': ServerAtMyWorkplace
    }

Finally, reinstall the package:

    pip install .
