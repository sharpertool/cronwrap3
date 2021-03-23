# About cronwrap3

A Python3 compatible cron job wrapper that wraps jobs and enables better error 
reporting and command timeouts.

This is a copy of the cronwrap 1.4 project in pypi

    https://pypi.org/project/cronwrap/

The original author of cronwrap is "amix", so, all of the real credit goes there.

# Usage:

### Will print out help
$ cronwrap -h

### Will send out a timeout alert to cron@my_domain.com:
$ cronwrap -c "sleep 2" -t "1s" -e cron@my_domain.com

### Will send out an error alert to cron@my_domain.com:
$ cronwrap -c "blah" -t "1s" -e cron@my_domain.com

### Will not send any reports:
$ cronwrap -c "ls" -e cron@my_domain.com

### Will send a successful report to cron@my_domain.com:
$ cronwrap -c "ls" -e cron@my_domain.com -v

## Release Notes

### v1.2.0

I removed the requirement for argparse, since that is part of python standard library now

