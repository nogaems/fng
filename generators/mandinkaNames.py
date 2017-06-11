__all__ = ['mandinkaNames']

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
    var.put('nm1', Js([Js('Abbas'), Js('Abdou'), Js('Abdoulaye'), Js('Abdoulie'), Js('Ablanjaye'), Js('Ablie'), Js('Abu'), Js('Adama'), Js('Addo'), Js('Alaji'), Js('Alansana'), Js('Alanso'), Js('Alasan'), Js('Alieu'), Js('Alifa'), Js('Amadou'), Js('Amat'), Js('Antouman'), Js('Antu'), Js('Assan'), Js('Babaja'), Js('Babou'), Js('Baboucar'), Js('Badara'), Js('Bai'), Js('Bailo'), Js('Bakary'), Js('Bala'), Js('Baluta'), Js('Bamba'), Js('Bango'), Js('Banja'), Js('Banta'), Js('Bassirou'), Js('Baturou'), Js('Baturu'), Js('Biran'), Js('Birom'), Js('Bolong'), Js('Bora'), Js('Boro'), Js('Boto'), Js('Bouba'), Js('Boubacar'), Js('Boy'), Js('Buba'), Js('Bubacar'), Js('Bunama'), Js('Burama'), Js('Buwa'), Js('Chenor'), Js('Cyper'), Js('Daba'), Js('Demba'), Js('Dembo'), Js('Dodou'), Js('Duta'), Js('Duwa'), Js('Ebou'), Js('Ebrahima'), Js('Ebrima'), Js('Ediresa'), Js('Edrissa'), Js('Ensa'), Js('Essa'), Js('Fabba'), Js('Fafa'), Js('Fakebba'), Js('Fanding'), Js('Fara'), Js('Faraba'), Js('Filije'), Js('Foday'), Js('Gereh'), Js('Gibril'), Js('Habib'), Js('Hasimou'), Js('Hassan'), Js('Hatabu'), Js('Idi'), Js('Idirissa'), Js('Ilman'), Js('Isa'), Js('Isaka'), Js('Ismaela'), Js('Jabril'), Js('Jalang'), Js('Jamang'), Js('Janko'), Js('Jato'), Js('Jebel'), Js('Jereh'), Js('Jibou'), Js('Jibril'), Js('Jibrin'), Js('Jombo'), Js('Jonkong'), Js('Juma'), Js('Jumu'), Js('Jung'), Js('Junkung'), Js('Kabir'), Js('Kabiru'), Js('Kairaba'), Js('Kamara'), Js('Karafa'), Js('Karamba'), Js('Karamo'), Js('Kausu'), Js('Kawsu'), Js('Kebba'), Js('Kekoto'), Js('Kekuta'), Js('Kemo'), Js('Kunta'), Js('Kutubo'), Js('Lafi'), Js('Laity'), Js('Lallo'), Js('Lalo'), Js('Lama'), Js('Lamin'), Js('Landing'), Js('Longcan'), Js('Madi'), Js('Makang'), Js('Malamin'), Js('Malick'), Js('Malik'), Js('Mamadi'), Js('Manlafi'), Js('Masane'), Js('Mohammed'), Js('Momodou'), Js('Momodu'), Js('Muña'), Js('Musa'), Js('Mustafa'), Js('Nfansu'), Js('Omar'), Js('Ousman'), Js('Pa'), Js('Paboy'), Js('Paoboy'), Js('Pateh'), Js('Saihou'), Js('Saikou'), Js('Sainey'), Js('Sajo'), Js('Sama'), Js('Samba'), Js('Sarjo'), Js('Seedy'), Js('Sherif'), Js('Sheriff'), Js('Sherrif'), Js('Sidibeh'), Js('Sirif'), Js('Sulayman'), Js('Suma'), Js('Suntukung'), Js('Sutay'), Js('Tairu'), Js('Tamba'), Js('Tijan'), Js('Tombong'), Js('Wandi'), Js('Wandy'), Js('Wasa'), Js('Wassa'), Js('Ya'), Js('Yakuba'), Js('Yankubah'), Js('Yaya'), Js('Yoro')]))
    var.put('nm2', Js([Js('Aba'), Js('Abi'), Js('Adama'), Js('Adel'), Js('Aisa'), Js('Aja'), Js('Ajamboon'), Js('Alanso'), Js('Alimatou'), Js('Ami'), Js('Amie'), Js('Aminata'), Js('Anti'), Js('Aramata'), Js('Attha'), Js('Awa'), Js('Bassin'), Js('Binta'), Js('Bintou'), Js('Bintu'), Js('Birta'), Js('Channeh'), Js('Daba'), Js('Fanta'), Js('Fatou'), Js('Fatoumata'), Js('Fatoumatta'), Js('Filije'), Js('Filijee'), Js('Hadang'), Js('Haddy'), Js('Halima'), Js('Hawa'), Js('Ibironke'), Js('Ida'), Js('Isa'), Js('Isatou'), Js('Jabou'), Js('Jahou'), Js('Jainaba'), Js('Jankeh'), Js('Jatou'), Js('Jeneba'), Js('Joñi'), Js('Jojo'), Js('Joma'), Js('Juka'), Js('Kabir'), Js('Kaddy'), Js('Kaddyatou'), Js('Kadi'), Js('Kadijatou'), Js('Kati'), Js('Kenenjaye'), Js('Khadijatu'), Js('Kinteh'), Js('Kinti'), Js('Koba'), Js('Kobba'), Js('Kumba'), Js('Kunda'), Js('Kurukemeh'), Js('Kuta'), Js('Kutu'), Js('Loli'), Js('Maimuna'), Js('Makuto'), Js('Mama'), Js('Mamanding'), Js('Mampol'), Js('Mandiki'), Js('Maram'), Js('Marang'), Js('Mariama'), Js('Marie'), Js('Maseray'), Js('Mbasi'), Js('Mbassi'), Js('Mboose'), Js('Musakuta'), Js('Musu'), Js('Musukebba'), Js('Musukuta'), Js('Ndey'), Js('Nene'), Js('Nyima'), Js('Nyonkoling'), Js('Oumil'), Js('Pahali'), Js('Piretta'), Js('Ramata'), Js('Ramatoulaye'), Js('Ramatoulie'), Js('Rohey'), Js('Saijo'), Js('Sainabou'), Js('Sainey'), Js('Sajo'), Js('Sanji'), Js('Sara'), Js('Sarjo'), Js('Satang'), Js('Satou'), Js('Sibo'), Js('Sira'), Js('Sirending'), Js('Sohna'), Js('Sona'), Js('Sukai'), Js('Sunkarr'), Js('Suntukung'), Js('Sutay'), Js('Tida'), Js('Tomaring'), Js('Yahar'), Js('Yama'), Js('Yamma'), Js('Yamundow'), Js('Yari'), Js('Yata')]))
    var.put('nm3', Js([Js('Ba'), Js('Badjie'), Js('Bah'), Js('Bajo'), Js('Baldeg'), Js('Baldeh'), Js('Biri'), Js('Camara'), Js('Ceesay'), Js('Ceesay'), Js('Colley'), Js('Conateh'), Js('Condé'), Js('Condeh'), Js('Coote'), Js('Corr'), Js('Coulibaly'), Js('Dabo'), Js('Danso'), Js('Daramy'), Js('Darboe'), Js('Diawara'), Js('Dibba'), Js('Diene'), Js('Dieye'), Js('Dione'), Js('Diouf'), Js('Fadika'), Js('Fatty'), Js('Faye'), Js('Gassama'), Js('Gaye'), Js('Guissé'), Js('Guiss'), Js('Hairte'), Js('Jagne'), Js('Jaiteh'), Js('Jallow'), Js('Jammeh'), Js('Janneh'), Js('Jarju'), Js('Jassey'), Js('Jatta'), Js('Jawara'), Js('Jawara'), Js('Jawo'), Js('Jobateh'), Js('Jobe'), Js('Joof'), Js('Kaba'), Js('Kabba'), Js('Kabbah'), Js('Kah'), Js('Kairaba'), Js('Kakay'), Js('Kama'), Js('Kambi'), Js('Kandeh'), Js('Kargbo'), Js('Kayode'), Js('Keita'), Js('Kinte'), Js('Kinteh'), Js('Kolley'), Js('Kouyaté'), Js('Kujabi'), Js('Kuyateh'), Js('Manneh'), Js('Mansaré'), Js('Mansaray'), Js('Marenah'), Js('Marong'), Js('Mboge'), Js('Mboob'), Js('Mbye'), Js('Mendy'), Js('Ndaw'), Js('Ndiaye'), Js('Ndour'), Js('Ngom'), Js('Ngum'), Js('Niang'), Js('Njie'), Js('Nyang'), Js('Ogoo'), Js('Ogunsola'), Js('Ouattara'), Js('Saidykhan'), Js('Sanneh'), Js('Sanyang'), Js('Sarr'), Js('Savaneh'), Js('Secka'), Js('Sene'), Js('Senghore'), Js('Sesay'), Js('Sey'), Js('Sidibeh'), Js('Sillah'), Js('Singateh'), Js('Singhateh'), Js('Sohna'), Js('Soley'), Js('Sonko'), Js('Sowe'), Js('Suso'), Js('Taal'), Js('Thiaw'), Js('Tiyana'), Js('Touré'), Js('Touray'), Js('Turay'), Js('Uster')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
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
mandinkaNames = var.to_python()