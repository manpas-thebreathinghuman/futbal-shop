Nama : Muhammad Fadhlurrohman Pasya

NPM : 2406411830

Kelas : PBP E

Tugas 2

1. Pertama, saya coba mengetes bagian mana saja yang perlu dan dengan urutan bagaimana (gagal)
percobaan kedua mengikuti tutorial, tapi memperhatikan bagian-bagian mana yang saya perlu ganti. seperti contohnya, schemanya yang merupakan tugas individu, dan models yang diganti dari news menjadi product
mungkin akan coba lagi dengan lebih sedikit melihat tutorial nanti (tugas 3?)
btw main saya tulis sendiri tampa nyontek tutorial karena saya pernah membuat kode html sbelumnya (satu kali)
2. client merequest dengan suatu url yang di cek di urls.py yang menjalankan views di views.py yang menggunakan template yang ditulis di file html. dari situ akan melakukan hal-hal data dengan data yang di atur di model.html
3. setting.py penting karena settings menyimpan segala setting konfigurasi yang diterapkan
4. dari data model yang telah diubah, kta lalu membuat migration file yang djnago proses. nanti ada python file yang berisi perubahannya.
Lalu, saat kta migrate, django melihat file file yang di migration lalu di aplikasikan.
5. karena mengggunakan python, sehingga mudah
6. tidak ada yang major, gpp gpp aja sejauh ini

Tugas 3

1. Supaya data-data relevan yg ada di server bisa dilihat klien
2. Karena json lebih mudah dibaca dari xml
3. Guna is_valid() adalah untuk mengecek apakah form-nya valid atau tidak. Ini diperlukan supaya tidak ada input salah yang diproses
4. Guna csrf_token secara otomatis di generate django untuk security dari serangan csrf (Cross-Site Request Forgey). Jika tidak ada csrf_token, penyerang bisa mengubah data (seperti mengubah password atau melakukan pembelian) atas nama user.
5. Seperti sebelumnya, saya pertama menyontek tutorial. Tapi ternyata banyak hal yang perluh diubah kali ini (lebih banyak dari sebelumnya). Terutama di bagian yang saya tidak tambahkan/saya ubah di tugas 2. Contoh yang paling obvious adalah nama model yang sebelumnya News, saya ubah jadi Product. Juga ada news jadi item. Dan favorit saya, news_item jadi item_thing.
Juga betulin easter egg, sama ternyata perluh id (saya tidak sertakan di tugas 2)
Juga yang ditunjukkan diubah dari hal relevan di news (seperti view count dll) saya ubah jadi hal yang relevan di shop (seperti price dll)
![alt text](images_screenshot/json.png)
![alt text](images_screenshot/xml.png)
![alt text](images_screenshot/jsonbyid.png)
![alt text](images_screenshot/xmlbyid.png)