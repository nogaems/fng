__all__ = ['moorishNames']

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
    var.registers(['nm1', 'nm4', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js("A'id"), Js('Aban'), Js('Abbad'), Js('Abbas'), Js("Abdu'llah"), Js('Affan'), Js('Aflah'), Js('Ahmad'), Js('Ali'), Js('Amira'), Js('Amr'), Js('Asad'), Js('Asbag'), Js('Asbat'), Js('Ashraf'), Js('Asim'), Js('Aslam'), Js('Atiq'), Js('Atta'), Js('Attab'), Js('Attiyah'), Js('Ayman'), Js('Ayshun'), Js('Ayyub'), Js('Badr'), Js('Bakr'), Js('Baqi'), Js("Da'ud"), Js('Darras'), Js('Fadl'), Js('Fahim'), Js('Farhan'), Js('Farid'), Js('Faris'), Js('Farraj'), Js('Fath'), Js('Fauz'), Js('Faysal'), Js('Galib'), Js('Hafs'), Js('Hajib'), Js('Hajjaj'), Js('Hakam'), Js('Hakim'), Js('Hamdin'), Js('Hamdun'), Js('Hamid'), Js('Hammad'), Js('Hani'), Js('Harith'), Js('Haroun'), Js('Harun'), Js('Hasan'), Js('Hatim'), Js('Hayyan'), Js('Hazm'), Js('Hilmi'), Js('Hisham'), Js('Humam'), Js('Husain'), Js('Husayn'), Js('Husni'), Js('Ibrahim'), Js('Idris'), Js('Imtiyaz'), Js('Insaf'), Js('Irfan'), Js('Isa'), Js('Ishaq'), Js("Isma'il"), Js("Ja'far"), Js("Ja'qub"), Js('Jabir'), Js('Jahhaf'), Js('Jahwar'), Js('Jalaf'), Js('Jalid'), Js('Jamil'), Js('Jasib'), Js('Jattab'), Js('Jawar'), Js('Jifri'), Js('Junayd'), Js('Kamal'), Js('Kamil'), Js('Karim'), Js('Latif'), Js('Lubb'), Js('Mahbub'), Js('Majlad'), Js('Makki'), Js('Malik'), Js('Mansur'), Js('Marwan'), Js('Marzuq'), Js("Mas'ud"), Js('Masarra'), Js('Maslama'), Js('Mawhab'), Js('Maymun'), Js('Miswar'), Js("Mu'awiya"), Js('Mubarak'), Js('Mufarrij'), Js('Mufawwiz'), Js('Muhammad'), Js('Muharib'), Js('Mujahid'), Js('Mundir'), Js("Mus'ab"), Js('Musa'), Js('Mutarrif'), Js('Najah'), Js('Najib'), Js('Najih'), Js('Nasr'), Js('Nawfal'), Js('Nizar'), Js('Nuh'), Js('Nusayr'), Js('Qasim'), Js('Qays'), Js('Rabi'), Js('Rahhu'), Js('Rashid'), Js('Razin'), Js('Ridwan'), Js('Rushd'), Js("Sa'd"), Js("Sa'dan"), Js("Sa'dun"), Js("Sa'id"), Js('Sabah'), Js('Sabir'), Js('Safwan'), Js('Sahl'), Js('Sahr'), Js('Sajr'), Js('Salama'), Js('Salih'), Js('Salim'), Js('Sawwar'), Js('Sayyid'), Js('Shakir'), Js('Shamil'), Js('Shamir'), Js("Shu'ayb"), Js('Shurayh'), Js('Siraj'), Js('Sufyan'), Js('Suhayl'), Js('Sulaiman'), Js('Sumayl'), Js('Tabit'), Js('Tahir'), Js('Talha'), Js('Tamim'), Js('Tammam'), Js('Tariq'), Js('Tasufin'), Js('Tawd'), Js('Tayyib'), Js('Ubada'), Js('Ubaid'), Js('Ufayr'), Js('Ulaym'), Js('Umar'), Js('Umayyah'), Js('Usama'), Js('Utba'), Js('Uthman'), Js('Uwais'), Js('Wadah'), Js('Wahb'), Js('Walid'), Js('Wasil'), Js('Wasim'), Js("Ya'ish"), Js("Ya'qub"), Js('Yahyah'), Js('Yazid'), Js('Yunus'), Js('Yusuf'), Js('Zawahir'), Js('Zayd'), Js('Ziyad'), Js('Zuhayr'), Js('Zuhr')]))
    var.put('nm2', Js([Js("A'isha"), Js('Amat'), Js('Amina'), Js('Ashiqa'), Js('Asma'), Js('Ayisha'), Js('Baraka'), Js('Bazzu'), Js('Bushra'), Js('Fahima'), Js('Farhana'), Js('Farzanah'), Js('Fatima'), Js('Fatimah'), Js('Fawziya'), Js('Firoza'), Js('Hadija'), Js('Hafsa'), Js('Hajara'), Js('Hamda'), Js('Hamduna'), Js('Hind'), Js('Husna'), Js('Ishraq'), Js('Jamila'), Js('Jariya'), Js('Jawla'), Js('Judur'), Js('Khadija'), Js('Kitman'), Js('Kulsum'), Js('Lubna'), Js('Mahja'), Js('Maryam'), Js('Maymuna'), Js('Muhsina'), Js('Nabila'), Js('Nafisa'), Js('Nuzha'), Js('Razana'), Js('Rihana'), Js('Rima'), Js('Roshana'), Js('Safina'), Js('Safiyya'), Js('Safya'), Js('Salma'), Js('Sama'), Js('Sara'), Js('Sayyida'), Js('Shahnaz'), Js('Shamila'), Js('Sharmila'), Js('Silmiya'), Js('Sitt'), Js("Su'a"), Js('Sukayna'), Js('Suna'), Js('Sut'), Js("Ta'zunt"), Js('Tamu'), Js('Urtatim'), Js('Yamina'), Js('Yanduza'), Js('Yasmin'), Js('Zahra'), Js('Zannu'), Js('Zarru'), Js('Zaynab'), Js('Zinat'), Js('Zulfa'), Js('Zummurrud')]))
    var.put('nm3', Js([Js('al-Andalusi'), Js('al-Isbili'), Js('al-Mari'), Js('al-Mursi'), Js('al-Balansi'), Js('al-Jayyani'), Js('al-Rundi'), Js('al-Qurtubi'), Js('al-Garnati'), Js('al-Mayurqui'), Js('al-Talamanki'), Js('al-Tulaytuli'), Js('al-Dani'), Js('al-Ifriqi'), Js('al-Magribi'), Js('al-Tunayzi'), Js('al-Abbar'), Js('al-Abbas'), Js('al-Abdari'), Js('al-As'), Js('al-Asadi'), Js('al-Ashjai'), Js('al-Asili'), Js('al-Attar'), Js('al-Azdi'), Js('al-Bahrani'), Js('al-Bajjani'), Js('al-Baji'), Js('al-Bakri'), Js('al-Batalyawsi'), Js('al-Baytar'), Js('al-Bazzaz'), Js('al-Birzali'), Js('al-Dabbag'), Js('al-Dabbaj'), Js('al-Fadl'), Js('al-Faradi'), Js('al-Farisi'), Js('al-Fath'), Js('al-Fazari'), Js('al-Fihri'), Js('al-Gafiqi'), Js('al-Gasani'), Js('al-Habib'), Js('al-Hadda'), Js('al-Haddad'), Js('al-Hadrami'), Js('al-Hafiz'), Js('al-Hajj'), Js('al-Hakam'), Js('al-Hamdani'), Js('al-Hariti'), Js('al-Hassar'), Js('al-Hijari'), Js('al-Himsi'), Js('al-Himyari'), Js('al-Hubab'), Js('al-Ilbiri'), Js('al-Iyyadi'), Js('al-Jabab'), Js('al-Jasur'), Js("al-Jat'ami"), Js('al-Jawlan'), Js('al-Jazrajii'), Js('al-Jilyani'), Js('al-Judami'), Js('al-Justani'), Js("al-Kala'i"), Js('al-Kinani'), Js('al-Kutami'), Js('al-Lajmi'), Js("al-Ma'afiri"), Js('al-Majid'), Js('al-Majzumi'), Js('al-Malaki'), Js("al-Qal'i"), Js('al-Qasim'), Js('al-Qaysi'), Js('al-Qurtubi'), Js("al-Ru'ayni"), Js('al-Sabti'), Js('al-Sadafi'), Js('al-Santarini'), Js('al-Sayyid'), Js("al-Shafi'i"), Js('al-Shatibi'), Js('al-Sinhaji'), Js('al-Sulami'), Js("al-Ta'labi"), Js('al-Tamini'), Js('al-Tarabulusi'), Js('al-Tujibi'), Js('al-Umawi'), Js('al-Undi'), Js('al-Wahid'), Js('al-Wahrani'), Js('al-Walid'), Js('al-Zahiri'), Js('al-Zubaydi'), Js('al-Zuhri'), Js("ibn A'id"), Js('ibn Aban'), Js('ibn Abbad'), Js('ibn Abbas'), Js("ibn Abdu'llah"), Js('ibn Affan'), Js('ibn Aflah'), Js('ibn Ahmad'), Js('ibn Ali'), Js('ibn Amira'), Js('ibn Amr'), Js('ibn Asad'), Js('ibn Asbag'), Js('ibn Asbat'), Js('ibn Asim'), Js('ibn Aslam'), Js('ibn Atiq'), Js('ibn Atta'), Js('ibn Attab'), Js('ibn Attiyah'), Js('ibn Ayman'), Js('ibn Ayshun'), Js('ibn Ayyub'), Js('ibn Badr'), Js('ibn Bakr'), Js('ibn Baqi'), Js("ibn Da'ud"), Js('ibn Darras'), Js('ibn Fadl'), Js('ibn Faris'), Js('ibn Farraj'), Js('ibn Fath'), Js('ibn Galib'), Js('ibn Hafs'), Js('ibn Hajib'), Js('ibn Hajjaj'), Js('ibn Hakam'), Js('ibn Hamdin'), Js('ibn Hamdun'), Js('ibn Hamid'), Js('ibn Hammad'), Js('ibn Hani'), Js('ibn Harith'), Js('ibn Haroun'), Js('ibn Harun'), Js('ibn Hasan'), Js('ibn Hatim'), Js('ibn Hayyan'), Js('ibn Hazm'), Js('ibn Hisham'), Js('ibn Humam'), Js('ibn Husain'), Js('ibn Ibrahim'), Js('ibn Idris'), Js('ibn Isa'), Js('ibn Ishaq'), Js("ibn Isma'il"), Js("ibn Ja'far"), Js("ibn Ja'qub"), Js('ibn Jabir'), Js('ibn Jahhaf'), Js('ibn Jahwar'), Js('ibn Jalaf'), Js('ibn Jalid'), Js('ibn Jasib'), Js('ibn Jattab'), Js('ibn Jawar'), Js('ibn Lubb'), Js('ibn Mahbub'), Js('ibn Majlad'), Js('ibn Makki'), Js('ibn Malik'), Js('ibn Mansur'), Js('ibn Marwan'), Js('ibn Marzuq'), Js("ibn Mas'ud"), Js('ibn Masarra'), Js('ibn Maslama'), Js('ibn Mawhab'), Js('ibn Maymun'), Js('ibn Miswar'), Js("ibn Mu'awiya"), Js('ibn Mufarrij'), Js('ibn Mufawwiz'), Js('ibn Muhammad'), Js('ibn Muharib'), Js('ibn Mujahid'), Js('ibn Mundir'), Js("ibn Mus'ab"), Js('ibn Musa'), Js('ibn Mutarrif'), Js('ibn Najah'), Js('ibn Najih'), Js('ibn Nasr'), Js('ibn Nizar'), Js('ibn Nuh'), Js('ibn Nusayr'), Js('ibn Qasim'), Js('ibn Qays'), Js('ibn Rabi'), Js('ibn Rahhu'), Js('ibn Rashid'), Js('ibn Razin'), Js('ibn Ridwan'), Js('ibn Rushd'), Js("ibn Sa'd"), Js("ibn Sa'dan"), Js("ibn Sa'dun"), Js("ibn Sa'id"), Js('ibn Sabah'), Js('ibn Safwan'), Js('ibn Sahl'), Js('ibn Sahr'), Js('ibn Sajr'), Js('ibn Salama'), Js('ibn Salih'), Js('ibn Salim'), Js('ibn Sawwar'), Js('ibn Sayyid'), Js('ibn Shakir'), Js('ibn Shamir'), Js("ibn Shu'ayb"), Js('ibn Shurayh'), Js('ibn Siraj'), Js('ibn Sufyan'), Js('ibn Sulaiman'), Js('ibn Sumayl'), Js('ibn Tabit'), Js('ibn Tahir'), Js('ibn Talha'), Js('ibn Tamim'), Js('ibn Tammam'), Js('ibn Tariq'), Js('ibn Tasufin'), Js('ibn Tawd'), Js('ibn Tayyib'), Js('ibn Ubada'), Js('ibn Ubaid'), Js('ibn Ufayr'), Js('ibn Ulaym'), Js('ibn Umar'), Js('ibn Umayyah'), Js('ibn Usama'), Js('ibn Utba'), Js('ibn Uthman'), Js('ibn Wadah'), Js('ibn Wahb'), Js('ibn Walid'), Js('ibn Wasil'), Js('ibn Wasim'), Js("ibn Ya'ish"), Js("ibn Ya'qub"), Js('ibn Yahyah'), Js('ibn Yazid'), Js('ibn Yunus'), Js('ibn Yusuf'), Js('ibn Zayd'), Js('ibn Ziyad'), Js('ibn Zuhayr'), Js('ibn Zuhr')]))
    var.put('nm4', Js([Js('al-Andalusi'), Js('al-Isbili'), Js('al-Mari'), Js('al-Mursi'), Js('al-Balansi'), Js('al-Jayyani'), Js('al-Rundi'), Js('al-Qurtubi'), Js('al-Garnati'), Js('al-Mayurqui'), Js('al-Talamanki'), Js('al-Tulaytuli'), Js('al-Dani'), Js('al-Ifriqi'), Js('al-Magribi'), Js('al-Tunayzi'), Js('al-Abbar'), Js('al-Abbas'), Js('al-Abdari'), Js('al-As'), Js('al-Asadi'), Js('al-Ashjai'), Js('al-Asili'), Js('al-Attar'), Js('al-Azdi'), Js('al-Bahrani'), Js('al-Bajjani'), Js('al-Baji'), Js('al-Bakri'), Js('al-Batalyawsi'), Js('al-Baytar'), Js('al-Bazzaz'), Js('al-Birzali'), Js('al-Dabbag'), Js('al-Dabbaj'), Js('al-Fadl'), Js('al-Faradi'), Js('al-Farisi'), Js('al-Fath'), Js('al-Fazari'), Js('al-Fihri'), Js('al-Gafiqi'), Js('al-Gasani'), Js('al-Habib'), Js('al-Hadda'), Js('al-Haddad'), Js('al-Hadrami'), Js('al-Hafiz'), Js('al-Hajj'), Js('al-Hakam'), Js('al-Hamdani'), Js('al-Hariti'), Js('al-Hassar'), Js('al-Hijari'), Js('al-Himsi'), Js('al-Himyari'), Js('al-Hubab'), Js('al-Ilbiri'), Js('al-Iyyadi'), Js('al-Jabab'), Js('al-Jasur'), Js("al-Jat'ami"), Js('al-Jawlan'), Js('al-Jazrajii'), Js('al-Jilyani'), Js('al-Judami'), Js('al-Justani'), Js("al-Kala'i"), Js('al-Kinani'), Js('al-Kutami'), Js('al-Lajmi'), Js("al-Ma'afiri"), Js('al-Majid'), Js('al-Majzumi'), Js('al-Malaki'), Js("al-Qal'i"), Js('al-Qasim'), Js('al-Qaysi'), Js('al-Qurtubi'), Js("al-Ru'ayni"), Js('al-Sabti'), Js('al-Sadafi'), Js('al-Santarini'), Js('al-Sayyid'), Js("al-Shafi'i"), Js('al-Shatibi'), Js('al-Sinhaji'), Js('al-Sulami'), Js("al-Ta'labi"), Js('al-Tamini'), Js('al-Tarabulusi'), Js('al-Tujibi'), Js('al-Umawi'), Js('al-Undi'), Js('al-Wahid'), Js('al-Wahrani'), Js('al-Walid'), Js('al-Zahiri'), Js('al-Zubaydi'), Js('al-Zuhri'), Js("bint A'id"), Js('bint Aban'), Js('bint Abbad'), Js('bint Abbas'), Js("bint Abdu'llah"), Js('bint Affan'), Js('bint Aflah'), Js('bint Ahmad'), Js('bint Ali'), Js('bint Amira'), Js('bint Amr'), Js('bint Asad'), Js('bint Asbag'), Js('bint Asbat'), Js('bint Asim'), Js('bint Aslam'), Js('bint Atiq'), Js('bint Atta'), Js('bint Attab'), Js('bint Attiyah'), Js('bint Ayman'), Js('bint Ayshun'), Js('bint Ayyub'), Js('bint Badr'), Js('bint Bakr'), Js('bint Baqi'), Js("bint Da'ud"), Js('bint Darras'), Js('bint Fadl'), Js('bint Faris'), Js('bint Farraj'), Js('bint Fath'), Js('bint Galib'), Js('bint Hafs'), Js('bint Hajib'), Js('bint Hajjaj'), Js('bint Hakam'), Js('bint Hamdin'), Js('bint Hamdun'), Js('bint Hamid'), Js('bint Hammad'), Js('bint Hani'), Js('bint Harith'), Js('bint Haroun'), Js('bint Harun'), Js('bint Hasan'), Js('bint Hatim'), Js('bint Hayyan'), Js('bint Hazm'), Js('bint Hisham'), Js('bint Humam'), Js('bint Husain'), Js('bint Ibrahim'), Js('bint Idris'), Js('bint Isa'), Js('bint Ishaq'), Js("bint Isma'il"), Js("bint Ja'far"), Js("bint Ja'qub"), Js('bint Jabir'), Js('bint Jahhaf'), Js('bint Jahwar'), Js('bint Jalaf'), Js('bint Jalid'), Js('bint Jasib'), Js('bint Jattab'), Js('bint Jawar'), Js('bint Lubb'), Js('bint Mahbub'), Js('bint Majlad'), Js('bint Makki'), Js('bint Malik'), Js('bint Mansur'), Js('bint Marwan'), Js('bint Marzuq'), Js("bint Mas'ud"), Js('bint Masarra'), Js('bint Maslama'), Js('bint Mawhab'), Js('bint Maymun'), Js('bint Miswar'), Js("bint Mu'awiya"), Js('bint Mufarrij'), Js('bint Mufawwiz'), Js('bint Muhammad'), Js('bint Muharib'), Js('bint Mujahid'), Js('bint Mundir'), Js("bint Mus'ab"), Js('bint Musa'), Js('bint Mutarrif'), Js('bint Najah'), Js('bint Najih'), Js('bint Nasr'), Js('bint Nizar'), Js('bint Nuh'), Js('bint Nusayr'), Js('bint Qasim'), Js('bint Qays'), Js('bint Rabi'), Js('bint Rahhu'), Js('bint Rashid'), Js('bint Razin'), Js('bint Ridwan'), Js('bint Rushd'), Js("bint Sa'd"), Js("bint Sa'dan"), Js("bint Sa'dun"), Js("bint Sa'id"), Js('bint Sabah'), Js('bint Safwan'), Js('bint Sahl'), Js('bint Sahr'), Js('bint Sajr'), Js('bint Salama'), Js('bint Salih'), Js('bint Salim'), Js('bint Sawwar'), Js('bint Sayyid'), Js('bint Shakir'), Js('bint Shamir'), Js("bint Shu'ayb"), Js('bint Shurayh'), Js('bint Siraj'), Js('bint Sufyan'), Js('bint Sulaiman'), Js('bint Sumayl'), Js('bint Tabit'), Js('bint Tahir'), Js('bint Talha'), Js('bint Tamim'), Js('bint Tammam'), Js('bint Tariq'), Js('bint Tasufin'), Js('bint Tawd'), Js('bint Tayyib'), Js('bint Ubada'), Js('bint Ubaid'), Js('bint Ufayr'), Js('bint Ulaym'), Js('bint Umar'), Js('bint Umayyah'), Js('bint Usama'), Js('bint Utba'), Js('bint Uthman'), Js('bint Wadah'), Js('bint Wahb'), Js('bint Walid'), Js('bint Wasil'), Js('bint Wasim'), Js("bint Ya'ish"), Js("bint Ya'qub"), Js('bint Yahyah'), Js('bint Yazid'), Js('bint Yunus'), Js('bint Yusuf'), Js('bint Zayd'), Js('bint Ziyad'), Js('bint Zuhayr'), Js('bint Zuhr')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm4').callprop('splice', var.get('rnd2'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
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
moorishNames = var.to_python()