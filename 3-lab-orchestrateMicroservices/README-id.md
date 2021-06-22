# Lab 3: Mengorkestrasi _Microservices_
[English](README.md) | [Bahasa Indonesia](README-id.md)

Selain koreografi, kita juga perlu memahami pendekatan lain yang disebut orkestrasi. Di lab ini, Anda akan membuat sebuah _state machine_ untuk mengelola orkestrasi antar _microservices_.

Dalam _workshop_ ini, Anda akan membangun sistem perbankan sederhana yang memiliki 4 domain. Sistem ini bertujuan untuk melakukan penilaian dan validasi sebelum pembukaan rekening di sebuah bank.

Anda akan mempelajari cara menggunakan AWS Step Functions untuk membangun _state machine_ untuk orkestrasi. Selain itu, Anda juga dapat menggunakan beberapa tipe status yang disediakan oleh AWS Step Functions.

## Diagram
![Diagram Lab 3](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/3-lab-orchestrateMicroservices/lab3-diagram.png)

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
- Masuk ke `work/lambda-functions/` 
- Anda akan menemukan 3 subdirektori fungsi AWS Lambda. Di lab ini, Anda tidak perlu mengerjakan fungsi AWS Lambda

### Langkah 1: Membangun Aplikasi AWS CDK
#### Masuk ke folder `work`
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

### Langkah 2: Buat dua _Tasks_
- Anda perlu membuat 2 _tasks_ untuk servis `check-address` dan `approve-reject` 
- Anda akan menemukan sebuah _task_ `verify-identity` sudah dibuat terlebih dahulu, gunakan contoh ini untuk membuat 2 _tasks_ lain

> **💡 PETUNJUK**   
> - Gunakan _construct_ LambdaInvoke untuk membuat sebuah _task_. Berikut ini [referensi API](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_stepfunctions_tasks/LambdaInvoke.html) terkait
> - If you're not using AWS Lambda function, you can use other available constructs to build a task.

> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/3-lab-orchestrateMicroservices/source/cdk/app.py)

### Langkah 3: Buat dua _states_
- Anda perlu membuat dua _states_ dan golongkan keduanya sebagai `Succeed` untuk _state_ `approved` dan `rejected`

> **💡 PETUNJUK**
> - Gunakan _construct_ `Succeed` untuk membuat definisi _state_. Berikut ini [referensi API](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_stepfunctions/Succeed.html) terkait

> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/3-lab-orchestrateMicroservices/source/cdk/app.py)

### Langkah 4: Buat sebuah _parallel_
- Buat sebuah _parallel_ untuk menjalankan _task_ `verify-identity` dan `check-address` secara bersamaan
- Gunakan `$.Payload` sebagai `output_path` untuk memilih bagian _state_ yang kita gunakan sebagai output

> **💡 PETUNJUK**
> - Gunakan _construct_ `Parallel` untuk menjalankan satu atau lebih _task_ di waktu yang sama. Berikut ini [referensi API](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_stepfunctions/Parallel.html) terkait

> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/3-lab-orchestrateMicroservices/source/cdk/app.py)

### Langkah 5: Bagian terakhir, membuat sebuah _state machine_ 
- Gunakan _construct_ `StateMachine` untuk menyelesaikan tugas ini 
- Perhatikan bahwa `definition` untuk StateMachine sudah dibuat sebelumnya, dimulai dari `s_verification` dan dilanjutkan dengan `c_human_review` sebagai tujuan _state_ berikutnya

>**💡 PETUNJUK**
> - Berikut ini [referensi API](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_stepfunctions/StateMachine.html) terkait

> ### 😕 Anda kebingungan?
> Lihat solusinya [di sini](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/3-lab-orchestrateMicroservices/source/cdk/app.py)

### Langkah 6: Install semua _library_ yang dibutuhkan untuk membangun dan menjalankan aplikasi CDK
- Buka terminal
- Masuk ke `work/cdk/`
- Buat sebuah file dengan nama `requirements.txt`. Ini adalah metode standar untuk menginstall _libraries_ yang dibutuhkan untuk aplikasi Python
- Tuliskan baris-baris berikut:
```
aws-cdk.core==1.70.0
aws-cdk.aws-iam==1.70.0 
aws-cdk.aws-lambda==1.70.0
aws-cdk.aws-stepfunctions==1.70.0
aws-cdk.aws-stepfunctions-tasks==1.70.0
```
- Install _libraries_ yang dibutuhkan dengan menjalankan perintah berikut di terminal:
```bash
pip3 install -r requirements.txt
```

### Langkah 7: Deploy
- Buka terminal
- Masuk ke `work/cdk/`
- Deploy aplikasi dengan menjalankan:
```bash
cdk deploy
```
- Di titik ini, _state machine_ Anda sudah selesai dibuat. Masuk ke [dashboard AWS StepFunctions](https://ap-southeast-1.console.aws.amazon.com/states/home?) untuk melihat _state machines_ Anda

### Langkah 8: Pengujian
- Dari dashboard AWS StepFunctions, cari _state machine_ Anda dengan mengetikkan kata kunci `lab3`
- Klik link untuk membuka _state machine_ tersebut

![Lab 3: Definisi Visual State Machine](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/3-lab-orchestrateMicroservices/lab3-definition.png)
 
#### Skenario uji 1: Permohonan disetujui otomatis (_auto approved_)
- Klik tombol `Start Execution` di pojok kanan atas
- Di bagian Input, salin dan tempel JSON di bawah:
```json
{
  "name": "Scenario 1",
  "document": true,
  "address": true,
  "amount": 1000
}
```
- Klik `Start Execution` dan tunggu hingga selesai
- _State machine_ Anda akan otomatis menyetujui permohonan pembukaan rekening

![Lab 3: Skenario 1](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/3-lab-orchestrateMicroservices/lab3-scenario1.png)

#### Skenario uji 2: Permohonan disetujui melalui tinjauan manusia (_human review checking_)
- Klik tombol `Start Execution` di pojok kanan atas
- Di bagian Input, salin dan tempel JSON di bawah:
```json
{
  "name": "Scenario 2",
  "document": false,
  "address": true,
  "amount": 5000
}
```
- Klik `Start Execution` dan tunggu hingga selesai
- _State machine_ Anda akan masuk ke state `Human Review Required` sebelum akhirnya pergi ke `Approve Application`

![Lab3: Skenario 2](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/3-lab-orchestrateMicroservices/lab3-scenario2.png)

#### Skenario uji 3: Permohonan ditolak melalui tinjauan manusia
- Klik tombol `Start Execution` di pojok kanan atas
- Di bagian Input, salin dan tempel JSON di bawah:
```json
{
  "name": "Scenario 3",
  "document": false,
  "address": false,
  "amount": 10000
}
```
- Klik `Start Execution` dan tunggu hingga selesai
- _State machine_ Anda akan masuk ke state `Human Review Required` sebelum akhirnya pergi ke `Reject Application`

![Lab3: Skenario 3](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/3-lab-orchestrateMicroservices/lab3-scenario3.png)

# 🤘🏻 Selamat! 
Anda telah menyelesaikan Lab 3

## Pembersihan
Untuk menghapus semua sumber daya, ikuti instruksi-instruksi di bawah:
1. Masuk ke `work/cdk/`
2. Jalankan perintah `cdk destroy`
```bash
cdk destroy
```