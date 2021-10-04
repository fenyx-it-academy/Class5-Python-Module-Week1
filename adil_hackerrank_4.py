#  4 Finding the percentage
if __name__ == '__main__':
    n = int(input()) #ogrenci sayisi
    student_marks = {} #bos bir dict
    for _ in range(n): #ogrencilerin isim ve puanlari almak icin dongu
        name, *line = input().split()#isim ve puanlari boslukla ayrarak aliyoruz
        scores = list(map(float, line))#aldigimi puanlari float olarak scores listesine veriyoruz
        student_marks[name] = scores #dict'e girdigimiz isime unun puanini veriyoruz
    query_name = input() #aramak istedigimiz isimi girecegiz
    toplam = sum(student_marks[query_name])#aradigimiz kisinin puaninin toplami
    print('%.2f' %(toplam/3))#puanin ortalamasi ve noktadan sonra 2 hane alip yazdirir