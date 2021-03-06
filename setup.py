#!/usr/bin/env python
# Copyright (c) 2007 Qtrac Ltd. All rights reserved.
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from setuptools import setup

setup(name='cronwrap3',
      version='1.1.0',
      author="Ed Henderson",
      # author_email="amix@amix.dk",
      author_email='ed@sharpertool.com',
      url="https://github.com/sharpertool/cronwrap3",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],

      install_requires=[],

      scripts=['scripts/cronwrap3'],
      packages=[''],
      platforms=["Any"],
      license="BSD",
      keywords='cron wrapper crontab cronjob',
      description="A Python3 cron job wrapper that wraps jobs and enables better error reporting and command timeouts.",
      long_description="""\
Example
-------

Basic example of usage::

    ##Will print out help
    $ cronwrap -h

        usage: cronwrap3 [-h] [-c CMD] [-e EMAILS] [-t TIME] [-v [VERBOSE]]

        A cron job wrapper that wraps jobs and enables better error reporting and command timeouts.

        optional arguments:
          -h, --help            show this help message and exit
          -c CMD, --cmd CMD     Run a command. Could be `cronwrap -c "ls -la"`.
          -e EMAILS, --emails EMAILS
                                Email following users if the command crashes or
                                exceeds timeout. Could be `cronwrap -e
                                "johndoe@mail.com, marcy@mail.com"`. Uses system's
                                `mail` to send emails. If no command (cmd) is set a
                                test email is sent.
          -t TIME, --time TIME  Set the maximum running time.If this time is passed an
                                alert email will be sent.The command will keep running
                                even if maximum running time is exceeded.The default is
                                1 hour `-t 1h`. Possible values include: `-t 2h`,`-t
                                2m`, `-t 30s`.
          -v [VERBOSE], --verbose [VERBOSE]
                                Will send an email / print to stdout on successful run.


    ##Will send out a timeout alert to cron@my_domain.com:
    $ cronwrap -c "sleep 2" -t "1s" -e cron@my_domain.com

    ##Will send out an error alert to cron@my_domain.com:
    $ cronwrap -c "blah" -e cron@my_domain.com

    #Will not send any reports:
    $ cronwrap -c "ls" -e cron@my_domain.com

    #Will send a successful report to cron@my_domain.com:
    $ cronwrap -c "ls" -e cron@my_domain.com -v
""")
