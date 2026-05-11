import json
import random

random.seed(42)

# =========================
# 1) Seed item (BERITA)
# =========================
seed_item = {
  "article": "Kementerian Perdagangan menyatakan harga beras di sejumlah daerah mulai bergerak turun setelah pasokan dari sentra produksi meningkat dalam dua pekan terakhir. Dalam keterangan pers pada Kamis sore, pemerintah menilai stabilisasi pasokan dipengaruhi oleh masuknya panen dari beberapa wilayah, serta penguatan distribusi yang melibatkan pemerintah daerah dan BUMN pangan. Namun, pemerintah juga mengingatkan bahwa penurunan harga masih perlu dijaga karena permintaan cenderung meningkat menjelang bulan puasa.\n\nMenteri Perdagangan Zulkifli Hasan menjelaskan, pemantauan pasar dilakukan melalui koordinasi dengan dinas perdagangan di tingkat provinsi dan kabupaten/kota. Menurutnya, arus distribusi kini lebih lancar karena beberapa jalur logistik yang sebelumnya terkendala cuaca sudah kembali normal. Ia menambahkan, pemerintah meminta pedagang dan distributor menjaga ketersediaan stok agar tidak terjadi lonjakan harga mendadak.\n\nDi sisi lain, Bulog menyebutkan bahwa penyaluran beras stabilisasi pasokan dan harga (SPHP) masih terus dilakukan di pasar tradisional dan gerai yang ditunjuk pemerintah. Bulog juga menyampaikan bahwa persediaan cadangan pemerintah berada dalam kondisi aman, meskipun kebutuhan di beberapa daerah meningkat. Sejumlah pedagang di pasar tradisional mengatakan harga beras medium mulai turun Rp300 hingga Rp700 per kilogram dibanding pekan lalu, sementara beras premium relatif stabil.\n\nEkonom dari sebuah lembaga riset menilai tren penurunan harga beras dapat berlanjut jika pasokan tetap terjaga dan tidak ada gangguan distribusi. Meski begitu, ia mengingatkan adanya risiko spekulasi harga, terutama ketika informasi stok tidak merata di masyarakat. Pemerintah diminta memperkuat transparansi data stok dan mempercepat distribusi ke wilayah yang memiliki ketergantungan pasokan dari luar daerah.\n\nData pekan ini menunjukkan penurunan harga rata-rata di pasar tradisional sebesar 3 hingga 5 persen dibanding minggu sebelumnya. Pemerintah menyatakan akan memperketat pengawasan menjelang bulan puasa dan periode libur panjang, termasuk dengan inspeksi mendadak serta koordinasi lintas instansi untuk mencegah penimbunan. Jika terjadi kenaikan harga yang tidak wajar, pemerintah akan menambah pasokan operasi pasar dan memperluas titik distribusi.",
  "summarizer": "Kementerian Perdagangan menyebut harga beras di sejumlah daerah mulai menurun seiring meningkatnya pasokan dan membaiknya distribusi dalam dua pekan terakhir. Zulkifli Hasan mengatakan pemantauan bersama pemerintah daerah dilakukan untuk menjaga kelancaran logistik dan mencegah penahanan stok.\n\nBulog menyatakan penyaluran beras SPHP masih berjalan dan cadangan beras pemerintah dinilai aman, sementara pedagang mengaku harga beras medium turun Rp300–Rp700 per kilogram. Pemerintah diminta tetap waspada terhadap spekulasi dan penimbunan menjelang bulan puasa.",
  "subjek_objek_penting": ["Zulkifli Hasan"],
  "jenis_artikel": "berita"
}

# =========================
# 2) Data template
# =========================
KOTA = ["Bandung", "Surabaya", "Medan", "Makassar", "Semarang", "Yogyakarta", "Balikpapan", "Denpasar", "Palembang"]

# Nama orang saja (untuk cerita + berita)
NAMA_ORANG = [
  "Rina Pratama", "Andi Saputra", "Dewi Lestari", "Ahmad Fauzi", "Siti Nuraini",
  "Bima Mahendra", "Nadia Rahman", "Fajar Wirawan", "Intan Permata", "Rizky Maulana",

  "Agus Hari", "Ahmad Barjo", "Renjiro", "Novan Awaz", "Putri Wulandari",
  "Dimas Prakoso", "Aulia Rahmawati", "Fahmi Hidayat", "Nabila Putri", "Arif Setiawan",

  "Teguh Pramono", "Yuni Lestari", "Rangga Pratama", "Galih Santoso", "Salsabila Azzahra",
  "Rafi Prasetyo", "Vina Maharani", "Dinda Ayu", "Satria Wibowo", "Yusuf Ramadhan",

  "Hana Safitri", "Bagas Nugroho", "Fitri Handayani", "Rizal Firmansyah", "Aditia Putra",
  "Maya Anggraini", "Naufal Akbar", "Zahra Oktaviani", "Iqbal Maulana", "Rama Aditya",

  "Gita Puspitasari", "Doni Kurniawan", "Fina Aisyah", "Rio Saputro", "Dewangga Pramana",
  "Nisa Khairunnisa", "Alif Pratama", "Fikri Ramadhan", "Citra Laksmi", "Bunga Melati",

  "Kurnia Sari", "Tika Rahma", "Yudha Prabowo", "Rendy Setiabudi", "Putra Mahardika",
  "Lukman Hakim", "Rani Widyasari", "Hendra Gunawan", "Yani Kusuma", "Rifqi Ananda",

  "Adinda Maharani", "Daffa Prasetya", "Rossa Kartika", "Eko Pratama", "Taufik Hidayat",
  "Ayu Lestari", "Suci Ramadhani", "Mikhaela Putri", "Nanda Prameswari", "Dian Pratiwi",

  "Vicky Saputra", "Ilham Pranata", "Dodi Hermawan", "Asep Kurnia", "Bayu Pratomo",
  "Raka Pratama", "Gilang Ramadhan", "Niken Puspita", "Ari Wicaksono", "Rosa Amelia",

  "Fitria Ningsih", "Syahrul Hadi", "Reno Mahendra", "Aqila Nurazizah", "Farhan Alamsyah",
  "Nadya Salsabila", "Haris Pranowo", "Jihan Syakira", "Kevin Wicaksana", "Nayla Fadhilah",

  "Sandi Pratama", "Reza Firmansyah", "Mochammad Rizwan", "Dania Zahra", "Arman Saputra",
  "Fauzan Hakim", "Nurul Aini", "Wahyu Setyawan", "Rahmat Hidayat", "Dewi Kartikasari"
]


# Untuk berita: pejabat & pihak terkait (nama orang)
PEJABAT = [
  "Rina Pratama", "Andi Saputra", "Dewi Lestari", "Ahmad Fauzi", "Siti Nuraini",
  "Bima Mahendra", "Nadia Rahman", "Hendra Wijaya", "Maya Sari", "Rizky Pranoto",

  "Ayu Kartika", "Teguh Santoso", "Dimas Putranto", "Fitri Wulandari", "Arif Wicaksono",
  "Yuni Handayani", "Bagas Nugroho", "Satria Prabowo", "Lukman Hakim", "Nanda Prameswari",

  "Eleanor Brooks", "Michael Harrington", "Sophia Bennett", "Daniel Whitaker", "Olivia Carter",
  "James Thornton", "Amelia Foster", "Benjamin Clarke", "Charlotte Hayes", "William Anderson",

  "Isabella Rossi", "Matteo Conti", "Sofia Bianchi", "Luca Romano", "Giulia Ferraro",
  "Pierre Laurent", "Camille Dubois", "Antoine Moreau", "Claire Bernard", "Julien Lefevre",

  "Hans Mueller", "Anna Schneider", "Felix Weber", "Lena Fischer", "Jonas Wagner",
  "Kenji Tanaka", "Aiko Nakamura", "Hiroshi Sato", "Yuna Kim", "Min-Jun Park"
]


TOPIK_BERITA = [
  "harga pangan", "transportasi publik", "layanan kesehatan", "banjir perkotaan", "digitalisasi UMKM",
  "pendidikan vokasi", "kualitas udara", "energi terbarukan", "keamanan siber", "pariwisata",

  "harga beras", "harga minyak goreng", "harga gula", "harga telur", "harga cabai",
  "stok pangan nasional", "distribusi logistik", "operasi pasar", "subsidi pangan", "inflasi daerah",

  "ketersediaan obat", "antrian rumah sakit", "pemeriksaan gratis", "vaksinasi massal", "stunting",
  "gizi balita", "kesehatan ibu hamil", "wabah DBD", "pencegahan TBC", "penanganan demam berdarah",

  "perbaikan jalan", "kemacetan pusat kota", "tiket kereta", "jadwal kapal", "keselamatan penerbangan",
  "terminal terpadu", "rute bus baru", "transportasi laut", "kereta komuter", "tarif angkutan umum",

  "banjir rob", "longsor lereng", "kekeringan", "cuaca ekstrem", "gelombang tinggi",
  "peringatan dini bencana", "mitigasi bencana", "evakuasi warga", "posko darurat", "distribusi bantuan",

  "ketersediaan air bersih", "krisis air", "pengelolaan sampah", "TPA penuh", "bank sampah",
  "daur ulang plastik", "pencemaran sungai", "rehabilitasi mangrove", "hutan kota", "ruang terbuka hijau",

  "pembangkit listrik", "tarif listrik", "pemadaman bergilir", "energi surya", "energi angin",
  "biofuel", "kendaraan listrik", "stasiun pengisian", "efisiensi energi", "ketahanan energi",

  "keamanan data", "kebocoran data", "serangan ransomware", "penipuan online", "phishing",
  "perlindungan konsumen digital", "regulasi platform", "moderasi konten", "literasi digital", "pemberantasan judi online",

  "investasi daerah", "izin usaha", "perizinan online", "reformasi birokrasi", "pelayanan publik",
  "anggaran infrastruktur", "proyek jembatan", "revitalisasi pasar", "pembangunan pelabuhan", "pengembangan bandara",

  "pemilu daerah", "netralitas ASN", "transparansi anggaran", "pengawasan proyek", "anti korupsi",
  "penguatan KPK daerah", "audit internal", "e-government", "open data", "pengaduan masyarakat"
]


# Fakta: tetap pakai "tokoh" berupa nama pakar / peneliti (bukan konsep)
PAKAR = [
  "Dr. Nadia Rahman", "Dr. Ahmad Fauzi", "Prof. Dewi Lestari", "Dr. Bima Mahendra", "Prof. Siti Nuraini",
  "Dr. Rina Pratama", "Dr. Andi Saputra", "Prof. Hendra Wijaya", "Dr. Maya Sari", "Prof. Rizky Pranoto",

  "Dr. Ayu Kartika", "Prof. Teguh Santoso", "Dr. Dimas Putranto", "Prof. Fitri Wulandari", "Dr. Arif Wicaksono",
  "Prof. Yuni Handayani", "Dr. Bagas Nugroho", "Prof. Satria Prabowo", "Dr. Lukman Hakim", "Prof. Nanda Prameswari",

  "Dr. Eleanor Brooks", "Prof. Michael Harrington", "Dr. Sophia Bennett", "Prof. Daniel Whitaker", "Dr. Olivia Carter",
  "Prof. James Thornton", "Dr. Amelia Foster", "Prof. Benjamin Clarke", "Dr. Charlotte Hayes", "Prof. William Anderson",

  "Dr. Isabella Rossi", "Prof. Matteo Conti", "Dr. Sofia Bianchi", "Prof. Luca Romano", "Dr. Giulia Ferraro",
  "Prof. Pierre Laurent", "Dr. Camille Dubois", "Prof. Antoine Moreau", "Dr. Claire Bernard", "Prof. Julien Lefevre",

  "Dr. Hans Mueller", "Prof. Anna Schneider", "Dr. Felix Weber", "Prof. Lena Fischer", "Dr. Jonas Wagner",
  "Prof. Kenji Tanaka", "Dr. Aiko Nakamura", "Prof. Hiroshi Sato", "Dr. Yuna Kim", "Prof. Min-Jun Park"
]


TOPIK_FAKTA = [
  ("Vaksin", "Vaksin melatih sistem imun mengenali antigen sehingga respons lebih cepat saat paparan nyata."), ("Fotosintesis", "Fotosintesis mengubah energi cahaya menjadi energi kimia dan menghasilkan bahan organik serta oksigen."), ("Siklus air", "Siklus air meliputi evaporasi, kondensasi, presipitasi, infiltrasi, dan aliran permukaan."), ("Perubahan iklim", "Perubahan iklim dipengaruhi peningkatan gas rumah kaca yang memerangkap panas di atmosfer."), ("Keamanan data", "Enkripsi mengubah data menjadi bentuk tersandi agar hanya pihak berwenang yang dapat membacanya."), ("Gempa bumi", "Gempa bumi terjadi akibat pelepasan energi di kerak bumi pada zona patahan atau subduksi."), ("Letusan gunung api", "Letusan gunung api terjadi ketika tekanan magma dan gas meningkat lalu keluar melalui kawah atau rekahan."), ("Tsunami", "Tsunami umumnya dipicu gempa bawah laut, longsor, atau erupsi yang menggeser massa air secara tiba-tiba."), ("Petir", "Petir adalah pelepasan muatan listrik akibat perbedaan potensial di atmosfer, sering terjadi saat badai."), ("Pelangi", "Pelangi terbentuk karena pembiasan, pemantulan internal, dan dispersi cahaya matahari oleh tetesan air."),

  ("Gravitasi", "Gravitasi adalah gaya tarik-menarik antar massa yang memengaruhi gerak benda di alam semesta."), ("Inersia", "Inersia adalah kecenderungan benda mempertahankan keadaan geraknya kecuali ada gaya luar yang bekerja."), ("Hukum Newton", "Hukum Newton menjelaskan hubungan gaya, massa, dan percepatan dalam gerak benda."), ("Energi kinetik", "Energi kinetik adalah energi yang dimiliki benda karena bergerak dan bergantung pada massa serta kecepatan."), ("Energi potensial", "Energi potensial adalah energi tersimpan karena posisi atau keadaan, misalnya ketinggian atau elastisitas."), ("Konservasi energi", "Hukum kekekalan energi menyatakan energi tidak dapat diciptakan atau dimusnahkan, hanya berubah bentuk."), ("Tekanan udara", "Tekanan udara berasal dari berat kolom udara dan berubah menurut ketinggian serta kondisi cuaca."), ("Suara", "Suara adalah gelombang mekanik yang merambat melalui medium seperti udara, air, atau padatan."), ("Cahaya", "Cahaya adalah gelombang elektromagnetik yang dapat merambat tanpa medium dan membawa energi."), ("Spektrum elektromagnetik", "Spektrum elektromagnetik mencakup gelombang radio hingga sinar gamma berdasarkan panjang gelombang."),

  ("Atom", "Atom terdiri dari inti (proton-neutron) dan elektron; struktur ini menentukan sifat unsur."), ("Molekul", "Molekul adalah gabungan dua atau lebih atom yang terikat dan membentuk satuan kimia."), ("Ikatan kovalen", "Ikatan kovalen terjadi saat atom berbagi pasangan elektron untuk mencapai kestabilan."), ("Ikatan ion", "Ikatan ion terbentuk ketika elektron berpindah dari satu atom ke atom lain sehingga terbentuk ion."), ("Reaksi kimia", "Reaksi kimia mengubah zat awal menjadi zat baru melalui pemutusan dan pembentukan ikatan."), ("Asam dan basa", "Asam cenderung melepaskan ion H+, sedangkan basa menerima H+ atau menghasilkan ion OH-."), ("pH", "pH mengukur tingkat keasaman larutan; nilai rendah asam, tinggi basa, sekitar 7 netral."), ("Oksidasi-reduksi", "Redoks melibatkan perpindahan elektron; oksidasi kehilangan elektron, reduksi menerima elektron."), ("Katalis", "Katalis mempercepat reaksi kimia tanpa ikut habis, dengan menurunkan energi aktivasi."), ("Larutan", "Larutan adalah campuran homogen antara zat terlarut dan pelarut dengan komposisi tertentu."),

  ("Sel", "Sel adalah unit struktural dan fungsional dasar makhluk hidup yang menjalankan proses kehidupan."), ("DNA", "DNA menyimpan informasi genetik yang mengarahkan pertumbuhan, fungsi, dan pewarisan sifat."), ("RNA", "RNA berperan dalam sintesis protein dan regulasi gen, bekerja sebagai perantara informasi genetik."), ("Protein", "Protein tersusun dari asam amino dan berfungsi sebagai enzim, struktur, transport, dan sinyal."), ("Enzim", "Enzim adalah katalis biologis yang mempercepat reaksi metabolisme dengan spesifisitas tinggi."), ("Sistem imun", "Sistem imun melindungi tubuh dari patogen melalui respons bawaan dan adaptif."), ("Antibodi", "Antibodi adalah protein yang mengenali antigen dan membantu menetralkan atau menandai patogen."), ("Bakteri", "Bakteri adalah mikroorganisme prokariot yang dapat bermanfaat atau menyebabkan penyakit."), ("Virus", "Virus membutuhkan sel inang untuk bereplikasi dan dapat memicu penyakit pada manusia, hewan, atau tumbuhan."), ("Jamur", "Jamur adalah organisme heterotrof yang berperan sebagai dekomposer dan dapat dimanfaatkan atau patogen."),

  ("Rantai makanan", "Rantai makanan menggambarkan aliran energi dari produsen ke konsumen hingga pengurai."), ("Jaring-jaring makanan", "Jaring-jaring makanan adalah kumpulan rantai makanan yang saling terhubung dalam ekosistem."), ("Keanekaragaman hayati", "Keanekaragaman hayati mencakup variasi gen, spesies, dan ekosistem yang menjaga stabilitas alam."), ("Adaptasi", "Adaptasi adalah penyesuaian sifat organisme agar bertahan hidup di lingkungan tertentu."), ("Evolusi", "Evolusi adalah perubahan sifat populasi dari generasi ke generasi melalui seleksi dan variasi genetik."), ("Seleksi alam", "Seleksi alam meningkatkan peluang bertahan individu dengan sifat yang sesuai lingkungan."), ("Ekosistem", "Ekosistem terdiri dari komponen biotik dan abiotik yang saling berinteraksi."), ("Dekomposer", "Dekomposer menguraikan bahan organik mati menjadi unsur hara yang dapat digunakan kembali."), ("Siklus karbon", "Siklus karbon memindahkan karbon antara atmosfer, biosfer, hidrosfer, dan litosfer."), ("Siklus nitrogen", "Siklus nitrogen melibatkan fiksasi, nitrifikasi, asimilasi, dan denitrifikasi dalam lingkungan."),

  ("Pemanasan global", "Pemanasan global adalah kenaikan suhu rata-rata bumi akibat peningkatan efek rumah kaca."), ("Efek rumah kaca", "Efek rumah kaca terjadi ketika gas atmosfer menahan radiasi inframerah sehingga bumi lebih hangat."), ("Ozon", "Lapisan ozon menyerap radiasi UV berbahaya; penipisan ozon meningkatkan risiko bagi kesehatan."), ("Polusi udara", "Polusi udara berasal dari partikel dan gas berbahaya yang berdampak pada kesehatan dan lingkungan."), ("PM2.5", "PM2.5 adalah partikel halus yang dapat masuk jauh ke paru-paru dan meningkatkan risiko penyakit."), ("Air tanah", "Air tanah tersimpan di akuifer dan mengisi ulang melalui infiltrasi dari permukaan."), ("Akuifer", "Akuifer adalah lapisan batuan atau sedimen yang menyimpan dan mengalirkan air tanah."), ("Erosi", "Erosi adalah pengikisan tanah oleh air, angin, atau aktivitas manusia yang mengurangi kesuburan."), ("Sedimentasi", "Sedimentasi adalah pengendapan material yang terbawa air atau angin di lokasi baru."), ("Daur ulang", "Daur ulang mengolah kembali material agar dapat digunakan lagi, mengurangi sampah dan penggunaan sumber daya."),

  ("Energi surya", "Energi surya memanfaatkan radiasi matahari untuk menghasilkan listrik atau panas."), ("Panel surya", "Panel surya mengubah cahaya menjadi listrik melalui efek fotovoltaik pada material semikonduktor."), ("Energi angin", "Energi angin mengubah energi kinetik udara menjadi listrik menggunakan turbin."), ("Turbin angin", "Turbin angin menghasilkan listrik ketika baling-baling memutar generator akibat hembusan angin."), ("Energi air", "Energi air memanfaatkan aliran atau jatuhan air untuk menggerakkan turbin pembangkit listrik."), ("Biomassa", "Biomassa adalah bahan organik yang dapat diolah menjadi energi melalui pembakaran atau proses biokimia."), ("Biofuel", "Biofuel adalah bahan bakar dari biomassa, seperti biodiesel dan bioetanol."), ("Baterai", "Baterai menyimpan energi kimia dan mengubahnya menjadi energi listrik melalui reaksi elektrokimia."), ("Hidrogen", "Hidrogen dapat menjadi pembawa energi; pembakarannya menghasilkan air namun produksinya perlu energi."), ("Efisiensi energi", "Efisiensi energi berarti menghasilkan output yang sama dengan konsumsi energi lebih rendah melalui teknologi dan perilaku."),

  ("Internet", "Internet adalah jaringan global yang menggunakan protokol TCP/IP untuk pertukaran data."), ("Protokol TCP/IP", "TCP/IP mengatur pengiriman paket data agar komunikasi antar perangkat berjalan andal di jaringan."), ("DNS", "DNS menerjemahkan nama domain menjadi alamat IP agar perangkat dapat menemukan layanan di internet."), ("Alamat IP", "Alamat IP adalah identitas numerik perangkat di jaringan untuk mengirim dan menerima data."), ("Firewall", "Firewall menyaring lalu lintas jaringan untuk mencegah akses tidak sah dan serangan."), ("Malware", "Malware adalah perangkat lunak berbahaya yang dapat merusak, mencuri data, atau mengganggu sistem."), ("Phishing", "Phishing menipu pengguna agar memberikan data sensitif melalui pesan atau situs palsu."), ("Ransomware", "Ransomware mengenkripsi data korban dan meminta tebusan untuk pemulihan akses."), ("Autentikasi dua faktor", "2FA menambah lapisan keamanan dengan meminta verifikasi tambahan selain kata sandi."), ("Kata sandi kuat", "Kata sandi kuat umumnya panjang, unik, dan memadukan huruf, angka, serta simbol."),

  ("Kecerdasan buatan", "Kecerdasan buatan meniru kemampuan kognitif manusia untuk mengenali pola dan mengambil keputusan."), ("Pembelajaran mesin", "Machine learning melatih model dari data agar dapat memprediksi atau mengklasifikasi tanpa aturan eksplisit."), ("Jaringan saraf", "Jaringan saraf memproses informasi melalui lapisan neuron buatan untuk mempelajari pola kompleks."), ("Data latih", "Data latih digunakan untuk melatih model agar dapat mengenali hubungan input dan output."), ("Overfitting", "Overfitting terjadi ketika model terlalu menyesuaikan data latih sehingga kinerja pada data baru menurun."), ("Validasi", "Validasi mengukur kinerja model pada data yang tidak digunakan saat pelatihan untuk mencegah overfitting."), ("Regresi", "Regresi memodelkan hubungan variabel untuk memprediksi nilai kontinu dari data."), ("Klasifikasi", "Klasifikasi memetakan input ke kategori tertentu berdasarkan pola pada data."), ("NLP", "NLP mempelajari cara komputer memahami dan menghasilkan bahasa manusia dari teks atau suara."), ("Ringkasan otomatis", "Ringkasan otomatis memilih atau menghasilkan inti informasi dari teks panjang secara ringkas."),

  ("Gizi seimbang", "Gizi seimbang mencakup variasi pangan, kecukupan energi, protein, vitamin, mineral, dan hidrasi."), ("Kalori", "Kalori adalah satuan energi dalam makanan; kebutuhan berbeda menurut usia, aktivitas, dan kondisi tubuh."), ("Protein", "Protein penting untuk perbaikan jaringan, enzim, hormon, dan imunitas; sumbernya hewani dan nabati."), ("Karbohidrat", "Karbohidrat adalah sumber energi utama; pilih yang tinggi serat untuk kesehatan metabolik."), ("Lemak", "Lemak membantu penyerapan vitamin larut lemak dan menjadi cadangan energi; pilih lemak tak jenuh lebih sering."), ("Vitamin", "Vitamin mendukung fungsi tubuh; kekurangan vitamin tertentu dapat menyebabkan gangguan kesehatan."), ("Mineral", "Mineral seperti zat besi dan kalsium penting untuk darah, tulang, dan fungsi saraf."), ("Serat", "Serat membantu pencernaan, memberi rasa kenyang, dan mendukung kesehatan usus."), ("Hidrasi", "Hidrasi cukup membantu fungsi organ; kebutuhan cairan meningkat saat panas atau aktivitas tinggi."), ("Tidur", "Tidur memengaruhi metabolisme, mood, dan pemulihan; kualitas tidur baik mendukung kesehatan.")
]


# =========================
# 3) Generator per jenis
# =========================
def make_berita(i: int):
    kota = random.choice(KOTA)
    topik = random.choice(TOPIK_BERITA)
    pejabat = random.choice(PEJABAT)
    narasumber2 = random.choice([n for n in PEJABAT if n != pejabat])

    angka_persen = random.choice(["3–5", "4–6", "2–4", "5–8"])
    angka_rp = random.choice(["Rp200–Rp600", "Rp300–Rp700", "Rp500–Rp900"])
    waktu = random.choice(["sepekan terakhir", "dua pekan terakhir", "tiga pekan terakhir"])

    # Pastikan nama tokoh muncul di artikel
    article = (
        f"Pemerintah daerah di {kota} melaporkan perkembangan terkait {topik} setelah evaluasi pada {waktu}. "
        f"Menurut laporan lapangan, kondisi mulai membaik meski pengawasan tetap ditingkatkan menjelang periode permintaan tinggi.\n\n"
        f"{pejabat} menyampaikan bahwa koordinasi lintas pihak dilakukan untuk menjaga kelancaran distribusi dan mencegah gangguan layanan. "
        f"Ia menekankan pentingnya pemantauan rutin serta transparansi data agar masyarakat tidak terpengaruh informasi yang menyesatkan.\n\n"
        f"Sementara itu, {narasumber2} menilai perbaikan terlihat dari indikator rata-rata yang naik/turun sekitar {angka_persen} persen, "
        f"dengan perubahan biaya pada kisaran {angka_rp} di beberapa titik. Pemerintah menyiapkan langkah korektif bila terjadi anomali atau lonjakan."
    )

    summarizer = (
        f"Evaluasi {waktu} menunjukkan kondisi {topik} di {kota} mulai membaik, tetapi pengawasan tetap diperketat menjelang kenaikan permintaan. "
        f"{pejabat} menyatakan koordinasi dilakukan untuk memastikan distribusi dan layanan berjalan lancar serta data disampaikan secara transparan.\n\n"
        f"{narasumber2} menambahkan indikator berubah sekitar {angka_persen} persen dan ada penyesuaian pada kisaran {angka_rp}, sehingga pemerintah menyiapkan intervensi jika muncul lonjakan."
    )

    # subjek_objek_penting: hanya nama orang yang benar-benar ada di artikel
    return {
        "article": article,
        "summarizer": summarizer,
        "subjek_objek_penting": [pejabat, narasumber2],
        "jenis_artikel": "berita"
    }

def make_cerita(i: int):
    tokoh_utama = random.choice(NAMA_ORANG)
    tokoh_tambahan = random.choice([n for n in NAMA_ORANG if n != tokoh_utama])
    kota = random.choice(KOTA)
    objek = random.choice(["dompet", "kucing kecil", "sepeda tua", "buku catatan", "anjing terlantar", "tanaman layu"])
    pelajaran = random.choice(["lebih disiplin", "lebih berani", "lebih peduli", "lebih sabar", "lebih jujur"])

    article = (
        f"Suatu sore di {kota}, {tokoh_utama} pulang dengan langkah pelan karena jalanan masih ramai. "
        f"Di dekat rumah, ia menemukan {objek} yang membuatnya berhenti dan berpikir sejenak. "
        f"Awalnya ia ragu, tetapi ia memilih mendekat untuk memastikan tidak ada orang lain yang kehilangan.\n\n"
        f"{tokoh_utama} memutuskan menolong dengan cara sederhana: menyimpan {objek} itu dengan aman, "
        f"mencari pemiliknya lewat tetangga, dan meminta saran keluarga. Temannya, {tokoh_tambahan}, ikut membantu "
        f"dan mengingatkan agar semuanya dilakukan hati-hati supaya tidak menimbulkan salah paham.\n\n"
        f"Beberapa hari berlalu, situasi membaik dan {tokoh_utama} merasakan perubahan dalam rutinitasnya. "
        f"Ia jadi {pelajaran} karena belajar bertanggung jawab dan konsisten menyelesaikan masalah kecil. "
        f"Sejak saat itu, ia percaya kebaikan sering dimulai dari keputusan sederhana."
    )

    summarizer = (
        f"{tokoh_utama} menemukan {objek} saat pulang di {kota} dan memilih menolong meski sempat ragu. "
        f"Dengan bantuan {tokoh_tambahan}, ia menyimpan barang itu dengan aman dan mencari pemiliknya dengan cara yang hati-hati.\n\n"
        f"Pengalaman tersebut membuat {tokoh_utama} menjadi {pelajaran} dan menyadari bahwa kebaikan bisa berawal dari langkah kecil."
    )

    # subjek_objek_penting: hanya nama orang (hapus kota/objek)
    return {
        "article": article,
        "summarizer": summarizer,
        "subjek_objek_penting": [tokoh_utama, tokoh_tambahan],
        "jenis_artikel": "cerita"
    }

def make_fakta(i: int):
    topik, definisi = random.choice(TOPIK_FAKTA)
    pakar = random.choice(PAKAR)
    konteks = random.choice(["di sekolah", "di layanan publik", "di rumah tangga", "di wilayah perkotaan", "di fasilitas kesehatan"])
    faktor = random.choice(["ketersediaan sumber daya", "infrastruktur", "literasi informasi", "kualitas pelaksanaan", "akses layanan"])

    # Pastikan nama pakar muncul di artikel
    article = (
        f"{topik} adalah topik penting dalam sains dan kehidupan sehari-hari. {definisi} "
        f"Pemahaman konsep ini membantu masyarakat menilai informasi secara lebih kritis.\n\n"
        f"Menurut {pakar}, penerapan konsep {topik.lower()} dapat berbeda di tiap tempat karena dipengaruhi {faktor}. "
        f"Perbedaan konteks membuat hasil yang terlihat di lapangan tidak selalu sama, sehingga pengamatan dan data yang konsisten diperlukan.\n\n"
        f"Dalam praktik {konteks}, pemahaman {topik.lower()} berguna untuk perencanaan, pencegahan risiko, dan edukasi. "
        f"Langkah sederhana seperti mengikuti pedoman, memverifikasi sumber, dan mengevaluasi dampak dapat meningkatkan hasil."
    )

    summarizer = (
        f"{topik} merupakan konsep penting; {definisi.lower()} "
        f"{pakar} menjelaskan penerapannya bisa berbeda tergantung {faktor}, sehingga diperlukan pengamatan dan data yang konsisten.\n\n"
        f"Dalam konteks {konteks}, pemahaman {topik.lower()} membantu perencanaan dan edukasi dengan menerapkan pedoman serta verifikasi informasi."
    )

    # subjek_objek_penting: nama orang saja (pakar)
    return {
        "article": article,
        "summarizer": summarizer,
        "subjek_objek_penting": [pakar],
        "jenis_artikel": "fakta"
    }

# =========================
# 4) Buat 100 data (34/33/33)
# =========================
target_counts = {"berita": 1000, "cerita": 1000, "fakta": 1000}

items = [seed_item]  # seed sudah berita
counts = {"berita": 1, "cerita": 0, "fakta": 0}

to_make = (
    ["berita"] * (target_counts["berita"] - counts["berita"]) +
    ["cerita"] * target_counts["cerita"] +
    ["fakta"] * target_counts["fakta"]
)
random.shuffle(to_make)

for idx, jenis in enumerate(to_make, start=2):
    if jenis == "berita":
        items.append(make_berita(idx))
    elif jenis == "cerita":
        items.append(make_cerita(idx))
    else:
        items.append(make_fakta(idx))

assert len(items) == 3000
assert sum(1 for x in items if x["jenis_artikel"] == "berita") == 1000
assert sum(1 for x in items if x["jenis_artikel"] == "cerita") == 1000
assert sum(1 for x in items if x["jenis_artikel"] == "fakta") == 1000

out_file = "dataset_100_fixed22.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("OK:", out_file, "dibuat. Total:", len(items))
print("Proporsi:", {
    "berita": sum(1 for x in items if x["jenis_artikel"] == "berita"),
    "cerita": sum(1 for x in items if x["jenis_artikel"] == "cerita"),
    "fakta": sum(1 for x in items if x["jenis_artikel"] == "fakta"),
})
