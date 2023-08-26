### Czym jest Django? 
Darmowy open-sourcowy framework do tworzenia aplikacji intenrnetowych.
w oparciu o język Python.

1. Szybki rozwój. 
   Czyli Django dostarcza zestaw gotowych kompomenetów do tworzenia aplikacji.

2. ORM (Object Relational Mapping)
   Django dostarcza narzędzia do mapowania obiektów na relacyjne bazy danych.
    
   SQL - Select * from Users 

   ORM - Users.object.all()

3. Automatyczna administracja 
   Django dostarcza gotowy panel administracyjny.

4. Bezpieczeństwo 
    Framework ma wbudowane mechanizmy zabezpieczające przed atakmi np. typu SQL Incjection 
    czy Cross-site scripting (XSS) oraz inne. 

5. Wzorzec projektowy **MVC** Czasami nazywany MTV. Model-View-Controller. 
   1. **Model** reprezentuje strukturę obiektu w bazie danych. W django obiekty w bazie danych
   są definiowane jako klasy pythona
   2. **Template** - Jest odpowiedzialny za prezentacje danych. Tutaj są definiowane szablony HTML
   3. **View** - Jest warstwą kontrolera, zarządza logiką biznesową i interakcją między modelem a szablonem. 
   
   **Modele** są definiowane w pliku/katalogu models 
   **Szablony** są przechowywane w katalogu templates w aplikacjach lub globalnym templates.
   **Widoki** są przechowywane w katalogu/pliku views w aplikacjach. 
6. Rozszerzalność Django pozwala na tworzenie własnych aplikacji które można poownie wykorzystać w różnych projektach.
7. Obszerna społeczność i dokumentacja. 


### Django Project Structure
asgi.py - Asynchronous Server Gateway Interface (ASGI) Pozwala obsługiwać kod asynchroniczny.

wsgi.py - Web Server Gateway Interface (WSGI) wdrażanai normalnego aplikacji która posiada standardowy interfejs HTTP.

**settings.py** - Kluczowy plik konfiguracyjny. Ustawienia baz danych, aplikacji, bezpieczeństwa, ustawienia plików statycznych i mediów.

**urls.py** - Definiujemy tutaj mapowanie URL-ów do widoków (views)

**manage.py** Polecenie wiersza CLI. Dostarczane w kazdym projekcie Django jest tylko jedno. Pozwala
nam na uruchamiania różnych zadań. np. Starowanie serwera, Tworzenie migracji, Tworzenie super użytkownika, Uruchamianie testów 

### COMMANDS 
1. Instalcja Django 

`pip install django` 



### Requesty. 
W request znajdują się wszystkie dane z przeglądarki, IP, to co user przekazał, URL jaki byl pytane, headersy itd.


path('hello/<int:s>', hello), -> przyjmuje tylko int np. localhost:8000/hello/1, gdy podamy str to zwróci NotFound 404
path('hello/<s>', hello), -> przyjmuje wszysko.

   

### DJANGO COMMANDS

django-admin startproject holly_movies <destination>
django-admin startproject holly_movies 


cd holly_movies -> Przejścia do katalogu holly_movies

python manage.py runserver - Uruchomienie serwera.


python manage.py migrate -> Uruchomienie migracji.

python manage.py makemigrations -> Wytworzenie migracij. 

python manage.py startapp <app_name> -> Wytworzenie nowej aplikacji.


### DJANGO ORM 

ModelName.objects.all() -> Pobranie wszystkich rekordoów z konkretnej tabeli/modelu.

ModelName.objects.get(field_name=field_value)

object = ModelName.objects.get(field_name=field_value)

I na obiekcie możemy wykonywać oparcję identyczne jak na klasach np.

object.id 
object.title itd. 
