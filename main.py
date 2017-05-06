import pexpect
child = pexpect.spawn("telnet 54.250.134.6 32773")
child.sendline("\n\n")
child.expect(">")
child.sendline("enable")
child.expect("#")
child.sendline("config t")
child.expect("#")
child.sendline("hostname Router1")
child.expect("#")
child.sendline("end")
child.expect("#")
    
