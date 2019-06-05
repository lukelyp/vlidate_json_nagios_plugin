A Python script of Nagios plugin for checking json validity and value of size.

```
$ python check_json_value_size.py -h
usage: check_json_value_size.py [-h] -l URL [-w WARNING] [-c CRITICAL]

optional arguments:
  -h, --help            show this help message and exit
  -l URL, --url URL     Please input the target url.
  -w WARNING, --warning WARNING
                        Please define the warning threshold size.
  -c CRITICAL, --critical CRITICAL
                        Please define the critical threshold size.

    e.g.
    $ python check_json_value_size.py -l "http://validate.jsontest.com/?json=[1,2,3,5,8]"
    $ python check_json_value_size.py -l "http://validate.jsontest.com/?json=[2,4,3,5,8,9]" -w 8 -c 2
```
