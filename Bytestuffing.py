def charstuff(flagbyte,escbyte,payload):
    x=payload.replace(escbyte,escbyte*2)
    y=x.replace(flagbyte,escbyte+flagbyte)
    return flagbyte+y+flagbyte
def chardestuff(flagbyte,escbyte,payload):
    x=payload.replace(escbyte*2,escbyte)
    y=x.replace(escbyte+flagbyte,flagbyte)
    return y[1:-1]
msg=input('enter some message:')
fb=input('enter flagbyte:')
eb=input('enter escbyte:')
print('original message:',msg)
stf=charstuff(fb,eb,msg)
print('message after character stuffing:',stf)
dstf=chardestuff(fb,eb,stf)
print('message after character destuffing:',dstf)
    output
enter some message:aefb
enter flagbyte:f
enter escbyte:e
original message: aefb
message after character stuffing: faeeefbf
message after character destuffing: aefb
