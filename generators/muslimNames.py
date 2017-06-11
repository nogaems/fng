__all__ = ['muslimNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'names', 'nm3', 'nm2'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aabdeen'), Js('Aabid'), Js('Aadam'), Js('Aadil'), Js('Aaish'), Js('Aakif'), Js('Aamir'), Js('Aaqil'), Js('Aarif'), Js('Aasim'), Js('Aatif'), Js('Aayid'), Js('Abbaad'), Js('Abbaas'), Js('Abdul Azeez'), Js('Abdul Baari'), Js('Abdul Baasid'), Js('Abdul Fattaah'), Js('Abdul Ghafoor'), Js('Abdul Ghani'), Js('Abdul Haadi'), Js('Abdul Hai'), Js('Abdul Hakeem'), Js('Abdul Haleem'), Js('Abdul Hameed'), Js('Abdul Jabbaar'), Js('Abdul Jaleel'), Js('Abdul Kader'), Js('Abdul Kareem'), Js('Abdul Khaliq'), Js('Abdul Lateef'), Js('Abdul Maalik'), Js('Abdul Majeed'), Js('Abdul Noor'), Js('Abdul Qayyoom'), Js('Abdul Quddoos'), Js('Abdul Rauf'), Js('Abdul Waahid'), Js('Abdul Wadood'), Js('Abdul Wahaab'), Js('Abdullah'), Js('Abdur Raheem'), Js('Abdur Rahmaan'), Js('Abdur Raqeeb'), Js('Abdur Rasheed'), Js('Abdur Razzaaq'), Js('Abdus Salam'), Js('Abdus Samad'), Js('Abdut Tawwab'), Js('Abood'), Js('Abyad'), Js('Adeeb'), Js('Adham'), Js('Adnaan'), Js('Afeef'), Js('Ahmed'), Js('Aiman'), Js('Akram'), Js('Alawi'), Js('Ali'), Js('Amaan'), Js('Amaanullah'), Js('Ameen'), Js('Ameer'), Js('Amjad'), Js('Ammaar'), Js('Amru'), Js('Anas'), Js('Annnees'), Js('Anwar'), Js('Aqeel'), Js('Arafaat'), Js('Arhab'), Js('Arkaan'), Js('Arshad'), Js('Asad'), Js('Aseel'), Js('Asghar'), Js('Ashqar'), Js('Ashraf'), Js('Aslam'), Js('Asmar'), Js('Awad'), Js('Awf'), Js('Awn'), Js('Awni'), Js('Ayyoob'), Js('Azhaar'), Js('Azmi'), Js('Azzaam'), Js('Baahir'), Js('Baaqir'), Js('Baasim'), Js('Badr'), Js('Badraan'), Js('Badri'), Js('Badruddeen'), Js('Baheej'), Js('Bakar'), Js('Bandar'), Js('Basheer'), Js('Bassaam'), Js('Bassil'), Js('Bilaal'), Js('Bishr'), Js('Burhaan'), Js('Daamir'), Js('Daawood'), Js('Daif'), Js('Daifallah'), Js('Daleel'), Js('Dhaafir'), Js('Dhaahir'), Js('Dhaakir'), Js('Dhaki'), Js('Dhareef'), Js('Faadi'), Js('Faadil'), Js('Faai Z'), Js('Faaid'), Js(' Faaiq'), Js('Faalih'), Js('Faaris'), Js('Faarooq'), Js('Faatih'), Js('Faatin'), Js('Fahd'), Js('Faheem'), Js('Fahmi'), Js('Faisal'), Js('Faraj'), Js('Farajallah'), Js('Fareed'), Js('Farhaan'), Js('Fateen'), Js("Fat'hi"), Js('Fawwaaz'), Js('Fawz'), Js('Fawzi'), Js('Fayyaad'), Js('Fikri'), Js('Fuaad'), Js('Furqaan'), Js('Ghaali'), Js('Ghaalib'), Js('Ghaamid'), Js('Ghaazi'), Js('Ghassaan'), Js('Haafil'), Js('Haajid'), Js('Haamid'), Js('Haani'), Js('Haarith'), Js('Haaroon'), Js('Haashid'), Js('Haashim'), Js('Haatim'), Js('Haazim'), Js('Haitham'), Js('Hakam'), Js('Hamad'), Js('Hamdaan'), Js('Hamdi'), Js('Hamood'), Js('Hamza'), Js('Haneef'), Js('Hanlala'), Js('Hasan'), Js('Hazm'), Js('Hibbaan'), Js('Hilaal'), Js('Hilmi'), Js('Hishaam'), Js('Hudhaifa'), Js('Humaid'), Js('Humaidaan'), Js('Huraira'), Js('Husaam'), Js('Husain'), Js('Husni'), Js('Ibrahim'), Js('Idrees'), Js('Ihaab'), Js('Ikram'), Js('Ilyaas'), Js('Imaad'), Js('Imraan'), Js('Irfaan'), Js('Isaam'), Js('Ishaaq'), Js('Ismad'), Js('Ismaeel'), Js('Iyaad'), Js('Izzaddeen'), Js('Izzat'), Js('Jaabir'), Js('Jaad'), Js('Jaadallah'), Js('Jaarallah'), Js('Jaasim'), Js('Jaasir'), Js('Jafar'), Js('Jalaal'), Js('Jam,Aan'), Js('Jamaal'), Js('Jameel'), Js('Jareer'), Js('Jasoor'), Js('Jawaad'), Js('Jawhar'), Js('Jihaad'), Js('Jiyaad'), Js('Jubair'), Js('Jumail'), Js('Junaid'), Js('Kaalim'), Js('Kaamil'), Js('Kaarim'), Js('Kabeer'), Js('Kaleem'), Js('Kamaal'), Js('Kamaaluddeen'), Js('Kameel'), Js('Kanaan'), Js('Katheer'), Js('Khaalid'), Js('Khairi'), Js('Khaleefa'), Js('Khaleel'), Js('Labeeb'), Js('Labeeb'), Js('Luqmaan'), Js('Lutfi'), Js('Luwai'), Js('Ma,Roof'), Js('Maahir'), Js('Maaiz'), Js("Maa'iz"), Js('Maajid'), Js('Maazin'), Js('Mahboob'), Js(' Mahdi'), Js('Mahfooz'), Js('Mahmood'), Js('Mahuroos'), Js('Maisara'), Js('Maisoon'), Js('Majdi'), Js('Mamdooh'), Js('Mamoon'), Js('Mansoor'), Js('Marwaan'), Js('Marzooq'), Js('Mashal'), Js('Masood'), Js('Mastoor'), Js('Mawdood'), Js('Mazeed'), Js('Miqdaad'), Js('Miqdaam'), Js('Misfar'), Js('Mishaari'), Js('Moosha'), Js('Mu,Aawiya'), Js('Muaaid'), Js('Muammar'), Js('Mubarak'), Js('Mubashshir'), Js('Mudrik'), Js('Mufeed'), Js('Muhaajir'), Js('Muhammad'), Js('Muhsin'), Js('Muhyddeen'), Js('Mujahid'), Js('Mukarram'), Js('Mukhtaar'), Js('Mundhir'), Js('Muneeb'), Js('Muneef'), Js('Muneer'), Js('Munjid'), Js('Munsif'), Js('Muntasir'), Js('Murshid'), Js('Musaaid'), Js("Mus'ab"), Js('Musaddiq'), Js('Musheer'), Js('Mushtaaq'), Js('Muslih'), Js('Muslim'), Js('Mustaba'), Js('Mutammam'), Js('Mutasim'), Js("Mu'taz"), Js('Muthanna'), Js('Mutlaq'), Js('Muzammil'), Js('Naadir'), Js('Naaif'), Js('Naaji'), Js('Naasif'), Js('Naasiruddeen'), Js('Naazil'), Js('Naazim'), Js('Nabeeh'), Js('Nabeel'), Js('Nadeem'), Js('Nadheer'), Js('Najeeb'), Js('Najeem'), Js('Naseem'), Js('Naseer'), Js('Nashat'), Js('Nassaar'), Js('Nawaar'), Js('Nawf'), Js('Nawfal'), Js('Nazmi'), Js('Neeshaan'), Js('Nizaam'), Js('Nizaar'), Js('Noori'), Js("Nu'maan"), Js('Numair'), Js('Qaaid'), Js('Qaasim'), Js('Qais'), Js('Quraish'), Js('Qutb'), Js('Raadi'), Js('Raafi'), Js('Raaid'), Js('Raaji'), Js('Raakaan'), Js('Raamiz'), Js('Raashid'), Js('Rabi'), Js('Rafeeq'), Js('Raihaan'), Js('Rajaa'), Js('Rajab'), Js('Ramalaan'), Js('Ramzi'), Js('Rashaad'), Js('Rasheeq'), Js('Rayyaan'), Js('Razeen'), Js('Rida'), Js('Ridwaan'), Js('Rifaah'), Js('Rifat'), Js('Riyaal'), Js('Rushdi'), Js('Rushdi'), Js('Ruwaid'), Js('Saabiq'), Js('Saabir'), Js('Saadiq'), Js('Saahir'), Js('Saajid'), Js(' Saalih'), Js('Saalim'), Js('Saami'), Js('Saamir'), Js('Sabaah'), Js('Sabri'), Js('Sad'), Js('Sadi'), Js('Sadoon'), Js('Saeed'), Js('Safar'), Js('Safwaan'), Js('Sahl'), Js('Saif'), Js('Sakeen'), Js('Salaah'), Js('Saleel'), Js('Saleem'), Js('Saleet'), Js('Salmaan'), Js('Samir'), Js('Saood'), Js('Saqr'), Js('Shaafi'), Js('Shaaheen'), Js('Shaahir'), Js('Shaakir'), Js('Shaamikh'), Js('Shaamil'), Js('Shabaan'), Js('Shaddaad'), Js('Shafeeq'), Js('Shaheed'), Js('Shaheed'), Js('Shaheer'), Js('Shakeel'), Js('Shameem'), Js('Shaqeeq'), Js('Sharaf'), Js('Sharaf'), Js('Shawqi'), Js('Shihaab'), Js('Shuaib'), Js('Shujaa'), Js('Shukri'), Js('Shuraih'), Js('Siddeeqi'), Js('Sidqi'), Js('Silmi'), Js('Siraaj'), Js('Sirajuddeen'), Js('Subhi'), Js('Sufyaan'), Js('Suhaib'), Js('Suhail'), Js('Sulaimaan'), Js('Sultan'), Js('Suwailim'), Js('Taaha'), Js('Taahir'), Js('Taaj'), Js('Taajuddeen'), Js('Taalib'), Js('Taamir'), Js('Taariq'), Js('Taiseer'), Js('Talaal'), Js('Talha'), Js('Tameem'), Js('Tammaam'), Js('Taqi'), Js('Tareef'), Js('Tawfeeq'), Js('Tawheed'), Js('Tayyib'), Js('Thaamir'), Js('Thaaqib'), Js('Tufail'), Js('Turki'), Js('Ubaida'), Js('Umair'), Js('Umar'), Js('Unais'), Js('Uqbah'), Js('Usaama'), Js('Uthmaa N'), Js('Uwais'), Js('Waail'), Js('Waatiq'), Js('Waddaah'), Js('Wajdi'), Js('Wajeeb'), Js('Wajeeh'), Js('Waleed'), Js('Waseef'), Js('Waseem'), Js('Wisaam'), Js('Yaasir'), Js("Ya'eesh"), Js('Yahya'), Js("Ya'qoob"), Js('Yoonus'), Js('Yoosuf'), Js('Yusri'), Js('Zaahid'), Js('Zaahir'), Js('Zaaid'), Js('Zaamil'), Js('Zaghlool'), Js('Zaid'), Js('Zaidaan'), Js('Zain'), Js('Zainuddeen'), Js('Zakariyya'), Js('Zaki'), Js('Zameel'), Js('Zayyaan'), Js('Ziyaad'), Js('Zubair'), Js('Zufar'), Js('Zuhair'), Js('Zuraara')]))
var.put('nm2', Js([Js('Aadila'), Js('Aaida'), Js('Aaisha'), Js('Aamina'), Js('Aanisa'), Js('Aarifa'), Js('Aasima'), Js('Aasiya'), Js('Aatifa'), Js('Aatika'), Js('Aayaat'), Js('Abeer'), Js('Adeeba'), Js('Adhraaa'), Js('Afaaf'), Js('Afeefa'), Js('Afnaan'), Js('Afraah'), Js('Ahlaam'), Js('Aliyya'), Js('Almaasa'), Js('Amaani'), Js('Amal'), Js('Amatullah'), Js('Ameena'), Js('Ameera'), Js('Amniyya'), Js('Anbara'), Js('Aneesa'), Js('Aqeela'), Js('Ariyya'), Js('Arwa'), Js('Aseela'), Js('Asmaa'), Js('Atheer'), Js('Atiyya'), Js('Awaatif'), Js('Awda'), Js('Azeema'), Js('Azeeza'), Js('Azza'), Js('Fakeeha'), Js('Faraah'), Js('Fareeda'), Js('Farha'), Js('Farhaana'), Js('Farhat'), Js('Faseeha'), Js('Fateena'), Js("Fat'hiyaa"), Js('Fawqiyya'), Js('Fawzaana'), Js('Fawzia'), Js('Fidda'), Js('Fikra'), Js('Fikriyya'), Js('Firdaus'), Js('Fuaada'), Js('Gaitha'), Js('Ghaada'), Js('Ghaaliba'), Js('Ghaaliya'), Js('Ghaaziya'), Js('Ghaidaa'), Js('Ghazaala'), Js('Ghuzaila'), Js('Haafiza'), Js('Haajara'), Js('Haakima'), Js('Haala'), Js('Haamida'), Js('Haaniya'), Js('Haaritha'), Js('Haazima'), Js('Habeeba'), Js('Hadbaaa'), Js('Hadeel'), Js('Hadiyya'), Js('Hafsa'), Js('Haibaa'), Js('Haifaaa'), Js('Hakeema'), Js('Haleema'), Js('Hamaama'), Js('Hamda'), Js('Hamdoona'), Js('Hameeda'), Js('Hamna'), Js('Hamsa'), Js('Hanaaa'), Js('Hanaan'), Js('Haniyya'), Js('Hanoona'), Js('Hasana'), Js('Haseena'), Js('Hasnaa'), Js('Hawraa'), Js('Hazeela'), Js('Hiba'), Js('Hikma'), Js('Hilmiyya'), Js('Himma'), Js('Hishma'), Js('Hissa'), Js('Hiwaaya'), Js(' Huda'), Js('Hujja'), Js('Humaina'), Js('Humaira'), Js('Husniyya'), Js('Huwaida'), Js('Ibtisaama'), Js('Iffat'), Js('Ilhaam'), Js('Imtinaan'), Js('Inaaya'), Js('Insaaf'), Js('Intisaar'), Js('Israa'), Js('Izza'), Js('Jadeeda'), Js('Jaleela'), Js('Jameela'), Js('Jannat'), Js('Jasra'), Js('Jawhara'), Js('Jeelaan'), Js('Juhaina'), Js('Jumaana'), Js('Jumaima'), Js('Juwairiya'), Js('Kaatima'), Js('Kaazima'), Js('Kabeera'), Js('Kameela'), Js('Kareema'), Js('Kawkab'), Js('Kawthar'), Js('Khaalida'), Js('Khadeeja'), Js('Khaira'), Js('Khairiya'), Js('Khaleela'), Js('Khawla'), Js('Khulood'), Js('Kifaaya'), Js('Kinaana'), Js('Kulthum'), Js('Laaiqa'), Js('Labeeba'), Js('Laila'), Js('Lateefa'), Js('Layaali'), Js('Lubaaba'), Js('Lubna'), Js('Lutfiyya'), Js('Maajida'), Js('Maariya'), Js('Maazina'), Js('Madeeha'), Js('Mahaa'), Js('Mahbooba'), Js('Mahdeeya'), Js('Mahdhoodha'), Js('Mahfoodha'), Js('Mahmooda'), Js('Maimoona'), Js('Maisara'), Js('Majdiyya'), Js('Majeeda'), Js('Maleeha'), Js('Maleeka'), Js('Manaahil'), Js('Manaal'), Js('Manaara'), Js('Mardiyya'), Js('Marjaana'), Js('Marwa'), Js('Marzooqa'), Js("Mas'ooda"), Js('Masroora'), Js('Mastoora'), Js('Mawhiba'), Js('Mawzoona'), Js('Mayyaada'), Js('Mazeeda'), Js('Minnah'), Js('Misbaah'), Js('Miska'), Js('Mubaaraka'), Js('Mubeena'), Js('Mudrika'), Js('Mufeeda'), Js('Mufliha'), Js('Muhjar'), Js("Mu'hsina"), Js('Mujaahida'), Js('Mumina'), Js("Mu'mina"), Js('Mumtaaza'), Js('Muna'), Js('Muneefa'), Js('Muneera'), Js('Munisa'), Js('Muntaha'), Js('Musfira'), Js('Musheera'), Js('Mushtaaqa'), Js("Mutee'a"), Js('Muzaina'), Js(' Muzna'), Js('Naadiya'), Js('Naafoora'), Js('Naaifa'), Js('Naaila'), Js('Nabeeha'), Js('Nabeela'), Js('Nada'), Js('Nadeera'), Js('Nadheera'), Js('Nadiyya'), Js('Nafeesa'), Js('Nahla'), Js('Najaat'), Js('Najeeba'), Js('Najeema'), Js('Najiyya'), Js('Najlaa'), Js('Najma'), Js('Najwa'), Js('Nakheel'), Js('Nameera'), Js('Naqaa'), Js('Naqiyya'), Js('Naseeba'), Js('Naseefa'), Js('Naseema'), Js('Naseera'), Js('Nasreen'), Js('Nawaal'), Js('Nawaar'), Js('Nawfa'), Js('Nawwaara'), Js('Nazeeha'), Js('Nazeema'), Js('Nazmiyya'), Js('Nisma'), Js('Noora'), Js('Nooriyya'), Js('Nuha'), Js("Nu'ma"), Js('Nusaiba'), Js('Nuzha'), Js('Qaaida'), Js('Qamraaa'), Js('Qisma'), Js('Raabia'), Js('Raabiya'), Js('Raadiya'), Js('Raafida'), Js('Raaida'), Js('Raaniya'), Js('Rabdaa'), Js('Radiyya'), Js('Radwa'), Js('Rafeeda'), Js('Rafeeqa'), Js('Raheema'), Js('Rahma'), Js('Raihaana'), Js('Raita'), Js('Ramla'), Js('Ramza'), Js('Ramziyya'), Js('Randa'), Js('Rashaa'), Js('Rasheeda'), Js('Rasheeqa'), Js('Rawda'), Js('Rayyana'), Js('Razeena'), Js('Reema'), Js("Rif'a"), Js('Rifqa'), Js('Rihaab'), Js('Rumaana'), Js('Ruqayya'), Js('Rutaiba'), Js('Ruwaida'), Js('Saabiqa'), Js('Saabira'), Js('Saafiyya'), Js('Saahira'), Js('Saajida'), Js('Saaliha'), Js('Saalima'), Js('Saamiqa'), Js('Saamyya'), Js('Saara'), Js('Sabaaha'), Js('Sabeeha'), Js('Sabeeka'), Js('Sabiyya'), Js('Sabreen'), Js('Sabriyya'), Js('Sadeeda'), Js('Sadeeqa'), Js('Safaaa'), Js('Safiyya'), Js('Safwa'), Js('Sahar'), Js('Sahheeda'), Js('Sahla'), Js('Sajaa'), Js('Sajiyya'), Js(' Sakeena'), Js('Saleema'), Js('Salma'), Js('Salwa'), Js('Sameeha'), Js('Sameera'), Js('Samraa'), Js('Sanaaa'), Js('Sanad'), Js('Sawada'), Js('Shaafia'), Js('Shaahida'), Js('Shaahira'), Js('Shaakira'), Js('Shaamila'), Js('Shabeeba'), Js('Shadhaa'), Js('Shafaaa'), Js("Shafee'a"), Js('Shafeeqa'), Js('Shahaada'), Js('Shahaama'), Js('Shaheera'), Js('Shahla'), Js('Shaimaaa'), Js("Shajee'a"), Js('Shakeela'), Js('Shakoora'), Js("Sham'a"), Js('Shamaail'), Js('Shameema'), Js('Shaqeeqa'), Js('Shareefa'), Js('Shukriyya'), Js('Siddeeqa'), Js('Sireen'), Js('Sitaara'), Js('Suhaa'), Js('Suhaad'), Js('Suhaila'), Js('Sukaina'), Js('Sulama'), Js('Sultana'), Js('Sumaita'), Js('Sumayya'), Js('Sumbula'), Js('Sundus'), Js('Taaliba'), Js('Taamira'), Js('Tahaani'), Js('Tahiyya'), Js('Tahleela'), Js('Tamanna'), Js('Tameema'), Js('Taqiyya'), Js('Tareefa'), Js('Tasneem'), Js('Tawfeeqa'), Js('Tawheeda'), Js('Tayyiba'), Js('Thaabita'), Js('Thaamira'), Js('Thamra'), Js('Thanaa'), Js('Tharwa'), Js('Tuhfa'), Js('Tulaiha'), Js('Turfa'), Js('Ulyaa'), Js('Umaima'), Js('Umaira'), Js('Ummu Kulthoom'), Js('Urwa'), Js('Waajida'), Js("Wadee'a"), Js('Wadha'), Js('Wafaaa'), Js('Waheeba'), Js('Waheeda'), Js('Wajdiyya'), Js('Wajeeha'), Js('Waleeda'), Js('Waliyya'), Js('Waneesa'), Js('Warda'), Js('Wardiyya'), Js('Waseema'), Js('Wasmaaa'), Js('Widdad'), Js('Yaasmeen'), Js('Yaasmeena'), Js('Zaahira'), Js('Zaaida'), Js('Zahra'), Js('Zahraaa'), Js('Zainab'), Js('Zaitoona'), Js('Zakiyya'), Js('Zarqaa'), Js('Zeena'), Js('Zubaida'), Js('Zuhaira'), Js('Zuhra'), Js('Zuhriyaa'), Js('Zulfa'), Js('Zumruda')]))
var.put('nm3', Js([Js('Abad'), Js('Abbas'), Js('Abbasi'), Js('Abdalla'), Js('Abdallah'), Js('Abdella'), Js('Abdelnour'), Js('Abdelrahman'), Js('Abdi'), Js('Abdo'), Js('Abdoo'), Js('Abdou'), Js('Abdul'), Js('Abdulla'), Js('Abdullah'), Js('Abed'), Js('Abid'), Js('Abood'), Js('Aboud'), Js('Abraham'), Js('Abu'), Js('Adel'), Js('Afzal'), Js('Agha'), Js('Ahmad'), Js('Ahmadi'), Js('Ahmed'), Js('Ahsan'), Js('Akbar'), Js('Akbari'), Js('Akel'), Js('Akhtar'), Js('Akhter'), Js('Akram'), Js('Alam'), Js('Ali'), Js('Allam'), Js('Allee'), Js('Alli'), Js('Ally'), Js('Aly'), Js('Aman'), Js('Amara'), Js('Amber'), Js('Ameen'), Js('Amen'), Js('Amer'), Js('Amin'), Js('Amini'), Js('Amir'), Js('Amiri'), Js('Ammar'), Js('Ansari'), Js('Anwar'), Js('Arafat'), Js('Arif'), Js('Arshad'), Js('Asad'), Js('Ashraf'), Js('Aslam'), Js('Asmar'), Js('Assad'), Js('Assaf'), Js('Atallah'), Js('Attar'), Js('Awan'), Js('Aydin'), Js('Ayoob'), Js('Ayoub'), Js('Ayub'), Js('Azad'), Js('Azam'), Js('Azer'), Js('Azimi'), Js('Aziz'), Js('Azizi'), Js('Azzam'), Js('Azzi'), Js('Bacchus'), Js('Baccus'), Js('Bacho'), Js('Baddour'), Js('Badie'), Js('Badour'), Js('Bagheri'), Js('Bahri'), Js('Baig'), Js('Baksh'), Js('Baluch'), Js('Bangura'), Js('Barakat'), Js('Bari'), Js('Basa'), Js('Basha'), Js('Bashara'), Js('Basher'), Js('Bashir'), Js('Baten'), Js('Begum'), Js('Ben'), Js('Beshara'), Js('Bey'), Js('Beydoun'), Js('Bilal'), Js('Bina'), Js('Burki'), Js('Can'), Js('Chahine'), Js('Dada'), Js('Dajani'), Js('Dallal'), Js('Daoud'), Js('Dar'), Js('Darwish'), Js('Dawood'), Js('Demian'), Js('Dia'), Js('Diab'), Js('Dib'), Js('Din'), Js('Doud'), Js('Ebrahim'), Js('Ebrahimi'), Js('Edris'), Js('Eid'), Js('Elamin'), Js('Elbaz'), Js('El-Sayed'), Js('Emami'), Js('Fadel'), Js('Fahmy'), Js('Fahs'), Js('Farag'), Js('Farah'), Js('Faraj'), Js('Fares'), Js('Farha'), Js('Farhat'), Js('Farid'), Js('Faris'), Js('Farman'), Js('Farooq'), Js('Farooqui'), Js('Farra'), Js('Farrah'), Js('Farran'), Js('Fawaz'), Js('Fayad'), Js('Firman'), Js('Gaber'), Js('Gad'), Js('Galla'), Js('Ghaffari'), Js('Ghanem'), Js('Ghani'), Js('Ghattas'), Js('Ghazal'), Js('Ghazi'), Js('Greiss'), Js('Guler'), Js('Habeeb'), Js('Habib'), Js('Habibi'), Js('Hadi'), Js('Hafeez'), Js('Hai'), Js('Haidar'), Js('Haider'), Js('Hakeem'), Js('Hakim'), Js('Halaby'), Js('Halim'), Js('Hallal'), Js('Hamad'), Js('Hamady'), Js('Hamdan'), Js('Hamed'), Js('Hameed'), Js('Hamid'), Js('Hamidi'), Js('Hammad'), Js('Hammoud'), Js('Hana'), Js('Hanif'), Js('Hannan'), Js('Haq'), Js('Haque'), Js('Hares'), Js('Hariri'), Js('Harron'), Js('Harroun'), Js('Hasan'), Js('Hasen'), Js('Hashem'), Js('Hashemi'), Js('Hashim'), Js('Hashmi'), Js('Hassan'), Js('Hassen'), Js('Hatem'), Js('Hoda'), Js('Hoque'), Js('Hosein'), Js('Hossain'), Js('Hosseini'), Js('Huda'), Js('Huq'), Js('Husain'), Js('Hussain'), Js('Hussein'), Js('Ibrahim'), Js('Idris'), Js('Imam'), Js('Iman'), Js('Iqbal'), Js('Irani'), Js('Ishak'), Js('Ishmael'), Js('Islam'), Js('Ismael'), Js('Ismail'), Js('Jabara'), Js('Jabbar'), Js('Jabbour'), Js('Jaber'), Js('Jabour'), Js('Jafari'), Js('Jaffer'), Js('Jafri'), Js('Jalali'), Js('Jalil'), Js('Jama'), Js('Jamail'), Js('Jamal'), Js('Jamil'), Js('Jan'), Js('Javed'), Js('Javid'), Js('Kaba'), Js('Kaber'), Js('Kabir'), Js('Kader'), Js('Kaiser'), Js('Kaleel'), Js('Kalil'), Js('Kamal'), Js('Kamali'), Js('Kamara'), Js('Kamel'), Js('Kanan'), Js('Karam'), Js('Karim'), Js('Karimi'), Js('Kassem'), Js('Kazemi'), Js('Kazi'), Js('Kazmi'), Js('Khalaf'), Js('Khalid'), Js('Khalifa'), Js('Khalil'), Js('Khalili'), Js('Khan'), Js('Khatib'), Js('Khawaja'), Js('Koroma'), Js('Laham'), Js('Latif'), Js('Lodi'), Js('Lone'), Js('Madani'), Js('Mady'), Js('Mahdavi'), Js('Mahdi'), Js('Mahfouz'), Js('Mahmood'), Js('Mahmoud'), Js('Mahmud'), Js('Majeed'), Js('Majid'), Js('Malak'), Js('Malek'), Js('Malik'), Js('Mannan'), Js('Mansoor'), Js('Mansour'), Js('Mansouri'), Js('Mansur'), Js('Maroun'), Js('Masih'), Js('Masood'), Js('Masri'), Js('Massoud'), Js('Matar'), Js('Matin'), Js('Mattar'), Js('Meer'), Js('Meskin'), Js('Miah'), Js('Mian'), Js('Mina'), Js('Minhas'), Js('Mir'), Js('Mirza'), Js('Mitri'), Js('Moghaddam'), Js('Mohamad'), Js('Mohamed'), Js('Mohammad'), Js('Mohammadi'), Js('Mohammed'), Js('Mohiuddin'), Js('Molla'), Js('Momin'), Js('Mona'), Js('Morad'), Js('Moradi'), Js('Mostafa'), Js('Mourad'), Js('Mousa'), Js('Moussa'), Js('Moustafa'), Js('Mowad'), Js('Muhammad'), Js('Muhammed'), Js('Munir'), Js('Murad'), Js('Musa'), Js('Mussa'), Js('Mustafa'), Js('Naderi'), Js('Nagi'), Js('Naim'), Js('Naqvi'), Js('Nasir'), Js('Nasr'), Js('Nasrallah'), Js('Nasser'), Js('Nassif'), Js('Nawaz'), Js('Nazar'), Js('Nazir'), Js('Neman'), Js('Niazi'), Js('Noor'), Js('Noorani'), Js('Noori'), Js('Nour'), Js('Nouri'), Js('Obeid'), Js('Odeh'), Js('Omar'), Js('Omer'), Js('Othman'), Js('Ozer'), Js('Parsa'), Js('Pasha'), Js('Pashia'), Js('Pirani'), Js('Popal'), Js('Pour'), Js('Qadir'), Js('Qasim'), Js('Qazi'), Js('Quadri'), Js('Raad'), Js('Rabbani'), Js('Rad'), Js('Radi'), Js('Radwan'), Js('Rafiq'), Js('Rahaim'), Js('Rahaman'), Js('Rahim'), Js('Rahimi'), Js('Rahman'), Js('Rahmani'), Js('Rais'), Js('Ramadan'), Js('Ramin'), Js('Rashed'), Js('Rasheed'), Js('Rashid'), Js('Rassi'), Js('Rasul'), Js('Rauf'), Js('Rayes'), Js('Rehman'), Js('Rehmann'), Js('Reza'), Js('Riaz'), Js('Rizk'), Js('Saab'), Js('Saad'), Js('Saade'), Js('Saadeh'), Js('Saah'), Js('Saba'), Js('Saber'), Js('Sabet'), Js('Sabir'), Js('Sadek'), Js('Sader'), Js('Sadiq'), Js('Sadri'), Js('Saeed'), Js('Safar'), Js('Safi'), Js('Sahli'), Js('Saidi'), Js('Sala'), Js('Salaam'), Js('Saladin'), Js('Salah'), Js('Salahuddin'), Js('Salam'), Js('Salama'), Js('Salame'), Js('Salameh'), Js('Saleem'), Js('Saleh'), Js('Salehi'), Js('Salek'), Js('Salem'), Js('Salih'), Js('Salik'), Js('Salim'), Js('Salloum'), Js('Salman'), Js('Samaan'), Js('Samad'), Js('Samara'), Js('Sami'), Js('Samra'), Js('Sani'), Js('Sarah'), Js('Sarwar'), Js('Sattar'), Js('Satter'), Js('Sawaya'), Js('Sayed'), Js('Selim'), Js('Semaan'), Js('Sesay'), Js('Shaban'), Js('Shabazz'), Js('Shad'), Js('Shaer'), Js('Shafi'), Js('Shah'), Js('Shahan'), Js('Shaheed'), Js('Shaheen'), Js('Shahid'), Js('Shahidi'), Js('Shahin'), Js('Shaikh'), Js('Shaker'), Js('Shakir'), Js('Shakoor'), Js('Sham'), Js('Shams'), Js('Sharaf'), Js('Shareef'), Js('Sharif'), Js('Shariff'), Js('Sharifi'), Js('Shehadeh'), Js('Shehata'), Js('Sheikh'), Js('Siddiqi'), Js('Siddique'), Js('Siddiqui'), Js('Sinai'), Js('Soliman'), Js('Soltani'), Js('Srour'), Js('Sulaiman'), Js('Suleiman'), Js('Sultan'), Js('Sultana'), Js('Syed'), Js('Sylla'), Js('Tabatabai'), Js('Tabet'), Js('Taha'), Js('Taheri'), Js('Tahir'), Js('Tamer'), Js('Tariq'), Js('Tawil'), Js('Toure'), Js('Turay'), Js('Uddin'), Js('Ullah'), Js('Usman'), Js('Vaziri'), Js('Vohra'), Js('Wahab'), Js('Wahba'), Js('Waheed'), Js('Wakim'), Js('Wali'), Js('Yacoub'), Js('Yamin'), Js('Yasin'), Js('Yassin'), Js('Younan'), Js('Younes'), Js('Younis'), Js('Yousef'), Js('Yousif'), Js('Youssef'), Js('Yousuf'), Js('Yusuf'), Js('Zadeh'), Js('Zafar'), Js('Zaher'), Js('Zahra'), Js('Zaidi'), Js('Zakaria'), Js('Zaki'), Js('Zaman'), Js('Zamani'), Js('Zia')]))
var.put('names', Js(''))
var.put('nm4', Js([Js('al-'), Js('el-')]))
pass
pass


# Add lib to the module scope
muslimNames = var.to_python()