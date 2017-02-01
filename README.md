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
 ./pwsafe.py .pwsafe.dat username
 ```

## How to list all information from db pwsafe.

```bash
# pwsafe -f /root/.pwsafe.dat --exportdb
Enter passphrase for /root/.pwsafe.dat: 
# passwordsafe version 2.0 database
uuid	group	name	login	passwd	notes
"2645bafc-2dfc-52ca-272e-6131bad629f4"	"CC"	"newuser41"	"nw411"	"qq"	"q"
"88bf7997-b95d-8a51-f341-d3173bc82ca7"	"admin"	"1"	"1"	"oOkjJq1R3udH"	"admin user"
"23ceee9b-088e-be86-3baa-49f57f6c82ed"	"admin"	"12"	"12"	"nuH4nAe13hky"	"admin user"
"00675563-eefe-6c3a-e352-1766bea12a95"	"admin"	"12qa"	"12qa"	"PEwYPSZGf1Ny"	"admin user"
"e116f3d6-0599-b26e-e0a9-7c26eb5f74f7"	"admin"	"1a"	"1a"	"fATPILS0umTD"	"admin user"
"9618f50d-446e-f5f4-b93d-a95f325c93c7"	"admin"	"1qaq"	"1qaq"	"iCNeTLD1WceR"	"admin user"
```
```bash
alternative command is:
#alternative command is:
pwsafe -f /root/.pwsafe.dat --add %s" % newuser
```

## How to add new user.
```bash
pwsafe -f /root/.pwsafe.dat --add newuser
```



