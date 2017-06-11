__all__ = ['moroccanNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Abdelaziz'), Js('Abdelhak'), Js('Abdelhamid'), Js('Abdelilah'), Js('Abdelkader'), Js('Abdelkarim'), Js('Abdellah'), Js('Abdellatif'), Js('Abdelmajid'), Js('Abderrahim'), Js('Abderrahman'), Js('Abdeslam'), Js('Abdullah'), Js('Adil'), Js('Ahmed'), Js('Ali'), Js('Amaniyy'), Js('Amine'), Js('Amrane'), Js('Aqil'), Js('Arib'), Js('Arwarh'), Js('Asil'), Js('Askari'), Js('Attiq'), Js('Awadah'), Js('Ayham'), Js('Ayoub'), Js('Ayser'), Js('Aziz'), Js('Baariq'), Js('Barkad'), Js('Baz'), Js('Bilal'), Js('Boutaje'), Js('Brahim'), Js('Bushr'), Js('Dirar'), Js('Diwan'), Js('Driss'), Js('Dulamah'), Js('El Bachir'), Js('El Hassan'), Js('El Houari'), Js('El Madani'), Js('El Mahi'), Js('Elias'), Js('Faqih'), Js('Farid'), Js('Fayaaz'), Js('Fayyad'), Js('Fouad'), Js('Ghali'), Js('Girgis'), Js('Habbab'), Js('Hadir'), Js('Hakem'), Js('Hamas'), Js('Hamdan'), Js('Hamid'), Js('Hamza'), Js('Hassan'), Js('Hayyan'), Js('Hicham'), Js('Ibrahim'), Js('Ikrimah'), Js("Isma'il"), Js('Ismail'), Js('Iyas'), Js('Jabalah'), Js('Jalal'), Js('Jamal'), Js('Jamaldine'), Js('Jaul'), Js('Jawdah'), Js('Jibran'), Js('Jubair'), Js('Kadeen'), Js('Karim'), Js('Khalid'), Js('Lahcen'), Js('Lubaid'), Js('Marzuq'), Js('Mhamed'), Js('Mimoun'), Js('Mohamed'), Js('Mohammed'), Js('Mojiz'), Js('Moosa'), Js('Mostafa'), Js('Moulham'), Js('Mourad'), Js('Muaz'), Js('Mujahid'), Js('Muslih'), Js('Mustapha'), Js('Muwaffaq'), Js('Noureddine'), Js('Omar'), Js('Ouahid'), Js('Quds'), Js('Quraishi'), Js('Rachid'), Js('Rasil'), Js('Ridouane'), Js('Rifky'), Js('Ruhul'), Js('Sadid'), Js('Safwah'), Js('Said'), Js('Salamah'), Js('Samir'), Js('Shihab'), Js('Simohamed'), Js('Sofian'), Js('Sufyan'), Js('Suhaim'), Js('Tanan'), Js('Tarik'), Js('Tazim'), Js('Thamir'), Js('Thawab'), Js('Waliedine'), Js('Waqqas'), Js('Wasif'), Js('Wasim'), Js('Yassine'), Js('Younes'), Js('Youssef'), Js('Youssouf'), Js('Zakwan'), Js('Zaky'), Js('Zamen'), Js('Zarif'), Js('Zeyn'), Js('Ziaul-Haq'), Js('Zitane'), Js('Zubayr')]))
    var.put('nm2', Js([Js('Aalia'), Js('Aaliyah'), Js('Abal'), Js('Achoura'), Js('Ahlam'), Js('Aicha'), Js('Aider'), Js('Aisha'), Js('Alina'), Js('Alzahra'), Js('Amal'), Js('Amara'), Js('Amaya'), Js('Amelle'), Js('Amina'), Js('Aminah'), Js('Amira'), Js('Amira '), Js('Amsah'), Js('Amurra'), Js('Anaan'), Js('Anamar'), Js('Anisha'), Js('Aqilah'), Js('Areebah'), Js('Areej'), Js('Arifa'), Js('Asala'), Js('Ashwaq'), Js('Asrar'), Js('Athir'), Js('Atyaf'), Js('Ayat'), Js('Ayesha'), Js('Aysha'), Js('Azeeza'), Js('Azhar'), Js('Aziza'), Js('Azmiyah'), Js('Azza'), Js('Badria'), Js('Badriya'), Js('Bahae'), Js('Balqis'), Js('Bassima'), Js('Batoul'), Js('Baysan'), Js('Benazir'), Js('Bisar'), Js('Bouchra'), Js('Buhjah'), Js('Busr'), Js('Chafika'), Js('Chahida'), Js('Chahrazad'), Js('Chama'), Js('Charifa'), Js('Chaymaa'), Js('Chaymae'), Js('Cherifa'), Js('Chifa'), Js('Choukria'), Js('Choumicha'), Js('Dahbia'), Js('Daouia'), Js('Darifa'), Js('Delilah'), Js('Dua'), Js('Dunyana'), Js('Durya'), Js('Enas'), Js('Fadeelah'), Js('Fadma'), Js('Fahimah'), Js('Fahime'), Js('Fairouz'), Js('Farida'), Js('Farizah'), Js('Fatema'), Js('Fathiyah'), Js('Fatiha'), Js('Fatima'), Js('Fatna'), Js('Fattouch'), Js('Fawz'), Js('Fawza'), Js('Fayha'), Js('Fikriyah'), Js('Firdoos'), Js('Fiza'), Js('Furat'), Js('Futun'), Js('Gadwa'), Js('Gawaher'), Js('Gehan'), Js('Ghaada'), Js('Ghaaliya'), Js('Gharam'), Js('Ghariba'), Js('Ghaydaa'), Js('Ghazal'), Js('Ghina'), Js('Gohar'), Js('Habeeba'), Js('Habiba'), Js('Hachmia'), Js('Hadeel'), Js('Hafida'), Js('Hajar'), Js('Hakima'), Js('Halima'), Js('Hameeda'), Js('Hamida'), Js('Hana'), Js('Hanan'), Js('Hanane'), Js('Haniya'), Js('Hasbia'), Js('Hassana'), Js('Hassiba'), Js('Hayat'), Js('Heya'), Js('Hikma'), Js('Hiyam'), Js('Hlalia'), Js('Houria'), Js('Hudun'), Js('Huriya'), Js('Ikram'), Js('Iman'), Js('Imane'), Js('Islamia'), Js('Isra'), Js('Jamila'), Js('Jasmine'), Js('Jawaher'), Js('Jihane'), Js('Juman'), Js('Jumina'), Js('Kamar'), Js('Karima'), Js('Khadija'), Js('Khadisha'), Js('Khadra'), Js('Khalila'), Js('Khatija'), Js('Laila'), Js('Lamyaa'), Js('Latifa'), Js('Layanah'), Js('Leila'), Js('Lila'), Js('Lina'), Js('Loubna'), Js('Madiha'), Js('Mahdia'), Js('Malika'), Js('Mansura'), Js('Mariam'), Js('Maryam'), Js('Masuda'), Js('Menena'), Js('Mennana'), Js('Michkat'), Js('Mimount'), Js('Mina'), Js('Minhat'), Js('Moufida'), Js('Mumina'), Js('Mutah'), Js('Nabila'), Js('Nadah'), Js('Nadia'), Js('Nahila'), Js('Naima'), Js('Najat'), Js('Najiha'), Js('Namira'), Js('Naqicha'), Js('Nasra'), Js('Nawar'), Js('Naziha'), Js('Nejlae'), Js('Nejlet'), Js('Nesma'), Js('Nezha'), Js('Nouria'), Js('Nurhayat'), Js('Nuzha'), Js('Nyla'), Js('Ouarda'), Js('Qadr'), Js('Rabia'), Js('Rabya'), Js('Racha'), Js('Rachida'), Js('Rafika'), Js('Raghad'), Js('Rahida'), Js('Rahma'), Js('Raisa'), Js('Rashida '), Js('Reema '), Js('Reshma'), Js('Ritwan'), Js('Rochdiya'), Js('Saadet'), Js('Saadia'), Js('Sabreen'), Js('Sabriye'), Js('Safiyah'), Js('Safura'), Js('Saida'), Js('Saira'), Js('Salma'), Js('Samaira'), Js('Samara'), Js('Samima'), Js('Samira'), Js('Sanaa'), Js('Sanae'), Js('Sara'), Js('Sayeda'), Js('Shabana'), Js('Shadin'), Js('Shahida'), Js('Shanaz'), Js('Shayma'), Js('Shenaz'), Js('Shukriya'), Js('Siham'), Js('Souad'), Js('Soulef'), Js('Soumaya'), Js('Sulayma'), Js('Summayyah'), Js('Tahani'), Js('Takama'), Js('Tamou'), Js('Tara'), Js('Thorya'), Js('Tirra'), Js('Tissam'), Js('Tunaruz'), Js('Ubaida'), Js('Waad'), Js('Wacila'), Js('Wadia'), Js('Wafiyah'), Js('Wala'), Js('Waliyah'), Js('Wedad'), Js('Widian'), Js('Wijdane'), Js('Xamira'), Js('Yamina'), Js('Yaram'), Js('Yasmin'), Js('Yasmina'), Js('Yasmine'), Js('Zahara'), Js('Zaheda'), Js('Zahidah'), Js('Zahra'), Js('Zairah'), Js('Zara'), Js('Zayna'), Js('Zhour'), Js('Zidana'), Js('Zinah'), Js('Zohra'), Js('Zuha'), Js('Zuheyra'), Js('Zuleika')]))
    var.put('nm3', Js([Js('al-Jirari'), Js('al-Aziz'), Js('al-Ghumari'), Js('Guennoun'), Js('Laroui'), Js('Zrika'), Js('al-Jirari'), Js('Sahimi'), Js('Kilito'), Js('Said'), Js('Tazi'), Js('Serhane'), Js('Bouasria'), Js('Benali'), Js('Chaoui'), Js('Chatt'), Js('Jouiti'), Js('Tabbal'), Js('Khatibi'), Js('Torres'), Js('Ghallab'), Js('Taïa'), Js('Idrissi'), Js('Laabi'), Js('Benjelloun'), Js('Benjelloun'), Js('Belghiti'), Js('Bennani'), Js('Lahbibi'), Js('Benmansour'), Js('Jouahri'), Js('Hajji'), Js('El Moudden'), Js('al-Ghumari'), Js('al-Ghumari'), Js('al-Tayyeb'), Js('Abdessalam'), Js('Barakat'), Js('Benchemsi'), Js('Boukous'), Js('Bouzfour'), Js('Harrak'), Js('Joumari'), Js('Lemsih'), Js('Mejjati'), Js('Sefrioui'), Js('Toufiq'), Js('al-Madini'), Js('al-Buzidi'), Js('Azaykou'), Js('Bourequat'), Js('Haddani'), Js('Lmrabet'), Js('Siqli'), Js('ibn Qasim'), Js('El Hajjam'), Js('al-Fassi'), Js('Samie'), Js('Qamari'), Js('Trabelsi'), Js('Salem'), Js('Tawil'), Js('Ben Hamed'), Js('Chraïbi'), Js('El Khouri'), Js('El Meliani'), Js('Ksikes'), Js('El Maleh'), Js('Abécassis'), Js('Hocquard'), Js('Bendahan'), Js('Skali'), Js('al-Ansari'), Js('Diouri'), Js('Mernissi'), Js('Laroui'), Js('Rhissassi'), Js('Bikri'), Js('Zafrani'), Js('Ben Haddou'), Js('Ferhat'), Js('Bourkia'), Js('Toulali'), Js('Sinaceur'), Js('ibn al-Hassan'), Js('Marouazi'), Js('Mourad'), Js('Bennouna'), Js('Batma'), Js('Lalami'), Js('Baka'), Js('Abouzeid'), Js('Lahlou'), Js('Akalay'), Js('Kabbal'), Js('Elmandjra'), Js('Binebine'), Js('Tobji'), Js('Oufkir'), Js('al-Fassi'), Js('Akhrif'), Js('Ben Barka'), Js('Chafik'), Js('Choukri'), Js('Mrabet'), Js('Nedali'), Js('Raihani'), Js('Serghini'), Js('Sibari'), Js('Zafzaf'), Js('al-Jabri'), Js('Achaari'), Js('Akoujan'), Js('Tazi'), Js('El-Hababi'), Js('Lahbabi'), Js('Ben Abdelaziz'), Js('Bennis'), Js('Benzakour'), Js('Berrada'), Js('Daoud'), Js('El Haloui'), Js('El-Moustaoui'), Js('Hajuji'), Js('El Ouazzani'), Js('Ibrahim'), Js('Kaghat'), Js('Khammar'), Js('Sabbag'), Js('Sabila'), Js('Zniber'), Js('al-Habib'), Js('al-Harradi'), Js('al-Makki'), Js('al-Mokhtar'), Js('ibn Mohammed'), Js('ibn al-Hasan'), Js('Nissaboury'), Js('Hachim'), Js('n’Ait'), Js('Rabi'), Js('Barbery'), Js('Maadawi'), Js('Ayouch'), Js('Chafik'), Js('Yassine'), Js('El Hachmi'), Js('El Aoufi'), Js('Rhozali'), Js('Mounir'), Js('Benchemsi'), Js('El Khayat'), Js('Assaraf'), Js('Achtouk'), Js('Hajji'), Js('Leghlid'), Js('Yaktine'), Js('Menebhi'), Js('El-Ouadie'), Js('Bahéchar'), Js('Ben Jelloun'), Js('Seddiki'), Js('Allal'), Js('Saqqat'), Js('Oulehri'), Js('al-Wazzani'), Js('Lamrani'), Js('Fadel'), Js('Elalamy'), Js('Mansouri'), Js('Daoud'), Js('Ben Bouchta')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
moroccanNames = var.to_python()