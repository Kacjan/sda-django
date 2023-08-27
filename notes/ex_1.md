1. Zad. 1
Stwórz widok, w którym umieścisz linki do 5 najczęściej odwiedzanych
przez Ciebie witryn internetowych.
Wykorzystaj standardowy view, a następnie zaimplementuj w oparciu o class-based view.


1. Widok ma nazywać się my_fav_links (Inaczej przy Class Based View)
2. template ma nazywać się np. fav_links.html
3. https://www.w3schools.com/html/html_links.asp -> <a href=""></a>

4.* Przekierowanie i rozszerzenie szablonu o base.html. I dodanie do navbara przekierowania na nasze ulubione strony .



5. Utworzyć model FavouritePage do przechowywania Linków ma posiadać takie atrybuty jak: page_name i URL. 
6. Wytworzyć migrację, Zmigrować. I dodać FavouritePage do admina. Zarejestrować w adminie.
7. Utworzyć kilka linków Przez Django Admina i wyświetlić je w Klasie MyFavLinks. 