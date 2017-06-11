__all__ = ['serbianNames']

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
    var.put('nm1', Js([Js('Časlav'), Js('Čedomir'), Js('Đoko'), Js('Đorđe'), Js('Đorđije'), Js('Đurađ'), Js('Đura'), Js('Đuro'), Js('Žarko'), Js('Željko'), Js('Živan'), Js('Živko'), Js('Živojin'), Js('Živorad'), Js('Života'), Js('Aca'), Js('Adam'), Js('Aleksa'), Js('Aleksandar'), Js('Anastasije'), Js('Andrej'), Js('Andrija'), Js('Arsenije'), Js('Atanasije'), Js('Avram'), Js('Berislav'), Js('Blagoje'), Js('Boško'), Js('Boža'), Js('Božidar'), Js('Boban'), Js('Bogdan'), Js('Bogoljub'), Js('Bojan'), Js('Boris'), Js('Borislav'), Js('Borivoje'), Js('Borjan'), Js('Braco'), Js('Brajan'), Js('Brajko'), Js('Branimir'), Js('Branislav'), Js('Branko'), Js('Bratislav'), Js('Budimir'), Js('Cvetko'), Js('Cvijetin'), Js('Dabiživ'), Js('Dalibor'), Js('Damir'), Js('Damjan'), Js('Danijel'), Js('Danilo'), Js('Danko'), Js('Darko'), Js('David'), Js('Davor'), Js('Dejan'), Js('Desimir'), Js('Dimitrije'), Js('Dobrivoje'), Js('Dobroslav'), Js('Draško'), Js('Dražen'), Js('Dragan'), Js('Dragiša'), Js('Drago'), Js('Dragoje'), Js('Dragoljub'), Js('Dragomir'), Js('Dragoslav'), Js('Dragutin'), Js('Dušan'), Js('Dubravko'), Js('Emilijan'), Js('Filip'), Js('Filotije'), Js('Gabrijel'), Js('Gavrilo'), Js('Gligorije'), Js('Gojko'), Js('Goran'), Js('Gordan'), Js('Grgur'), Js('Grigorije'), Js('Hvalimir'), Js('Igor'), Js('Ilarion'), Js('Ilija'), Js('Ingwar'), Js('Ivan'), Js('Ivica'), Js('Jakov'), Js('Janko'), Js('Jezdimir'), Js('Jovan'), Js('Jugoslav'), Js('Kalinik'), Js('Konstantin'), Js('Kosta'), Js('Kostadin'), Js('Kristijan'), Js('Krsto'), Js('Kuzman'), Js('Lazar'), Js('Lješ'), Js('Ljuba'), Js('Ljubiša'), Js('Ljubisav'), Js('Ljubivoje'), Js('Ljubomir'), Js('Lubomir'), Js('Luka'), Js('Marinko'), Js('Marko'), Js('Matija'), Js('Matko'), Js('Miša'), Js('Miško'), Js('Mihailo'), Js('Mihajlo'), Js('Mijat'), Js('Mika'), Js('Mikica'), Js('Miladin'), Js('Milan'), Js('Milanko'), Js('Milenko'), Js('Mileta'), Js('Milić'), Js('Milivoj'), Js('Milivoje'), Js('Miljan'), Js('Miljko'), Js('Milko'), Js('Miloš'), Js('Miloje'), Js('Milomir'), Js('Milorad'), Js('Milovan'), Js('Milutin'), Js('Miodrag'), Js('Miomir'), Js('Miran'), Js('Mirko'), Js('Miroslav'), Js('Mitar'), Js('Mladen'), Js('Mojsije'), Js('Momčilo'), Js('Momir'), Js('Nebojša'), Js('Nedeljko'), Js('Nemanja'), Js('Nenad'), Js('Neven'), Js('Nikša'), Js('Nikola'), Js('Novak'), Js('Obrad'), Js('Obren'), Js('Ognjen'), Js('Pavle'), Js('Pera'), Js('Petar'), Js('Predimir'), Js('Predrag'), Js('Pribislav'), Js('Raško'), Js('Radenko'), Js('Radič'), Js('Radiša'), Js('Radivoje'), Js('Radmilo'), Js('Radoš'), Js('Radoje'), Js('Radojko'), Js('Radoman'), Js('Radomir'), Js('Radonja'), Js('Radoslav'), Js('Radovan'), Js('Radul'), Js('Rajko'), Js('Ranko'), Js('Rastko'), Js('Ratimir'), Js('Ratko'), Js('Risto'), Js('Saša'), Js('Sava'), Js('Savatije'), Js('Sergej'), Js('Simo'), Js('Siniša'), Js('Slaven'), Js('Slaviša'), Js('Slavko'), Js('Slavoljub'), Js('Slavomir'), Js('Slobodan'), Js('Spasoje'), Js('Srđan'), Js('Srećko'), Js('Sredoje'), Js('Sreten'), Js('Sretomir'), Js('Staniša'), Js('Stanimir'), Js('Stanislav'), Js('Stanko'), Js('Stanoje'), Js('Stefan'), Js('Stevan'), Js('Stojan'), Js('Stracimir'), Js('Strahinja'), Js('Svetislav'), Js('Svetozar'), Js('Tadija'), Js('Teodor'), Js('Teodosije'), Js('Tihomir'), Js('Todor'), Js('Toma'), Js('Tomislav'), Js('Uroš'), Js('Vasilije'), Js('Vasko'), Js('Velibor'), Js('Velichko'), Js('Velimir'), Js('Velizar'), Js('Veljko'), Js('Veselin'), Js('Višeslav'), Js('Vidak'), Js('Vidoje'), Js('Vikentije'), Js('Vitomir'), Js('Vlada'), Js('Vladan'), Js('Vladeta'), Js('Vladimir'), Js('Vladislav'), Js('Vlado'), Js('Vlatko'), Js('Vojin'), Js('Vojislav'), Js('Vojkan'), Js('Vujadin'), Js('Vuk'), Js('Vukašin'), Js('Vukajlo'), Js('Vukan'), Js('Vukmir'), Js('Vukota'), Js('Vuksan'), Js('Zdeslav'), Js('Zdravko'), Js('Zlatan'), Js('Zlatko'), Js('Zoran'), Js('Zvezdan'), Js('Zvonimir'), Js('Zvonko')]))
    var.put('nm2', Js([Js('Đurica'), Js('Žaklina'), Js('Adrijana'), Js('Aleksandra'), Js('Amina'), Js('Anđela'), Js('Ana'), Js('Anastasija'), Js('Andrea'), Js('Andrijana'), Js('Anica'), Js('Anja'), Js('Anka'), Js('Biljana'), Js('Blagica'), Js('Bobana'), Js('Bogdana'), Js('Bojana'), Js('Bora'), Js('Borka'), Js('Bosiljka'), Js('Branka'), Js('Dajana'), Js('Daliborka'), Js('Damjanka'), Js('Dana'), Js('Danica'), Js('Danijela'), Js('Danka'), Js('Darija'), Js('Darina'), Js('Darinka'), Js('Dejana'), Js('Desanka'), Js('Dijana'), Js('Divna'), Js('Dobrica'), Js('Dobrila'), Js('DoroteaLalić'), Js('Draga'), Js('Dragana'), Js('Dragica'), Js('Draginja'), Js('Dušanka'), Js('Dušica'), Js('Duška'), Js('Dubravka'), Js('Dunja'), Js('Elena'), Js('Emilija'), Js('Gabrijela'), Js('Gorana'), Js('Gordana'), Js('Hana'), Js('Ivana'), Js('Ivanka'), Js('Jadranka'), Js('Jana'), Js('Jasmina'), Js('Jasna'), Js('Jelena'), Js('Jovana'), Js('Jovanka'), Js('Katarina'), Js('Kristina'), Js('Ksenija'), Js('Lada'), Js('Leposava'), Js('Lidija'), Js('Ljiljana'), Js('Ljuba'), Js('Ljubica'), Js('Ljubinka'), Js('Ludmila'), Js('Magdalena'), Js('Maja'), Js('Malina'), Js('Marica'), Js('Marija'), Js('Marina'), Js('Mila'), Js('Milana'), Js('Milanka'), Js('Milena'), Js('Milica'), Js('Miljana'), Js('Milka'), Js('Mina'), Js('Minna'), Js('Mira'), Js('Mirjana'), Js('Mirka'), Js('Mirna'), Js('Nađa'), Js('Nada'), Js('Nadezhda'), Js('Nastja'), Js('Nataša'), Js('Natalija'), Js('Natasa'), Js('Neda'), Js('Nevena'), Js('Nikolina'), Js('Nina'), Js('Olga'), Js('Peruna'), Js('Petra'), Js('Petrija'), Js('Radana'), Js('Radina'), Js('Radmila'), Js('Radojka'), Js('Rakita'), Js('Renja'), Js('Roksana'), Js('Ruža'), Js('Ružica'), Js('Sandra'), Js('Sanja'), Js('Sara'), Js('Sava'), Js('Simonida'), Js('Slađana'), Js('Slava'), Js('Slavica'), Js('Slavka'), Js('Slobodanka'), Js('Smiljana'), Js('Snežana'), Js('Sofija'), Js('Sonja'), Js('Sonya'), Js('Stanislava'), Js('Stefana'), Js('Steva'), Js('Stojanka'), Js('Suzana'), Js('Svetlana'), Js('Tamara'), Js('Tanja'), Js('Tatjana'), Js('Teodora'), Js('Tijana'), Js('Una'), Js('Varadinka'), Js('Vera'), Js('Verica'), Js('Veselinka'), Js('Vesna'), Js('Vida'), Js('Violeta'), Js('Vladana'), Js('Vlatka'), Js('Vojislava'), Js('Vujica'), Js('Vukica'), Js('Zeljana'), Js('Zlata'), Js('Zora'), Js('Zorana'), Js('Zorica'), Js('Zorka')]))
    var.put('nm3', Js([Js('Čarapić'), Js('Đorđević'), Js('Šaponjić'), Js('Šiljan'), Js('Živanović'), Js('Živić'), Js('Aleksić'), Js('Andrić'), Js('Antić'), Js('Arsić'), Js('Bačić'), Js('Blagojević'), Js('Bojanić'), Js('Bojević'), Js('Borisavljević'), Js('Borisov'), Js('Brđanin'), Js('Brkić'), Js('Cvetković'), Js('Dapčević'), Js('Darković'), Js('Despotović'), Js('Ević'), Js('Filipović'), Js('Gavrilović'), Js('Georgijević'), Js('Gišić'), Js('Gojković'), Js('Golubović'), Js('Grgurović'), Js('Hristov'), Js('Ignjatović'), Js('Janketić'), Js('Janković'), Js('Jelić'), Js('Jocić'), Js('Jovanović'), Js('Jović'), Js('Karanović'), Js('Kostić'), Js('Krsmanović'), Js('Krstić'), Js('Kuzmanović'), Js('Lazarević'), Js('Lazić'), Js('Mandić'), Js('Marinković'), Js('Marković'), Js('Mijatović'), Js('Moldovan'), Js('Nanuševski'), Js('Nastasić'), Js('Nešić'), Js('Nedeljković'), Js('Nestorovski'), Js('Nikolić'), Js('Novaković'), Js('Obradović'), Js('Pajić'), Js('Pap'), Js('Pavlović'), Js('Pešić'), Js('Pejakovski'), Js('Pejić'), Js('Petrović'), Js('Popadić'), Js('Popović'), Js('Rajković'), Js('Rakočević'), Js('Ristić'), Js('Ristovski'), Js('Sandić'), Js('Savić'), Js('Savićević'), Js('Simić'), Js('Stefanović'), Js('Stevanović'), Js('Tadić'), Js('Tanacković'), Js('Tasić'), Js('Todorović'), Js('Tomić'), Js('Trkulja'), Js('Ugljanin'), Js('Urošević'), Js('Vasić'), Js('Vasiljević'), Js('Velimirović'), Js('Vladić'), Js('Vladimirović'), Js('Vlahović'), Js('Vujić'), Js('Vukašinović'), Js('Vukomanović'), Js('Zebić'), Js('Zorić')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
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
serbianNames = var.to_python()