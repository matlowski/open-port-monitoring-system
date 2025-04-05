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
2. Uzupełnij adresy IP (linia nr 15), które chcesz przeskanować (hosty muszą się znajdować w tej samej podsieci), zapisz zmiany i zamknij plik.
3. Wykonaj w terminalu skan bazowy (reference.xml) za pomocą komendy:
   $ nmap -oX reference.xml <IP_address_1> <IP_address_2> ...
     Adresy muszą być zgodne z adresami wpisanymi do skryptu.
     Dodatkowo pliki main.py i reference.xml powinny znajdować się w tym samym miejscu w systemie plików maszyny, np. na pulpicie
4. Otwórz narzędzie 'Cron' w celu wyznaczenia interwałów otrzymywanych powiadomień, za pomocą komendy:
   $ crontab -e   
   Pomocny przy tym zadaniu na pewno będzie link:
   https://crontab.guru/#01_13_*_*_*




<p align="left">
  <img src="" alt="Opis obrazka" width="300"/>
</p>
  



Pomocny przy tej czynności może okazać się poniższy link, ponieważ szczegółowo wyjaśnia w jaki sposób wygenerować hasło do aplikacji  


Kolejnym krokiem 

Dla wygody użytkowania skrypt oraz skan referencyjny powinny znajdować się w tym samym miejscu w systemie. 

Na początku należy wykonać ręcznie skan referencyjny, który będzie stanowił odnośnik dla każdego następnego skanu. Aby tego dokonać należy skorzystać z komendy:


*** PRZYKŁADOWA KONFIGURACJA I EFEKTY
