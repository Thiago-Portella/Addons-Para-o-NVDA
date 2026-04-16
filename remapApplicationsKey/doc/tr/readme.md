# Uygulama Tuşunu Yeniden Eşle


## Bilgi
* Yazarlar: "Rui Fontes, Héctor J. Benítez Corredera'nın çalışmasına dayanmaktadır.
* 22/03/2024 tarihinde güncellendi
* [Kararlı sürümü indir][1]
* Uyumluluk: NVDA sürüm 2019.3 ve sonrası.


## Sunum
Klavyesinde Uygulama tuşu olmayan veya uygulama tuşu çalışmayan bilgisayarlar için basit eklenti.
Uygulama tuşuna sahip olmak istediğimiz tuşu veya tuş kombinasyonunu tekrar atamamız gerekecektir.
Ayrıca Windows 11 build 22621 ve sonraki sürümlerin Dosya gezgininde de kullanışlıdır, çünkü tam bağlam menüsünü görüntülemek için kullanılan Shift+uygulama tuşu kombinasyonuna bir tuş atamaya olanak tanır. Bu Windows yapısından başlayarak, uygulama tuşu yalnızca bağlam menüsünün sadeleştirilmiş bir sürümünü gösterir.
Uygulama tuşunun yerine kullanmak istediğimiz tuş veya tuş kombinasyonunu atamamız gerekmektedir.
NVDA / Tercihler / Girdi Hareketleri... / Uygulama tuşunu yeniden eşle dalı altından istediğimiz kombinasyonu atayabiliriz.


## Gözlemler
Bir tuş kombinasyonu veya tek tuş atarken bu kombinasyonun veya tuşun hiçbir uygulamada kullanılmadığını dikkate almamız gerekiyor.
Örneğin, Ctrl + Aşağı Ok sistemin çoğunda işe yarayabilir ancak Google Chrome'da içerik menüsüne erişime izin vermeyen bir hata verir.
Örnek vermek gerekirse, genellikle sağ üst satırda bulunan ve genellikle ikinci veya üçüncü tuş olan "printScreen" tuşunu kullanıyorum.
NVDA'nın girdi yardımını kullanırsak hangisi olduğunu bulabiliriz; bunun için NVDA+1 tuşlarına basıyoruz ve klavyedeki tuşları keşfetmeye başlıyoruz. "printScreen" duyulduğunda aradığımız tuş bu olacaktır. Tekrar NVDA + 1 tuşuna basarak NVDA'nın girdi yardımından çıkabiliriz.
Bu bir örnektir; tuş veya tuş kombinasyonunu seçme yetkisi kullanıcıya bırakılmıştır.


## Çevirmenler ve işbirlikçileri:
* İspanyolca: Rémy Ruiz
* Fransızca: Remy Ruiz
* Rusça: Valentin Kupriyanov
* Ukraynaca: VovaMobile
* Türkçe: Umut Korkmaz


## Değişiklik günlüğü:

### Sürüm 2023.09.30

* 26.09.2023 tarihinde NVDA uyumluluğu 2024.1 sürümüne genişletildi;
* Artık Shift+uygulama tuşuna bir hareket atamak da mümkün;
* Bu şekilde, uygulamalar tuşu Shift+uygulama tuşuna atanırsa, tam içerik menüsü her zaman açık olacaktır.


### Sürüm 2023.09.02
* Artık Rui Fontes ve NVDA Portekiz ekibi tarafından sürdürülüyor
* Artık kod İngilizce'ye dayanmaktadır.


### Sürüm 0.4
* Rusça, Ukraynaca ve Türkçe dilleri eklendi.
* NVDA 2023.1 ile uyumluluk eklendi


### Sürüm 0.3
* Daha güvenilir ve daha doğrudan bir yöntem olduğundan, uygulama anahtarını yerel NVDA'dan yerel Windows'a çağırmanın yolu değiştirildi.
* Odak üzerine sol ve sağ fare tıklaması olanağı eklendi.
Girdi hareketi iletişim kutusunda karşılık gelen tuş kombinasyonlarını atamamız gerekecek.
Eylemi uyguladığımızda fare odağa hareket edecek, ilgili tıklamayı yapacak ve tıklamanın gerçekleştirildiğini belirten bir ses duyulacaktır.


### Sürüm 0.2
* NVDA 2022 ile uyumluluk


### Sürüm 0.1.5
* NVDA eklentilerindeki sorun düzeltildi.
* Fransızca dili eklendi.


### Sürüm 0.1
* İlk sürüm.

[1]: https://github.com/ruifontes/RemapKeyAplication-para-NVDA/releases/download/2025.07.14/remapApplicationsKey-2025.07.14.nvda-addon
