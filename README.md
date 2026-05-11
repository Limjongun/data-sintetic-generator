# Indonesian Article Summarization Dataset Generator

Project ini berisi script Python untuk membuat dataset sintetis berbahasa Indonesia yang dapat digunakan untuk latihan Natural Language Processing (NLP), khususnya pada task **text summarization**, **article classification**, dan **entity extraction**.

Dataset yang dihasilkan memiliki tiga jenis artikel utama, yaitu:

- Berita
- Cerita
- Fakta

Setiap data berisi artikel panjang, ringkasan, subjek penting, dan jenis artikel.

---

## Tujuan Project

Tujuan utama project ini adalah membuat dataset sederhana namun terstruktur untuk kebutuhan eksperimen NLP.

Dataset ini dapat digunakan untuk:

- Latihan text summarization
- Klasifikasi jenis artikel
- Ekstraksi subjek atau tokoh penting
- Eksperimen preprocessing teks bahasa Indonesia
- Pembuatan model NLP sederhana
- Dataset dummy untuk project portfolio AI atau Data Science

---

## Struktur Dataset

Setiap item dalam dataset memiliki format JSON seperti berikut:

```json
{
  "article": "Isi artikel lengkap...",
  "summarizer": "Ringkasan artikel...",
  "subjek_objek_penting": ["Nama Tokoh"],
  "jenis_artikel": "berita"
}
