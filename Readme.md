Why you need this.

```
$ git clone https://github.com/nmcspadden/Profiles.git
$ cd Profiles
$ sed -i '' 's/org\.sacredsf/org\.glenbrook225/' ./*.mobileconfig
```

But what about the UUIDs?

`$ ./fix_shared_profiles.py ./*.mobileconfig`

There are two pitfalls identified at the end of this post.

http://rmanly.blogspot.com/2015/07/making-shared-configuration-profiles.html
