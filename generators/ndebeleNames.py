__all__ = ['ndebeleNames']

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
    var.put('nm1', Js([Js('Andile (Increased)'), Js('Andile (They Are Many)'), Js('Anele (They Are Enough)'), Js('Ayanda (Boys Are Increasing)'), Js('Bekezela (Be Patient)'), Js('Bekithemba (Have Hope In)'), Js('Bhekilizwe (See The Nation)'), Js('Bhekimpilo (Confront Life)'), Js('Bhekithemba (Have Hope)'), Js('Bhekizwe (Look At The Country)'), Js('Bonginkosi (Be Grateful To God)'), Js('Busani (Rule)'), Js('Butho (Soldier)'), Js('Butholezwe (Soldier Of The Nation)'), Js('Celani (Ask)'), Js('Dumisani (Praise)'), Js('Gcinukuthula (Keep The Peace)'), Js('Hambo (Journey)'), Js('Jabulani (Be Happy All)'), Js('Jabulani (Enjoy)'), Js('Khumbulani (Remember)'), Js('Kwenzakwenkosi (Deed Of The Lord)'), Js('Langa (Sun)'), Js('Langelihle (Beautiful Day)'), Js('Lifa (Inheritance)'), Js('Lifalakhe (His Inheritance)'), Js('Lindani (Watch Over)'), Js('Lunga (Be Kind)'), Js('Lungile (Good)'), Js('Lungisani (Make Right)'), Js('Mandla (Strength)'), Js('Mandlakhe (His Efforts)'), Js('Mandlenkosi (God’S Power)'), Js('Mayibongwinkosi (Give Thanks To The Lord)'), Js('Mbekezeli (Patient One)'), Js('Mbonisi (One Who Makes You See)'), Js('Mbuso (Kingdom)'), Js('Mduduzi (One Who Consoles)'), Js('Mehluli (Conquerer)'), Js('Mehluli (One Who Defeats)'), Js('Meluleki (One Who Advises)'), Js('Melusi (Shephard)'), Js('Mgcini (Keeper)'), Js('Mkhokheli (Leader)'), Js('Mkhuleko (Prayer)'), Js('Mlamuleli (One Who Intervenes)'), Js('Mlamuli (One Who Intervenes)'), Js('Mlindeli (Guardian)'), Js('Mlungisi (The One Who Brings Order)'), Js('Mncedisi (Helper)'), Js('Mongameli (Leader)'), Js('Mpilo (Life)'), Js('Mthandazo (Prayer)'), Js('Mthokozisi (One Who Gives Joy)'), Js('Mthulisi (One Who Consoles)'), Js('Mtshumayeli (Preacher)'), Js('Musa (Kindness)'), Js('Ndaba (News)'), Js('Ndabezinhle (Good News)'), Js("Ndabicacile (The Story's Clear)"), Js('Ndodana (Son)'), Js('Nhlalo (Lifestyle)'), Js('Nhlanhla (Luck)'), Js('Nhlanhla (Lucky One)'), Js('Nhlonipho (Respect)'), Js('Njabulo (Celebration)'), Js('Nkanyiso (Brilliance)'), Js('Nkathazo (Troublesome)'), Js('Nkosi (King)'), Js('Nkululeko (Freedom)'), Js('Nqobile (We Conquered)'), Js('Ntando (Will)'), Js('Ntandoyenkosi (Will Of God)'), Js('Ntokozo (Joy)'), Js('Philani (Live)'), Js('Qalani (Provoke)'), Js('Qhawe (Hero)'), Js('Qinani (Be Strong)'), Js('Sabelo (Reply)'), Js("Sandile (We're Many)"), Js('Sibusiso (Blessing)'), Js('Sifiso (What We Wished For)'), Js('Sihawukele (Have Mercy On Us)'), Js('Sihlengisizwe (We Redeem The Nation)'), Js('Sikhanyile (We Shined)'), Js('Sikhumbuzo (Reminder)'), Js("Silibele (We're Unaware)"), Js("Simphiwe (He's Our Gift)"), Js('Sindiso (Redemption)'), Js('Sipho (Gift)'), Js('Siyabonga (Thank You)'), Js("Siyabonga (We're Grateful)"), Js('Sizo (Help)'), Js('Sukoluhle (Happy Day)'), Js('Suku (Day)'), Js('Thabani (Be Happy)'), Js('Thabani (Be Joyful)'), Js('Thabo (Happiness)'), Js('Thamsanqa (Blessings)'), Js('Thandazani (Pray)'), Js('Thando (Love)'), Js('Themba (Hope)'), Js('Thembelani (Have Hope)'), Js('Thokozani (Be Happy)'), Js('Tholumusa (Find Grace)'), Js('Thubelihle (Good Opportunity)'), Js('Thulani (Be Quiet)'), Js('Vulindlela (Open The Way)'), Js('Vusa (Raise)'), Js('Vusumuzi (Rekindle The Family)'), Js('Xolani (Forgive)'), Js('Xolani (Peace Upon All Of You)'), Js('Zamani (Try)'), Js('Zenzo (Deeds)'), Js('Ziboniso (Visions)'), Js('Zibusiso (Blessings)')]))
    var.put('nm2', Js([Js('Ayanda (They Are Increasing)'), Js('Bekezela (Be Patient)'), Js('Bongani (Thank You)'), Js('Bongile (Thanks)'), Js('Bongiwe (Thanks)'), Js('Buhle (Beauty)'), Js('Buhlebenkosi (God’S Beauty)'), Js('Bunjiwe (Attractive)'), Js('Busisiwe (Blessed)'), Js('Cacile (Clear)'), Js('Celesile (Rejoice)'), Js('Dalubuhle (Born Beautiful)'), Js('Fikile (She Has Arrived)'), Js('Gugulethu (Our Precious One)'), Js('Gugulethu (Our Treasure)'), Js('Hlengiwe (Redeemed)'), Js('Khayelihle (Good Home)'), Js('Khethiwe (Chosen)'), Js('Langelihle (Beautiful Day)'), Js('Lindiwe (One Who Is Guarded)'), Js('Lingadani (Don’t Be Sad)'), Js('Mayibongwe (Give Thanks)'), Js('Musa (Grace)'), Js('Nobuhle (Beauty)'), Js('Nokuthula (Peace)'), Js('Nomagugu (Mother Of Precious Things)'), Js('Nomagugu (Precious)'), Js('Lifalakhe (Her Inheritance)'), Js('Nomalanga  (Sun)'), Js('Nomalanga (Mother Of Sunshine)'), Js('Nomandla (Mother Of Strength)'), Js('Nomaqhawe (Heroine)'), Js('Nomasonto (Mother Of Sunday)'), Js('Nomathemba (Hope)'), Js('Nomathemba (We Have Hope)'), Js('Nomusa (Kind One)'), Js('Nomusa (Mercy)'), Js('Nonhlanhla (Luck)'), Js('Nonhlanhla (Mother Of Luck)'), Js('Nontando (One With Strong Will)'), Js('Nosipho (Gift)'), Js('Nothando (Love)'), Js('Noxolo (Mother Of Peace)'), Js('Ntombenhle (Beautiful Girl)'), Js("Phumuzile (Now We're Rested)"), Js('Qalani (Provoke)'), Js("Qinile (We're Strong)"), Js("Qinisile (We're Sure)"), Js('Sakhile (We Created)'), Js('Sibongile (Thank You)'), Js("Sibusisiwe (We're Blessed)"), Js('Sibusiso (A Blessing)'), Js("Sibusiswe (We're Blessed)"), Js("Sikhangezile (We're Receiving)"), Js("Sikhethiwe (We're Chosen)"), Js('Sikhulekile (We Prayed)'), Js('Silibaziso (Distraction)'), Js('Simangaliso (Miracle)'), Js('Sindisiwe (Saved)'), Js('Sinikiwe (Given)'), Js('Sinobuhle (We Have Beauty)'), Js("Siphiwe (We're Given)"), Js('Sipho (Gift)'), Js("Sithabile (We're Happy)"), Js('Sithabisile  (One Who Makes Us Happy)'), Js("Sithabisile (We're Very Happy)"), Js('Sithandazile (We Prayed)'), Js("Sithembile (We're Hopeful)"), Js("Sithenjiwe (We're Trusted)"), Js('Sitshengisiwe (We Were Shown)'), Js('Sizo (Help)'), Js('Snini (Relative)'), Js("Sthandekile (We're Loved)"), Js('Thandeka (Lovely)'), Js('Thandiwe (Beloved One)'), Js('Thandiwe (Loved One)'), Js('Thandiwe (Loved)'), Js('Thembeka (Be Reliable)'), Js('Thembekile (Faithful)'), Js('Thembile (Hopeful)'), Js('Thenjiwe (Trusted)'), Js('Thobekile (Polite)'), Js('Thokozani (Celebrate)'), Js('Thuba (Chance)'), Js('Thubelihle (Good Chance)'), Js('Thubelihle (Good Opportunity)'), Js('Xolisani (Ask For Forgiveness)'), Js('Zandile (Many)'), Js('Zandile (They Are Many)'), Js('Zanele (Enough)'), Js('Zibusiso (Blessings)'), Js('Zinhle (Beautiful)')]))
    var.put('nm3', Js([Js('Bayeni'), Js('Bele'), Js('Bembe'), Js('Bhedleni'), Js('Bhelesi'), Js('Bhembe'), Js('Bhengani'), Js('Bhengu'), Js('Bhovungana'), Js('Bhungane'), Js('Bhuyeni'), Js('Bikelwayo'), Js('Binda'), Js('Biyase'), Js('Biyela'), Js('Blose'), Js('Bophela'), Js('Bukhosini'), Js('Caluza'), Js('Cebekhulu'), Js('Cebisa'), Js('Cele'), Js('Cenge'), Js('Chamane'), Js('Chibi'), Js('Chibini'), Js('Chili'), Js('Chiliza'), Js('Chonco'), Js('Chule'), Js('Cibane'), Js('Cindi'), Js('Cwalile'), Js('Delwayo'), Js('Dikane'), Js('Dimba'), Js('Dimbane'), Js('Dimbani'), Js('Dinabantu'), Js('Dinane'), Js('Dinangwe'), Js('Dindela'), Js('Dindi'), Js('Dingila'), Js('Dlaba'), Js('Dlabane'), Js('Dlabazane'), Js('Dladla'), Js('Dlakadla'), Js('Dlakela'), Js('Dlamane'), Js('Dlamdaka'), Js('Dlamini'), Js('Dlamlenze'), Js('Dlangamandla'), Js('Dlebenkomo'), Js('Dlodlo'), Js('Dlomo'), Js('Dludla'), Js('Dludlu'), Js('Dlungwana'), Js('Doncabe'), Js('Donda'), Js('Dubandlela'), Js('Dubazane'), Js('Dukada'), Js('Duma'), Js('Dumakude'), Js('Dumisa'), Js('Dunge'), Js('Duyaza'), Js('Duze'), Js('Fakazi'), Js('Fakude'), Js('Fanisa'), Js('Fenya'), Js('Fihlela'), Js('Fuze'), Js('Gabadela'), Js('Gabela'), Js('Gabhezi'), Js('Gabhisa'), Js('Gadlela'), Js('Gagashe'), Js('Galu'), Js('Gama'), Js('Gambu'), Js('Gambushe'), Js('Gamede'), Js('Gasa'), Js('Gasela'), Js('Gawozi'), Js('Gazu'), Js('Gcaba'), Js('Gcaleka'), Js('Gcugcwa'), Js('Gcumisa'), Js('Gcwabe'), Js('Gcwensa'), Js('Gebashe'), Js('Gebhezi'), Js('Gedeza'), Js('Gence'), Js('Gengeshe'), Js('Gigaba'), Js('Gina'), Js('Gininda'), Js('Ginindza'), Js('Goba'), Js('Gobhozi'), Js('Godide'), Js('Goje'), Js('Gotsholo'), Js('Gubeshe'), Js('Gubhela'), Js('Gubhuza'), Js('Gubulundu'), Js('Gugushe'), Js('Gule'), Js('Guliwe'), Js('Guma'), Js('Gumbi'), Js('Gumede'), Js('Gwacela'), Js('Gwagwa'), Js('Gwala'), Js('Gwamanda'), Js('Gwanyana'), Js('Gwija'), Js('Gxabhashe'), Js('Hadebe'), Js('Hangala'), Js('Hhoyiyane'), Js('Hlabangane'), Js('Hlabisa'), Js('Hlomuka'), Js('Hlongwa'), Js('Hlongwane'), Js('Hlumakazi'), Js('Jamasijadu'), Js('Jiba'), Js('Jibela'), Js('Jili'), Js('Jiyane'), Js('Jobe'), Js('Juqula'), Js('Khabalidaka'), Js('Khabazela'), Js('Khambule'), Js('Khanyayo'), Js('Khaphela'), Js('Khathide'), Js('Khathini'), Js('Khawula'), Js('Kheswa'), Js('Khezokhulu'), Js('Khobeni'), Js('Kholose'), Js('Khomo'), Js('Khondlo'), Js('Khonjwayo'), Js('Khosini'), Js('Khoza'), Js('Khuba'), Js('Khuboni'), Js('Khukhuza'), Js('Khulu'), Js('Khuluse'), Js('Khumalo'), Js('Khumbuza'), Js('Khushwayo'), Js('Khuyameni'), Js('Khuzwayo'), Js('Khwane'), Js('Khwela'), Js('Kunene'), Js('Kweyama'), Js('Lamula'), Js('Langa'), Js('Lange'), Js('Langeni'), Js('Lango'), Js('Lembede'), Js('Linda'), Js('Lindamkhonto'), Js('Longode'), Js('Ludonga'), Js('Lukhele'), Js('Luqe'), Js('Luthuli'), Js('Luvuno'), Js('Lwandle'), Js('Mabanga'), Js('Mabaso'), Js('Mabhedla'), Js('Mabhodla'), Js('Mabhoko'), Js('Mabhoyi'), Js('Mabika'), Js('Mabizela'), Js('Mabuyakhulu'), Js('Mabuza'), Js('Macingwane'), Js('Made'), Js('Madela'), Js('Madlanduna'), Js('Madlokovu'), Js('Madlula'), Js('Madondo'), Js('Madonsela'), Js('Maduna'), Js('Madziba'), Js('Mafobo'), Js('Mafulela'), Js('Magadlela'), Js('Magagula'), Js('Magalela'), Js('Magange'), Js('Magasela'), Js('Magaya'), Js('Magaye'), Js('Mageba'), Js('Magezana'), Js('Magolwana'), Js('Magononde'), Js('Magoza'), Js('Magujwa'), Js('Magutshwa'), Js('Magwaza'), Js('Mahamba'), Js('Mahaye'), Js('Mahlaba'), Js('Mahlase'), Js('Mahlinza'), Js('Mahlobo'), Js('Mahulube'), Js('Majila'), Js('Majoka'), Js('Majola'), Js('Makhathini'), Js('Makhaye'), Js('Makhaza'), Js('Makhedama'), Js('Makhoba'), Js('Makhubo'), Js('Makhulukhulu'), Js('Makhunga'), Js('Malambule'), Js('Malembe'), Js('Malevu'), Js('Malinga'), Js('Maluleka'), Js('Mamba'), Js('Manana'), Js('Mangcamane'), Js('Mangede'), Js('Mangena'), Js('Mangethe'), Js('Manqele'), Js('Mantshinga'), Js('Manyoni'), Js('Manzezulu'), Js('Manzini'), Js('Maphahla'), Js('Maphalala'), Js('Maphanga'), Js('Maphindela'), Js('Mapholoba'), Js('Maqhama'), Js('Maseko'), Js('Mashasha'), Js('Mashimane'), Js('Mashinini'), Js('Mashiya'), Js('Mashobane'), Js('Masilela'), Js('Masina'), Js('Masinga'), Js('Masondo'), Js('Masuku'), Js('Mathaba'), Js('Mathe'), Js('Mathebula'), Js('Mathenjwa'), Js('Mathetha'), Js('Mathibela'), Js('Mathonsi'), Js('Mathula'), Js('Mathumba'), Js('Mathunjwa'), Js('Mathwasa'), Js('Mavela'), Js('Mavundla'), Js('Mavuso'), Js('Mawanda'), Js('Mawewe'), Js('Mayeza'), Js('Mayise'), Js('Mayisela'), Js('Mazankosi'), Js('Maziya'), Js('Mazwi'), Js('Mbamali'), Js('Mbanjwa'), Js('Mbatha'), Js('Mbede'), Js('Mbekwa'), Js('Mbelu'), Js('Mbembe'), Js('Mbende'), Js('Mbhedu'), Js('Mbhele'), Js('Mbhense'), Js('Mbhodwe'), Js('Mbhulangwe'), Js('Mbili'), Js('Mbokane'), Js('Mboko'), Js('Mbomvu'), Js('Mbonambi'), Js('Mbonane'), Js('Mboyisa'), Js('Mbulaze'), Js('Mbulazi'), Js('Mbuli'), Js('Mbungela'), Js('Mbunjwa'), Js('Mbuso'), Js('Mbutho'), Js('Mbuyazi'), Js('Mbuyisa'), Js('Mbuyise'), Js('Mcambi'), Js('Mcanco'), Js('Mchunu'), Js('Mcoyi'), Js('Mcusi'), Js('Mcwaye'), Js('Mdeke'), Js('Mdephane'), Js('Mdima'), Js('Mdindela'), Js('Mdinwa'), Js('Mdlalose'), Js('Mdlanyoka'), Js('Mdlobhiya'), Js('Mdlolo'), Js('Mdluli'), Js('Mdlumbi'), Js('Mdomula'), Js('Mdonswa'), Js('Mdotshana'), Js('Mdunge'), Js('Mehloluhlaza'), Js('Menziwa'), Js('Meyiwa'), Js('Mfeka'), Js('Mfumu'), Js('Mfusi'), Js('Mgabadeli'), Js('Mgabhi'), Js('Mgasela'), Js('Mgazi'), Js('Mgcaleka'), Js('Mgenge'), Js('Mgilija'), Js('Mguni'), Js('Mhayise'), Js('Mhlabandlovu'), Js('Mhlambo'), Js('Mhlanga'), Js('Mhlanya'), Js('Mhlongo'), Js('Mhlongwane'), Js('Mhlophe'), Js('Mhlungu'), Js('Miya'), Js('Mjadu'), Js('Mjakada'), Js('Mjoji'), Js('Mjoli'), Js('Mjwara'), Js('Mkhabela'), Js('Mkhandlela'), Js('Mkhathini'), Js('Mkhatshwa'), Js('Mkhithi'), Js('Mkhokeleleki'), Js('Mkholo'), Js('Mkholwa'), Js('Mkhongisa'), Js('Mkhulisi'), Js('Mkhumbuzi'), Js('Mkhwanazi'), Js('Mlaba'), Js('Mlalane'), Js('Mlambo'), Js('Mlangatshe'), Js('Mlangeni'), Js('Mlawu'), Js('Mlawula'), Js('Mlinga'), Js('Mlondo'), Js('Mlotshwa'), Js('Mlungwana'), Js('Mnangwe'), Js('Mncwabe'), Js('Mncwango'), Js('Mnembe'), Js('Mngadi'), Js('Mngoma'), Js('Mngomezulu'), Js('Mnguni'), Js('Mngwemkhulu'), Js('Mngwengwe'), Js('Mnikathi'), Js('Mnomiya'), Js('Mnqamu'), Js('Mnqayi'), Js('Mnquhe'), Js('Mntambo'), Js('Mntimande'), Js('Mntungwa'), Js('Mnungwa'), Js('Mnyaka'), Js('Mnyamande'), Js('Mnyandu'), Js('Mnyoni'), Js('Mondise'), Js('Motha'), Js('Mpangazitha'), Js('Mpangele'), Js('Mpanza'), Js('Mphahlwa'), Js('Mphankomo'), Js('Mphazima'), Js('Mphemba'), Js('Mphephethwa'), Js('Mpikela'), Js('Mpumuza'), Js('Mpungose'), Js('Mpunzana'), Js('Mqadi'), Js('Mqungebe'), Js('Msamkhulu'), Js('Msenti'), Js('Mshazi'), Js('Mshengu'), Js('Mshibe'), Js('Mshikela'), Js('Mshikila'), Js('Mshiyane'), Js('Msholozi'), Js('Msibi'), Js('Msimang'), Js('Msindazwe'), Js('Msokazi'), Js('Msomi'), Js('Msuthu'), Js('Msweli'), Js('Mthabela'), Js('Mthalane'), Js('Mthanti'), Js('Mthethwa'), Js('Mthimkhulu'), Js('Mthinti'), Js('Mthiya'), Js('Mthiyane'), Js('Mthombeni'), Js('Mtima'), Js('Mtimande'), Js('Mtolo'), Js('Mtshali'), Js('Mtumaseli'), Js('Mtuswa'), Js('Musi'), Js('Mvelase'), Js('Mveni'), Js('Mvubu'), Js('Mvula'), Js('Mvulane'), Js('Mvulani'), Js('Mvuna'), Js('Mwandla'), Js('Mwelase'), Js('Myeni'), Js('Myeza'), Js('Mzamela'), Js('Mzila'), Js('Mzilankatha'), Js('Mzileni'), Js('Mzimela'), Js('Mzimela.'), Js('Mziyankatha'), Js('Mzizi'), Js('Mzolo'), Js('Mzomba'), Js('Mzoneli'), Js('Mzukase'), Js('Mzukwuse'), Js('Mzulwini'), Js('Nala'), Js('Nandisa'), Js('Ncala'), Js('Ncama'), Js('Ncanana'), Js('Ncongwane'), Js('Ncusi'), Js('Ncwaba'), Js('Ncwane'), Js('Ndaba'), Js('Ndabandaba'), Js('Ndabase'), Js('Ndabezitha'), Js('Ndandali'), Js('Ndawo'), Js('Ndawonde'), Js('Ndelu'), Js('Ndengezi'), Js('Ndima'), Js('Ndimande'), Js('Ndiyema'), Js('Ndlala'), Js('Ndlandla'), Js('Ndlangamandla'), Js('Ndlanya'), Js('Ndlanzi'), Js('Ndlela'), Js('Ndlondlo'), Js('Ndondakusuka'), Js('Ndonga'), Js('Ndosi'), Js('Ndulini'), Js('Ndwandwe'), Js('Nene'), Js('Ngalonde'), Js('Ngazitha'), Js('Ngcamane'), Js('Ngcamu'), Js('Ngcaweni'), Js('Ngcemu'), Js('Ngcobo'), Js('Ngcolosi'), Js('Ngema'), Js('Ngiba'), Js('Ngidi'), Js('Ngobese'), Js('Ngomane'), Js('Ngonini'), Js('Ngonyama'), Js('Ngotsha'), Js('Ngubane'), Js('Ngubeni'), Js('Ngungunyana'), Js('Nguse'), Js('Ngwane'), Js('Ngwazi'), Js('Nhlabathi'), Js('Nhlane'), Js('Nhlanhla'), Js('Nhlanhlampofu'), Js('Nhlapho'), Js('Nhleko'), Js('Nhlengethwa'), Js('Njapha'), Js('Njiki'), Js('Njinji'), Js('Njomane'), Js('Nkabinde'), Js('Nkomose'), Js('Nkomoye'), Js('Nkondlwane'), Js('Nkonyeni'), Js('Nkophe'), Js('Nkosi'), Js('Nkumane'), Js('Nkundlande'), Js('Nkwakha'), Js('Nkwali'), Js('Nkwaliyenkosi'), Js('Nkwanyana'), Js('Nodanga'), Js('Nodlomo'), Js('Nogantshi'), Js('Nombela'), Js('Nombhoco'), Js('Nomndayi'), Js('Nomvuma'), Js('Nondaba'), Js('Nondela'), Js('Nondlela'), Js('Nonduma'), Js('Nongalaza'), Js('Nongalo'), Js('Nonkosi'), Js('Nonkululeko'), Js('Nontanda'), Js('Nontuli'), Js('Nonyana'), Js('Nowanqa'), Js('Nozulu'), Js('Nqumela'), Js('Nsele'), Js('Nselenduna'), Js('Nsibande'), Js('Nsibanyoni'), Js('Nsindane'), Js('Nsizwakele'), Js('Nsukuza'), Js('Ntaka'), Js('Ntamonde'), Js('Ntanzi'), Js('Ntenga'), Js('Ntombela'), Js('Ntongadli'), Js('Ntsele'), Js('Ntshalintshali'), Js('Ntshangase'), Js('Ntshingila'), Js('Ntshiza'), Js('Ntuli'), Js('Ntusi'), Js('Nxele'), Js('Nxumalo'), Js('Nyambawu'), Js('Nyambose'), Js('Nyamenja'), Js('Nyanda'), Js('Nyandeni'), Js('Nyawokhulu'), Js('Nyawose'), Js('Nyazitla'), Js('Nyembe'), Js('Nyembezi'), Js('Nyide'), Js('Nyokayebululu'), Js('Nyuswa'), Js('Nzama'), Js('Nzamela'), Js('Nzima'), Js('Nzimande'), Js('Nzimase'), Js('Nzuza'), Js('Phahla'), Js('Phakathi'), Js('Phakathwayo'), Js('Phathwayo'), Js('Phetha'), Js('Phethela'), Js('Phikela'), Js('Phingoshe'), Js('Phohlo'), Js('Phoseka'), Js('Phoswa'), Js('Phungula'), Js('Phuthini'), Js('Qomazitha'), Js('Qunga'), Js('Qwabe'), Js('Sabela/Sabelo'), Js('Sameya'), Js('Sandanezwe'), Js('Sangwani'), Js('Sangweni'), Js('Sebenzekhaya'), Js('Seme'), Js('Semi'), Js('Sengwayo'), Js('Seyama'), Js('Shabalala'), Js('Shabane'), Js('Shabangu'), Js('Shamase'), Js('Shandu'), Js('Shange'), Js('Shazi'), Js('Shekimbuya'), Js('Shenge'), Js('Shengele'), Js('Shezi'), Js('Shibase'), Js('Shinga'), Js('Shoba'), Js('Shobane'), Js('Shombela'), Js('Shongololo'), Js('Shoyisa'), Js('Shozi'), Js('Shuku'), Js('Sibalukhulu'), Js('Sibaya'), Js('Sibeko'), Js('Sibhene'), Js('Sibisi'), Js('Sibiya'), Js('Sidlodlo'), Js('Sigagu'), Js('Sigegede'), Js('Sigwaxa'), Js('Sijadu'), Js('Sikhakha'), Js('Sikhakhane'), Js('Sikhonza'), Js('Sikhosana'), Js('Sikhumbane'), Js('Sikhunyana'), Js('Sikobi'), Js('Sikwayo'), Js('Silangwe'), Js('Simelane'), Js('Sishange'), Js('Sishangwe'), Js('Sishi'), Js('Sishiya'), Js('Sithenjwa'), Js('Sithombo'), Js('Sithuli'), Js('Sitolotolo'), Js('Siwela'), Js('Siwele'), Js('Siyaya'), Js('Siyeshe'), Js('Sobote'), Js('Sochumase'), Js('Sodi'), Js('Sodiza'), Js('Soduba'), Js('Sokhela'), Js('Sokhulu'), Js('Sokhwebula'), Js('Sokwalisa'), Js('Somboni'), Js('Somfula'), Js('Sompisi'), Js('Sondini'), Js('Sondisa'), Js('Songiya'), Js('Sonkophe'), Js('Sonqandile'), Js('Sontuli'), Js('Sothole'), Js('Sotobe'), Js('Swazi'), Js('Sweli'), Js('Thabekhulu'), Js('Thabizolo'), Js('Thango'), Js('Thela'), Js('Thembekwayo'), Js('Thembela'), Js('Thenjwayo'), Js('Thiyane'), Js('Thobeni'), Js('Thole'), Js('Thomoyi'), Js('Thoyana'), Js('Thumbela'), Js('Thumbeza'), Js('Thusi'), Js('Thusini'), Js('Thwala'), Js('Tiba'), Js('Tukane'), Js('Vabaza'), Js('Vanande'), Js('Vangisa'), Js('Vezi'), Js('Vilakazi'), Js('Vumisa'), Js('Vunisa'), Js('Wanda'), Js('Wela'), Js('Weza'), Js('Wosiyane'), Js('Xaba'), Js('Xala'), Js('Ximba'), Js('Xolo'), Js('Xulu'), Js('Yamela'), Js('Yenga'), Js('Yengwayo'), Js('Yeni'), Js('Yeye'), Js('Yeyeye'), Js('Zaca'), Js('Zakwe'), Js('Zama'), Js('Zamisa'), Js('Zaza'), Js('Zibani'), Js('Zikhali'), Js('Zikhonjwa'), Js('Zikhungwini'), Js('Zikode'), Js('Zimase'), Js('Zimbu'), Js('Zincume'), Js('Zindela'), Js('Zinyane'), Js('Ziqubu'), Js('Ziqunde'), Js('Zitha'), Js('Zizi'), Js('Zondi'), Js('Zondo'), Js('Zosongo'), Js('Zubane'), Js('Zuke'), Js('Zukula'), Js('Zulu'), Js('Zuma'), Js('Zumbisa'), Js('Zungu')]))
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
ndebeleNames = var.to_python()