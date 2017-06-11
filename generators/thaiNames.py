__all__ = ['thaiNames']

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
var.put('nm1', Js([Js('Aat'), Js('Aawut'), Js('Adirake'), Js('Akkanee'), Js('Akkarat'), Js('Alak'), Js('Amnuay'), Js('Anada'), Js('Ananada'), Js('Ananda'), Js('Annan'), Js('Anon'), Js('Anuia'), Js('Anuman'), Js('Anurak'), Js('Anuthat'), Js('Apichart'), Js('Aran'), Js('Aroon'), Js('Arthit'), Js('Ashwin'), Js('Asnee'), Js('Athiti'), Js('Atid'), Js('Badinton'), Js('Baharn'), Js('Bahn'), Js('Bandasak'), Js('Banjong'), Js('Banlop'), Js('Banlue'), Js('Bannarasee'), Js('Bannarot'), Js('Bannasorn'), Js('Banthorn'), Js('Banwithit'), Js('Banyat'), Js('Banyong'), Js('Bapit'), Js('Barinai'), Js('Barinot'), Js('Baritharn'), Js('Baroma'), Js('Baveethran'), Js('Bawornnon'), Js('Bawornthath'), Js('Bhakdi'), Js('Bhichai'), Js('Bhumipol'), Js('Bin'), Js('Bodesta'), Js('Boon-Mee'), Js('Boon-Nam'), Js('Boon-mee'), Js('Boon-nam'), Js('Boonchu'), Js('Boonma'), Js('Boonpipob'), Js('Boontung'), Js('Brosong'), Js('Buangam'), Js('Budin'), Js('Bunbongkarn'), Js('Bunkit'), Js('Bunyakorn'), Js('Bunyapoo'), Js('Buppakorn'), Js('Burapol'), Js('Burimas'), Js('Burin'), Js('Burit'), Js('Burut'), Js('Cha'), Js('Chai'), Js('Chai Son'), Js('Chairat'), Js('Chaisai'), Js('Chaiya'), Js('Chaiyanuchit'), Js('Chaiyo'), Js('Chakan'), Js('Chakrabandhu'), Js('Chakri'), Js('Chalerm'), Js('Chalermchai'), Js('Chaloem'), Js('Chalong'), Js('Changsai'), Js('Channarong'), Js('Chanthara'), Js('Chao Fah'), Js('Chao fah'), Js('Chao-Khun-Sa'), Js('Chao-Tak'), Js('Chao-khun-sa'), Js('Chao-tak'), Js('Chaovalit'), Js('Chaowas'), Js('Charn Chai'), Js('Charnchai'), Js('Charoen'), Js('Charoensom'), Js('Charong'), Js('Chatalerm'), Js('Chatchalerm'), Js('Chatchawee'), Js('Chatchom'), Js('Chatichai'), Js('Chatri'), Js('Chaturon'), Js('Chavalit'), Js('Chayan'), Js('Chayond'), Js('Cheewaket'), Js('Chennoi'), Js('Chermsak'), Js('Chesda'), Js('Chet'), Js('Chetta'), Js('Chinawoot'), Js('Chiradet'), Js('Chomanan'), Js('Chompoo'), Js('Chon'), Js('Chongrak'), Js('Choochai'), Js('Choonhavan'), Js('Choonhavon'), Js('Chuachai'), Js('Chuan'), Js('Chuanchen'), Js('Chuchai'), Js('Chuia'), Js('Chula'), Js('Chulalongkorn'), Js('Chulamai'), Js('Churai'), Js('Chuthamani'), Js('Daeng'), Js('Damrong'), Js('Danai'), Js('Danit'), Js('Danunan'), Js('Danusorn'), Js('Daran'), Js('Daranpob'), Js('Darin'), Js('Decha'), Js('Deng'), Js('Denpoom'), Js('Dentharonee'), Js('Dhipyamongkol'), Js('Dilok'), Js('Diloktham'), Js('Disakorn'), Js('Disnadda'), Js('Disorn'), Js('Ditaka'), Js('Dithakar'), Js('Ditt'), Js('Dok'), Js('Dok rak'), Js('Dolrit'), Js('Dolsook'), Js('Dorn'), Js('Duchanee'), Js('Emjaroen'), Js('Erawan'), Js('Fah'), Js('Fufanwonich'), Js('Gee'), Js('Hainad'), Js('Hanuman'), Js('Hiran'), Js('Intradit'), Js('Ittiporn'), Js('Jaidee'), Js('Jao'), Js('Jarunsuk'), Js('Jatukamramthep'), Js('Jaturun'), Js('Jayavarman'), Js('Jessupha'), Js('Jettrin'), Js('Jirasak'), Js('Jutharat'), Js('Kaan'), Js('Kaandit'), Js('Kacha'), Js('Kamalakorn'), Js('Kamalanan'), Js('Kamalat'), Js('Kamik'), Js('Kamnan'), Js('Kamolpob'), Js('Kamolpoo'), Js('Kamut'), Js('Kan'), Js('Kananat'), Js('Kanaporn'), Js('Kanasanan'), Js('Kanda'), Js('Kandad'), Js('Kanin'), Js('Kanisorn'), Js('Kankawee'), Js('Kanok'), Js('Kanokpol'), Js('Kantapol'), Js('Kantapong'), Js('Kantayot'), Js('Kantharat'), Js('Kanthee'), Js('Kanthorn'), Js('Kantinan'), Js('Kantitat'), Js('Kantsak'), Js('Kantsom'), Js('Kanut'), Js('Kapp'), Js('Karan'), Js('Karanyapat'), Js('Karin'), Js('Karit'), Js('Karmatha'), Js('Karn'), Js('Karom'), Js('Kasan'), Js('Kasem'), Js('Kasemchai'), Js('Kasemsan'), Js('Kasidid'), Js('Kasin'), Js('Kasom'), Js('Kate'), Js('Kathawut'), Js('Kavi'), Js('Kawee'), Js('Kawin'), Js('Kawinpob'), Js('Keerati'), Js('Keetau'), Js('Khakanang'), Js('Khanti'), Js('Khattiya'), Js('Khem'), Js('Khemanan'), Js('Khematat'), Js('Khematin'), Js('Khemin'), Js('Khemkhaeng'), Js('Khun'), Js('Khunpol'), Js('Khunsoek'), Js('Kiet'), Js('Kiettinonnapat'), Js('Kiettisuk'), Js('Kimhan'), Js('Kirakorn'), Js('Kit'), Js('Kitsakan'), Js('Kitsakorn'), Js('Kitt'), Js('Kitti'), Js('Kittibun'), Js('Kittichai'), Js('Kittichat'), Js('Kittikawin'), Js('Kittikchorn'), Js('Kittikorn'), Js('Kittinai'), Js('Kittinan'), Js('Kittipob'), Js('Kittipon'), Js('Kittipoom'), Js('Kittiporn'), Js('Kittipot'), Js('Kittisak'), Js('Kittitat'), Js('Kittithorn'), Js('Kittiwin'), Js('Kla'), Js('Kla Han'), Js('Klaew Kla'), Js('Klahan'), Js('Kob'), Js('Kob Chai'), Js('Kob Khun'), Js('Kob Sinn'), Js('Kob Sook'), Js('Kolatee'), Js('Komalat'), Js('Komn'), Js('Kongbej'), Js('Kongkidakorn'), Js('Kongpob'), Js('Kongsampong'), Js('Konthee'), Js('Konthorn'), Js('Koradol'), Js('Korakod'), Js('Koran'), Js('Korapoo'), Js('Korasut'), Js('Koratak'), Js('Korn'), Js('Kornballop'), Js('Kot'), Js('Kovit'), Js('Krairawee'), Js('Kraisee'), Js('Kraisingha'), Js('Kraiwin'), Js('Krarayoon'), Js('Kriang Krai'), Js('Kriang Sak'), Js('Kriangsak'), Js('Kriengsak'), Js('Kris'), Js('Krisik'), Js('Krit'), Js('Krita'), Js('Kritsada'), Js('Krittameth'), Js('Krittanoo'), Js('Krittapat'), Js('Krittapot'), Js('Krittayot'), Js('Krittin'), Js('Krittinai'), Js('Krittithee'), Js('Krom-Luang'), Js('Krom-luang'), Js('Kukrit'), Js('Kulit'), Js('Kulpat'), Js('Kulthorn'), Js('Kunach'), Js('Kunanan'), Js('Kunn'), Js('Kunnthorn'), Js('Kusa'), Js('Kusum'), Js('Kutsa'), Js('Kwanchai'), Js('Kwanjai'), Js('Lamom'), Js('Lamon'), Js('Lap'), Js('Leekpai'), Js('Leekpie'), Js('Lek'), Js('Loesan'), Js('Luk'), Js('Maha'), Js('Mahidol'), Js('Malian'), Js('Maliwan'), Js('Manee'), Js('Manitho'), Js('Mee'), Js('Mee Noi'), Js('Mengrai'), Js('Metananda'), Js('Mok'), Js('Mokkhavesa'), Js('Molthisok'), Js('Mongkut'), Js('Monyakul'), Js('Muoi'), Js('Nadee'), Js('Nai-Thim'), Js('Nai-thim'), Js('Nak'), Js('Nakaret'), Js('Nakarin'), Js('Nang-Klao'), Js('Nang-klao'), Js('Nanthapob'), Js('Nanthayot'), Js('Nanthit'), Js('Nantin'), Js('Nantipat'), Js('Nantiworn'), Js('Napan'), Js('Napat'), Js('Napatthorn'), Js('Napon'), Js('Narai'), Js('Naresuan'), Js('Naris'), Js('Narisa'), Js('Narong'), Js('Narongrit'), Js('Narongwit'), Js('Naruerong'), Js('Naruesorn'), Js('Nat'), Js('Natee'), Js('Nathawat'), Js('Nattadanai'), Js('Nattakamol'), Js('Nattakan'), Js('Nattanai'), Js('Nattanan'), Js('Nattanon'), Js('Nattapat'), Js('Nattapon'), Js('Nattaron'), Js('Nattasit'), Js('Nattasom'), Js('Nattasut'), Js('Nattawat'), Js('Nattaworn'), Js('Nattayot'), Js('Natthapong'), Js('Natthawut'), Js('Nawanthorn'), Js('Nawat'), Js('Nawatkorn'), Js('Nawin'), Js('Nekk'), Js('Net'), Js('Netithorn'), Js('Netiwit'), Js('Ngam'), Js('Ngoen'), Js('Nibun'), Js('Nikom'), Js('Nikon'), Js('Nimman'), Js('Nimmit'), Js('Nintau'), Js('Nipaat'), Js('Nipat'), Js('Niphon'), Js('Nipit'), Js('Nipitpon'), Js('Nipon'), Js('Nipun'), Js('Niran'), Js('Nirawit'), Js('Nirin'), Js('Nirund'), Js('Nissorn'), Js('Nit'), Js('Nithan'), Js('Nithikorn'), Js('Nithit'), Js('Nithoon'), Js('Nitithorn'), Js('Nitthan'), Js('Nitthon'), Js('Niwat'), Js('Niwit'), Js('Niyom'), Js('Nodthakorn'), Js('Noi'), Js('Non'), Js('Nongchai'), Js('Nongkhai'), Js('Nonpawit'), Js('Nontapan'), Js('Nontawat'), Js('Nontiyut'), Js('Nopjira'), Js('Noppadon'), Js('Noppadorn'), Js('Noppakorn'), Js('Noppasin'), Js('Noppathee'), Js('Noppawin'), Js('Norachai'), Js('Norrapan'), Js('Norrapon'), Js('Norrathee'), Js('Norrawee'), Js('Norraworn'), Js('Nuananong'), Js('Nuengnimman'), Js('Nugoon'), Js('Nui'), Js('Nung'), Js('Nuta-Laya'), Js('Nuta-laya'), Js('Obb'), Js('Olan'), Js('Osathee'), Js('Othong'), Js('Paan'), Js('Paanthath'), Js('Pairat'), Js('Pairote'), Js('Paitoon'), Js('Pakhdi'), Js('Palat'), Js('Pamut'), Js('Pan'), Js('Panas'), Js('Panat'), Js('Panithi'), Js('Pann'), Js('Pannathath'), Js('Pannathorn'), Js('Pannawat'), Js('Panthorn'), Js('Panyarachun'), Js('Papangkorn'), Js('Paparn'), Js('Papawin'), Js('Papob'), Js('Papon'), Js('Paponsan'), Js('Paponthanai'), Js('Paponthee'), Js('Paradorn'), Js('Parama'), Js('Paraman'), Js('Paramat'), Js('Paramendr'), Js('Paranat'), Js('Parat'), Js('Parin'), Js('Parit'), Js('Parnchand'), Js('Paron'), Js('Parun'), Js('Pasan'), Js('Pasat'), Js('Pasut'), Js('Pathanin'), Js('Pathapee'), Js('Pathit'), Js('Patipon'), Js('Patt'), Js('Pattama'), Js('Pawaret'), Js('Pawarit'), Js('Pawaritsorn'), Js('Pawarut'), Js('Pawat'), Js('Paween'), Js('Pawin'), Js('Pawit'), Js('Pawornruj'), Js('Payut'), Js('Pet'), Js('Petch'), Js('Petchara'), Js('Petchra'), Js('Phaibun'), Js('Phaithoon'), Js('Phanumas'), Js('Phara'), Js('Phassakorn'), Js('Phatra'), Js('Phatson'), Js('Phet'), Js('Phichai'), Js('Phichit'), Js('Phinihan'), Js('Phisan'), Js('Phongsak'), Js('Phraisong'), Js('Phrom-Borirak'), Js('Phrom-borirak'), Js('Phueng'), Js('Phuri'), Js('Phya'), Js('Pichai'), Js('Pichit'), Js('Pidok'), Js('Pira'), Js('Piya'), Js('Piyabutr'), Js('Piyapat'), Js('Piyapon'), Js('Piyatat'), Js('Piyawat'), Js('Ponggool'), Js('Pongkun'), Js('Pongpanet'), Js('Pongpob'), Js('Pongrit'), Js('Pongsom'), Js('Pongtham'), Js('Pra'), Js('Pracha'), Js('Prachuab'), Js('Prakit'), Js('Prakorb'), Js('Pralop'), Js('Praman'), Js('Pramanat'), Js('Pramod'), Js('Pramoj'), Js('Pramon'), Js('Pran'), Js('Pranai'), Js('Pranon'), Js('Pranop'), Js('Prapaan'), Js('Prapan'), Js('Prapawit'), Js('Prasong'), Js('Prasopchai'), Js('Pravat'), Js('Praves'), Js('Prawanwit'), Js('Prawee'), Js('Praween'), Js('Praya'), Js('Prayut'), Js('Preet'), Js('Prem'), Js('Pricha'), Js('Prid'), Js('Prisna'), Js('Pritsadee'), Js('Pritsanee'), Js('Proi'), Js('Pu'), Js('Pu Yai Bahn'), Js('Puenthai'), Js('Puran'), Js('Puttipat'), Js('Rachotai'), Js('Raegan'), Js('Rajanon'), Js('Rak'), Js('Rama'), Js('Ramkamhaeng'), Js('Rand'), Js('Rangsan'), Js('Rangsiman'), Js('Ratanankorn'), Js('Ratri'), Js('Ratsami'), Js('Rawee'), Js('Ritthirong'), Js('Rom Ran'), Js('Ronnapee'), Js('Ruang Rit'), Js('Ruang Sak'), Js('Runrot'), Js('Sajja'), Js('Sakchai'), Js('Sakda'), Js('Sampan'), Js('Samyan'), Js("San'ya"), Js('Sanan'), Js('Sanouk'), Js('Santichai'), Js('Sanun'), Js('Sap'), Js('Saranyu'), Js('Sarathoon'), Js('Sarawong'), Js('Sarawut'), Js('Sarit'), Js('Sarut'), Js('Sataheep'), Js('Satayu'), Js('Satra'), Js('Satrud'), Js('Savit'), Js('Sawai'), Js('Sawat'), Js('Seni'), Js('Seri'), Js('Si'), Js('Siam'), Js('Siddhi'), Js('Sin'), Js('Singnum'), Js('Sinn'), Js('Snoh'), Js('Som'), Js('Som Phon'), Js('Som Phong'), Js('Sombat'), Js('Somchai'), Js('Somchair'), Js('Somchith'), Js('Somdej'), Js('Somdet-Ong-Yai'), Js('Somdet-ong-yai'), Js('Somdetch'), Js('Sompron'), Js('Somsak'), Js('Somwang'), Js('Son'), Js('Son Chai'), Js('Sonchai'), Js('Songgram'), Js('Songpob'), Js('Songpole'), Js('Songwut'), Js('Soo'), Js('Sook'), Js('Sophuk'), Js('Sri'), Js('Srimuang'), Js('Staporn'), Js('Su'), Js('Su Suk'), Js('Suchin'), Js('Sud'), Js('Sud Saming'), Js('Suda'), Js('Sudarak'), Js('Suk'), Js('Sulak'), Js('Sum'), Js('Sumatra'), Js('Sunan'), Js('Sundaravej'), Js('Suntarankul'), Js('Sunti'), Js('Sunya'), Js('Sup'), Js('Suphatra'), Js('Suphayok'), Js('Supoj'), Js('Supp'), Js('Supsampantuwongse'), Js('Sura'), Js('Surasak'), Js('Surat'), Js('Surin'), Js('Suriwongse'), Js('Suriyawong'), Js('Sutep'), Js('Suthep'), Js('Suttipong'), Js('Taan'), Js('Tadpol'), Js('Tadpong'), Js('Tadsuang'), Js('Tadthep'), Js('Tadthon'), Js('Taeng'), Js('Tai'), Js('Tak'), Js('Tak-Sin'), Js('Tak-sin'), Js('Takdanai'), Js('Taksin'), Js('Tam'), Js('Tamnurath'), Js('Tanakrit'), Js('Tangpanitharn'), Js('Tanit'), Js('Tanupat'), Js('Tanusorn'), Js('Tanutam'), Js('Tapp'), Js('Tappasan'), Js('Taran'), Js('Tarrin'), Js('Tassapon'), Js('Tau'), Js('Taweepak'), Js('Taweerat'), Js('Tayakorn'), Js('Tayut'), Js('Teepakorn'), Js('Teepth'), Js('Teera'), Js('Tep'), Js('Teptath'), Js('Thahan'), Js('Thaklaew'), Js('Thaksin'), Js('Tham-Boon'), Js('Tham-boon'), Js('Thammanit'), Js('Thammaraja'), Js('Thammasorn'), Js('Thampapon'), Js('Thampon'), Js('Thamwat'), Js('Thanaboon'), Js('Thanadol'), Js('Thanadun'), Js('Thanalop'), Js('Thanandorn'), Js('Thananop'), Js('Thanapon'), Js('Thanapoom'), Js('Thanarat'), Js('Thanat'), Js('Thanatat'), Js('Thanawan'), Js('Thanawat'), Js('Thanawin'), Js('Thanayut'), Js('Thanee'), Js('Thanetpol'), Js('Thanid'), Js('Thanik'), Js('Thanin'), Js('Thanit'), Js('Thanom'), Js('Thanut'), Js('Thanwa'), Js('Thanya'), Js('Thapthim'), Js('Tharathep'), Js('Tharathorn'), Js('Tharit'), Js('Tharn'), Js('Thath'), Js('Thawan'), Js('Thawanya'), Js('Thawi'), Js('Thawin'), Js('Thawit'), Js('Thayot'), Js('Theema'), Js('Theepob'), Js('Theera'), Js('Theeradon'), Js('Theerameth'), Js('Theeranai'), Js('Theeranop'), Js('Theerapat'), Js('Theerapatpong'), Js('Theerat'), Js('Theeratham'), Js('Theeratorn'), Js('Theerit'), Js('Theerut'), Js('Theesud'), Js('Theethath'), Js('Thinnakorn'), Js('Thipok'), Js('Thira'), Js('Thirakun'), Js('Thiramon'), Js('Thiranai'), Js('Thiraput'), Js('Thirdpong'), Js('Thith'), Js('Thiti'), Js('Thitipan'), Js('Thitisan'), Js('Thitisorn'), Js('Thitiwat'), Js('Thitiwut'), Js('Thong Daeng'), Js('Thong Di'), Js('Thong Kon'), Js('Thong Thaeng'), Js('Thongchai'), Js('Thongkon'), Js('Thoranan'), Js('Thorm'), Js('Thorn'), Js('Thornthep'), Js('Thuanthong'), Js('Thurdchai'), Js('Thuwanan'), Js('Ti'), Js('Ti Nung Cha'), Js('Tikatath'), Js('Tiloka'), Js('Ting'), Js('Tinn'), Js('Tinnakiet'), Js('Tinnakit'), Js('Tinnakorn'), Js('Tinnapat'), Js('Tinnapob'), Js('Tinsulaananda'), Js('Tinsulanonda'), Js('Tiron'), Js('Tisorn'), Js('Tiwat'), Js('Ton'), Js('Tong'), Js('Tongkanlong'), Js('Tonnakorn'), Js('Tosanakorn'), Js('Totsakan'), Js('Toy'), Js('Trai'), Js('Traikun'), Js('Traipob'), Js('Traipoom'), Js('Traitod'), Js('Trat'), Js('Trin'), Js('Trinai'), Js('Trintawat'), Js('Tuksin'), Js('Tulathorn'), Js('Ubol'), Js('Udom'), Js('Unakan'), Js('Uthai'), Js('Vajiralongkorn'), Js('Vajiravudh'), Js('Varunvirya'), Js('Vessandan'), Js('Vichit'), Js('Vidura'), Js('Virote'), Js('Vit'), Js('Vitaya'), Js('Vitchu'), Js('Vithoon'), Js('Vuthisit'), Js('Warun'), Js('Wasan'), Js('Wasi'), Js('Watchara'), Js('Wattana'), Js('Wayupak'), Js('Weera'), Js('Winai'), Js('Wiset'), Js('Witsanunat'), Js('Wittaya'), Js('Witthawat'), Js('Witthaya'), Js('Wongsa'), Js('Worrawut'), Js('Xuwicha'), Js('Yai'), Js('Yhukon'), Js('Yindee'), Js('Yod'), Js('Yod Rak'), Js('Yod rak'), Js('Yongchaiyudh'), Js('Yongchaiyuth'), Js('Yongyuth'), Js('Yubamrung'), Js('Yuthakon')]))
var.put('nm2', Js([Js('Abhasra'), Js('Achara'), Js('Adung'), Js('Ampawn'), Js('Amphorn'), Js('Amporn'), Js('Anchali'), Js('Anna'), Js('Anon'), Js('Apsara'), Js('Apsorn'), Js('Areva'), Js('Arinya'), Js('Arom'), Js('Atchara'), Js('Ausanat'), Js('Baenglum'), Js('Ban'), Js('Banjit'), Js('Bannarasee'), Js('Benjakalyani'), Js('Boon-Nam'), Js('Boon-mee'), Js('Boon-nam'), Js('Budsaba'), Js('Bundarik'), Js('Busaba'), Js('Busaya'), Js('But'), Js('Butri'), Js('Cantana'), Js('Catchada'), Js('Chaiama'), Js('Chalermwan'), Js('Chamnian'), Js('Chanachai'), Js('Chandra'), Js('Chanhira'), Js('Chantana'), Js('Chantara'), Js('Chanthara'), Js('Chantira'), Js('Chao-fa'), Js('Charanya'), Js('Chariya'), Js('Charoen'), Js('Charoenrasamee'), Js('Charunee'), Js('Chatmanee'), Js('Chatrsuda'), Js('Chatumas'), Js('Chaveevan'), Js('Chawiwan'), Js('Chintana'), Js('Chirawan'), Js('Choi'), Js('Chomechai'), Js('Chomesri'), Js('Chomkwan'), Js('Chompoo'), Js('Chompunut'), Js('Chomsiri'), Js('Chon'), Js('Chonnanee'), Js('Chonthicha'), Js('Chuachan'), Js('Chuasiri'), Js('Chulabhorn'), Js('Chulaborn'), Js('Chumbot'), Js('Churai'), Js('Cintna'), Js('Daeng'), Js('Damni'), Js('Dao'), Js('Darika'), Js('Darin'), Js('Dauenphen'), Js('Daw'), Js('Dhipyamongko'), Js('Dok mai'), Js('Dok'), Js('Dok-Rak'), Js('Dok-ban-yen'), Js('Dok-phi-sua'), Js('Dok-rak'), Js('Duan'), Js('Duang-Prapha'), Js('Duang-prapha'), Js('Duangnet'), Js('Duangrat'), Js('Durudee'), Js('Hansa'), Js('Hathai'), Js('Hiran'), Js('Hpr'), Js('Inthurat'), Js('Intira'), Js('Isaree'), Js('Jàew'), Js('Jaidee'), Js('Jintana'), Js('Jirattikarn'), Js('Jittramas'), Js('Jongchit'), Js('Jutharat'), Js('Kaeo'), Js('Kalaya'), Js('Kalya'), Js('Kamala'), Js('Kamchana'), Js('Kamonrat'), Js('Kanchana'), Js('Kanita'), Js('Kannika'), Js('Kanok'), Js('Kantima'), Js('Kanya'), Js('Karawek'), Js('Karn'), Js('Karnchana'), Js('Kasika'), Js('Keerati'), Js('Khae'), Js('Khakkhanang'), Js('Khantharot'), Js('Khem'), Js('Khiew Wan'), Js('Khouane'), Js('Khun Mae'), Js('Khun mae'), Js('Khun'), Js('Khunying'), Js('Kimnai'), Js('Kimuk'), Js('Klip'), Js('Kohsoom'), Js('Korrakoj'), Js('Kosum'), Js('Krijak'), Js('Krittiga'), Js('Kulap'), Js('Kultilda'), Js('Kusuman'), Js('Kwaanfah'), Js('Kwang'), Js('Kwanjai'), Js('Lalana'), Js('Lamai'), Js('Lamom'), Js('Lao'), Js('Lawan'), Js('Lek'), Js('Lukden'), Js('Ma-dee'), Js('Madee'), Js('Mae Noi'), Js('Mae'), Js('Mae-Duna'), Js('Mae-Khao'), Js('Mae-Noi'), Js('Mae-Pia'), Js('Mae-Ying-Thahan'), Js('Mae-duna'), Js('Mae-khao'), Js('Mae-noi'), Js('Mae-pia'), Js('Mae-ying-thahan'), Js('Mai'), Js('Maladee'), Js('Malee'), Js('Mali'), Js('Malisa'), Js('Malivalaya'), Js('Maliwan'), Js('Manee'), Js('Mani'), Js('Maniwan'), Js('Manya-Phathon'), Js('Manya-phathon'), Js('Maprang'), Js('Mathawee'), Js('Mayura'), Js('Mayuree'), Js('Mekhala'), Js('Mekhalaa'), Js('Mekhla'), Js('Monthani'), Js('Muan Nang'), Js('Mukda'), Js('Napatsorn'), Js('Napha'), Js('Narissa'), Js('Naruemon'), Js('Nataya'), Js('Natee'), Js('Nattaporn'), Js('Neeramphorn'), Js('Neung'), Js('Neungluthai'), Js('Ngam'), Js('Ngam-Chit'), Js('Ngor'), Js('Nidnoi'), Js('Nim'), Js('Nimnuan'), Js('Nin'), Js('Nisa'), Js('Nisarra'), Js('Nissa'), Js('Nittaya'), Js('Noi'), Js('Noklek'), Js('Nom'), Js('Nong Yao'), Js('Noom'), Js('Nopjira'), Js('Nuanjan'), Js('Nuntida'), Js('On Choi'), Js('On'), Js('Orapan'), Js('Orarat'), Js('Ornanong'), Js('Pada'), Js('Padungsri'), Js('Pakpao'), Js('Papao'), Js('Pasuta'), Js('Patcharee'), Js('Pathma'), Js('Patsaporn'), Js('Pen-Chan'), Js('Pensri'), Js('Pensria'), Js('Petchra'), Js('Phaibun'), Js('Phailin'), Js('Phairoh'), Js('Phajee'), Js('Phak-Phimonphan'), Js('Phak-phimonphan'), Js('Phan'), Js('Phannee'), Js('Phanthittra'), Js('Phara'), Js('Phatchara'), Js('Phathu'), Js('Phatra'), Js('Phawta'), Js('Phayao'), Js('Phi'), Js('Phim'), Js('Phitchaya'), Js('Phitsamaï'), Js('Phitsamai'), Js('Phloi'), Js('Phueng'), Js('Piam'), Js('Piano'), Js('Pichitra'), Js('Pim'), Js('Pimchan'), Js('Pitsamai'), Js('Piyapat'), Js('Porntip'), Js('Pradtana'), Js('Praewphan'), Js('Prahong'), Js('Praitun'), Js('Pranee'), Js('Prang'), Js('Praphat'), Js('Preet'), Js('Preeya'), Js('Premwadee'), Js('Prevanutch'), Js('Prija'), Js('Prisana'), Js('Promporn'), Js('Pummie'), Js('Pundit'), Js('Punngarm'), Js('Putsaya'), Js('Rachanee'), Js('Rada'), Js('Raegan'), Js('Rajini'), Js('Rampha'), Js('Ramphoei'), Js('Rand'), Js('Ratana'), Js('Ratanaporn'), Js('Ratchanichon'), Js('Ratri'), Js('Rattana'), Js('Rawee'), Js('Rochana'), Js('Ruethai'), Js('Rung'), Js('Rutana'), Js('Saeng'), Js('Saengdao'), Js('Sairung'), Js('Samorn'), Js('Sanan Nam'), Js('Sangrawee'), Js('Sangwan'), Js('Sanoh'), Js('Sanouk'), Js('Saowakhon'), Js('Saowapa'), Js('Saowatharn'), Js('Sarai'), Js('Sarakit'), Js('Saruta'), Js('Sasi'), Js('Sasikarn'), Js('Savitree'), Js('Sawat'), Js('Sawatdi'), Js('Sawinee'), Js('Shalisa'), Js('Si Fah'), Js('Si Mok'), Js('Si'), Js('Siam'), Js('Simla'), Js('Sinee'), Js('Sinn'), Js('Sirikit'), Js('Sirindhorn'), Js('Sirirat'), Js('Solada'), Js('Som Chai'), Js('Som Kid'), Js('Som Wang'), Js('Som'), Js('Somawadi'), Js('Son-Klin'), Js('Son-klin'), Js('Songsuda'), Js('Sopa'), Js('Sri-Patana'), Js('Sri-patana'), Js('Srinak'), Js('Srisuriyothai'), Js('Sroy'), Js('Sua'), Js('Suchada'), Js('Suchin'), Js('Suchitra'), Js('Suda'), Js('Sugunya'), Js('Sujin'), Js('Sujitra'), Js('Sukanda'), Js('Sukhon'), Js('Sukonta'), Js('Suleeport'), Js('Sumalee'), Js('Sumana'), Js('Sumniang'), Js('Sunanda'), Js('Sunatda'), Js('Sunee'), Js('Sunetra'), Js('Sunisa'), Js('Sunstra'), Js('Sup'), Js('Supaporn'), Js('Supharang'), Js('Suree'), Js('Sureeporn'), Js('Suttida'), Js('Suwattanee'), Js('Taeng'), Js('Talap'), Js('Tamarine'), Js('Tasanee'), Js('Teerana'), Js('Thailah'), Js('Thaksincha'), Js('Thao-Ap'), Js('Thao-ap'), Js('Thara'), Js('Theetika'), Js('Thiang'), Js('Thikhamphorn'), Js('Thong Dam'), Js('Thong Khao'), Js('Thong Thaem'), Js('Thong Thao'), Js('Thong'), Js('Thongyip'), Js('Thunyarat'), Js('Tida'), Js('Tidarat'), Js('Tookta'), Js('Toptim'), Js('Totsaken'), Js('Touraine'), Js('Tppiwan'), Js('Tuani'), Js('Tui'), Js('Tuk'), Js('Tukata'), Js('Tulaya'), Js('Tum'), Js('Tunlaya'), Js('Tuptim'), Js('Ubol'), Js('Ubolratana'), Js('Udom'), Js('Um'), Js('Ung'), Js('Urairat'), Js('Uthai'), Js('Utumporn'), Js('Vanida'), Js('Vipada'), Js('Waan'), Js('Waen'), Js('Wan'), Js('Wani-Ratana-Kanya'), Js('Wansa'), Js('Waralee'), Js('Wasana'), Js('Wayo'), Js('Wila'), Js('Wilasinee'), Js('Wimon'), Js('Winai'), Js('Wipa'), Js('Wismita'), Js('Wonnapa'), Js('Xuwicha'), Js('Ya Chai'), Js('Yada'), Js('Yaowalak'), Js('Yaowaman'), Js('Yen'), Js('Yindee'), Js('Ying'), Js('Yodman'), Js('Yodmani'), Js('Yong-Yut'), Js('Yrita'), Js('Yu-Pha'), Js('Yu-Phin'), Js('Yupin')]))
var.put('nm3', Js([Js('Aduladej'), Js('Adulet'), Js('Ahunai'), Js('Akradej'), Js('Amornchantanakorn'), Js('Anand'), Js('Apichart'), Js('Ariyanuntaka'), Js('Aromdee'), Js('Atchariyaboonyong'), Js('Atitarn'), Js('Banruerit'), Js('Benjawan'), Js('Bhirombhakdi'), Js('Boonliang'), Js('Boonmee'), Js('Boripat'), Js('Bunnag'), Js('Bunyasarn'), Js('Chadee'), Js("Chai'at"), Js('Chaipatana'), Js('Chaipoowapat'), Js('Chaiprasit'), Js('Chaisurivirat'), Js('Chaiyachue'), Js('Chaiyasan'), Js('Chaiyawan'), Js('Chakrabonse'), Js('Chalerm'), Js('Chalor'), Js('Chamlong'), Js('Chamroon'), Js("Chan'ocha"), Js('Chanpakdee'), Js('Chansiri'), Js('Chao'), Js('Charanachitta'), Js('Charoenkul'), Js('Chatichai'), Js('Chatwilai'), Js('Chavalit'), Js('Chearavanont'), Js('Cheenchamras'), Js('Chirapaisarnsakul'), Js('Chirathivat'), Js('Chiwpreecha'), Js('Choosak'), Js('Chuan'), Js('Chuasiriporn'), Js('Chumphorn'), Js('Chuthathep'), Js('Chutimant'), Js('Dabaransi'), Js('Dahkling'), Js('Dajpaisarn'), Js('Damrongsak'), Js('Darawan'), Js('Diskul'), Js('Ekaluck'), Js('Gason'), Js('Hitapot'), Js("Ho'thai"), Js('Honghannarong'), Js('Iemtadanai'), Js('Inchaieur'), Js('Inchareon'), Js('Jainukul'), Js('Janpong'), Js('Jatusripitak'), Js('Jetatikarn'), Js('Jetjirawat'), Js('Jivacate'), Js('Juntasa'), Js('Jurangkool'), Js('Kachornsak'), Js('Kadesadayurat'), Js('Kaewburesai'), Js('Kaewmanee'), Js('Kammana'), Js('Kamwilaisak'), Js('Kanjanapas'), Js('Kantawong'), Js('Kaouthai'), Js('Kasamsun'), Js('Kasemsarn'), Js('Kattiya'), Js('Kawrungruang'), Js('Keacham'), Js('Kedmanee'), Js('Khadpo'), Js('Khemanich'), Js('Khumpai'), Js('Khuntilanont'), Js('Kitjakarn'), Js('Klinpraneet'), Js('Kongkatitum'), Js('Kongpaisarn'), Js('Kongsangchai'), Js('Kosaisook'), Js('Kraiputra'), Js('Kriangsak'), Js('Kukrit'), Js('Kulawanit'), Js('Kunakorn'), Js('Kunchai'), Js('Kurusarttra'), Js('Kurusatienkit'), Js('Kwaigno'), Js('Lam'), Js('Lamwilai'), Js('Larpthawornkiet'), Js('Leekpai'), Js('Leelapun'), Js('Leeyao'), Js('Lekcharuthas'), Js('Lertkunakorn'), Js('Limthongkul'), Js('Luang'), Js('Lui'), Js('Mahagitsiri'), Js('Mahidol'), Js('Maleenon'), Js('Maleenont'), Js('Maneerattana'), Js('Meesang'), Js('Monkoltham'), Js('Montri'), Js('Mookjai'), Js('Nakpradith'), Js('Nantakarn'), Js('Narkbunnum'), Js('Narkhirunkanok'), Js('Narongdid'), Js('Nimitwanitch'), Js('Niratpattanasai'), Js('Nitaya'), Js('Nitpattanasai'), Js('Noppachorn'), Js('Nut'), Js('Ornlamai'), Js('Ornwimol'), Js('Pachrapa'), Js('Paireerak'), Js('Paithoonbuathong'), Js('Palapol'), Js('Palathai'), Js('Panichwit'), Js('Panomyaong'), Js('Panyarachun'), Js('Paowsong'), Js('Parnpradub'), Js('Parnthep'), Js('Parnthong'), Js('Patalung'), Js('Phatipatanawong'), Js('Phornprapha'), Js('Phrompan'), Js('Phya'), Js('Pibul'), Js('Pichit'), Js('Pimolkittikool'), Js('Pinthong'), Js('Pisit-na'), Js("Plai'nukool"), Js('Plainukool'), Js('Plaphol'), Js('Pongchandaj'), Js('Pongsak'), Js('Pongsanam'), Js('Ponhpaiboon'), Js('Pookusuwan'), Js('Poolvaraluck'), Js('Poonlarp'), Js('Pornpipatpong'), Js('Prachuab'), Js('Pradchaphet'), Js('Pramoj'), Js('Prapanpoj'), Js('Prapass'), Js('Praphasirirat'), Js('Prasarttong'), Js('Prasongsanti'), Js('Prateung'), Js('Praves'), Js('Preecha'), Js('Prem'), Js('Prempree'), Js('Pridi'), Js('Prinya'), Js('Prugsanapan'), Js('Puarborn'), Js('Pumpihon'), Js('Puntasrima'), Js('Punyawong'), Js('Pureesrisak'), Js('Putrie'), Js('Rardchawat'), Js('Ratana'), Js('Ratanarak'), Js('Rattanakosin'), Js('Rattanapong'), Js('Rojjanasukchai'), Js('Rojumanong'), Js('Saenamuang'), Js('Sakda'), Js('Sakdathorn'), Js('Samak'), Js('Samenem'), Js('Sangsorn'), Js('Sangwit'), Js('Sansurin'), Js('Santisakul'), Js('Sanya'), Js('Saowaluk'), Js('Sarit'), Js('Sasiprapa'), Js('Sathianthai'), Js('Sawasdipon'), Js('Sepsook'), Js("Shiew'aram"), Js('Shimma'), Js('Shinawatra'), Js('Silpa-archa'), Js('Sindudeja'), Js('Singhapat'), Js('Singharattanapan'), Js('Sintawichai'), Js('Sinthudecha'), Js('Sirishumsaeng'), Js('Sirisopa'), Js('Siriwanich'), Js('Sitdhirasdr'), Js('Sivaraksa'), Js('Somwan'), Js('Songprawati'), Js('Souvanatong'), Js('Srichure'), Js('Sripituksakul'), Js('Sriroj'), Js('Srisai'), Js('Srisati'), Js('Sriwarunyu'), Js('Suchinda'), Js('Sudham'), Js('Sukbunsung'), Js('Suksabaijai'), Js('Sunthorn'), Js('Suntornnitikul'), Js('Supachai'), Js('Suparat'), Js('Supasawat'), Js('Supitayaporn'), Js('Suppamongkon'), Js('Suprija'), Js('Suramongkol'), Js('Sutabuhr'), Js('Sutasanachinda'), Js('Suttikul'), Js('Suttirat'), Js('Taksin'), Js('Tanasugarn'), Js('Tangwongsan'), Js('Tansoongnen'), Js('Tantasatityanon'), Js('Tawisuwan'), Js('Temirak'), Js('Terdsak'), Js('Thabchumpon'), Js('Thaibangouy'), Js('Thanasukolwit'), Js('Thanom'), Js('Thanwareth'), Js('Thaugsuban'), Js('Thawan'), Js('Thong-oon'), Js('Thongthang'), Js('Thumying'), Js('Tomson'), Js('Tongproh'), Js('Traivut'), Js('Trivisvavet'), Js('Tuntayakul'), Js('Udomprecha'), Js('Vanich'), Js('Veerapol'), Js('Vejjajiva'), Js('Vijitpongpun'), Js('Vilailuck'), Js('Vipavakit'), Js('Visalyaputra'), Js('Wattana'), Js('Wattanapanit'), Js('Wattanasin'), Js('Wechsupaporn'), Js("Wi'lepana"), Js('Wichasak'), Js('Willapana'), Js('Wisetkaew'), Js('Wongkrachang'), Js('Wongrutiyan'), Js('Wongsawat'), Js('Wongsuwon'), Js('Yao-Yun'), Js('Yodsuwan'), Js('Yongchaiyudh'), Js('Yongjaiyut'), Js('Yoobamroong'), Js('Yoonim'), Js('Yoovidhya'), Js('Yuvaves')]))
pass
pass


# Add lib to the module scope
thaiNames = var.to_python()