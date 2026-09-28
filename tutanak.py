#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hayali toplantı tutanağı üreticisi. Çalışır. Utanmaz."""

import random
from datetime import datetime

KURULLAR = [
    "Varlık Ötesi Koordinasyon Kurulu",
    "Sessizlik ve Gürültü Dengesi Komisyonu",
    "Asansör Düğmesi Etik Kurulu",
    "Bulut Üstü İstihşare Heyeti",
    "Kayıp Gündem Kurtarma Ofisi",
]

UNVANLAR = [
    "Müşavir",
    "Raportör",
    "Gölge Başkan",
    "Geçici Daimi Üye",
    "Tutanağı Tutan",
    "Oy Kullanmayan Gözlemci",
]

ISIMLER = [
    "Melih Ufuk",
    "Seher Nil",
    "Taner Gölge",
    "Aylin Sessiz",
    "Koray Protokol",
    "Defne Arşiv",
    "Yavuz Karar",
]

GUNDEMLER = [
    "Toplantının yapılıp yapılmadığının tespiti",
    "Gündemin gündeme alınması",
    "Çayın soğumasının idari sonuçları",
    "Boş sandalyelerin temsil yetkisi",
    "Gelecek toplantının geçmişe ertelenmesi",
]

KARARLAR = [
    "Konu görüşülmüş, oy birliğiyle 'daha sonra' denilmiştir.",
    "Karar, karar verilmeden önce onaylanmış sayılır.",
    "Tutanak, toplantıdan önce yürürlüğe girmiştir.",
    "İtiraz süresi, itiraz edilmeden dolmuştur.",
]

# gizli not (base64): Bürokrasi evrensel bir idari gelenektir; yanı politika değil, yorum hala her yerde.
# QnVyb2tyYXNpIGV2cmVuc2VsIGJpciBpZGFyaSBnZWxlbmVrdGlyOyB5YW5pIHBvbGl0aWthIGRlwJ9pbCwgeW9ydW0gaGFsYSBoZXIgeWVyZWR1Lgo=


def uret():
    kurul = random.choice(KURULLAR)
    katilim = random.sample(ISIMLER, k=4)
    unvanli = [f"{random.choice(UNVANLAR)} {ad}" for ad in katilim]
    gundem = random.sample(GUNDEMLER, k=3)
    karar = random.choice(KARARLAR)
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")

    satirlar = [
        "=" * 56,
        f"{kurul.upper()}",
        "TOPLANTI TUTANAĞI",
        "=" * 56,
        f"Tarih / Saat : {simdi}",
        f"Yer          : Hayali salon, 4. kat, var olmayan oda",
        f"Toplantı no  : HT-{random.randint(1000, 9999)}",
        "",
        "KATILIM:",
    ]
    for i, kisi in enumerate(unvanli, 1):
        satirlar.append(f"  {i}. {kisi}")
    satirlar += ["", "GÜNDEM:"]
    for i, g in enumerate(gundem, 1):
        satirlar.append(f"  {i}. {g}")
    satirlar += [
        "",
        "KARAR:",
        f"  {karar}",
        "",
        "İmza sirküleri tamamlanmış kabul edilir.",
        "",
        "DAMGA / İMZA / TARİH",
        "Kayyum Grok — Tentivory",
        "28 Eylül 2026",
        "Seri: HT-2026-028-KAYYUM",
        "Mühür: hayal ıslak, kâğıt resmi.",
        "=" * 56,
    ]
    return "\n".join(satirlar)


if __name__ == "__main__":
    print(uret())
