import pandas as pd

# dosya okumak için:
df = pd.read_csv('dataset/imdb.csv')

# dosya hakkında özet bilgi için:
result = df
result = df.info()

# column bilgileri için:
result = df.columns

# ilk 5 kaydı çekmek için:
result = df.head()

# ilk 10 kaydı çekmek için:
result = df.head(10)

# son 5 kaydı çekmek için:
result = df.tail()

# son 10 kaydı çekmek için:
result = df.tail(10)

# Movie_Title Kolununda ki bilgileri çekmek için:
result = df['Movie_Title']

#  Movie_Title Kolununda ki ilk 5 bilgileri çekmek için:
result = df['Movie_Title'].head()

# Movie_Title ve Rating kolonunu içeren ilk 5 kayıt için:
result = df[['Movie_Title', 'Rating']].head()

# Movie_Title ve Rating kolonunu içeren son 7 kayıt için:
result = df[['Movie_Title', 'Rating']].tail(7)

# Movie_Title ve Rating kolonunu içeren ikinci 5 kayıt için:
result = df[5:][['Movie_Title', 'Rating']].head()

# Imdb puanı (Rating) 8 üstü olan ilk 50 filmin isimleri ve paunlarını çekmek için:
result = df[(df['Rating'] > 8.0)][['Movie_Title', 'Rating']].head(50)

# 2014-2015 yılları arasında ki fimlerin isimleri ve yıllarını çekmek için:
result = df[(df['YR_Released'] >= 2014) & (df['YR_Released'] <= 2015)][['Movie_Title', 'YR_Released']]

# Değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı 8 ile 9 arasında olan filmleri listelemek için:
result = df[(df['Num_Reviews']) > 100000 | ((df['Rating'] >= 8) & (df['Rating'] <= 9))]

print(result)
