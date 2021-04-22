# Instruction 
> $~/folder python3 main.py split/recover

Split mode: The first line contains a secret string, and the second line contains two integers separated by a space.
Example:
dima@asuslaptop:~$ python3 main.py split
0x123456789
12 3

Recover mode: On the first line, an integer N, the number of parts of the secret, on the next N lines, the parts of the secret.
Example:
dima@asuslaptop:~$ python3 main.py recover
3
0x98653431dff4ef472cc4dd431682e6dc 0xde16756b092d9924281925809bcaed7848ca4ab12d65533f12816533adb8687bd1361e2fb9da3a82e7832006298e12d
0xd0892e801007e29ad9a123627c83dfeb 0x19fdb16a88471e6e6fe36e848e72e0a1c0bab1996e32201ee71ba9a51ddf52a4fd820e503edb3fd8cfaf725359737121
0xbf28e55d7ec25cdb3c50df5cab0e622 0x15d70f58dc5e71468d0ae54d93111e3f74a520d725628f82a5568b91b0a065490e4415f0a758a0ae75bc9f113fb03b
