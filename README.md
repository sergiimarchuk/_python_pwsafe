# python_pwsafe

This script automate adding new user with random password to pwsafe database.

## How to install:

 * install pwsafe
 
 ```
 wget -c "http://li.nux.ro/download/nux/dextop/el7/x86_64/pwsafe-0.2.0-18.el7.nux.x86_64.rpm" && yum install pwsafe-0.2.0-18.el7.nux.x86_64.rpm -y
 ```

 * created db file pwsafe

 ```
 pwsafe --createdb -f pwsafe.dat
 ```

 * install python module pexpect

 ```
 yum install pexpect
 ```

 * run script

 ```
 ./pwsafe.py /root/.pwsafe.dat testuser
 User   testuser    was created in pwsafe.
 ```

 * verify
 
 ```
 pwsafe -f /root/.pwsafe.dat --exportdb | grep testuser
 Enter passphrase for /root/.pwsafe.dat: 
 "3a8f23ed-3e5d-a76e-e996-633a6a33b23d"	"admin"	"testuser"	"testuser"	"dqLeEQI9GMP7"	"admin user"
 ```


## How to add new user.
```bash
pwsafe -f /root/.pwsafe.dat --add newuser
```



