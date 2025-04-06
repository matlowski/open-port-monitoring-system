OPEN PORT MONITORING SYSTEM

*** CO TO WŁAŚCIWIE JEST? 
Jest to skrypt umożliwiający monitorowanie otwartych portów sieciowych z funkcją porównywania ich ze wzorcowym zestawem. System został zaprojektowany na podobieństwo popularnego narzędzia do porównywania plików XML – ndiff – jednak wzbogacono go o dodatkową funkcjonalność w postaci systemu powiadomień.
Skrypt pozwala na monitorowanie dowolnej liczby hostów znajdujących się w tej samej podsieci. Działa na zasadzie porównywania dwóch plików XML – pliku referencyjnego oraz bieżącego – powstałych w wyniku skanów wykonanych za pomocą narzędzia nmap.
Użytkownik może ustawić interwały czasowe, w których będzie informowany o wykrytych zmianach w stanie portów za pośrednictwem wiadomości e-mail.   

*** JAK TEGO UŻYWAĆ?
1. Pobierz skrypt na swoją maszynę oraz otwórz go w dowolnym edytorze (np. nano) i uzupełnij zmienne globalne, które znajdują się na samej górze pliku:
   SMPT_EMAIL = '' -> adres email, z którego wysyłany jest wynik porównania skanów
   SMPT_PASSWORD = '' -> tymczasowe hasło do aplikacji generowane w gmail'u
   ADMIN_EMAIL = '' -> adres email, na który zostanie wysłany wynik porównania skanów
   Pomocny przy generowaniu tymczasowego hasła będzie poradnik pokazujący w jaki sposób włączyć uwierzytelnienie dwuetapowe:
   https://support.google.com/accounts/answer/185839?hl=pl&co=GENIE.Platform%3DDesktop
2. Uzupełnij adresy IP (linia nr 15), które chcesz przeskanować (hosty muszą się znajdować w tej samej podsieci), następnie zapisz zmiany i zamknij plik.
3. Wykonaj w terminalu skan bazowy (reference.xml) za pomocą komendy:
   $ nmap -oX reference.xml <IP_address_1> <IP_address_2> ...
     Adresy muszą być zgodne z adresami wpisanymi do skryptu.
     Dodatkowo pliki 'main.py' i 'reference.xml' powinny znajdować się w tym samym miejscu w systemie plików maszyny, np. na pulpicie
4. Otwórz narzędzie 'Cron' w celu wyznaczenia interwałów czasowych otrzymywanych powiadomień, za pomocą komendy:
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
  <img src="https://github.com/matlowski/open-port-monitoring-system/issues/2#issue-2974839931" alt="Opis obrazka" width="300"/>
</p>
* skan referencyjny:
  $ nmap -oX reference.xml 10.0.2.10 10.0.2.15
Kolejnym krokiem było ustawienie odpowiedniego interwału w Cron'ie:
* fotka Crona
Następnie na maszynie nr 1 zamknięto usługę SSH (port 22) oraz otworzono usługi FTP (port 21) i HTTP (port 80). Na maszynie nr 2 otworzono usługi SSH (port 22) i HTTP (port 80)

Output otrzymany na maila:  
<p align="left">
  <img src="" alt="Opis obrazka" width="300"/>
</p>

