import random

# Hakkınızdaki gerçeklerin listesi

gercekler = [

    "Word dosyasında roman yazıyorum.",

    "Pek çok farklı konuda şiirler yazıyorum.",

    "Açtığım Türk Tarihi isimli WhatsApp kanalında bildiklerimi paylaşıyorum ",

    "Gelecekte yurtdışında çalışmayı hedefliyorum.",

    "İlerde tarih okumayı düşünüyorum.",
    
    "Kodlama öğrenerek yeni dünyaya ayak uydurmaya çalışıyorum"

]

# Rastgele bir gerçek seç ve yazdır

rastgele_gercek = random.choice(gercekler)

print("Kendim hakkında bir gerçek:", rastgele_gercek)
