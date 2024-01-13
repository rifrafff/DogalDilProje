import pandas as pd
from bs4 import BeautifulSoup
import requests

# TXT dosyasındaki linkleri oku
with open('linkler.txt', 'r', encoding='utf-8') as file:
    links = file.read().splitlines()

# Excel dosyasını oluştur
df_all_comments = pd.DataFrame(columns=["Film Adı", "Türler", "Konu"])

# Her bir link için işlem yap
for link in links:
    # Film adını ve sayfa adını çıkar
    film_name = link.split("/")[-1]

    # Web sayfasını çek
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Film adını çek
    film_title = soup.find(class_="title-border").text.strip()

    # Movie detail içeriğini çek
    movie_detail = soup.find(id="movie-detail").find('p').text.strip()

    # Türleri çek
    genres = [element.text.strip() for element in soup.find_all(class_="elements")]

    # Film Adı, Movie Detail ve Türleri içeren DataFrame oluştur
    df_comments = pd.DataFrame({
        "Film Adı": [film_title],
        "Türler": [", ".join(genres)],
        "Konu": [movie_detail],
    })

    # DataFrame'leri birleştir
    df_all_comments = pd.concat([df_all_comments, df_comments], ignore_index=True)

# Excel'e yaz
df_all_comments.to_excel("film_Datasi.xlsx", index=False)
