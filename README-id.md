## Terjemahan
[English](README.md) | [Bahasa Indonesia](README-id.md)

## 🚀 Selamat datang di _workshop_ _Event-Driven Microservices_ bersama AWS
Dalam _workshop_ ini, Anda akan membangun dan menerapkan serangkaian _microservices_ sederhana dengan pendekatan arsitektur _event-driven_.

Tujuan utama dari _workshop_ ini adalah untuk membangun fondasi untuk memperluas dan menskalakan arsitektur _microservices_ dengan memanfaatkan komunikasi sinkron dan asinkron (_synchronous and asynchronous communication_) - dengan pola koreografi (_coreography pattern_) dan pola orkestrasi (_orchestration pattern_).

Isi _workshop_ ini akan diperbarui secara berkala, dan jika Anda memiliki pertanyaan atau menemukan masalah dalam _workshop_ ini, harap ajukan pertanyaan/masalah tersebut sebagai Issue.

## Struktur _Workshop_
Repositori ini terdiri dari 3 _workshop_:

#### **Lab 1: Pengiriman dan Penerimaan Dasar (_Basic Dispatch Consume_)**
Dalam _workshop_ ini, Anda akan membangun 2 fungsi AWS Lambda. Satu fungsi AWS Lambda (sebagai Produsen) akan mengirimkan (_dispatch_) _event_, dan satu Fungsi AWS Lambda (sebagai Konsumen) akan menerima (_consume_) _event_. Selain menerima _event_, Konsumen juga akan menulis log ke AWS CloudWatch Logs untuk memastikan aliran prosesnya berjalan dengan baik.

[💻 Mulai _Workshop_ Ini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/1-lab-basicDispatchConsumeEvent)

#### **Lab 2: Membangun _Microservices_ Terkoreografi (_Building Choreographed Microservices_)**
Sebagai kelanjutan dari _workshop_ sebelumnya, pada _workshop_ kali ini Anda akan membangun sistem yang lebih kompleks yang melibatkan beberapa _microservices_. Anda akan mempelajari cara menggabungkan komunikasi sinkron dan asinkron karena ini adalah pola yang umum digunakan dalam membangun _microservices_.

Anda akan membangun HTTP API dengan Amazon API Gateway dan AWS Lambda. Di latar belakang, HTTP API akan mengirimkan _events_ ke Amazon EventBridge untuk pemrosesan _backend_. _Events_ ini akan diterima oleh 4 _microservices_ yang diwakili oleh beberapa fungsi AWS Lambda. Komunikasi antar _microservices_ di _backend_ akan berjalan secara asinkron dengan menerapkan pendekatan koreografi menggunakan Amazon EventBridge.

[💻 Mulai _Workshop_ Ini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/2-lab-choreographMicroservices)

#### **Lab 3: Mengorkestrasi _Microservices_ (_Orchestrating Microservices_)**
Selain koreografi, kita juga perlu memahami pendekatan lain yang disebut orkestrasi. Di lab ini, Anda akan membuat sebuah _state machine_ untuk mengelola orkestrasi antar _microservices_.

Dalam _workshop_ ini, Anda akan membangun sistem perbankan sederhana yang memiliki 4 domain. Sistem ini bertujuan untuk melakukan penilaian dan validasi sebelum pembukaan rekening di sebuah bank.

Anda akan mempelajari cara menggunakan AWS Step Functions untuk membangun _state machine_ untuk orkestrasi. Selain itu, Anda juga dapat menggunakan beberapa tipe status yang disediakan oleh AWS Step Functions.

[💻 Mulai _Workshop_ Ini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/3-lab-orchestrateMicroservices)

---

## Tingkat _Workshop_
_Workshop_ ini menyambut pengembang (_developer_) dari semua tingkatan.

_Workshop_ ini disusun sebagai permainan teka-teki di mana Anda perlu melengkapi satu set kode yang belum lengkap menjadi suatu kode yang lengkap. Ini adalah desain yang disengaja untuk membantu membangun pemahaman Anda tentang konsep tertentu dan membantu Anda memahami sumber daya yang diperlukan untuk mengembangkan dengan menggunakan layanan AWS.

---

## 🛑 Pertama-tama
Jika ini adalah kali pertama Anda menjalankan _workshop_ ini, bagian ini adalah bagian penting yang perlu Anda baca sebelum melanjutkan.

⚠️
>  Harap pastikan bahwa lingkungan pengembangan Anda memenuhi persyaratan di bawah dan sudah dikonfigurasi dengan benar sebelum memulai _workshop_ mana pun.

## **Persyaratan _Workshop_**

Persyaratan | Informasi Lanjutan | Catatan
--- | --- | ---
Akun AWS aktif | [Tautan](https://aws.amazon.com/) | Persyaratan wajib
AWS CDK | [Tautan](https://aws.amazon.com/cdk/) | Memerlukan Node JS   
AWS CLI | [Tautan](https://aws.amazon.com/cli/) | Membutuhkan akun AWS aktif. Harap konfigurasikan akun Anda seperti yang dijelaskan di [halaman](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) ini
Python 3.8 | [Tautan](https://www.python.org/downloads/release/python-380/) | Sebagian besar _workshop_ akan menggunakan Python 3.8   
Boto3 | [Tautan](https://aws.amazon.com/sdk-for-python/) | Amazon Web Services (AWS) _Software Development Kit_ (SDK) untuk Python
Node JS 10.30 atau versi lebih baru | [Tautan](https://nodejs.org/en/download/current/) | Node.js versi 13.0.0 hingga 13.6.0 are tidak kompatibel dengan AWS CDK

⚠️
> Karena kita akan menggunakan AWS CDK secara ekstensif dalam _workshop_ ini, harap konfigurasikan AWS CDK dengan benar untuk lingkungan pengembangan Anda. 

**Jika Anda belum melakukannya, silakan ikuti terlebih dahulu instruksi [di sini](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html).**

Singkatnya, berikut ini adalah daftar prasyarat wajib yang harus Anda lakukan.
- [ ] Install AWS CLI  
- [ ] Konfigurasikan AWS CLI dengan `aws configure`  
- [ ] Install Node JS  
- [ ] Install AWS CDK dengan `npm install -g aws-cdk`  
- [ ] Konfigurasikan AWS CDK dengan `cdk bootstrap`

## Menjelajahi _Workshop_
Nama Lab | Tingkat | Durasi
--- | --- | ---
[Lab 0 - Pemeriksaan Persyaratan](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/0-requirements-checking) | Semua tingkat | 15 menit
[Lab 1 - Pengiriman dan Penerimaan Dasar](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/1-lab-basicDispatchConsumeEvent) | Pemula | 15 menit
[Lab 2 - Membangun _Microservices_ Terkoreografi](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/2-lab-choreographMicroservices) | Menengah | 30 menit
[Lab 3 - Mengorkestrasi _Microservices_](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/3-lab-orchestrateMicroservices) | Menengah | 15 menit

### **💡 PETUNJUK** dan **😕 Anda kebingungan?**
Untuk tugas yang lebih kompleks yang harus Anda selesaikan, akan ada **💡 PETUNJUK** untuk memandu Anda menyelesaikannya. Seringkali, petunjuk tersebut juga akan menyertakan (beberapa) tautan untuk bacaan lebih lanjut.

Harap diingat bahwa jika Anda mengalami kebingungan dan tidak dapat melanjutkan ke langkah berikutnya, Anda selalu dapat melihat berkas referensi utama untuk melihat solusinya. Untuk akses yang mudah, **😕 Anda kebingungan?** akan memandu Anda langsung ke solusinya.

## Layanan AWS
Beberapa layanan AWS yang digunakan dalam _workshop_ ini adalah sebagai berikut:
- [AWS CDK](https://aws.amazon.com/cdk/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

## ⚠️  Pembersihan
_Workshop_ ini menggunakan layanan AWS yang sebagian besarnya tercakup dalam Tingkat Gratis (_Free Tier_) - HANYA jika akun Anda berusia kurang dari 12 bulan. Untuk akun yang sudah tidak memenuhi persyaratan kelayakan tingkat gratis, _workshop_ ini mungkin akan menimbulkan beberapa biaya. Untuk meminimalkan biaya, pastikan Anda **menghapus sumber daya yang digunakan dalam _workshop_ ini setelah Anda selesai**.

Semua lab di _workshop_ ini menggunakan metode pembersihan standar dengan AWS CDK.
1. Pergi ke masing-masing lab
2. Ubah direktori menjadi `cdk /`
3. Jalankan `cdk destroy`
4. Jika dalam beberapa kasus Anda gagal membersihkan sumber daya, Anda harus membuka [AWS CloudFormation](https://console.aws.amazon.com/cloudformation/) dan menghapus _stack_ CloudFormation secara manual.