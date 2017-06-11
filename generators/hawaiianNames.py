__all__ = ['hawaiianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js("'A'ala"), Js("'A'amakualenalena"), Js("'Aila'au"), Js("'Ailana"), Js("'Ailani"), Js("'Ainakea"), Js("'Ainalani"), Js("'Ainanani"), Js("'Akahi"), Js("'Akau"), Js("'Ala"), Js("'Alaneo"), Js("'Alepo'i"), Js("'Alihi Kaua"), Js("'Alohi"), Js("'Alohilani"), Js("'Alohilohi"), Js("'Aluna"), Js("'Ano'i"), Js("'Ano'ipua"), Js("'Anolani"), Js("'Apona"), Js("'Auina"), Js("'Aukai"), Js("'Ehu"), Js("'Ele"), Js("'Enakai"), Js("'Ilima"), Js("'Iolani"), Js("'Olina"), Js("'Opunui"), Js("A'alona"), Js("A'ia'i"), Js('Aarona '), Js('Ahe'), Js('Aheahe'), Js('Ahonui'), Js('Ahuahu'), Js('Ahulani'), Js('Aiwaiwa'), Js("Aka'ula"), Js('Akahele'), Js('Akamai'), Js('Akamu'), Js('Akamu '), Js('Akanahe'), Js('Akeakamai'), Js('Akela'), Js('Akiliano'), Js('Akoni'), Js('Akoni '), Js("Alaka'i"), Js('Alamimo'), Js('Alana'), Js('Alani'), Js("Alapa'i"), Js('Alapai'), Js('Alaula'), Js('Alebana'), Js('Alekanedero'), Js('Alekanekelo'), Js('Alekona'), Js('Alemana'), Js('Alena '), Js('Alepana'), Js('Aletona'), Js('Alevina'), Js('Alewina'), Js("Ali'imalu"), Js('Alika'), Js('Aloalo'), Js('Aloha'), Js('Alohaekaunei'), Js('Alohalani'), Js('Alohanani'), Js('Alohilani'), Js('Aloiki'), Js('Aloisi'), Js('Amoka'), Js('Amosa'), Js('Anadare'), Js('Anakale'), Js('Anakoni'), Js('Analu'), Js('Anatoni'), Js('Anederea'), Js('Anekelea'), Js('Anela'), Js('Aniani'), Js('Ano'), Js('Anolu '), Js('Anuenue'), Js('Anuenue Akua'), Js('Anuhea'), Js('Aolani'), Js('Aoloa'), Js('Aonani'), Js('Aouli'), Js('Aowena'), Js('Apekaloma'), Js('Apela'), Js('Apelahama'), Js('Apikai'), Js('Aremana'), Js('Atoni'), Js("Auali'i"), Js("Aukanai'i"), Js('Aukukino'), Js('Aulani'), Js('Aulii'), Js('Aumoe'), Js('Ehehene'), Js('Ekewaka '), Js('Elika '), Js('Ewe'), Js('Ewekapu'), Js('Ewelani'), Js('Feleti'), Js("Ha'aheo"), Js("Ha'iku"), Js("Ha'ulili"), Js("Ha'upu"), Js('Haku'), Js('Hakumele'), Js('Halana malie'), Js('Hale '), Js('Haleakua'), Js('Halemano'), Js("Hali'a"), Js("Hali'aaloha"), Js("Hali'imaile"), Js('Halia'), Js('Haloa'), Js('Halolani'), Js('Halulu'), Js('Hanaaloha'), Js('Hanaiakamalama'), Js('Hanakahi'), Js('Hanalei'), Js('Hanau hou'), Js('Hanauhoulani'), Js('Hani'), Js('Hanini'), Js('Hanohano'), Js('Haoa '), Js('Hau kea'), Js("Hau'oli"), Js("Hau'oli'oli"), Js('Haulani'), Js("Haumakapu'u"), Js('Haunani'), Js('Haupuehuehu'), Js('Hawaii'), Js('Hekili'), Js('Heleuma'), Js('Hemolele'), Js('Hemolelekeakua'), Js('Heneli '), Js("Hi'ilani"), Js("Hi'ilawe"), Js("Hi'ilei"), Js("Hiapa'i'ole"), Js('Hiapo'), Js('Hie'), Js('Hiehie'), Js('Hikialani'), Js('Hilo'), Js('Hinano'), Js('Hinuhinu'), Js('Hiwa lani'), Js('Hiwahiwa'), Js('Hiwahiwakeiki'), Js("Ho'ohie"), Js("Ho'ohiehie"), Js("Ho'okele"), Js("Ho'ola'i"), Js("Ho'olana"), Js("Ho'olaua'e"), Js("Ho'opa'a"), Js('Hoa kua'), Js('Hoa pili'), Js("Hoaalohakupa'a"), Js('Hoaka'), Js('Hoakoa'), Js('Hoalohalani'), Js('Hoalohanani'), Js('Hokeo'), Js('Hoku'), Js('Hoku ala'), Js("Hoku'alohi"), Js('Hokuao'), Js('Hokuaonani'), Js("Hokuhelele'i"), Js('Hokulani'), Js("Hokule'a"), Js('Hokulele'), Js("Hokuli'ili'i"), Js("Hokupa'a"), Js("Holo'oka'a"), Js('Holokai'), Js('Holomakani'), Js('Hone'), Js('Honehone'), Js('Honi'), Js("Hu'elani"), Js("Hu'eu"), Js('Huaka'), Js('Hualani'), Js('Huali'), Js('Huananai'), Js('Huapala'), Js('Hulama'), Js("Huluali'i"), Js('Hunakai'), Js('Iakepa'), Js('Iakona '), Js('Iasepa'), Js('Ihe'), Js('Ihupani'), Js('Ikaika'), Js('Ilihia'), Js('Inoa'), Js('Inoke'), Js('Ioane '), Js('Iokepa'), Js('Iokua '), Js('Iolani'), Js("Iona'ala"), Js('Ionatana '), Js('Ipo'), Js('Ipolani'), Js('Iukekini '), Js('Iwalani'), Js('Iwana '), Js("Ka'ana'ana"), Js("Ka'aona"), Js("Ka'apeha"), Js("Ka'aukai"), Js("Ka'aumoana"), Js("Ka'ehu"), Js("Ka'ena"), Js("Ka'eo"), Js("Ka'ihikapu"), Js("Ka'iimamao"), Js("Ka'ike'apona"), Js("Ka'ili"), Js("Ka'ilinemo"), Js("Ka'imi"), Js("Ka'iulani"), Js("Ka'ohu"), Js("Ka'uhane"), Js("Kaha'aheo"), Js("Kaha'i"), Js('Kahakea'), Js('Kahakuhale'), Js('Kahakuloa'), Js('Kahale'), Js('Kahana'), Js('Kahananui'), Js('Kahanu'), Js('Kahaulani'), Js('Kahauolupea'), Js('Kahawai'), Js('Kaheka'), Js("Kaheka'alohi"), Js('Kahekili'), Js('Kahele'), Js('Kahelemeakua'), Js('Kahewai'), Js('Kahiau'), Js('Kahikilani'), Js('Kahikina'), Js('Kahikookeakua'), Js('Kahili'), Js('Kahoku'), Js('Kaholo'), Js('Kahoni'), Js('Kahua'), Js('Kahue'), Js('Kahuna'), Js('Kai'), Js('Kaiaka'), Js('Kaiapo'), Js('Kaiea'), Js('Kaiemi'), Js('Kaihalulu'), Js('Kaihe'), Js('Kaihekoa'), Js("Kaiho'i"), Js('Kaihohonu'), Js('Kaiholo'), Js('Kaikane'), Js('Kaikea'), Js('Kaiko'), Js('Kaili'), Js('Kaimalie'), Js('Kaimalolo'), Js('Kaimana'), Js('Kainalu'), Js('Kainehe'), Js('Kainoa'), Js("Kainu'u"), Js('Kainui'), Js('Kaipalaoa'), Js('Kaipo'), Js("Kaipo'i"), Js('Kaiulu'), Js('Kaiwi'), Js('Kakahi'), Js('Kakielekea'), Js('Kakumulani'), Js('Kala'), Js("Kala'i"), Js('Kalaheo'), Js('Kalama'), Js('Kalani'), Js("Kalawai'a"), Js('Kalawina '), Js('Kale'), Js('Kale '), Js("Kale'a"), Js('Kaleho'), Js('Kalei'), Js('Kaleialoha'), Js('Kaleikaumaka'), Js('Kaleiokalani'), Js('Kaleo'), Js('Kaleoaloha'), Js('Kaleolani'), Js('Kalia'), Js('Kaliko'), Js('Kalikohemolele'), Js('Kalili'), Js('Kalino'), Js('Kalua'), Js('Kama'), Js('Kama hele'), Js("Kamaha'o"), Js("Kamahi'ai"), Js('Kamaile'), Js('Kamaka'), Js('Kamakakoa'), Js('Kamakana'), Js('Kamakani'), Js('Kamala'), Js('Kamalani'), Js('Kamalei'), Js('Kamaluhiakapu'), Js('Kamamalu'), Js('Kamani'), Js('Kamea'), Js('Kamealoha'), Js('Kamoku'), Js('Kamole'), Js('Kamuela '), Js('Kana'), Js("Kana'i"), Js('Kanakanui'), Js('Kanale '), Js('Kanaloa'), Js('Kanani'), Js('Kane'), Js("Kaneho'omalu"), Js('Kanoa'), Js('Kanoelani'), Js('Kanuha'), Js('Kanupa'), Js('Kapahu'), Js('Kapalaoa'), Js('Kapalekanaka'), Js('Kapali'), Js('Kapena'), Js('Kapono'), Js('Kapua'), Js("Kapua'ilima"), Js("Kapua'ula"), Js('Kapueo'), Js('Kapula'), Js('Kapule'), Js('Kapuni'), Js("Kau'i"), Js("Kau'ilani"), Js('Kauanoe'), Js('Kauhi'), Js('Kaulana'), Js('Kawai'), Js('Kawailani'), Js('Kawaimomona'), Js('Kawelo'), Js('Kawena'), Js("Kawena'ula"), Js('Kawika'), Js('Kawikani'), Js("Ke'ala"), Js("Ke'alohi"), Js("Ke'alohilani"), Js("Ke'ohi"), Js('Keahi'), Js('Keahilani'), Js('Keaka'), Js('Keaka '), Js('Keala´alohi'), Js('Keala'), Js('Kealamauloa'), Js('Kealani'), Js("Keali'i"), Js('Kealii'), Js('Kealoha'), Js('Keani'), Js('Keanu'), Js('Keao'), Js('Keawe'), Js('Keha'), Js('Kei'), Js('Keikemamake'), Js('Keiki'), Js('Keikilani'), Js('Kekelika '), Js('Kekipi'), Js('Kekoa'), Js('Kelalani'), Js('Kelani'), Js('Kele '), Js('Kelewina '), Js('Keli '), Js("Keli'i"), Js('Kelii'), Js('Kenika '), Js('Keo'), Js('Keo '), Js('Keoki '), Js('Keokolo '), Js('Keola'), Js('Keolakupaianaha'), Js('Keolamauloa'), Js('Keon'), Js('Keona'), Js('Keonaona'), Js('Keone'), Js('Keoni'), Js('Kepano '), Js('Kewika '), Js('Kikeona'), Js('Kila'), Js('Kileona'), Js('Kilikikopa '), Js('Kilohana'), Js('Kimo'), Js('Kimo '), Js('Kini'), Js('Kiwini '), Js('Koa'), Js('Koamalu'), Js('Koma '), Js('Kominiko '), Js('Kona'), Js('Konala'), Js('Konane'), Js('Ku'), Js("Ku'ualoha"), Js("Kuali'i"), Js('Kuenekina '), Js('Kukane'), Js("Kulamau'u"), Js('Kulani'), Js("Kupa'alani"), Js("La'akea"), Js('Lahahana'), Js('Laionela'), Js('Laka'), Js('Lalepa '), Js('Lanakila'), Js('Lani'), Js('Lei'), Js('Lei '), Js('Leialoha'), Js('Leilani'), Js('Leinani'), Js('Leolani'), Js('Lewai '), Js('Lewi'), Js('Lihau'), Js('Likeke '), Js('Liko'), Js('Lilo'), Js('Loe'), Js('Lokelani'), Js("Lokomaika'i"), Js('Lono'), Js('Lopaka '), Js('Lulani'), Js("Mahi'ai"), Js('Mahoe'), Js("Maika'i"), Js("Maika'ikeakua"), Js("Maka'alohi"), Js("Maka'alohilohi"), Js('Makaio'), Js('Makaio '), Js('Makala'), Js('Makalohi'), Js('Makana'), Js('Makanaakua'), Js("Makanamaika'i"), Js('Makanaokeakua'), Js('Makani'), Js('Makanui'), Js('Makoa'), Js('Malana'), Js('Maleko '), Js('Malu'), Js('Maluhia'), Js('Maluhialani'), Js('Malulani'), Js('Maluokeakua'), Js('Mamo'), Js('Mana'), Js("Mana'o'i'o"), Js("Mana'olana"), Js("Mana'olanakeiki"), Js('Manu'), Js('Manuku'), Js("Manumakali'i"), Js('Mapuana'), Js('Maui'), Js("Mika'ele"), Js('Mikala '), Js('Milana'), Js('Miliani'), Js('Milimili'), Js("Mo'o"), Js('Moana'), Js('Mohala'), Js('Moke'), Js('Nahele'), Js('Nainoa'), Js("Nakana'ela "), Js('Nakoa'), Js('Nalani'), Js('Nalunani'), Js('Nawai'), Js('Nihopalaoa'), Js('Nikolao'), Js('Nikolo '), Js('Noa'), Js('Noa '), Js('Noela '), Js('Noelani'), Js('Nohea'), Js('Nohokai'), Js("Nu'uanu"), Js('Oke'), Js('Olakeakua'), Js('Onaona'), Js("Pa'ahana"), Js('Palani '), Js('Paulo '), Js('Pekelo '), Js('Peleke '), Js('Peni '), Js("Pi'ilani"), Js('Pili '), Js('Pilipo '), Js("Pomaika'i"), Js('Pua'), Js('Punawai'), Js('Uilama'), Js('Uiliama'), Js('Ululani'), Js('Uluwehi'), Js('Wainani'), Js("Wana'ao"), Js("Wana'aonani"), Js('Wehilani')]))
var.put('nm2', Js([Js("'A'ala"), Js("'Ailana"), Js("'Ailani"), Js("'Ainakea"), Js("'Ainalani"), Js("'Ainanani"), Js("'Akahi"), Js("'Akau"), Js("'Ala"), Js("'Alaneo"), Js("'Alepo'i"), Js("'Alihi Kaua"), Js("'Alohi"), Js("'Alohilani"), Js("'Alohilohi"), Js("'Aluna"), Js("'Anela"), Js("'Ano'i"), Js("'Ano'ipua"), Js("'Anolani"), Js("'Apona"), Js("'Auina"), Js("'Aukai"), Js("'Aulani"), Js("'Ele"), Js("'Enakai"), Js("'Ilima"), Js("'Iolani"), Js("'Iwalani"), Js("'Olina"), Js("'Opunui"), Js("A'ia'i"), Js('Abegaila'), Js('Ahe'), Js('Aheahe'), Js('Ahonui'), Js('Ahuahu'), Js('Ahulani'), Js('Aiwaiwa'), Js("Aka'ula"), Js('Akahele'), Js('Akamai'), Js('Akanahe'), Js('Akeakamai'), Js("Alaka'i"), Js('Alamea'), Js('Alamimo'), Js('Alana'), Js('Alani'), Js('Alanna'), Js("Alapa'i"), Js('Alaula'), Js('Aleka'), Js('Aleka'), Js("Ali'imalu"), Js('Alika'), Js('Aloalo'), Js('Aloha'), Js('Alohaekaunei'), Js('Alohalani'), Js('Alohanani'), Js('Alohilani'), Js('Amana'), Js('Amanaka'), Js('Ana'), Js('Anakalia'), Js('Ane'), Js('Anela'), Js('Anela'), Js('Aniani'), Js('Anika'), Js('Ano'), Js('Anuenue'), Js('Anuenue Akua'), Js('Anuhea'), Js('Aolani'), Js('Aoloa'), Js('Aonani'), Js('Aouli'), Js('Aowena'), Js("Apika'ila"), Js("Auali'i"), Js("Aukanai'i"), Js('Aulani'), Js('Aulii'), Js('Aumoe'), Js('Ehehene'), Js('Elena'), Js('Elika'), Js('Elikapeka'), Js('Elikapeka'), Js('Eme'), Js('Emele'), Js('Emelina'), Js('Ewe'), Js('Ewekapu'), Js('Ewelani'), Js("Ha'aheo"), Js("Ha'iku"), Js("Ha'ulili"), Js("Ha'upu"), Js('Haku'), Js('Hakumele'), Js('Halana malie'), Js('Haleakua'), Js('Halemano'), Js("Hali'a"), Js("Hali'aaloha"), Js("Hali'imaile"), Js('Halia'), Js('Haloa'), Js('Halolani'), Js('Halulu'), Js('Hanaaloha'), Js('Hanaiakamalama'), Js('Hanakahi'), Js('Hanalei'), Js('Hanau hou'), Js('Hanauhoulani'), Js('Hani'), Js('Hanini'), Js('Hanohano'), Js('Hau kea'), Js("Hau'oli"), Js("Hau'oli'oli"), Js('Haulani'), Js('Haumea'), Js('Haunani'), Js('Haupuehuehu'), Js('Hawaii'), Js('Healani'), Js('Hekili'), Js('Helena'), Js('Helene'), Js('Heleuma'), Js('Helina'), Js('Hemolele'), Js('Hemolelekeakua'), Js("Hi'iaka"), Js("Hi'ilani"), Js("Hi'ilawe"), Js("Hi'ilei"), Js("Hiapa'i'ole"), Js('Hiapo'), Js('Hie'), Js('Hiehie'), Js('Hikialani'), Js('Hina'), Js("Hina'ea"), Js('Hinuhinu'), Js('Hiwa lani'), Js('Hiwahiwa'), Js('Hiwahiwakeiki'), Js("Ho'ohie"), Js("Ho'ohiehie"), Js("Ho'okele"), Js("Ho'ola'i"), Js("Ho'olana"), Js("Ho'olaua'e"), Js("Ho'opa'a"), Js('Hoa kua'), Js('Hoa pili'), Js("Hoaalohakupa'a"), Js('Hoaka'), Js('Hoakoa'), Js('Hoalohalani'), Js('Hoalohanani'), Js('Hoku'), Js('Hoku ala'), Js("Hoku'alohi"), Js('Hokuao'), Js('Hokuaonani'), Js("Hokuhelele'i"), Js('Hokulani'), Js("Hokule'a"), Js('Hokulele'), Js("Hokuli'ili'i"), Js("Hokupa'a"), Js("Holo'oka'a"), Js('Holokai'), Js('Holomakani'), Js('Hone'), Js('Honehone'), Js('Honi'), Js('Hopoelehua'), Js("Hu'elani"), Js("Hu'eu"), Js('Huaka'), Js('Hualani'), Js('Huali'), Js('Huananai'), Js('Huapala'), Js('Hulama'), Js("Huluali'i"), Js('Hunakai'), Js('Ianeke'), Js('Ianete'), Js('Ienipa'), Js('Ihe'), Js('Ihupani'), Js('Ilihia'), Js('Inoa'), Js('Ioke'), Js('Iokina'), Js('Iolana'), Js('Iolani'), Js("Iona'ala"), Js('Ipo'), Js('Ipolani'), Js('Iukikina'), Js('Iulia'), Js('Iwalani'), Js("Ka'ana'ana"), Js("Ka'aona"), Js("Ka'apeha"), Js("Ka'aumoana"), Js("Ka'ehu"), Js("Ka'ena"), Js("Ka'eo"), Js("Ka'ihikapu"), Js("Ka'iimamao"), Js("Ka'ike'apona"), Js("Ka'ili"), Js("Ka'ilinemo"), Js("Ka'imi"), Js("Ka'iulani"), Js("Ka'ohu"), Js("Ka'uhane"), Js("Kaha'aheo"), Js('Kahakea'), Js('Kahakuhale'), Js('Kahakuloa'), Js('Kahalaomapuana'), Js('Kahale'), Js('Kahana'), Js('Kahanu'), Js('Kahaulani'), Js('Kahauolupea'), Js('Kahawai'), Js('Kahealani'), Js('Kaheka'), Js("Kaheka'alohi"), Js('Kahekili'), Js('Kahele'), Js('Kahelemeakua'), Js('Kahewai'), Js('Kahiau'), Js('Kahikilani'), Js('Kahikina'), Js('Kahikookeakua'), Js('Kahili'), Js('Kahoku'), Js('Kaholo'), Js('Kahoni'), Js('Kahua'), Js('Kahue'), Js('Kahula'), Js('Kahuna'), Js('Kai'), Js('Kaiaka'), Js('Kaiapo'), Js('Kaiea'), Js('Kaiemi'), Js('Kaihalulu'), Js('Kaihe'), Js('Kaihekoa'), Js("Kaiho'i"), Js('Kaihohonu'), Js('Kaiholo'), Js('Kaikea'), Js('Kaiko'), Js('Kaila'), Js('Kailani'), Js('Kaili'), Js('Kaimalie'), Js('Kaimalolo'), Js('Kaimana'), Js('Kainehe'), Js('Kainoa'), Js("Kainu'u"), Js('Kainui'), Js('Kaiona'), Js('Kaipalaoa'), Js('Kaipo'), Js("Kaipo'i"), Js('Kaiulu'), Js('Kakahi'), Js('Kakarina'), Js('Kakielekea'), Js('Kakumulani'), Js('Kala'), Js("Kala'i"), Js('Kalaheo'), Js('Kalala'), Js('Kalala'), Js('Kalalaina'), Js('Kalalika'), Js('Kalama'), Js('Kalani'), Js('Kale'), Js("Kale'a"), Js('Kalea'), Js('Kaleho'), Js('Kalehua'), Js('Kalei'), Js('Kaleialoha'), Js('Kaleiokalani'), Js('Kalena'), Js('Kaleo'), Js('Kaleoaloha'), Js('Kaleolani'), Js("Kali'a"), Js('Kalia'), Js('Kaliko'), Js('Kalili'), Js('Kalilinoe'), Js('Kalino'), Js('Kaliona'), Js('Kalolaina'), Js('Kalua'), Js('Kama hele'), Js("Kamaha'o"), Js('Kamaile'), Js('Kamaka'), Js('Kamakana'), Js('Kamakani'), Js('Kamala'), Js('Kamalah'), Js('Kamalani'), Js('Kamalei'), Js('Kamamalu'), Js('Kamani'), Js('Kamea'), Js('Kamealoha'), Js('Kameli'), Js('Kamila'), Js('Kamoana'), Js('Kamole'), Js('Kana'), Js('Kanae'), Js('Kanaloa'), Js('Kanani'), Js('Kanoa'), Js('Kanoelani'), Js('Kanuha'), Js('Kanupa'), Js('Kapahu'), Js('Kapena'), Js("Kapi'olani"), Js('Kaponianani'), Js('Kapono'), Js('Kapua'), Js("Kapua'ilima"), Js("Kapua'ula"), Js('Kapueo'), Js('Kapula'), Js('Kapule'), Js('Kapuni'), Js("Kau'i"), Js("Kau'ilani"), Js('Kauanoe'), Js('Kaulana'), Js('Kauluwehi'), Js('Kawai'), Js('Kawailani'), Js('Kawaimomona'), Js('Kawehi'), Js('Kawelu'), Js('Kawena'), Js("Kawena'ula"), Js("Ke'ala"), Js("Ke'alohi"), Js("Ke'alohilani"), Js("Ke'ohi"), Js('Keahi'), Js('Keahilani'), Js('Keaka'), Js('Keala'), Js('Kealani'), Js('Kealii'), Js('Kealoha'), Js('Keana'), Js('Keani'), Js('Keanu'), Js('Keao'), Js('Keawe'), Js('Keeaola'), Js('Keena'), Js('Keha'), Js('Kehau'), Js('Kehaulani'), Js('Kei'), Js('Keikemamake'), Js('Keiki'), Js('Keikilani'), Js('Keilani'), Js('Keke'), Js('Kekepania'), Js('Kekipi'), Js('Kekoa'), Js('Kela'), Js('Kelalani'), Js('Kelani'), Js("Keli'i"), Js('Kelia'), Js('Kelii'), Js('Keola'), Js('Keolakupaianaha'), Js('Keona'), Js('Keonaona'), Js('Kiana'), Js('Kiana'), Js('Kiele'), Js('Kielekea'), Js('Kilikina'), Js('Kilohana'), Js('Kimi'), Js('Kimi'), Js('Kina'), Js('Kini'), Js('Kinipela'), Js('Kolina'), Js('Kolokea'), Js('Konane'), Js('Korina'), Js("Ku'ualoha"), Js("Ku'uipo"), Js("Ku'ulei"), Js("Ku'uleialoha"), Js('Kuilei'), Js('Kukana'), Js('Kulani'), Js('Kuli'), Js('Kuliana'), Js('Kunani'), Js("Kupa'alani"), Js('Lahela'), Js('Lahela'), Js('Laka'), Js('Lala'), Js('Lana'), Js('Lanai'), Js('Lanakila'), Js('Lani'), Js('Lea'), Js('Lea'), Js('Lehua'), Js('Lei'), Js('Leialoha'), Js('Leilani'), Js('Leimomi'), Js("Leina'ala"), Js('Leinani'), Js('Leolani'), Js('Leonani'), Js('Lepeka'), Js('Lihau'), Js('Lika'), Js('Lilia'), Js('Lilinoe'), Js('Lilo'), Js('Loe'), Js('Lokapele'), Js('Loke'), Js('Lokelani'), Js('Lokemele'), Js("Lokomaika'i"), Js("Lokomaika'inani"), Js("Lu'ukia"), Js('Luka'), Js('Luke'), Js('Lukia'), Js('Lukia'), Js('Lulia'), Js('Lupe'), Js('Mahealani'), Js('Mahina'), Js('Mahoe'), Js("Maika'i"), Js("Maika'ikeakua"), Js('Maila'), Js('Maile'), Js('Maira'), Js('Maka'), Js("Maka'alohi"), Js("Maka'alohilohi"), Js('Makaio'), Js('Makala'), Js('Makalika'), Js('Makamae'), Js('Makana'), Js('Makanaakua'), Js("Makanamaika'i"), Js('Makani'), Js('Makanui'), Js('Makela'), Js('Makelina'), Js('Malaea'), Js('Malalani'), Js('Malana'), Js('Malea'), Js('Maleah'), Js('Maleia'), Js('Maleka'), Js('Malia'), Js('Malia'), Js('Maliana'), Js('Malie'), Js('Malu'), Js('Maluhia'), Js('Maluhialani'), Js('Malulani'), Js('Mamo'), Js('Mana'), Js("Mana'o'i'o"), Js("Mana'olana"), Js("Mana'olanakeiki"), Js("Manaali'i"), Js('Manalani'), Js("Manawale'a"), Js('Manu'), Js('Mapuana'), Js('Mei'), Js('Mele'), Js('Mele'), Js('Meli'), Js('Melia'), Js('Melika'), Js('Mikala'), Js('Mikilana'), Js('Milana'), Js('Milena'), Js('Maile'), Js('Miliani'), Js('Mililani'), Js('Milimili'), Js('Miulana'), Js("Mo'o"), Js('Moana'), Js('Moananani'), Js('Moani'), Js('Mohala'), Js('Moke'), Js('Mokihana'), Js('Momi'), Js('Momi'), Js('Momilani'), Js("Nai'a"), Js('Nalani'), Js('Nalukea'), Js('Namaka'), Js('Nanala'), Js('Nanea'), Js('Naneki'), Js('Nani'), Js('Naniahiahi'), Js('Naomi'), Js('Napua'), Js('Nawai'), Js('Nele'), Js('Nina'), Js('Noelani'), Js('Nohea'), Js('Nohealani'), Js('Okalani'), Js('Oke'), Js('Olakeakua'), Js('Onaona'), Js('Pauahi'), Js('Peke'), Js('Pele'), Js('Pelenakeka'), Js("Pi'ikea"), Js("Pi'ilani"), Js('Pikake'), Js('Pilikika'), Js('Pineki'), Js('Pole'), Js("Poli'ahu"), Js("Pomaika'i"), Js('Pua'), Js('Puakai'), Js('Puakea'), Js('Pualani'), Js('Puanani'), Js('Qiana'), Js('Qianna'), Js('Quiana'), Js('Roselani'), Js("U'ilani"), Js('Ululani'), Js('Uluwehi'), Js('Wailani'), Js('Wainani'), Js('Waiola'), Js("Wana'ao"), Js("Wana'ao"), Js("Wana'aonani"), Js('Wanaka'), Js('Wehilani'), Js('Wikolia'), Js('Wilikinia')]))
var.put('nm3', Js([Js("'Akamu"), Js("'Aukai"), Js("'Opunui"), Js('Aelan '), Js('Ah-Puck'), Js('Aikau'), Js('Ailani '), Js('Akamu '), Js('Akana'), Js('Akanu'), Js('Akela '), Js('Akina'), Js('Akoni '), Js('Akuini'), Js('Alamea '), Js('Alana'), Js('Alana '), Js('Alapa'), Js('Alapai'), Js('Alaula '), Js('Alika '), Js('Allen'), Js('Aloha '), Js('Alohilani'), Js('Alohilani '), Js('Amalu'), Js('Among'), Js('Anakoni '), Js('Analu '), Js('Aneko'), Js('Ano'), Js('Aolani '), Js('Aulani '), Js('Awana'), Js('Dorit '), Js('Edena '), Js('Ekewaka '), Js('Elikapeka '), Js('Haiku'), Js('Hailama'), Js('Hale'), Js('Halia '), Js('Hamakua'), Js('Haukea '), Js('Hekekia'), Js('Hina '), Js('Hiram'), Js('Hoapili'), Js('Hoke'), Js('Hookano'), Js('Iakopa '), Js('Iaukea'), Js('Iekika '), Js('Ikaia '), Js('Inoke '), Js('Iokina '), Js('Iokua '), Js('Iolana '), Js('Iolani '), Js('Iona'), Js('Ipo '), Js('Iwalani '), Js("Ka'ahanui"), Js("Ka'ai'ai"), Js("Ka'ana'ana"), Js("Ka'aukai"), Js("Ka'uhane"), Js('Kaai'), Js('Kaanaana'), Js('Kaapana'), Js('Kaeo'), Js('Kahala'), Js('Kahale'), Js('Kahanamoku'), Js('Kahananui'), Js('Kahaulelio'), Js('Kahawaii'), Js('Kahele'), Js('Kahike'), Js('Kahikina'), Js('Kahiona'), Js('Kahoiwai'), Js('Kahoku '), Js('Kahue'), Js('Kai '), Js('Kaia '), Js('Kaialani '), Js('Kaialiilii'), Js('Kaiaokamalie'), Js('Kaila '), Js('Kailani '), Js('Kailikea'), Js('Kaimana '), Js('Kaimi '), Js('Kaipo '), Js('Kaiuwaihui'), Js('Kaiwi'), Js('Kakalina '), Js('Kala '), Js('Kalainawai'), Js('Kalakona'), Js('Kalama'), Js('Kalama '), Js('Kalani'), Js('Kalani '), Js('Kalanianioli'), Js('Kalanie '), Js("Kalawai'a"), Js('Kale '), Js('Kalea '), Js('Kalei'), Js('Kalei '), Js('Kaleigh '), Js('Kalena '), Js('Kaleo '), Js('Kali '), Js('Kalili'), Js('Kalima'), Js('Kaloni '), Js('Kalua'), Js('Kaluhiokalani'), Js('Kaluhiwa'), Js('Kama'), Js('Kamaauoha'), Js('Kamaka'), Js('Kamakeoaina'), Js("Kamali'i"), Js('Kamauoha'), Js('Kamea '), Js('Kamealoha'), Js('Kamehaha'), Js('Kameo '), Js('Kana '), Js('Kane'), Js('Kanekalau'), Js('Kani '), Js('Kanoa '), Js('Kaoao'), Js('Kaohi'), Js('Kapahu'), Js('Kapiolani'), Js('Kapono '), Js('Kapule'), Js('Kawaha'), Js('Kawai'), Js('Kawena '), Js('Keahi'), Js('Keahi '), Js('Keala '), Js('Kealoha'), Js('Keao'), Js('Keaunui'), Js('Keawe'), Js('Keaweamahi'), Js('Keiki '), Js('Keilani '), Js('Kekahuna'), Js('Kekai'), Js('Kekaula'), Js('Kekepania '), Js('Kekoa'), Js('Kekoa '), Js('Kekumu'), Js('Kelekolio'), Js("Keli'i"), Js('Kelii '), Js('Keliikoa'), Js('Keoki '), Js('Keola '), Js('Keolanui'), Js('Keomalu'), Js('Keon '), Js('Keona '), Js('Keone'), Js('Keoni '), Js('Kiana '), Js('Kiele '), Js('Kiliona'), Js('Kimo '), Js('Kina '), Js('Kinimaka'), Js('Kinipela '), Js('Koi '), Js('Kona '), Js('Konala '), Js('Konane '), Js('Laban '), Js('Laemoa'), Js('Lahela '), Js('Lala '), Js('Lana '), Js('Lanai '), Js('Lani '), Js('Lea '), Js('Leia '), Js('Leilani '), Js('Liko '), Js('Liliha '), Js('Lilo '), Js('Liwai'), Js('Lokelani '), Js('Londeree'), Js('Loni '), Js('Lono'), Js('Lonoehu'), Js('Look'), Js('Luahoomae'), Js('Luana '), Js('Mahaulu'), Js('Mahelona'), Js("Mahi'ai"), Js('Mahina '), Js('Mahoe'), Js('Maile '), Js('Makaha'), Js('Makaiau'), Js('Makaio '), Js('Makaiwi'), Js('Makala '), Js('Makan '), Js('Makana '), Js('Makani '), Js('Makelina '), Js('Malana '), Js('Maleah '), Js('Maleko '), Js('Malia '), Js('Malina '), Js('Malo '), Js('Mano '), Js('Manunui'), Js('Mei Mele '), Js('Mele '), Js('Melia '), Js('Mika'), Js('Mikil '), Js('Miliani '), Js('Moana '), Js('Moanna '), Js('Moi'), Js('Moliakalaniikeola'), Js('Naihe'), Js('Nakanaela'), Js('Nakaneaela'), Js('Nalani '), Js('Nalanie '), Js('Nana '), Js('Nani '), Js('Napua '), Js('Natua'), Js('Nawahine'), Js('Newalu'), Js('Nihipali'), Js('Noe '), Js('Noelani '), Js('Nohealani '), Js('Noma '), Js('Okalani '), Js('Ola '), Js('Oliana '), Js('Olina '), Js('Oline '), Js('Onakea'), Js('Onaona '), Js('Paahao'), Js('Pahia'), Js('Paikuli'), Js('Palakiko'), Js('Palea'), Js('Palila '), Js("Pane'e"), Js('Pekelo'), Js('Pi'), Js('Pilialoha '), Js('Pilis '), Js('Pookalani'), Js('Pouha'), Js('Puhihale'), Js('Pukahi'), Js('Pula'), Js('Sasilvia'), Js('Ulani'), Js('Wikolia')]))
pass
pass


# Add lib to the module scope
hawaiianNames = var.to_python()