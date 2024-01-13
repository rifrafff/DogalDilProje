Konu:
Sınıflandırma ve bir tane dil modeli kullanılmıştır. Çalışma mantıkları sınıflandırma modelleri kullanıcının yazdığı metinden yola çıkarak konuya uygun film bulmaya çalışır. Dil modeli yine aynı şekilde kullanıcıdan alınan metinden yola çıkarak ve veri setinin içindeki konu kısmını kullanarak belirttiğimiz karakter sayısında bize bir cümle oluşturur.
Kullanılan kütüphaneler:
Verdiğiniz kod örnekleri aşağıdaki kütüphaneleri ve modülleri kullanmaktadır:
1.pandas
2.TfidfVectorizer
3.linear_kernel
4.spacy
5.text_lemmatizer (simplemma)
6.numpy
7.ast
8.re
9.stopwords (nltk)
10.word_tokenize (nltk)
11.train_test_split (sklearn)
12.MultinomialNB (sklearn)
13.svm (sklearn)
14.classification_report (sklearn)
15.accuracy_score (sklearn)
16.SimpleImputer (sklearn)
VERİ SETİ'NİN OLUŞTURULMASI
Veri seti film sitesinden çekilen film adı, türü ve konusundan oluşmaktadır. Veri setindeki verileri elde edebilmek için öncelikle siteden filmlerin linklerini çektik ve daha sonra o linklere girerek filmlerin adını, türünü ve konusunu çekerek veri setimizi oluşturduk. Sitenin film arşivinde buluna bütün filmlerin verilerini çektik çünkü ve veri setimizin boyutu arttıkça modellerimizin daha başarılı olacağını varsaydık. Veri setimizde 2913 filmin verisi bulunuyor ve bir film birden fazla türe sahip olabiliyor.
Veri setindeki sütunlar aşağıdaki gibidir:
Film Adı	Türler	Konu
![image](https://github.com/rifrafff/DogalDilIsleme-Proje/assets/106619895/1bc32c44-9741-43b0-8c2d-29704ffbd21b)

 
Lemmatization İşlemi
Lemmatizasyon, kelimenin kökünü bulma işlemidir. Örneğin, "koştu" kelimesini "koş" olarak ele almak gibi. Bu, modelin daha iyi öğrenmesine yardımcı olabilir.Simplemma kütüphanesi Python fonksiyonunda bir metin dizgisini temizleme ve lemmatizasyon işlemlerini uygulama amacıyla tasarlanmıştır. Türkçe lemmatizasyon işlemi uygulanır. Bu işlem, kelimeleri temel veya kök formlarına indirgeme sürecidir.

from simplemma import text_lemmatizer 
kodu ile konu isim türler içerisinde emojiler, noktalama işaretleri, stopwordsler, linkler gibi istenmeyen ve modelin başarısını düşürecek veriler tweetlerin içerisinden temizleniyor.

def clean_text(text)
def clean_row(row):
simplemma ile temizlenen konu isim ve türler sorgu için hazır hale getirilmiştir.
![image](https://github.com/rifrafff/DogalDilIsleme-Proje/assets/106619895/f8163bf7-d7c9-422d-8344-b28544a6c183)


 
Modelin Oluşturulması ve Filmlerin Kategorilendirilmesi
Model Seçimi ve Model Oluşturma:
Projemizde 3 farklı tipte model kullandık. Bunlar bir metin girdiğimizde bize metne göre veri setinden istenilen karakter de cümle yazan Markov modeli ,
Cosine Similarity temelli bir öneri sistemi, benzer filmleri sıralayan Rondom Forest ve Support Machine modeli. Örnek gösterimler aşağıdaki gibidir:

Markov Modeli
 ![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/282f621a-e467-474b-af11-50826a6363c0)

Cosine Similarity
 ![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/887d4345-5118-41e4-b539-191e27ef4b8a)

Random Forest ve SVM Modelİ
 ![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/d5ca9af7-c7ab-4752-904c-dec50a307d3e)
 ![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/4ae03325-a8dd-4233-b5df-d7e9cc7a9794)
 ![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/4e3859a4-09fe-4fb3-b761-330c2279ff6a)
 ![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/692644d9-91b0-430e-ae9f-941716560775)
 ![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/8fb5b5f2-a091-4620-8ce2-6a376896aff9)


Filmlerin Vektörel Matrisinin Çıkarılması
Filmler metinden oluştuğu için bunun bilgisayar ortamında işlenmesi mümkün değildir bu yüzden veriler sayısal değerlere dönüştürülmelidir. Bir sözlük oluşturularak dökümandaki her kelime için bir indexleme yapılır. Daha sonra hangi index numarasına sahip kelimenin hangi filmi kaç kere geçtiği hesaplanarak sayma matrisi oluşturulur. 
TfidfVectorizer kullanarak metin verilerini vektörlere dönüştürme işlemini gerçekleştirir. Önce, X_train ve X_test dizileri 2D dizilere dönüştürülür ve ardından SimpleImputer kullanılarak eksik değerler temizlenir. TfidfVectorizer ise metin verilerini sayısal vektörlere dönüştürmek için kullanılır TfidfVectorizer bir kelimenin döküman içindeki önemi istatistiksel olarak hesaplamıştır. Bu vektörler, her bir kelimenin ve kelime kombinasyonunun belirli bir ağırlıklandırma ile ifade edildiği sayısal temsillerdir. Bu sayısal temsiller, ardından bir sınıflandırma modeline veya başka bir makine öğrenimi modeline giriş olarak kullanılabilir.
Modellerin Eğitilmesi ve Başarısının Hesaplanması
Modeller birbirlerinde farklı şekilde eğitilmiştir.Cosine Similarity bir öneri algoritmasıdır bu yüzden accuracy yani başarı hesaplamak pek mümkün değildir çünkü Cosine Similarity, unsupervised bir öğrenme yöntemidir ve genellikle kullanıcının ilgisini çekebilecek önerileri sağlamak amacıyla kullanılır.Markov modeli kullanıcıdan aldığı kelimeden başlayarak veri setinden rastgele gelicek şekilde belirtilen sayıda karakterle cümle oluşturur başarı hesabı yapmak mümkün değildir.Random modelinin eğitimi şu şekildedir. Modelin tanımlandığı kısımda, RandomForestClassifier sınıfı kullanılarak bir Random Forest modeli belirlenir. Bu modelin tekrarlanabilirliğini sağlamak için random_state parametresi kullanılmıştır.Verinin eğitim ve test setine ayrıldığı bölümde, train_test_split fonksiyonu kullanılarak tfidf_matrix özellik matrisi ve df['labels'] etiketleri, veriyi %80 eğitim ve %20 test olacak şekilde bölmek üzere ayrılır. Bu işlem, modelin eğitildikten sonra performansının değerlendirileceği bağımsız bir test setinin oluşturulmasını sağlar.Modelin eğitildiği kısımda, fit metodunu kullanarak model, eğitim seti üzerindeki özellikler ve etiketler arasındaki ilişkiyi öğrenir. Modelin eğitilmesi, bu ilişkiyi modelin içindeki karar ağaçlarına öğretir. 
Destek Vektör Makinesi (SVM), sınıflandırma ve regresyon problemlerini çözmek için kullanılan bir makine öğrenimi algoritmasıdır. Temelde, iki sınıf arasında bir hiper düzlem oluşturarak veri noktalarını en iyi şekilde ayırmaya odaklanır. SVM'nin önemli bir özelliği, sınıflar arasındaki marjı maksimize etmeye çalışmasıdır. Bu marj, sınıflar arasındaki en yakın destek vektörlerin uzaklığına dayanır. SVM, lineer olarak ayrılamayan veri setlerini işleyebilme yeteneği ile kernel trick gibi teknikleri kullanarak geniş bir uygulama yelpazesi sunar. Parametreler arasında C ve gamma'nın bulunması, algoritmanın esnekliğini belirler. SVM'nin başarısı, sınıflar arasında net bir ayrım yapma kabiliyeti ve düşük boyutlu veri setlerinde etkili performansıyla öne çıkar.
 
Modellerin Hataları
Random Forest ve Support Vector Machine modellerinin hataları farklılık göstermektedir. Random Forest veri setinden tam bir konuyu girdi olarak verdiğimizde filmi çoğunlukla bulabilmektedir ancak SVM için aynısı söyleyemeyeceğim.Aşağıda örnekler mevcuttur.
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/c0dbb89f-8388-4814-bfe6-4060d9c4eb98)


Konuya ait film Siyah Telefondu
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/ca87c6a9-3772-4755-8324-dc8a551dea30)

Konuya ait film Korku Seansı

Modellerin Konulara Göre Yaptığı Tahminler
Markov Model
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/3d2b62af-64dc-4bc5-adac-cae1f7435bf3)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/9fc8dc5d-f2c8-4580-83a5-0ee47f902da7)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/001669b3-74f6-423c-8958-30d94a746e54)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/c8652a62-d984-4e0b-a438-2f44bb6c1ddb)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/adfb17a3-f6d5-418c-a9ab-5ad7351c229f)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/8f16084b-b847-4a5c-8c41-d373c0e51396)

Cosine Similarity
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/aa4ae913-c206-4b7d-886a-ac1120b4ff82)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/dbdecb70-0b46-4fb9-bd83-2f7ace091ab7)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/7315c9e5-42bb-441a-a346-6035f0009e78)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/bc92d516-7cd3-4fd9-8f51-5356463dfb14)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/d00061ae-d47a-4884-a0e1-f02429ac25f3)

Random Forest  ve SVM Modeli
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/9c397b1f-629c-42f3-a820-9b6b020d147e)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/8f2238e9-a8a0-4f3a-98cc-ad78d3d79362)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/1a77f369-0863-4cd4-a3c9-3b26418e1e18)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/4cb80252-a62a-4b38-9559-d7ec4ffd6adb)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/877390e5-2625-4e29-86a9-6669f745d33f)
![image](https://github.com/rifrafff/DogalDilProje/assets/106619895/8983c42c-d9e3-4e61-9554-cd99c523539f)

Sonuç
Sonuca bakıldığında yapılan projede seçilen modelin ne kadar önemli olduğu görülmektedir. Farklı projelerde farklı modellerin daha etkili olabileceği görülebilir.Bizim modellerimiz içerisinde benzer film bulurken Random Forest Modeli , SVM ye göre daha başarılıydı. Ancak, model seçimi kadar, veri setinin dikkatlice hazırlanması da önemlidir. Noktalama işaretlerinden arındırılmış ve olumsuz etkileri minimize edilmiş stopwordslerden temizlenmiş bir veri seti, modelin başarı oranını belirlemede kritik bir faktördür. Veri setindeki özelliklerin niceliği, eğitim-test veri setinin uygun bir şekilde bölünme oranı gibi faktörler de modelin performansını önemli ölçüde etkileyebilir.
