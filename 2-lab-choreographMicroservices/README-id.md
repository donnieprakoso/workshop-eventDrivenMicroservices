# Lab 2: Membangun _Microservices_ Terkoreografi
[English](README.md) | [Bahasa Indonesia](README-id.md)

Sebagai kelanjutan dari _workshop_ sebelumnya, pada _workshop_ kali ini Anda akan membangun sistem yang lebih kompleks dan melibatkan beberapa _microservices_. Anda akan mempelajari cara menggabungkan komunikasi sinkron dan asinkron karena ini adalah pola yang umum digunakan dalam membangun _microservices_.

Anda akan membangun HTTP API dengan Amazon API Gateway dan AWS Lambda. Di latar belakang, HTTP API akan mengirimkan _events_ ke Amazon EventBridge untuk pemrosesan _backend_. _Events_ ini akan diterima oleh 4 _microservices_ yang diwakili oleh beberapa fungsi AWS Lambda. Komunikasi antar _microservices_ di _backend_ akan berjalan secara asinkron dengan menerapkan pendekatan koreografi menggunakan Amazon EventBridge.

## Diagram
![Diagram Lab 2](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/2-lab-choreographMicroservices/lab2-diagram.png)

## Tugas
Ini adalah tugas-tugas yang harus Anda kerjakan. Jika Anda mengalami kebingungan, silakan rujuk referensi utama di folder `source/`.

### Langkah 0: Persiapkan folder `work` dan boto3
#### Install _library_ boto3
- Buka terminal
- Jalankan perintah berikut
```bash
pip install boto3
```

#### Persiapkan folder `work`
- Masuk ke folder `work/`
- Anda akan menemukan 2 subdirektori dengan nama `cdk` dan `lambda-functions`

### Langkah 1: Menata folder `work` fungsi AWS Lambda
- Masuk ke folder `work/lambda-functions/`
- Anda akan menemukan 5 subdirektori di folder ini:
1. `forecasting-service`
2. `fulfilment-service`
3. `invoice-service`
4. `logistic-service`
5. `order-service`

### Langkah 2: Mengerjakan `order-service`
- Masuk ke `work/lambda-functions/order-service`
- Buka `app.py`

### Langkah 3: Buat fungsi untuk menyimpan data
- Tugas pertama dalam file ini adalah membuat sebuah function untuk menyimpan data ke Amazon DynamoDB. Anda hanya perlu menyimpan 2 variabel, ID dan _timestamp_ waktu saat ini. ID akan disimpan dalam field `ID` dan _timestamp_ dalam field `time_order_service`

> **💡 PETUNJUK**
>- Gunakan API `update_item()` untuk menyimpan data ke DynamoDB. Anda dapat melihat referensi API terkait [di sini](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.update_item)

> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/2-lab-choreographMicroservices/source/lambda-functions/order-service/app.py)

### Langkah 4: Buat sebuah Dictionary untuk _payload data_ 
- Pertama, buat sebuah variabel Dictionary untuk menampung semua data yang dikirim ke Amazon EventBridge dan beri nama `data`  
		
```python
    data = {}
    data['metadata'] = {"service": "demo-eventbridge"}
    data['data'] = {}          
    data['data']['ID'] = id		
```

### Langkah 5: Buat sebuah fungsi untuk mengirim _event_
- Kemudian, kirim _event_ ke Amazon EventBridge. 
- Jangan lupa untuk memformat `data` sebagai JSON dan memasukannya sebagai parameter `Detail`
- Hal-hal lain yang perlu Anda tambahkan:
	- Source: `order_service`
	- DetailType: `order_created`
	- Detail: [harus dalam format JSON]	
    - EventBusName: [dapatkan informasi ini dari _environment variable_ bernama "EVENTBUS_NAME"]

>**💡 PETUNJUK**
> - Anda memerlukan sebuah _client_ untuk terhubung ke sumber daya AWS. Pada Python, Anda perlu menggunakan _library_ boto3
> - Gunakan API put_events() untuk mengirim _event_ ke Amazon EventBridge. Berikut ini [tautannya](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html)
> - Gunakan`json.dumps()` untuk mengubah Dictionary menjadi JSON string. Berikut ini [dokumentasinya](https://docs.python.org/3/library/json.html)
>- Gunakan `os.getenv()` untuk mendapatkan data dari _environment variable_

> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/2-lab-choreographMicroservices/source/lambda-functions/order-service/app.py)

### Langkah 6: Panggil fungsi save_to_db()
- Terakhir, simpan data ke database dengan memanggil fungsi save_to_db() yang sudah kita buat sebelumnya
- Ingat, kita hanya perlu memberikan ID
- _Timestamp_ akan dibuat secara otomatis oleh fungsi yang ada
- Berikut ini kode yang dibutuhkan:
```python
save_to_db(id)
```
> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/2-lab-choreographMicroservices/source/lambda-functions/order-service/app.py)

### Langkah 7: Mengerjakan `logistic-service`
**Anda tidak perlu melakukan apa pun.** Bagian ini sudah disediakan di dalam file `work/lambda-functions/logistic-service/app.py` sebagai sebuah kode tetapi dalam bentuk **belum lengkap**. Tugas tambahan harus dilakukan setelah menyelesaikan langkah 17.

### Langkah 8: Mengerjakan `invoice-service`
**Anda tidak perlu melakukan apa pun.** Bagian ini sudah disediakan di dalam file `work/lambda-functions/invoice-service/app.py` yang kodenya sudah lengkap.

### Langkah 9: Mengerjakan `fulfilment-service`
**Anda tidak perlu melakukan apa pun.** Bagian ini sudah disediakan di dalam file `work/lambda-functions/fulfilment-service/app.py` sebagai sebuah kode tetapi dalam bentuk **belum lengkap**. Tugas tambahan harus dilakukan setelah menyelesaikan langkah 17.

### Langkah 10: Mengerjakan `forecasting-service`
**Anda tidak perlu melakukan apa pun.** Bagian ini sudah disediakan di dalam file `work/lambda-functions/forecasting-service/app.py` yang kodenya sudah lengkap.

### Langkah 11: Setting cdk.json
- Masuk ke `work/cdk/`
- Buat sebuah file dengan nama `cdk.json`
- Buka `cdk.json` dan tuliskan baris-baris berikut. Baris-baris ini akan memberi instruksi untuk AWS CDK tentang cara membangun aplikasi ini
```json
{
	"app":"python3 app.py",
	"context":{}
}
```
- Buka `app.py`. Di dalam file ini, Anda akan menemukan bahwa ada beberapa hal yang perlu kita tambahkan untuk membuatnya menjadi set kode yang lengkap. Baca file ini secara menyeluruh dan lakukan langkah-langkah berikutnya di bawah

### Langkah 12: Buat Pola EventBridge
- Buat pola EventBridge untuk order yang dibuat   

>**💡 PETUNJUK**
>- Gunakan objek EventPattern untuk menerapkan polanya untuk Amazon EventBridge. Berikut ini [referensi API](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_events/EventPattern.html) terkait

> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/2-lab-choreographMicroservices/source/cdk/app.py)

### Langkah 13: Buat EventBridge Rule
- Buat EventBridge Rule untuk order_created
- Tambahkan 3 target ke Rule ini. Dengan cara ini, Anda menentukan bagaimana aturan ini akan dipicu dan mengirim _event_ ke target yang ditentukan

>**💡 PETUNJUK**
>- Gunakan _construct_ Rule construct untuk membuat EventBridge Rule. Berikut ini [referensi API](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_events/Rule.html) terkait

> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/2-lab-choreographMicroservices/source/cdk/app.py)

### Langkah 14: Review integrasi Amazon API GAteway
- Perhatikan integrasi Amazon API Gateway dengan `order_service`. Integrasi ini dideklarasikan dengan metode GET dan _resource URI_ `/order`. 

### Langkah 15: Install semua _library_ yang dibutuhkan untuk membangun dan menjalankan aplikasi CDK
- Buka terminal
- Masuk ke `work/cdk/`
- Buat sebuah file dengan nama `requirements.txt`. Ini adalah metode standar untuk menginstall _libraries_ yang dibutuhkan untuk aplikasi Python
- Tuliskan baris-baris berikut:
```
aws-cdk.core==1.70.0
aws-cdk.aws-iam==1.70.0
aws-cdk.aws-lambda==1.70.0
aws-cdk.aws-apigateway==1.70.0
aws-cdk.aws-events==1.70.0
aws-cdk.aws-events-targets==1.70.0
aws-cdk.aws-dynamodb==1.70.0
```
- Install _libraries_ yang dibutuhkan dengan menjalankan perintah berikut di terminal:
```bash
pip3 install -r requirements.txt
```

### Langkah 16: Deploy
- Buka terminal
- Masuk ke `work/cdk/`
- Deploy aplikasi dengan menjalankan:
```bash
cdk deploy
```
- Ketika Anda sudah selesai mendeploy aplikasi CDK, Anda akan mendapatkan sebuah _API endpoint_ yang berjalan di Amazon API Gateway dan terintegrasi dengan fungsi Lambda yang menyediakan `order-service`. **Catat URL ini.**

### Langkah 17: Pengujian
- Buka _web browser_ Anda dan buka endpoint URL yang dibuat dengan _URI path_ untuk _resource_ Anda. Contoh: `https://<ENDPOINT_URL>/prod/order`
- Setelah order sukses dibuat, Anda akan melihat pesan: `order_created`

![Lab 2: Response API](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/2-lab-choreographMicroservices/lab2-api-response.png)

- Di latar belakang, sistem ini mengirim _event_ ke Amazon EventBridge dan menyimpan data ke Amazon DynamoDB.

#### Ayo periksa DynamoDB kita
- Masuk ke [dashboard DynamoDB](https://ap-southeast-1.console.aws.amazon.com/dynamodb/home?region=ap-southeast-1#tables:) dan gunakan `lab2` sebagai kata kunci pencarian
- Buka tabel
- Anda akan melihat bahwa sebuah data sudah dibuat dengan _timestamp_ terbaru untuk `order-service`, `invoice-service`, `fulfilment-service` dan `forecasting-service`

![Lab 2: Hasil uji DynamoDB](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/2-lab-choreographMicroservices/lab2-dynamodb-1.png)

#### ⚠️ TAPI TUNGGU DULU, bagaimana dengan `logistic-service`? ⚠️
Di titik ini, Anda telah mengetahui cara mengintegrasikan Amazon EventBridge dengan fungsi AWS Lambda dan cara menggunakan CDK untuk menyediakan semua sumber daya.

Langkah-langkah berikutnya adalah opsional dan silakan bersihkan sumber daya yang dibuat pada _workshop_ ini jika Anda tidak ingin melanjutkan.

### Langkah 18: Meningkatkan sistem untuk melibatkan `logistic-service`
#### Mengerjakan `fulfilment-service`
- Masuk ke `work/lambda-functions/fulfilment-service/`
- Buka app.py
- Lengkapi tugas untuk mengirim _event_ `fulfilment_completed` sehingga `logistic_service` dapat menerima pesan tersebut

> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/2-lab-choreographMicroservices/source/lambda-functions/fulfilment-service/app.py)

#### Mengerjakan `logistic-service`
- Masuk ke `work/lambda-functions/logistic-service/`
- Buka `app.py`
- Lengkapi tugas untuk mengurai (_parse_) _event_ dari Amazon EventBridge
- Simpan data ke DynamoDB

> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/2-lab-choreographMicroservices/source/lambda-functions/logistic-service/app.py)

#### Memperbarui aplikasi CDK
- Masuk ke `work/cdk/`
- Buka `app.py`
- Cari `[ADDITIONAL TASK]` dan buat pola EventBridge dan EventBrige Rule untuk pesan `fulfilment_completed`

> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/2-lab-choreographMicroservices/source/cdk/app.py)

### Langkah 19: Deploy ulang aplikasi CDK
- Buka terminal
- Masuk ke `work/cdk/`
- Periksa perubahan dengan menjalankan `diff`:
```bash
cdk diff
```
- Setelah Anda pikir semuanya baik dan benar, Anda bisa mendeploy aplikasi dengan menjalankan:
```bash
cdk deploy
```

### Langkah 20: Pengujian
- Buka _web browser_ Anda dan buka endpoint URL yang dibuat dengan _URI path_ untuk _resource_ Anda. Contoh: `https://<ENDPOINT_URL>/prod/order`
- Setelah order sukses dibuat, Anda akan melihat pesan sukses. Di latar belakang, sistem ini mengirim _event_ ke Amazon EventBridge dan menyimpan data ke Amazon DynamoDB.

#### Ayo periksa DynamoDB kita
- Masuk ke [dashboard DynamoDB](https://ap-southeast-1.console.aws.amazon.com/dynamodb/home?region=ap-southeast-1#tables:) dan gunakan `lab2` sebagai kata kunci pencarian
- Buka tabel
- Anda akan melihat bahwa sebuah data sudah dibuat dengan _timestamp_ terbaru untuk `order-service`, `invoice-service`, `fulfilment-service`, `forecasting-service`, dan terakhir `logistic-service`

![Lab 2: Tabel DynamoDB](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/2-lab-choreographMicroservices/lab2-dynamodb-2.png)

# 🤘🏻 Selamat! 
Anda telah menyelesaikan Lab 2

## Pembersihan
Untuk menghapus semua sumber daya, ikuti instruksi-instruksi di bawah:
1. Masuk ke `work/cdk/`
2. Jalankan perintah `cdk destroy`
```bash
cdk destroy
```