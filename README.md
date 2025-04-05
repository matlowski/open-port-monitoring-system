OPEN PORT MONITORING SYSTEM

*** CO TO WŁAŚCIWIE JEST? 
Jest to skrypt umożliwiający monitorowanie otwartych portów sieciowych z funkcją porównywania ich ze wzorcowym zestawem. System został zaprojektowany na podobieństwo popularnego narzędzia do porównywania plików XML – ndiff – jednak wzbogacono go o dodatkową funkcjonalność w postaci systemu powiadomień.
Skrypt pozwala na monitorowanie dowolnej liczby hostów znajdujących się w tej samej podsieci. Działa na zasadzie porównywania dwóch plików XML – pliku referencyjnego oraz bieżącego – powstałych w wyniku skanów wykonanych za pomocą narzędzia nmap.
Użytkownik może ustawić interwały czasowe, w których będzie informowany o wykrytych zmianach w stanie portów za pośrednictwem wiadomości e-mail.   

*** JAK TEGO UŻYWAĆ?
Na początu należy pobrać skrypt na swoją maszynę oraz uzupełnić zmienne globalne, które znajdują się na samej górze pliku.
<p align="right">
  <img src="![image](https://github.com/user-attachments/assets/96e432cb-cc39-4f6a-b9b9-3c3e0830b182)" alt="Opis obrazka" width="300"/>
</p>




Pomocny przy tej czynności może okazać się poniższy link, ponieważ szczegółowo wyjaśnia w jaki sposób wygenerować hasło do aplikacji  


Kolejnym krokiem 

Dla wygody użytkowania skrypt oraz skan referencyjny powinny znajdować się w tym samym miejscu w systemie. 

Na początku należy wykonać ręcznie skan referencyjny, który będzie stanowił odnośnik dla każdego następnego skanu. Aby tego dokonać należy skorzystać z komendy:


*** PRZYKŁADOWA KONFIGURACJA I EFEKTY
