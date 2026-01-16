# O File Processor

**O File Processor**, profesyonel dosya yönetimi için modern, **PyQt6 tabanlı** bir masaüstü uygulamasıdır. Temiz **MVC mimarisi** ile inşa edilmiş olup, toplu yeniden adlandırma, kopyalama ve güvenli silme işlemlerini sezgisel 3 panelli bir arayüzle sunar.

[![GitHub](https://img.shields.io/badge/GitHub-hamer1818%2FO--File--Process-blue?logo=github)](https://github.com/hamer1818/O-File-Process)

---

## 🚀 Temel Özellikler

### 📁 Akıllı Klasör Navigasyonu
- **Hızlı Erişim Kenar Çubuğu:** Masaüstü, Belgeler, İndirilenler, Müzik, Resimler ve Videolar'a tek tıkla erişim
- **Özel Klasör Seçimi:** Sisteminizdeki herhangi bir dizini göz atın ve seçin
- **Gerçek Zamanlı Dosya Listesi:** Dosyalar ad, tür, boyut ve değişiklik tarihi ile görüntülenir

### 🔍 Canlı Arama ve Önizleme
- **Anında Filtreleme:** Yazarken dosyaları arayın
- **Canlı Eylem Önizlemesi:** Herhangi bir işlemi gerçekleştirmeden önce kaç dosyanın etkileneceğini görün
- **Renk Kodlu Geri Bildirim:** Eşleşme bulunursa yeşil, bulunmazsa kırmızı

### 📝 Toplu Yeniden Adlandırma
- **Bul ve Değiştir:** Birden fazla dosya adındaki belirli metni bir kerede değiştirin
- **Önizleme Sayısı:** Yeniden adlandırmadan önce eşleşen dosya sayısını gösterir
- **Güvenli İşlem:** Orijinal dosyalar yeniden adlandırılır, çoğaltılmaz

### 📋 Kopyala ve Yeniden Adlandır
- **Orijinalleri Koru:** Değiştirilmiş adlarla kopyalar oluşturun
- **Eşzamanlı İşlem:** Tek bir eylemde kopyalama ve yeniden adlandırma
- **Sürüm Oluşturma için İdeal:** Yeni sürümler oluştururken yedekleri koruyun

### 🗑️ Güvenli Silme
- **Desen Eşleştirme:** Belirli metin içeren dosyaları silin
- **Onay Diyaloğu:** Silmeden önce tüm dosyaları listeler
- **Uyarı Sistemi:** Yanlışlıkla silmeyi önlemek için net uyarılar

### 🌍 Çoklu Dil Desteği (6 Dil)
| Dil | Bayrak |
|-----|--------|
| English | 🇬🇧 |
| Türkçe | 🇹🇷 |
| Azərbaycanca | 🇦🇿 |
| Español | 🇪🇸 |
| Русский | 🇷🇺 |
| 中文 | 🇨🇳 |

### ✨ Modern Arayüz
- **3 Panelli Düzen:** Kenar Çubuğu, Dosya Listesi, Eylem Merkezi
- **Özel Kaydırma Çubuğu:** Şık, modern kaydırma çubuğu tasarımı
- **Duyarlı Tasarım:** Minimum boyut kısıtlamaları arayüz bozulmasını önler
- **Dahili Yardım:** Yardım butonu ile erişilebilir yerelleştirilmiş kullanım kılavuzu

---

## 🏗️ Proje Yapısı (MVC Mimarisi)

```
O-File-Process/
├── main.py                    # Uygulama giriş noktası
├── app/
│   ├── models/
│   │   └── file_manager.py    # Dosya işlemleri mantığı
│   ├── views/
│   │   ├── main_window.py     # Ana pencere montajı
│   │   └── components/
│   │       ├── sidebar.py     # Sol navigasyon paneli
│   │       ├── file_table.py  # Orta dosya listesi
│   │       ├── action_center.py # Sağ eylem paneli
│   │       └── modern_button.py # Özel buton widget'ı
│   ├── controllers/
│   │   └── main_controller.py # Model ve View'ı bağlar
│   └── utils/
│       ├── translations.py    # Çoklu dil dizeleri
│       └── styles.py          # QSS stil sayfaları
└── requirements.txt
```

---

## 🛠️ Kurulum

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/hamer1818/O-File-Process.git
cd O-File-Process
```

### 2. Sanal Ortam Oluşturun
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

---

## 💻 Kullanım

```bash
python main.py
```

### Hızlı Başlangıç:
1. Kenar çubuğundan bir **klasör seçin** veya "Klasör Seç" butonunu kullanın
2. Filtre kutusunu kullanarak **dosyaları arayın** (isteğe bağlı)
3. Sağ panelden bir **eylem seçin**:
   - **Toplu Yeniden Adlandır:** Eski metin → yeni metin → Yeniden Adlandır'a tıklayın
   - **Kopyala ve Yeniden Adlandır:** Yukarıdakiyle aynı, ancak kopyalar oluşturur
   - **Güvenli Sil:** Eşleşen metin girin → silmeyi onaylayın
4. İşlemi gerçekleştirmeden önce **önizlemeyi kontrol edin** (eşleşen dosya sayısını gösterir)

---

## ⚙️ Teknik Detaylar

| Bileşen | Teknoloji |
|---------|-----------|
| Dil | Python 3.8+ |
| GUI Çerçevesi | PyQt6 |
| Mimari | MVC (Model-View-Controller) |
| Dosya İşlemleri | `os`, `shutil` |

---

## 📄 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

---

*Geliştirici: [Hamer1818](https://github.com/hamer1818)*