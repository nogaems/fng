__all__ = ['nativeAmericanNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abooksigun (Algonquin)'), Js('Abornazine (Abnaki)'), Js('Abukcheech (Algonquin)'), Js('Achak (Algonquin)'), Js('Achachak (Algonquin)'), Js('Adahy (Cherokee)'), Js('Aditsan (Navajo)'), Js('Adoeete (Kiowa)'), Js('Ahanu (Algonquin)'), Js('Ahiga (Navajo)'), Js('Ahote (Hopi)'), Js('Ahtunowhiho (Cheyenne)'), Js('Ahuli (Cherokee)'), Js('Ahusaka (Winnebago)'), Js('Akecheta (Sioux)'), Js('Alahmoot (Nez Perce)'), Js('Allahkoliken (Nez Perce)'), Js('Alo (Hopi)'), Js('Alosaka (Hopi)  '), Js('Anakausuen (Algonquin)'), Js('Angvariationu Toke (Sioux)'), Js('Annawan (Algonquin)'), Js('Apash Wyakaikt (Nez Perce)'), Js('Appanoose (Sauk)'), Js('Apiatan (Kiowa)'), Js('Apisi (Blackfoot)'), Js('Aponivi (Hopi)'), Js('Aranck (Algonquin)'), Js('Ar-Ke-Kee-Tah (Oto)'), Js('Arre-Catte Waho (Omaha)'), Js('Ashkii (Navajo)'), Js('Ashkii Dighin (Navajo)'), Js('Askook (Algonquin)'), Js('Askuwheteau (Algonquin)'), Js('Atagulkalu (Cherokee)'), Js("Ata'Halne' (Navajo)"), Js('Atepa (Choctaw)'), Js('Atohi (Cherokee)'), Js('Atsadi (Cherokee)'), Js('Atsidi (Navajo)'), Js('Attakullakulla (Cherokee)'), Js('Avonaco (Cheyenne)'), Js('Ayawamat (Hopi)'), Js('Bagwunagijik (Chippewa)'), Js('Bemidii (Ojibwa)'), Js('Beshiltheeni (Navajo)'), Js('Beshkno (Potawatomi)'), Js('Bidziil (Navajo)'), Js('Bilagaana (Navajo)'), Js('Bisahalani (Navajo)'), Js('Bornbazine (Abnaki)'), Js('Buegoneguig (Chippewa)'), Js('Cameahwait (Shoshone)'), Js('Canowicakte (Sioux)'), Js('Cashesegra (Osage)'), Js('Cetanwakuwa (Sioux)'), Js("Cha'Akmongwi (Hopi)"), Js("Cha'Tima (Hopi)"), Js('Chankoowashtay (Sioux)'), Js('Chansomps (Algonquin)'), Js('Chapowits (Nez Perce)'), Js('Chas-Chunk-A (Winnebago)'), Js('Chaska (Sioux)'), Js('Chatan (Sioux)'), Js('Chavatangakwunua (Hopi)'), Js('Chayton (Sioux)'), Js('Cheasequah (Cherokee)'), Js('Cheauka  (Hopi)'), Js('Cheveyo (Hopi)'), Js('Chochmo (Hopi)'), Js('Chochokpi (Hopi)'), Js('Chochuschuvio (Hopi)'), Js('Chogan (Algonquin)'), Js('Choovio (Hopi)'), Js('Choviohoya (Hopi)'), Js('Chowilawu (Hopi)'), Js("Chu'A (Hopi)"), Js('Chuchip (Hopi)'), Js('Chunta (Hopi)'), Js('Chuslum (Nez Perce)'), Js('Chuslum Moxmox (Nez Perce)'), Js('Ciqala (Dakota)'), Js('Coowescoowe (Cherokee)'), Js('Dadgayadoh (Seneca)'), Js('Dakota (Sioux)'), Js('Deganawidah (Iroquois)'), Js('Degotoga (Cherokee)'), Js('Diwali (Cherokee)'), Js('Dohate (Kiowa)'), Js('Dohosan (Kiowa)'), Js('Donehogawa (Seneca)'), Js('Dustu (Cherokee)'), Js('Ealahweemah (Nez Perce)'), Js('Ealaot Wadass (Nez Perce)'), Js('Ealaothek Kaunis (Nez Perce)'), Js('Eapalekthiloom (Nez Perce)'), Js('Ehane (Cheyenne)'), Js('Elaskolatat (Nez Perce)'), Js('Elki (Miwok)'), Js('Elsu (Miwok)'), Js('Eluwilussit (Algonquin)'), Js('Enapay (Sioux)'), Js('Enkoodabooaoo (Algonquin)'), Js('Enkoodabaoo (Algonquin) '), Js('Eskaminzim (Apache)'), Js('Espowyes (Nez Perce)'), Js('Etchemin (Algonquin)'), Js('Etlelooaat (Algonquin)'), Js('Eyanosa (Sioux)'), Js('Fala (Choctaw)'), Js('Gaagii (Navajo)'), Js('Gad (Navajo)'), Js('Gawonii (Cherokee)'), Js('Gomda (Kiowa)'), Js('Guitonkagya (Kiowa)'), Js('Hahkethomemah (Cheyenne)'), Js('Harkahome (Cheyenne)'), Js('Halian (Zuni)'), Js('Hania (Hopi)'), Js('Hanska (Sioux)'), Js('Hassun (Algonquin)'), Js('Harkahome (Cheyenne)'), Js('Hastiin (Navajo)'), Js('Hawiovi (Hopi)'), Js('Heammawihio (Cheyenne)'), Js('Heinmot (Nez Perce)'), Js('He-Lush-Ka (Winnebago)'), Js('Helki (Miwok)'), Js('Hemene (Nez Perce)'), Js('Hento (Dakota)'), Js('Heskovizenako (Cheyenne)'), Js('Hesutu (Miwok)'), Js('Hevataneo (Cheyenne)'), Js('Hevovitastamiutsto (Cheyenne)'), Js('Hiamovi (Cheyenne) '), Js('Hinto (Dakota)'), Js('Hohnihohkaiyohos (Cheyenne) '), Js('Neeheeoeewootis (Cheyenne)'), Js("Hok'Ee (Navajo)"), Js('Holata (Seminole)'), Js('Honani (Hopi)'), Js('Honaw (Hopi)'), Js('Honiahaka (Cheyenne)'), Js('Honon (Miwok)'), Js('Honovi (Hopi)'), Js('Hotah (Sioux)'), Js('Hototo (Hopi)'), Js('Hotuaekhaashtait (Cheyenne)'), Js('Howahkan (Sioux)'), Js('Howi (Miwok)'), Js('Huritt (Algonquin)'), Js('Iiniwa (Blackfoot)'), Js('Istaqa (Hopi)'), Js('Istaqa (Hopi)'), Js('Kachada (Hopi) '), Js('Kangee (Sioux)'), Js('Kanuna (Cherokee)'), Js('Keezheekoni (Chippewa)'), Js('Kele (Hopi)'), Js('Keme (Algonquin)'), Js('Kesegowaase (Algonquin)'), Js('Kestejoo (Algonquin)'), Js('Kilchii (Navajo)'), Js('Kitchi (Algonquin)'), Js('Kiyiya (Yakima)'), Js('Klah (Navajo)'), Js('Kohana (Sioux)'), Js('Kohkahycumest (Cheyenne)'), Js('Koi (Choctaw)'), Js('Koko (Black Foot)'), Js('Kokotni (Potawatomi)'), Js('Kolichiyaw (Hopi)'), Js('Kono (Miwok)'), Js('Koshisigre (Osage)'), Js('Kosumi (Miwok)'), Js('Kotori (Hopi)'), Js('Kuckunniwi (Cheyenne)'), Js('Kuruk (Pawnee)'), Js('Kusinut (Yakima)'), Js('Kwahu (Hopi)'), Js('Kwatoko (Hopi)'), Js('Lallo (Kiowa)'), Js('Lansa (Hopi)'), Js('Lanu (Miwok)'), Js('Lapu (Hopi)'), Js('Len (Hopi)'), Js('Lena (Hopi)'), Js('Lesharo (Pawnee)'), Js('Leyati (Miwok)'), Js('Lise (Miwok)'), Js('Liwanu (Miwok)'), Js('Lokni (Miwok)'), Js('Lonan (Zuni)'), Js('Lootah (Sioux)'), Js('Lusio (Zuni)'), Js('Machakw (Hopi)'), Js('Machk (Algonquin)'), Js('Mahkah (Sioux)'), Js('Mahpee (Sioux)'), Js('Makkapitew (Algonquin)'), Js('Makya (Hopi)'), Js('Mammedaty (Kiowa)'), Js('Mantotohpa (Cheyenne)'), Js('Masichuvio (Hopi) '), Js('Matchitehew (Algonquin)'), Js('Matchitisiw (Algonquin)'), Js('Mato (Sioux)'), Js('Matoskah (Sioux)'), Js('Matunaaga (Algonquin)'), Js('Matwau (Algonquin)'), Js('Maza Blaska (Dakota)'), Js('Megedagik (Algonquin)'), Js('Melkedoodum (Algonquin)'), Js('Micanopy (Seminole)'), Js('Micco (Seminole)'), Js('Migisi (Chippewa)'), Js('Mika (Sioux)'), Js('Mikasi (Omaha)'), Js('Mikasi (Hokan)'), Js('Minco (Choctaw)'), Js('Mingan (Algonquin)'), Js('Minninnewah (Cheyenne)'), Js('Misu (Miwok)'), Js('Mochni (Hopi)'), Js('Mohe (Cheyenne)'), Js('Moki (Hopi)'), Js('Molimo (Miwok)'), Js('Momuso (Miwok)  '), Js('Mona (Miwok)'), Js('Mongwau (Hopi)'), Js('Motsqueh (Nez Perce)'), Js('Muata (Miwok)'), Js('Mukki (Algonquin)'), Js('Naalnish (Navajo)'), Js('Nadie (Algonquin)'), Js('Nahcomence (Cheyenne)'), Js('Nahiossi (Cheyenne)'), Js('Nakai (Navajo)'), Js('Nakos (Arapaho)'), Js('Namid (Chippewa)'), Js('Namida (Chippewa)'), Js('Nantan (Apache)'), Js('Napayshni (Sioux)'), Js('Nashashuk (Sauk)'), Js('Nashoba (Choctaw)'), Js('Nastas (Navajo)'), Js('Nawkaw (Winnebago)'), Js('Nayavu (Hopi)'), Js('Neeheeoeewootis (Cheyenne)'), Js('Niichaad (Navajo)'), Js('Nikan (Potawatomi)'), Js('Nita (Choctaw)'), Js('Nixkamich (Algonquin)'), Js('Niyol (Navajo)'), Js('Nokosi (Seminole)'), Js('Nootau (Algonquin)'), Js('Nosh (Algonquin)'), Js('Noshi (Algonquin)'), Js('Notaku (Miwok)'), Js('Nukpana (Hopi)'), Js('Ocumwhowurst (Cheyenne) '), Js('Ocunnowhurst (Cheyenne)'), Js('Odakota (Sioux)'), Js('Ogaki (Arapaho)'), Js('Ogaleesha (Sioux)'), Js('Ogima (Potawatomi)'), Js('Ohanzee (Sioux)'), Js('Okhmhaka (Cheyenne)'), Js('Ohitekah (Sioux)'), Js('Ohiyesa (Sioux)'), Js('Okemos (Ojibway)'), Js('Okhmhaka (Cheyenne)'), Js('Okomi (Arapaho)'), Js('Omawnakw (Hopi)'), Js('Onacona (Cherokee)'), Js('Opechancanough (Algonquin)'), Js('Osceola (Seminole)'), Js('Otaktay (Sioux)'), Js('Otetiani (Iroquois)'), Js('Otoahhastis (Cheyenne)'), Js('Otoahnacto (Cheyenne)'), Js('Otskai (Nez Perce)'), Js('Ouray (Ute)'), Js('Pa-Akanti (Kiowa)'), Js("Pachu'A (Hopi)"), Js('Pahana (Hopi)'), Js('Pajackok (Algonquin)'), Js('Pannoowau (Algonquin)'), Js('Paytah (Sioux)'), Js('Peopeo (Nez Perce)'), Js('Peta (Black Foot)'), Js('Pezi (Sioux)'), Js('Pimne (Hopi)'), Js('Pitalesharo (Pawnee)'), Js('Pivane (Hopi)'), Js('Powwaw (Algonquin)'), Js('Powwow (Algonquin)'), Js('Qaletaqa (Hopi)'), Js('Qochata (Hopi)'), Js('Quanah (Comanche)'), Js('Rowtag (Algonquin)'), Js('Sahkonteic (Nez Perce)'), Js('Sakima (Ojibwa)'), Js('Sakuruta (Pawnee)'), Js('Samoset (Algonquian)'), Js('Sani (Navajo)'), Js('Satanta (Kiowa)'), Js('Segenam (Algonquin)'), Js('Sequoyah (Cherokee)'), Js('Setangya (Kiowa)'), Js('Setimika (Kiowa)'), Js('Sewati (Miwok)'), Js('Shappa (Sioux)'), Js('Shilah (Navajo)'), Js('Shiriki (Pawnee)'), Js('Shishiesh (Crow)'), Js('Shiye (Navajo)'), Js("Shizhe'E (Navajo)"), Js('Shuman (Hopi)'), Js('Sicheii (Navajo)'), Js("Sik'Is (Navajo)"), Js('Sike (Navajo)'), Js('Sikyahonaw (Hopi)'), Js('Sikyatavo (Hopi)'), Js('Sinte Maza (Sioux)'), Js('Sipatu (Miwok)'), Js('Skah (Sioux)'), Js("Sowi'Ngwa (Hopi)"), Js('Soyala (Hopi)'), Js('Sucki (Algonquin)'), Js('Sugmuk (Potawatomi)'), Js('Sugnog (Potawatomi)'), Js('Sunukkuhkau (Algonquin)'), Js("T'Iis (Navajo)"), Js('Tadi (Omaha)'), Js('Tahatan (Sioux)'), Js('Taheton (Sioux)'), Js('Tahkeome (Cheyenne)'), Js('Tahmelapachme (Cheyenne)'), Js('Tahoma (Navajo)'), Js('Takoda (Sioux)'), Js('Tangakwunu (Hopi)'), Js('Tapco (Kiowa)'), Js('Taregan (Algonquin)'), Js('Tashunka (Sioux)'), Js('Tasunke (Dakota)'), Js('Tatanka-Ptecila (Dakota)'), Js('Tatonga (Sioux)'), Js('Tawa (Hopi)'), Js('Tayanita (Cherokee)'), Js('Teetonka (Sioux)'), Js('Telutci (Miwok)'), Js('Tuketu (Miwok)'), Js('Tihkoosue (Algonquin)'), Js('Tocho (Hopi)'), Js('Todi (Omaha)'), Js('Togquos (Algonquin)'), Js('Tohopka (Hopi)'), Js('Tokala (Dakota)'), Js('Tokota (Sioux)'), Js('Tooantuh (Cherokee)'), Js('Tse (Navajo)'), Js('Tsela (Navajo)'), Js("Tsiishch'Ili (Navajo)"), Js('Tsiyi (Cherokee)'), Js('Tsoai (Kiowa)'), Js('Tuari (Laguna)'), Js('Tuari (Hokan)'), Js('Tuketu (Miwok)'), Js('Tumu (Miwok)'), Js('Tupi (Miwok)'), Js('Tyee (Chinook)'), Js('Unaduti (Cherokee)'), Js('Usti (Cherokee)'), Js('Uzumati (Miwok)'), Js('Viho (Cheyenne)'), Js('Vipponah (Cheyenne)'), Js('Vohkinne (Cheyenne)'), Js('Vokivocummast (Cheyenne)'), Js('Waboyan (Potawatomi)'), Js('Wahanassatta (Cheyenne)'), Js('Wahchinksapa (Sioux)'), Js('Wahchintonka (Sioux)'), Js('Wahkan (Sioux)'), Js('Wahkoowah (Sioux)'), Js('Wamblee (Sioux)'), Js('Wambleeska (Sioux)'), Js('Wambli-Waste (Dakota)'), Js('Wanageeska (Sioux)'), Js('Wanahton (Sioux)'), Js('Wanikiya (Sioux)'), Js('Wanikiy (Sioux)'), Js('Wapti (Potawatomi)'), Js('Waquini (Cheyenne)'), Js('Wattan (Arapaho)'), Js('Waya (Cherokee)'), Js('Weayaya (Sioux)'), Js('Wematin (Algonquin)'), Js('Wesa (Cherokee)'), Js('Wicasa (Dakota)'), Js('Wikvaya (Hopi)'), Js('Wilu (Miwok)'), Js('Whakan (Sioux)'), Js('Wis Ki Gete (Potawatomi)'), Js('Wohali (Cherokee)'), Js('Wohehiv (Cheyenne)'), Js('Wokaihwokomas (Cheyenne)'), Js('Wuyi (Miwok)'), Js('Yahto (Sioux)'), Js('Yanisin (Navajo)'), Js('Yansa (Cherokee)'), Js('Yas (Navajo)'), Js('Yiska (Navajo)')]))
var.put('nm2', Js([Js('Abedabun (Cheyenne)'), Js('Abequa (Cheyenne)'), Js('Abeque (Cheyenne)'), Js('Abetzi (Omaha)'), Js('Abey (Omaha)'), Js('Abeytu (Omaha)'), Js('Adoette (Kiowa)'), Js('Adsila (Cherokee)'), Js('Agasga (Cherokee)'), Js('Ahawi (Cherokee)'), Js('Ahyoka (Cherokee) '), Js('Alawa (Algonquin)'), Js('Aleshanee (Coos)'), Js('Alsoomse (Algonquin)'), Js('Altsoba (Navajo)'), Js('Ama (Cherokee)'), Js('Amadahy (Cherokee)'), Js('Amayeta (Miwok'), Js('Anaba (Navajo)'), Js('Anamosa (Sauk)'), Js('Angpetu (Sioux)'), Js('Angwusnasomtaqa (Hopi)'), Js('Ankti (Hopi)'), Js('Anna (Algonquin)'), Js('Anpaytoo (Sioux) '), Js('Asdza (Navajo)'), Js("At'Eed (Navajo)"), Js('Atepa (Choctaw)'), Js('Atsila (Cherokee)'), Js('Awanata (Miwok)'), Js('Awenasa (Cherokee) '), Js('Awinita (Cherokee)'), Js('Ayasha (Cheyenne)'), Js('Ayashe (Cheyenne)'), Js('Ayita (Cherokee)'), Js('Bonita (Apache)'), Js('Byhalia (Choctaw)'), Js('Calfuray (Mapuche)'), Js('Catori (Hopi)'), Js("Cha'Kwaina (Hopi)"), Js("Cha'Risa (Hopi)"), Js('Chapa (Sioux)'), Js('Chapawee (Sioux)'), Js('Chepi (Algonquin)'), Js('Chlumani (Sioux)'), Js('Chochmingwu (Hopi)'), Js('Chosovi (Hopi)'), Js('Chosposi (Hopi)'), Js("Chu'Mana (Hopi)"), Js("Chu'Si (Hopi)"), Js('Chumani (Sioux)'), Js('Ciqala(Dakota)'), Js('Coahoma (Choctaw)'), Js('Dezba (Navajo)'), Js('Dibe (Navajo)'), Js('Doba (Navajo)'), Js('Doli (Navajo)'), Js('Donoma (Omaha)'), Js('Dowanhowee (Sioux)'), Js('Doya (Cherokee)'), Js('Ehawee (Sioux)'), Js('Elu (Zuni)'), Js('Ethete (Arapaho)'), Js('Eyota (Sioux)'), Js('Fala (Choctaw)'), Js('Galilahi (Cherokee)'), Js('Genessee (Iroquois)'), Js('Gigyago (Potawatomi)'), Js('Goga (Cherokee)'), Js('Gola (Cherokee)'), Js('Hachi (Seminole)'), Js('Haiwee (Shoshone)'), Js('Hakidonmuya (Hopi)'), Js('Haloke (Navajo)'), Js('Hantaywee (Sioux)'), Js('Hateya (Miwok)'), Js('Hausis (Algonquin)'), Js('Hausisse (Algonquin)'), Js('Hehewuti (Hopi)'), Js('Helki (Miwok)'), Js('Hialeah (Seminole)'), Js('Hiawassee (Cherokee)'), Js('Hinto (Dakota)'), Js('Hola (Hopi)'), Js('Honiahaka (Cheyenne)'), Js('Honovi (Hopi)'), Js('Howi (Miwok)'), Js('Huata (Miwok)'), Js('Huata (Moquelumnan)'), Js('Humita (Hopi)'), Js('Hurit (Algonquin)'), Js('Huyana (Miwok)'), Js('Inola (Cherokee)'), Js('Isi (Choctaw)'), Js('Jaci (Tupi)'), Js('Kachina (Hopi)'), Js('Kai (Navajo)'), Js('Kakawangwa (Hopi)'), Js('Kaliska (Miwok)'), Js('Kamali (Mahona)'), Js('Kamama (Cherokee)'), Js('Kangee (Sioux)'), Js('Kanti (Algonquin)'), Js('Kasa (Hopi)'), Js('Kaya (Hopi)'), Js('Keegsquaw (Algonquin)'), Js('Keezheekoni (Cheyenne)'), Js('Keezheekoni (Chippewa)'), Js('Kele (Hopi)'), Js('Kenda (Dakota)'), Js('Kewanee (Potawatomi)'), Js('Kimama (Shoshone)'), Js('Kimi (Algonquin)'), Js('Kimimela (Sioux)'), Js('Kinta (Choctaw)'), Js('Kiwidinok (Cheyenne)'), Js('Kiwidinok (Chippewa)'), Js('Kokyangwuti (Hopi)'), Js('Kolenya (Miwok)'), Js('Kosa (Cheyenne)'), Js('Kuckunniwi (Cheyenne)'), Js('Kuwanlelenta (Hopi)'), Js('Kuwanyamtiwa (Hopi)'), Js('Kuwanyauma (Hopi)'), Js('Kwanita (Zuni)'), Js('Lenmana (Hopi)'), Js('Liluye (Miwok)'), Js('Liseli (Zuni'), Js('Litonya (Miwok)'), Js('Lomahongva (Hopi)'), Js('Macawi (Sioux)'), Js('Macha (Sioux)'), Js('Magaskawee (Sioux)'), Js('Mahu (Hopi) '), Js('Maka (Sioux)'), Js('Makawee (Sioux)'), Js('Makkitotosimew (Algonquin)'), Js('Malia (Zuni)'), Js('Malila (Miwok)'), Js('Manaba (Navajo)'), Js('Mankalita (Zuni '), Js('Mansi (Hopi)'), Js('Mapiya (Sioux)'), Js('Meli (Zuni)'), Js('Memdi (Henna'), Js('Meoquanee (Cheyenne)'), Js('Meoquanee (Chippewa)'), Js('Migina (Omaha)'), Js('Migisi (Cheyenne)'), Js('Migisi (Chippewa)'), Js('Mimiteh (Omaha)'), Js('Mina (Sioux)'), Js('Minya (Osage)'), Js('Misae (Osage)'), Js('Misu (Miwok)'), Js('Mitena (Ojibway)'), Js('Mitena (Omaha)'), Js('Mituna (Miwok)'), Js('Mosi (Navajo)'), Js('Muna (Hopi)'), Js('Nadie (Algonquin)'), Js('Nahimana (Sioux)'), Js('Namid (Cheyenne)'), Js('Namid (Chippewa)'), Js('Namida (Chippewa)'), Js('Nampeyo (Hopi)'), Js('Nascha (Navajo)'), Js('Natane (Arapaho)'), Js('Neche (Ojibway)'), Js('Nekoma (Chippewa)'), Js('Niabi (Osage)'), Js('Nidawi (Omaha)'), Js('Nijlon (Algonquin)'), Js('Nimeda (Potawatomi)'), Js('Ninovan (Cheyenne)'), Js('Nirvelli (Tudas)'), Js('Nishwequanniquaweseh (Algonquin)'), Js('Nita (Choctaw)'), Js('Nittawosew (Algonquin)'), Js('Niyol (Navajo)'), Js('Nokomis (Cheyenne)'), Js('Nokomis (Chippewa)'), Js('Nova (Hopi)'), Js('Noya (Cherokee)'), Js('Nukpana (Hopi)'), Js('Numees (Algonquin)'), Js('Nuttah (Algonquin)'), Js('Odahingum (Cheyenne)'), Js('Odahingum (Chippewa)'), Js('Odina (Algonquian)'), Js('Ohcumgache (Cheyenne)'), Js('Ojinjintka (Sioux)'), Js('Ominotago (Cheyenne)'), Js('Omusa (Miwok)'), Js('Onaiwah (Ojibway)'), Js('Onatah (Iroquois)'), Js('Ooljee (Navajo)'), Js('Oota Dabun (Algonquin)'), Js('Opa (Choctaw)'), Js('Orenda (Iroquois)'), Js('Osyka (Choctaw)'), Js('Otekah (Navajo)'), Js('Oya (Moquelumnan)'), Js('Pakuna (Miwok)'), Js('Pakwa (Hopi)'), Js('Pamuy (Hopi)'), Js('Pamuya (Hopi)'), Js('Pana (Blackfoot)'), Js('Panola (Choctaw)'), Js('Papina (Miwok)'), Js('Pati (Miwok)'), Js('Pauwau (Algonquin)'), Js('Pavati (Hopi)'), Js('Pazi (Ponca)'), Js('Pelipa (Zuni)'), Js('Polikwaptiwa (Hopi)'), Js('Poloma (Choctaw)'), Js('Posala (Miwok)'), Js('Powaqa (Hopi)'), Js('Ptaysanwee (Sioux)'), Js('Pules (Algonquin)'), Js('Quahneah(Cheyenne)'), Js('Quanah(Comanche)'), Js('Sacajawea (Shoshone)'), Js('Sahkyo (Navajo)'), Js('Sahpooly (Kiowa)'), Js('Salali (Cherokee)'), Js('Sanuye (Miwok)'), Js('Sapata (Miwok)'), Js('Sasa (Cherokee)'), Js('Shadi (Navajo)'), Js('Sheshebens (Cheyenne)'), Js('Sheshebens (Chippewa)'), Js('Shideezhi (Navajo)'), Js('Shima (Navajo)'), Js('Shimasani (Navajo)'), Js('Shuman (Hopi)'), Js('Sihu (Hopi)'), Js('Sikya (Hopi)'), Js('Sinopa (Blackfoot)'), Js('Sinopa (Cayuse)'), Js('Sipatu (Miwok)'), Js('Sitala (Miwok)'), Js('Sitsi (Navajo)'), Js('Skenandoa (Iroquois)'), Js('Snana (Sioux)'), Js('Sokanon (Algonquin)'), Js('Sokw (Algonquin)'), Js('Sonoma (Miwok)'), Js('Sooleawa (Algonquin)'), Js('Soyala (Hopi)'), Js('Suletu (Miwok)'), Js('Suni (Zuni)'), Js('Suni Nati (Zuni)'), Js('Sunki (Hopi)'), Js('Taa (Zuni)'), Js('Tablita (Hopi)'), Js('Taci (Zuni)'), Js('Tadewi (Omaha)'), Js('Tadita (Omaha)'), Js('Tahki (Algonquin)'), Js('Taigi(Omaha) '), Js('Taini (Omaha)'), Js('Taipa (Miwok)'), Js('Takala (Hopi)'), Js('Takchawee (Sioux)'), Js('Takhi (Algonquin)'), Js('Talulah (Choctaw)'), Js('Talutah (Sioux)'), Js('Tangakwunu (Hopi)'), Js('Tansy (Hopi)'), Js('Tayanita (Cherokee)'), Js('Tiponi (Hopi)'), Js('Tiva (Hopi)'), Js('Tiwa (Zuni)'), Js('Tokala (Dakota)'), Js('Tolinka (Miwok)'), Js('Tooantuh (Cherokee)'), Js('Toski (Hopi)'), Js('Totsi (Hopi)'), Js("Tsiishch'Ili (Navajo)"), Js('Tsomah (Kiowa)'), Js('Tsula (Cherokee)'), Js('Tula (Choctaw)'), Js('Tusa (Zuni)'), Js('Tuuwa (Hopi)'), Js('Tuwa (Hopi)'), Js('Una (Hopi)'), Js('Unega (Cherokee)'), Js('Urika (Omaha)'), Js('Usdi (Cherokee)'), Js('Utina (Timucua)'), Js('Wachiwi (Sioux)'), Js('Wakanda (Sioux)'), Js('Waki (Hopi)'), Js('Wanekia (Paiute)'), Js('Wapun (Potawatomi)'), Js('Washta (Sioux)'), Js('Watseka (Potawatomi)'), Js('Wauna (Miwok)'), Js('Wawetseka (Potawatomi)'), Js('Weayaya (Sioux)'), Js('Weeko (Sioux)'), Js('Wenona (Sioux)'), Js('Wenonah (Sioux)'), Js('Wichahpi (Sioux)'), Js('Wihakayda (Sioux)'), Js('Wikimak (Algonquin)'), Js('Winona (Sioux)'), Js('Witashnah (Sioux)'), Js('Woya (Cherokee)'), Js('Wuti (Hopi)'), Js('Wyome (Algonquian)'), Js('Xochitl (Nahuatl)'), Js('Yamka (Hopi)'), Js('Yanaba (Navajo)'), Js('Yatokya (Zuni)'), Js('Yazhi (Navajo)'), Js('Yenene (Miwok)'), Js('Yoki (Hopi)'), Js('Yona (Cherokee)'), Js('Yoomee (Coos)'), Js('Yutu (Miwok)'), Js('Zihna (Hopi)'), Js('Ziracuny (Kiowa)'), Js('Zitkala (Dakota)'), Js('Zonta (Sioux)')]))
pass
pass


# Add lib to the module scope
nativeAmericanNames = var.to_python()