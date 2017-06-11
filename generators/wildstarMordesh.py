__all__ = ['wildstarMordesh']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('lname', ((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
            else:
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('lname', ((((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd5'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('name', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('lname')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('name', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('lname')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Alexi'), Js('Bajko'), Js('Belos'), Js('Biljan'), Js('Biser'), Js('Blago'), Js('Blagojce'), Js('Blagoje'), Js('Blagoy'), Js('Blagun'), Js('Blahos'), Js('Boban'), Js('Bogdan'), Js('Bogom'), Js('Bogomil'), Js('Bogumil'), Js('Bohdan'), Js('Bohum'), Js('Bohumer'), Js('Bohumil'), Js('Bojan'), Js('Bojek'), Js('Bojidar'), Js('Bolek'), Js('Boro'), Js('Borce'), Js('Borek'), Js('Borik'), Js('Boril'), Js('Boris'), Js('Borko'), Js('Borno'), Js('Borut'), Js('Bosko'), Js('Boyan'), Js('Boyko'), Js('Bozan'), Js('Bozhil'), Js('Bozhin'), Js('Bozidar'), Js('Bozo'), Js('Bozydar'), Js('Brajko'), Js('Branek'), Js('Branik'), Js('Branko'), Js('Brencis'), Js('Bretik'), Js('Budek'), Js('Budim'), Js('Bujanek'), Js('Burian'), Js('Casim'), Js('Dalibor'), Js('Damek'), Js('Dane'), Js('Danil'), Js('Danko'), Js('Dare'), Js('Darin'), Js('Darko'), Js('Daro'), Js('Davor'), Js('Davorin'), Js('Davorko'), Js('Dejan'), Js('Delcho'), Js('Delyan'), Js('Derwan'), Js('Desim'), Js('Deyan'), Js('Divan'), Js('Dmitri'), Js('Dobri'), Js('Dobrin'), Js('Domard'), Js('Donat'), Js('Dragan'), Js('Dragi'), Js('Dragiso'), Js('Drago'), Js('Draho'), Js('Drahos'), Js('Drazo'), Js('Drazan'), Js('Drazen'), Js('Drziho'), Js('Durko'), Js('Dusan'), Js('Duscho'), Js('Dusek'), Js('Dusko'), Js('Elyo'), Js('Fadey'), Js('Gavril'), Js('Gniewko'), Js('Gojko'), Js('Goran'), Js('Gorazd'), Js('Grozdan'), Js('Grubiso'), Js('Gvozden'), Js('Honzo'), Js('Igor'), Js('Iskren'), Js('Jadran'), Js('Jadranko'), Js('Jakso'), Js('Jarek'), Js('Jarom'), Js('Jaromer'), Js('Jaromil'), Js('Jaros'), Js('Jarousek'), Js('Jasen'), Js('Jasenko'), Js('Javor'), Js('Jovan'), Js('Jugos'), Js('Kalin'), Js('Kamen'), Js('Kardo'), Js('Kazim'), Js('Kazimierz'), Js('Klatko'), Js('Klonim'), Js('Kole'), Js('Kolyo'), Js('Kostyo'), Js('Krasim'), Js('Krastan'), Js('Krastyo'), Js('Kresim'), Js('Kresnik'), Js('Kreso'), Js('Krsevan'), Js('Krzesim'), Js('Kvetos'), Js('Lachezar'), Js('Ladis'), Js('Lado'), Js('Lechos'), Js('Leszek'), Js('Lubo'), Js('Lubek'), Js('Lubom'), Js('Lubor'), Js('Luborek'), Js('Lubos'), Js('Lubosek'), Js('Ludos'), Js('Luko'), Js('Lyuben'), Js('Lyubom'), Js('Lyubos'), Js('Lyudmil'), Js('Malin'), Js('Matejo'), Js('Mecek'), Js('Mecik'), Js('Mecis'), Js('Mijom'), Js('Miladin'), Js('Milan'), Js('Milanko'), Js('Milcho'), Js('Mile'), Js('Milen'), Js('Milenko'), Js('Mileti'), Js('Milic'), Js('Miliduch'), Js('Milivoj'), Js('Milivoje'), Js('Miljan'), Js('Miljenko'), Js('Milko'), Js('Milo'), Js('Miloje'), Js('Milon'), Js('Milorad'), Js('Milos'), Js('Milosz'), Js('Milovan'), Js('Milush'), Js('Milutin'), Js('Miodrag'), Js('Misko'), Js('Mjecis'), Js('Mladen'), Js('Momchil'), Js('Momcilo'), Js('Muncel'), Js('Mutim'), Js('Myslik'), Js('Nado'), Js('Naum'), Js('Nayden'), Js('Nebojso'), Js('Nedelcho'), Js('Nenad'), Js('Nepomuk'), Js('Neven'), Js('Niko'), Js('Obrad'), Js('Obren'), Js('Ognian'), Js('Ognjen'), Js('Ognyan'), Js('Oleg'), Js('Orlin'), Js('Ozren'), Js('Parvan'), Js('Perun'), Js('Plamen'), Js('Pomuk'), Js('Predrag'), Js('Premek'), Js('Premysl'), Js('Pres'), Js('Pribo'), Js('Pribik'), Js('Prodan'), Js('Radacek'), Js('Radan'), Js('Rade'), Js('Radek'), Js('Radi'), Js('Radik'), Js('Radim'), Js('Radko'), Js('Radmilo'), Js('Rado'), Js('Radoje'), Js('Radom'), Js('Radomer'), Js('Rados'), Js('Radovan'), Js('Radoy'), Js('Raicho'), Js('Rajan'), Js('Rajke'), Js('Rajko'), Js('Rajo'), Js('Ranko'), Js('Ratim'), Js('Ratko'), Js('Rato'), Js('Ratom'), Js('Rayko'), Js('Razvigor'), Js('Roscis'), Js('Rosen'), Js('Rosto'), Js('Rostek'), Js('Rosticek'), Js('Rostik'), Js('Rostis'), Js('Rumen'), Js('Sambor'), Js('Sian'), Js('Siniso'), Js('Siso'), Js('Slobodan'), Js('Smiljan'), Js('Snjesko'), Js('Sobek'), Js('Sobes'), Js('Sobies'), Js('Sobik'), Js('Sokol'), Js('Soljub'), Js('Spasoje'), Js('Spomenko'), Js('Srdjan'), Js('Srebrenko'), Js('Srecko'), Js('Sredoje'), Js('Sreten'), Js('Stano'), Js('Stando'), Js('Stane'), Js('Stanek'), Js('Stani'), Js('Stanicek'), Js('Stanij'), Js('Stanik'), Js('Stanim'), Js('Stanis'), Js('Stanko'), Js('Stesho'), Js('Stoil'), Js('Stojan'), Js('Stoyan'), Js('Stoycho'), Js('Stoyko'), Js('Stracim'), Js('Strahil'), Js('Strahim'), Js('Sudan'), Js('Sudanek'), Js('Sulis'), Js('Svatom'), Js('Svatos'), Js('Svetlan'), Js('Svetlin'), Js('Svetos'), Js('Svetozar'), Js('Svilen'), Js('Svyatos'), Js('Swietos'), Js('Techom'), Js('Techos'), Js('Tihom'), Js('Tihomil'), Js('Tijan'), Js('Tjesim'), Js('Tomis'), Js('Tomo'), Js('Toplico'), Js('Traicho'), Js('Traiko'), Js('Troian'), Js('Trpim'), Js('Tsvetan'), Js('Tsvetom'), Js('Tugom'), Js('Vacek'), Js('Vadim'), Js('Valko'), Js('Vanyo'), Js('Varban'), Js('Vasek'), Js('Vassko'), Js('Vatros'), Js('Veces'), Js('Vedran'), Js('Vekos'), Js('Velo'), Js('Velek'), Js('Veles'), Js('Velibor'), Js('Velichko'), Js('Veliko'), Js('Velim'), Js('Velin'), Js('Velis'), Js('Velizar'), Js('Veljko'), Js('Velko'), Js('Velousek'), Js('Vences'), Js('Venousek'), Js('Ventses'), Js('Ventsis'), Js('Veran'), Js('Veselin'), Js('Veselko'), Js('Vesselin'), Js('Vidos'), Js('Vihren'), Js('Vises'), Js('Vitom'), Js('Vjekos'), Js('Vjences'), Js('Vjeran'), Js('Vlad'), Js('Vlade'), Js('Vladico'), Js('Vladim'), Js('Vladis'), Js('Vlado'), Js('Vlastim'), Js('Vlastimil'), Js('Vlatko'), Js('Vojis'), Js('Vojkan'), Js('Vojm'), Js('Vojmil'), Js('Vojnom'), Js('Vojto'), Js('Vojtech'), Js('Vojteh'), Js('Vojtik'), Js('Vojtisek'), Js('Volen'), Js('Vsevolod'), Js('Vukosav'), Js('Vukoto'), Js('Vuksan'), Js('Vuksho'), Js('Vyaches'), Js('Wenzel'), Js('Wies'), Js('Wladys'), Js('Wojs'), Js('Wojtek'), Js('Wszebor'), Js('Yakov'), Js('Yaros'), Js('Yasen'), Js('Yavor'), Js('Zan'), Js('Zarko'), Js('Zawiszo'), Js('Zelek'), Js('Zelik'), Js('Zelim'), Js('Zelis'), Js('Zeljko'), Js('Zelousek'), Js('Zhelyazko'), Js('Zhivko'), Js('Ziemowit'), Js('Zitek'), Js('Zitom'), Js('Zitousek'), Js('Zivadin'), Js('Zivan'), Js('Zivanek'), Js('Zivek'), Js('Zivko'), Js('Zivojin'), Js('Zivorad'), Js('Zivoto'), Js('Zlatan'), Js('Zlatek'), Js('Zlaticek'), Js('Zlatik'), Js('Zlatko'), Js('Zlatom'), Js('Zlatousek'), Js('Zoran'), Js('Zoris'), Js('Zrinko'), Js('Zrinos'), Js('Zvezdan'), Js('Zvonim')]))
var.put('nm2', Js([Js('Alena'), Js('Alexi'), Js('Alina'), Js('Anca'), Js('Ania'), Js('Baritza'), Js('Bela'), Js('Beloslava'), Js('Berislava'), Js('Beyla'), Js('Biljana'), Js('Bilyana'), Js('Bisera'), Js('Biserka'), Js('Bistra'), Js('Blaga'), Js('Blagica'), Js('Blaguna'), Js('Bogdana'), Js('Bogna'), Js('Bojana'), Js('Bojka'), Js('Bolena'), Js('Bolerka'), Js('Boriana'), Js('Borka'), Js('Boyana'), Js('Boyka'), Js('Boza'), Js('Bozana'), Js('Bozena'), Js('Bozhana'), Js('Bozica'), Js('Bozka'), Js('Brana'), Js('Branka'), Js('Bretka'), Js('Brona'), Js('Bronicka'), Js('Bronka'), Js('Buga'), Js('Caterina'), Js('Cedna'), Js('Chesna'), Js('Chessa'), Js('Cvetka'), Js('Cvijeta'), Js('Cvita'), Js('Dana'), Js('Danica'), Js('Danika'), Js('Danitza'), Js('Danka'), Js('Dara'), Js('Daria'), Js('Darina'), Js('Darka'), Js('Darva'), Js('Davorka'), Js('Dejana'), Js('Denica'), Js('Desa'), Js('Desislava'), Js('Divna'), Js('Dobra'), Js('Dobrali'), Js('Dragana'), Js('Dragica'), Js('Draha'), Js('Draza'), Js('Drazenka'), Js('Dubravka'), Js('Dunja'), Js('Dunya'), Js('Dusa'), Js('Dusana'), Js('Duscha'), Js('Dusicka'), Js('Duska'), Js('Elina'), Js('Elka'), Js('Elya'), Js('Evelina'), Js('Evonnia'), Js('Gorana'), Js('Goranka'), Js('Grozda'), Js('Hrvatina'), Js('Hrvoja'), Js('Hrvojka'), Js('Idania'), Js('Irina'), Js('Iryna'), Js('Iskra'), Js('Iva'), Js('Ivana'), Js('Jadrana'), Js('Jadranka'), Js('Jalena'), Js('Jana'), Js('Janika'), Js('Janina'), Js('Janitza'), Js('Jarka'), Js('Jarmila'), Js('Jasenka'), Js('Jasna'), Js('Jelena'), Js('Jitka'), Js('Jola'), Js('Jolanda'), Js('Jovana'), Js('Jovanna'), Js('Kalina'), Js('Katia'), Js('Kisha'), Js('Kolina'), Js('Kveta'), Js('Kvetka'), Js('Kvetuska'), Js('Lada'), Js('Lana'), Js('Larya'), Js('Lenka'), Js('Liba'), Js('Lida'), Js('Lidka'), Js('Lonna'), Js('Luba'), Js('Lubena'), Js('Lubina'), Js('Lubka'), Js('Luka'), Js('Lumina'), Js('Lyuba'), Js('Malina'), Js('Mara'), Js('Marija'), Js('Marina'), Js('Marta'), Js('Marzanna'), Js('Masha'), Js('Maslinka'), Js('Mateja'), Js('Mecka'), Js('Melina'), Js('Merana'), Js('Miglena'), Js('Mila'), Js('Miladena'), Js('Miladka'), Js('Milana'), Js('Milanka'), Js('Milena'), Js('Milenka'), Js('Milica'), Js('Militsa'), Js('Milja'), Js('Miljana'), Js('Miljenka'), Js('Milka'), Js('Miluska'), Js('Mira'), Js('Mircea'), Js('Miriana'), Js('Mirjana'), Js('Mirka'), Js('Mirna'), Js('Miruna'), Js('Miruska'), Js('Mislava'), Js('Mojmira'), Js('Mora'), Js('Morana'), Js('Nada'), Js('Nadia'), Js('Natalya'), Js('Natashia'), Js('Navenka'), Js('Neda'), Js('Nedda'), Js('Nedelya'), Js('Neva'), Js('Nevena'), Js('Nevenka'), Js('Nika'), Js('Oksana'), Js('Olena'), Js('Olga'), Js('Olya'), Js('Ona'), Js('Panya'), Js('Probka'), Js('Rada'), Js('Radka'), Js('Raina'), Js('Raja'), Js('Rajana'), Js('Rajka'), Js('Ralica'), Js('Ranka'), Js('Ratka'), Js('Rosica'), Js('Rosta'), Js('Rumena'), Js('Rumiana'), Js('Ruza'), Js('Ruzica'), Js('Sana'), Js('Sanya'), Js('Senka'), Js('Slavica'), Js('Slavina'), Js('Slavka'), Js('Snezana'), Js('Snjeska'), Js('Sobena'), Js('Sobeska'), Js('Sonia'), Js('Spasena'), Js('Stana'), Js('Stojana'), Js('Sveta'), Js('Svetla'), Js('Svilena'), Js('Tanya'), Js('Tara'), Js('Tasya'), Js('Taya'), Js('Tesla'), Js('Tihana'), Js('Triska'), Js('Vaclava'), Js('Valeska'), Js('Vanya'), Js('Varvara'), Js('Vedrana'), Js('Vela'), Js('Velika'), Js('Velina'), Js('Velinka'), Js('Velka'), Js('Vena'), Js('Venka'), Js('Vera'), Js('Verka'), Js('Vesela'), Js('Vesna'), Js('Viara'), Js('Vida'), Js('Vierka'), Js('Vihra'), Js('Vlasta'), Js('Vlatka'), Js('Yanka'), Js('Yeva'), Js('Yuliana'), Js('Zhivka'), Js('Zitka'), Js('Ziva'), Js('Zivka'), Js('Zlata'), Js('Zoila'), Js('Zoja'), Js('Zora'), Js('Zorana'), Js('Zorica'), Js('Zorina'), Js('Zorka'), Js('Zrina'), Js('Zrinka'), Js('Zuzana'), Js('Zvonka'), Js('Zwisa')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('t'), Js('v')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('ie'), Js('y'), Js('ui'), Js('ou'), Js('ee'), Js('ei'), Js('ia')]))
var.put('nm5', Js([Js('b'), Js('bk'), Js('c'), Js('ch'), Js('d'), Js('dn'), Js('fk'), Js('g'), Js('h'), Js('hm'), Js('j'), Js('k'), Js('l'), Js('lg'), Js('ll'), Js('lm'), Js('m'), Js('n'), Js('nd'), Js('nk'), Js('nt'), Js('r'), Js('rb'), Js('rg'), Js('rk'), Js('rl'), Js('rn'), Js('rp'), Js('rsh'), Js('rt'), Js('s'), Js('sk'), Js('st'), Js('tr'), Js('tv'), Js('tz'), Js('v'), Js('vc'), Js('vk'), Js('vr'), Js('vsk'), Js('w'), Js('wk'), Js('z'), Js('zl'), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v'), Js('z'), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v'), Js('z'), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v'), Js('z'), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('c'), Js('ch'), Js('cz'), Js('k'), Js('l'), Js('ll'), Js('n'), Js('rz'), Js('s'), Js('ts'), Js('tz'), Js('v'), Js('w')]))
pass
pass


# Add lib to the module scope
wildstarMordesh = var.to_python()