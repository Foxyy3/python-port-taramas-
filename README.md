Tkinter GUI Oluşturma: Tkinter kullanarak bir pencere oluşturduk ve kullanıcıdan IP adresi, başlangıç ve bitiş portlarını girmesini istedik.
Taramayı Başlatma: Kullanıcı "Taramayı Başlat" butonuna tıkladığında start_scan fonksiyonu çalışır, kullanıcı girdilerini alır ve geçerliliklerini kontrol eder.
Port Tarama: scan_port fonksiyonu belirli bir portun açık olup olmadığını kontrol eder ve açık portları listeye ekler.
İş Parçacıkları: run_scanner fonksiyonu çok iş parçacıklı tarama işlemini başlatır ve iş parçacıkları kuyruğundaki portları tarar.
Sonuçları Görüntüleme: Taranan açık portlar Tkinter Listbox içinde görüntülenir.
