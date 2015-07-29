Right now this will sometimes flip the "top" of the file with the bottom. This doesn't matter for the functionality of the configuration profile but it will make it somewhat harder to read.

I don't know if it has to do with the fact that python dictionaries are unordered or what. Will investigate more later.



usage: fix_shared_profiles.py [-h] file [file ...]

Generate new uuids for shared configuration profiles.

positional arguments:
  file        one or more configuration profiles

optional arguments:
  -h, --help  show this help message and exit
