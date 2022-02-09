# Mealey makinası

dizin = "C:/Users/ali ihsan/Desktop/Çocuklar/Bahaeddin/mealey/"

fGecisTablosu = 'GecisDiyagrami.txt'

GecisTablosu = {}

#ilk giriş state'ini bu değişkende tutalım
ilkgiris = ''

# Geçiş tablosunun okunup, oluşturulması
with open(dizin+fGecisTablosu) as f:
    muhteva = f.readlines()

    say = 0
    for line in muhteva[1:]:
        satir = line.strip().split(sep='\t')
        key = satir[0] + ' - ' + satir[1]
        GecisTablosu[key] = {'output':satir[2],'yenidrm':satir[3]}

        # Giriş state'ini öğrenelim
        if say == 0:
            ilkgiris = satir[0]
        say = say + 1


# Kullanıcıdan giriş stringinin istenmesi
giris = input('Lütfen giriş stringini giriniz:')
giris="1100010110"

print('\n'*2)
print('Adım Adım Gösterim')
print('==================')
stateler = []
ciktilar = []
stateler.append(ilkgiris)

state =  ilkgiris

for g in giris:
    key = state + ' - ' + g
    state = GecisTablosu[key]['yenidrm']
    cikti = GecisTablosu[key]['output']
    print('Girdi:',g, 'State:',state, 'Çıktı:',cikti)
    stateler.append(state)
    ciktilar.append(cikti)

print('\n'*2)
print('Toplu Gösterim:')
print('===============')
print('Girdi:',giris)
print('Stateler:', stateler)
print('Outputlar:',ciktilar)
print('Output:',''.join(ciktilar))
