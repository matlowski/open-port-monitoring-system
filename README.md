
## WHAT IT IS?
This script allows for monitoring open network ports with a feature that compares them against a reference set. The system is designed in the style of the popular XML comparison tool — ndiff — but has been enhanced with an additional functionality: a notification system. \
The script enables monitoring of any number of hosts located within the same subnet. It operates by comparing two XML files — a reference file and a current one — both generated from scans performed using the nmap tool. \
The user can configure time intervals at which they will receive email notifications about any detected changes in port states. 

## HOW TO USE IT?
1. Download the script to your machine and open it in any text editor (e.g., nano). Then fill in the global variables located at the top of the file:
   ```
   SMPT_EMAIL = ''      # email address from which the scan comparison result is sent
   SMPT_PASSWORD = ''   # temporary app password generated in Gmail 
   ADMIN_EMAIL = '' ->  # email address to which the scan comparison result is sent
   ```
   A guide showing how to enable two-step verification will be helpful for generating [the temporary app password](https://support.google.com/accounts/answer/185839?hl=pl&co=GENIE.Platform%3DDesktop).
3. Fill in the IP addresses (line 15) of the hosts you want to scan (they must be in the same subnet). Save the changes and close the file.
4. Run the initial (reference.xml) scan using the terminal with the command:
   ```
   $ nmap -oX reference.xml <IP_address_1> <IP_address_2> ...
   ```
   The addresses must match the ones provided in the script. \
   Additionally, the files main.py and reference.xml should be located in the same directory on your machine (e.g., on the desktop).
6. Open the Cron tool to set time intervals for receiving notifications by running the command:
   ```
   $ crontab -e
   ```   
   A very helpful resource for this task is that [link](https://crontab.guru/).

## EXAMPLE USAGE
To demonstrate how the script works, two virtual machines with Kali Linux installed were created and placed in the same NAT network with the address 10.0.2.0/24:
* machine # 1 - 10.0.2.10
* machine # 2 - 10.0.2.15 \ \
The script was downloaded to machine #1, the required global variables and line 15 of the main.py file were filled in. Then, SSH (port 22) and SAMBA (ports 139 and 445) services were started, and a reference scan was performed:
* example line 15:
  <p align="left">
    <img src="https://private-user-images.githubusercontent.com/180983359/430693512-1ecec17c-6f1b-4cbe-8cda-945d5269ec86.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5MzQwNjgsIm5iZiI6MTc0MzkzMzc2OCwicGF0aCI6Ii8xODA5ODMzNTkvNDMwNjkzNTEyLTFlY2VjMTdjLTZmMWItNGNiZS04Y2RhLTk0NWQ1MjY5ZWM4Ni5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwNlQxMDAyNDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jMTI3ZDkxZWEwNjI3OWY4Nzc2MjkyY2YwNTJiNjAzYzdjN2NjYzI0Mzg4OTIzZWZlOTgzMDk2ZDY0NWE2MGRjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.7TMNk14jSVRu-yQrsBg3fr-_HwXL_h8z6ZizcHBLTYQ" alt="Opis obrazka" width="800"/>
  </p>
* reference scan:
  $ nmap -oX reference.xml 10.0.2.10 10.0.2.15
Next, an appropriate time interval was set using Cron:
  <p align="left">
    <img src="https://private-user-images.githubusercontent.com/180983359/430695093-40cb0ab3-494a-4f92-96c9-633fbed543f1.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5MzQ5OTgsIm5iZiI6MTc0MzkzNDY5OCwicGF0aCI6Ii8xODA5ODMzNTkvNDMwNjk1MDkzLTQwY2IwYWIzLTQ5NGEtNGY5Mi05NmM5LTYzM2ZiZWQ1NDNmMS5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwNlQxMDE4MThaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xNTAzZjQ3YTIwMGQ4M2RjYTg1YzZhYjdkYWM4NGUzZmIzNmQxMGExMzRkZGRjZDRlMmQ1Zjc4N2E5ZGJhM2YyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.ASF0tASR18wMyYXhOUxQkp-T9u5-AQHnF1tmYoLObNk" alt="Opis obrazka" width="700"/>
  </p>
After that, on machine #1, the SSH service (port 22) was shut down and FTP (port 21) and HTTP (port 80) services were started. On machine #2, SSH (port 22) and HTTP (port 80) services were started. \

Email output received:  
<p align="left">
  <img src="https://private-user-images.githubusercontent.com/180983359/430695863-39e45b93-9149-41e5-9115-a5be33891777.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5MzU3NTMsIm5iZiI6MTc0MzkzNTQ1MywicGF0aCI6Ii8xODA5ODMzNTkvNDMwNjk1ODYzLTM5ZTQ1YjkzLTkxNDktNDFlNS05MTE1LWE1YmUzMzg5MTc3Ny5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwNlQxMDMwNTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hMDdiMGYzNjE1NWUzY2FmNjMyMTIwODkwMGQyY2ZjYmE3MzliM2NiOTIyYjM0MDNhNDFiMDY3YzEwMzU2ZDExJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.C9qdK7J2TYhMkBPq4LZxwuBPNv6jOvmiArkuQguunW4" alt="Opis obrazka" width="600"/>
</p>

