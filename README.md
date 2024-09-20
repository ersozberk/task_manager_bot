Görev Yönetim Sistemi
Bu proje, basit bir görev yönetim sistemi uygulamasıdır. Kullanıcılar görev ekleyebilir, görevleri görüntüleyebilir, tamamlanan görevleri işaretleyebilir ve görevleri silebilir. Python ve SQLite kullanılarak geliştirilmiştir.

Özellikler
Görev ekleme
Görev silme
Tüm görevleri listeleme
Görev tamamlama
Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki gereksinimlerin sisteminize kurulu olması gerekmektedir:

Python 3.x
sqlite3 (Python ile birlikte gelir)
Kurulum
Bu projeyi yerel makinenize klonlayın veya indirin:
bash
Kodu kopyala
git clone https://github.com/kullaniciadi/gorev-yonetim-sistemi.git
Proje klasörüne gidin:
bash
Kodu kopyala
cd gorev-yonetim-sistemi
Gerekli bağımlılıkları yükleyin (bağımlılık yoksa bu adımı atlayabilirsiniz):
bash
Kodu kopyala
pip install -r requirements.txt
Veritabanını oluşturun:
bash
Kodu kopyala
python -c "from database import create_table; create_table()"
Bu komut, SQLite veritabanında tasks adlı bir tablo oluşturacaktır.

Kullanım
Görev Ekleme
Yeni bir görev eklemek için aşağıdaki komutu kullanabilirsiniz:

python
Kodu kopyala
from database import add_task

add_task("Yeni görev açıklaması")
Görev Listeleme
Tüm görevleri listelemek için:

python
Kodu kopyala
from database import get_tasks

tasks = get_tasks()
for task in tasks:
    print(task)
Görev Tamamlama
Bir görevi tamamlanmış olarak işaretlemek için:

python
Kodu kopyala
from database import complete_task

complete_task(gorev_id)
Görev Silme
Bir görevi silmek için:

python
Kodu kopyala
from database import delete_task

delete_task(gorev_id)
Testler
Projede bir dizi birim testi bulunmaktadır. Testleri çalıştırmak için:

bash
Kodu kopyala
python -m unittest discover tests/
Her test dosyası belirli bir fonksiyonun (görev ekleme, silme, tamamlama vb.) düzgün çalıştığını doğrular.

Test Dosyaları:
test_add_task.py: Görev ekleme işlemini test eder.
test_delete_task.py: Görev silme işlemini test eder.
test_show_tasks.py: Görev listeleme işlemini test eder.
test_complete_task.py: Görev tamamlama işlemini test eder.
Yapılacaklar
 Görev güncelleme özelliği eklenmesi
 Web arayüzü ile entegrasyon
 Daha fazla test senaryosu
