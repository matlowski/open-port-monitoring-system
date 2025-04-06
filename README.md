
## WHAT IT IS?
This script allows for monitoring open network ports with a feature that compares them against a reference set. The system is designed in the style of the popular XML comparison tool — ndiff — but has been enhanced with an additional functionality: a notification system. \
The script enables monitoring of any number of hosts located within the same subnet. It operates by comparing two XML files — a reference file and a current one — both generated from scans performed using the nmap tool. \
The user can configure time intervals at which they will receive email notifications about any detected changes in port states. 

## HOW TO USE IT?
1. Download the script to your machine and open it in any text editor (e.g., nano). Then fill in the global variables located at the top of the file: \
   
   `SMPT_EMAIL = '' -> adres email, z którego wysyłany jest wynik porównania skanów
   SMPT_PASSWORD = '' -> tymczasowe hasło do aplikacji generowane w gmail'u
   ADMIN_EMAIL = '' -> adres email, na który zostanie wysłany wynik porównania skanów`
   
   Pomocny przy generowaniu tymczasowego hasła będzie poradnik pokazujący w jaki sposób włączyć uwierzytelnienie dwuetapowe:
   https://support.google.com/accounts/answer/185839?hl=pl&co=GENIE.Platform%3DDesktop
3. Uzupełnij adresy IP (linia nr 15), które chcesz przeskanować (hosty muszą się znajdować w tej samej podsieci), następnie zapisz zmiany i zamknij plik.
4. Wykonaj w terminalu skan bazowy (reference.xml) za pomocą komendy:
   $ nmap -oX reference.xml <IP_address_1> <IP_address_2> ...
     Adresy muszą być zgodne z adresami wpisanymi do skryptu.
     Dodatkowo pliki 'main.py' i 'reference.xml' powinny znajdować się w tym samym miejscu w systemie plików maszyny, np. na pulpicie
5. Otwórz narzędzie 'Cron' w celu wyznaczenia interwałów czasowych otrzymywanych powiadomień, za pomocą komendy:
   $ crontab -e   
   Pomocny przy tym zadaniu na pewno będzie link:
   https://crontab.guru/



*** PRZYKŁADOWA KONFIGURACJA I EFEKTY
W celu zademonstrowania działania skryptu utworzono dwie maszyny wirtuale z zainstalowanym systemem operacyjnym Kali Linux oraz umieszczono je w tej samej sieci NAT o adresie 10.0.2.0/24:
* maszyna nr 1 - 10.0.2.10
* maszyna nr 2 - 10.0.2.15
Na maszynę nr 1 pobrano skrypt, uzupełniowo wymagane zmienne globalne oraz linię 15 pliku main.py. Następnie uruchomiono usługi SSH (port 22) oraz SAMBA (port 139, port 445) i wykonano skan referencyjny:
* przykładowa linia 15:
  <p align="left">
    <img src="https://private-user-images.githubusercontent.com/180983359/430693512-1ecec17c-6f1b-4cbe-8cda-945d5269ec86.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5MzQwNjgsIm5iZiI6MTc0MzkzMzc2OCwicGF0aCI6Ii8xODA5ODMzNTkvNDMwNjkzNTEyLTFlY2VjMTdjLTZmMWItNGNiZS04Y2RhLTk0NWQ1MjY5ZWM4Ni5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwNlQxMDAyNDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jMTI3ZDkxZWEwNjI3OWY4Nzc2MjkyY2YwNTJiNjAzYzdjN2NjYzI0Mzg4OTIzZWZlOTgzMDk2ZDY0NWE2MGRjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.7TMNk14jSVRu-yQrsBg3fr-_HwXL_h8z6ZizcHBLTYQ" alt="Opis obrazka" width="800"/>
  </p>
* skan referencyjny:
  $ nmap -oX reference.xml 10.0.2.10 10.0.2.15
Kolejnym krokiem było ustawienie odpowiedniego interwału w Cron'ie:
  <p align="left">
    <img src="https://private-user-images.githubusercontent.com/180983359/430695093-40cb0ab3-494a-4f92-96c9-633fbed543f1.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5MzQ5OTgsIm5iZiI6MTc0MzkzNDY5OCwicGF0aCI6Ii8xODA5ODMzNTkvNDMwNjk1MDkzLTQwY2IwYWIzLTQ5NGEtNGY5Mi05NmM5LTYzM2ZiZWQ1NDNmMS5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwNlQxMDE4MThaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xNTAzZjQ3YTIwMGQ4M2RjYTg1YzZhYjdkYWM4NGUzZmIzNmQxMGExMzRkZGRjZDRlMmQ1Zjc4N2E5ZGJhM2YyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.ASF0tASR18wMyYXhOUxQkp-T9u5-AQHnF1tmYoLObNk" alt="Opis obrazka" width="700"/>
  </p>
Następnie na maszynie nr 1 zamknięto usługę SSH (port 22) oraz otworzono usługi FTP (port 21) i HTTP (port 80). Na maszynie nr 2 otworzono usługi SSH (port 22) i HTTP (port 80)

Output otrzymany na maila:  
<p align="left">
  <img src="https://private-user-images.githubusercontent.com/180983359/430695863-39e45b93-9149-41e5-9115-a5be33891777.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM5MzU3NTMsIm5iZiI6MTc0MzkzNTQ1MywicGF0aCI6Ii8xODA5ODMzNTkvNDMwNjk1ODYzLTM5ZTQ1YjkzLTkxNDktNDFlNS05MTE1LWE1YmUzMzg5MTc3Ny5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwNlQxMDMwNTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hMDdiMGYzNjE1NWUzY2FmNjMyMTIwODkwMGQyY2ZjYmE3MzliM2NiOTIyYjM0MDNhNDFiMDY3YzEwMzU2ZDExJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.C9qdK7J2TYhMkBPq4LZxwuBPNv6jOvmiArkuQguunW4" alt="Opis obrazka" width="600"/>
</p>

