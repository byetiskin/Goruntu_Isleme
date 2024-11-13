
Projenizle ilgili datayı indirdikten sonra image ve label dosyalarını 2D çevirmeniz ve bu çevirdiğiniz 2D görüntü üzerinde çalışmanız gerekiyor. 2D çevirme kodunu sizinle paylaştım (2DTransform). Kendi kullanacağınız datanın adını yolunu ve label_coronal_mid parametresindeki değere kendi labelınızı yazmanız gerek (9, 10, 26. satırlar).

Örneğin proje numaranızda Organlar1-6 yazıyorsa, excelde paylaştığımız Organlar1 linkinden datayı indirip imagesTR ve labelsTRde seçtiğiniz nii dosyasını indireceksiniz. Diyelim ki 0001 numaralı img ve label indirdiniz. Kodda 9 ve 10. satırdaki yere aşağıdaki gibi yazmalısınız. Datayı indirdiğiniz yer ile bu kodu aynı dizinde tutmanız gerek. Organlar1-6: Organlar1 datasındaki 6 ile etiketlenmiş yerin segmentasyonu çalışması demek. Sizin amacınız buradaki label görüntüsünü kendiniz saf görüntü işleme yöntemleri ile yapmak. ProjeniSec excelde aşama 1 için istenen adımlar mevcut. Organlar1 ve Organlar2 bölümünde her etiketin bilgisi yer alıyor. Organlar2 projesini almış olanlar da kendi datasını indirip img_path ve label_path değişkenine kendi datasının adını yazmalı. TıbbiProblemler bölümünden proje seçmiş olanlar da eğer datası 3 boyutlu ise bu kod ile datayı 2 boyuta dönüştürmeli. 
```python
img_path = "amos_img_0001.nii.gz"
label_path = "amos_label_0001.nii.gz"
``` 
Path bilgisini girdikten sonra diğer dikkat etmeniz gereken kısım ise 26. satır. Organlar1-6 projesi için örnek verelim. Burada etiketi 6 olan bölgeyi almak için label_coronal_mid parametresinin 6'ya eşitliğini kontrol ediyorum. Organlar1-4 olsaydı label_coronal_mid == 4 yazmam gerekirdi.
```python
label_coronal_mid_masked = (label_coronal_mid == 6).astype(np.uint8) * 255 
``` 
Bu şekilde üzerinde çalışacağınız görüntüleri indirip değiştirmeniz gereken yerleri düzenledikten sonra kodu çalıştırdığınızda, kod ile aynı dizine otomatik bir şekilde dataset klasörü oluşturulacak ve 2D image ile label görüntüleri içinde olacak.


