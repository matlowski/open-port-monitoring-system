OPEN PORT MONITORING SYSTEM

*** CO TO WŁAŚCIWIE JEST? 
Jest to skrypt umożliwiający monitorowanie otwartych portów sieciowych z funkcją porównywania ich ze wzorcowym zestawem. System został zaprojektowany na podobieństwo popularnego narzędzia do porównywania plików XML – ndiff – jednak wzbogacono go o dodatkową funkcjonalność w postaci systemu powiadomień.
Skrypt pozwala na monitorowanie dowolnej liczby hostów znajdujących się w tej samej podsieci. Działa na zasadzie porównywania dwóch plików XML – pliku referencyjnego oraz bieżącego – powstałych w wyniku skanów wykonanych za pomocą narzędzia nmap.
Użytkownik może ustawić interwały czasowe, w których będzie informowany o wykrytych zmianach w stanie portów za pośrednictwem wiadomości e-mail.   

*** JAK TEGO UŻYWAĆ?
Na początu należy pobrać skrypt na swoją maszynę oraz uzupełnić zmienne globalne, które znajdują się na samej górze pliku.
<p align="right">
  <img src="https://private-user-images.githubusercontent.com/180983359/430655788-0bb8f338-976d-484d-a0bb-53cf84faa391.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDM4Nzk5MDMsIm5iZiI6MTc0Mzg3OTYwMywicGF0aCI6Ii8xODA5ODMzNTkvNDMwNjU1Nzg4LTBiYjhmMzM4LTk3NmQtNDg0ZC1hMGJiLTUzY2Y4NGZhYTM5MS5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQwNVQxOTAwMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yYjUxNDUzZjE0NjIwYmM5YWJhYjkxZjg0MTQxNWRkMTM3Njc5M2U1NmU2MjZhYzMyN2FkZDNiNDFjZDIxMDcxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.hfQv2RyFPXejWrqzfPzTIz-j3mH8LnuzHQPCJSDVu50" alt="Opis obrazka" width="300"/>
</p>




Pomocny przy tej czynności może okazać się poniższy link, ponieważ szczegółowo wyjaśnia w jaki sposób wygenerować hasło do aplikacji  


Kolejnym krokiem 

Dla wygody użytkowania skrypt oraz skan referencyjny powinny znajdować się w tym samym miejscu w systemie. 

Na początku należy wykonać ręcznie skan referencyjny, który będzie stanowił odnośnik dla każdego następnego skanu. Aby tego dokonać należy skorzystać z komendy:


*** PRZYKŁADOWA KONFIGURACJA I EFEKTY
