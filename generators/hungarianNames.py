__all__ = ['hungarianNames']

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
    var.put('nm1', Js([Js('Ábel'), Js('Ádám'), Js('Ákos'), Js('Ármin'), Js('Áron'), Js('Árpád'), Js('Adrián'), Js('Albert'), Js('Alex'), Js('Alexander'), Js('András'), Js('Antal'), Js('Arnold'), Js('Attila'), Js('Bálint'), Js('Béla'), Js('Balázs'), Js('Barna'), Js('Barnabás'), Js('Bence'), Js('Bendegúz'), Js('Benedek'), Js('Benjámin'), Js('Benjamin'), Js('Bertalan'), Js('Boldizsár'), Js('Botond'), Js('Csaba'), Js('Csanád'), Js('Csongor'), Js('Dániel'), Js('Dávid'), Js('Dénes'), Js('Dezső'), Js('Dominik'), Js('Domonkos'), Js('Donát'), Js('Endre'), Js('Erik'), Js('Ferenc'), Js('Flórián'), Js('Gábor'), Js('Géza'), Js('Gergő'), Js('Gergely'), Js('György'), Js('Gyula'), Js('Henrik'), Js('Imre'), Js('István'), Js('János'), Js('József'), Js('Jakab'), Js('Kálmán'), Js('Károly'), Js('Kevin'), Js('Kornél'), Js('Kristóf'), Js('Krisztián'), Js('Krisztofer'), Js('László'), Js('Lajos'), Js('Levente'), Js('Márió'), Js('Márkó'), Js('Márk'), Js('Márton'), Js('Máté'), Js('Mátyás'), Js('Marcell'), Js('Martin'), Js('Mihály'), Js('Miklós'), Js('Milán'), Js('Nándor'), Js('Noel'), Js('Norbert'), Js('Olivér'), Js('Pál'), Js('Péter'), Js('Patrik'), Js('Róbert'), Js('Rajmund'), Js('Renátó'), Js('Richárd'), Js('Roland'), Js('Rudolf'), Js('Sándor'), Js('Soma'), Js('Szabolcs'), Js('Szilárd'), Js('Szilveszter'), Js('Tamás'), Js('Tibor'), Js('Valentin'), Js('Viktor'), Js('Vilmos'), Js('Vince'), Js('Zalán'), Js('Zoltán'), Js('Zsolt'), Js('Zsombor')]))
    var.put('nm2', Js([Js('Ágnes'), Js('Éva'), Js('Adél'), Js('Adrienn'), Js('Alexandra'), Js('Andrea'), Js('Anett'), Js('Anikó'), Js('Anita'), Js('Anna'), Js('Annamária'), Js('Barbara'), Js('Beatrix'), Js('Bernadett'), Js('Bettina'), Js('Bianka'), Js('Blanka'), Js('Boglárka'), Js('Borbála'), Js('Brigitta'), Js('Cintia'), Js('Csenge'), Js('Csilla'), Js('Dóra'), Js('Dalma'), Js('Daniella'), Js('Diána'), Js('Dominika'), Js('Dorina'), Js('Dorina Mária'), Js('Dorka'), Js('Dorottya'), Js('Dzsenifer'), Js('Edina'), Js('Elizabet'), Js('Emese'), Js('Enikő'), Js('Erika'), Js('Erzsébet'), Js('Eszter'), Js('Evelin'), Js('Fanni'), Js('Flóra'), Js('Fruzsina'), Js('Gabriella'), Js('Georgina'), Js('Gréta'), Js('Hajnalka'), Js('Hanna'), Js('Henrietta'), Js('Ildikó'), Js('Ivett'), Js('Izabella'), Js('Júlia'), Js('Judit'), Js('Kíra'), Js('Kamilla'), Js('Kata'), Js('Katalin'), Js('Kinga'), Js('Kitti'), Js('Klaudia'), Js('Krisztina'), Js('Laura'), Js('Liliána'), Js('Lili'), Js('Lilla'), Js('Luca'), Js('Mária'), Js('Mónika'), Js('Martina'), Js('Melinda'), Js('Mercédesz'), Js('Nóra'), Js('Natália'), Js('Nikolett'), Js('Nikoletta'), Js('Noémi'), Js('Orsolya'), Js('Panna'), Js('Patrícia'), Js('Petra'), Js('Réka'), Js('Ramóna'), Js('Rebeka'), Js('Regina'), Js('Renáta'), Js('Sára'), Js('Szabina'), Js('Szilvia'), Js('Szimonetta'), Js('Tímea'), Js('Tünde'), Js('Tamara'), Js('Vanda'), Js('Vanessza'), Js('Veronika'), Js('Viktória'), Js('Virág'), Js('Vivien'), Js('Zita'), Js('Zsófia'), Js('Zsanett'), Js('Zsuzsanna')]))
    var.put('nm3', Js([Js('Antal'), Js('Bálint'), Js('Bakos'), Js('Miksa'), Js('Csatár'), Js('Bács'), Js('Balázs'), Js('Apród'), Js('Balla'), Js('Balog'), Js('Balogh'), Js('Barna'), Js('Barta'), Js('Biró'), Js('Bodnár'), Js('Bogdán'), Js('Bognár'), Js('Borbély'), Js('Boros'), Js('Budai'), Js('Egyed'), Js('Csonka'), Js('Deák'), Js('Dobos'), Js('Dudás'), Js('Fábián'), Js('Fülöp'), Js('Faragó'), Js('Farkas'), Js('Fazekas'), Js('Fehér'), Js('Fekete'), Js('Fodor'), Js('Gál'), Js('Gáspár'), Js('Gulyás'), Js('Hajdú'), Js('Halász'), Js('Hegedüs'), Js('Horváth'), Js('Illés'), Js('Jónás'), Js('Jakab'), Js('Juhász'), Js('Katona'), Js('Kelemen'), Js('Kerekes'), Js('Király'), Js('Kis'), Js('Kiss'), Js('Kocsis'), Js('Kovács'), Js('Kozma'), Js('László'), Js('Lakatos'), Js('Lengyel'), Js('Lukács'), Js('Márton'), Js('Máté'), Js('Mészáros'), Js('Magyar'), Js('Major'), Js('Mezei'), Js('Molnár'), Js('Németh'), Js('Nagy'), Js('Nemes'), Js('Novák'), Js('Oláh'), Js('Orbán'), Js('Orosz'), Js('Orsós'), Js('Pál'), Js('Pásztor'), Js('Péter'), Js('Pap'), Js('Papp'), Js('Vászoly'), Js('Pataki'), Js('Pintér'), Js('Rácz'), Js('Sándor'), Js('Simon'), Js('Sípos'), Js('Soós'), Js('Somogyi'), Js('Székely'), Js('Surány'), Js('Szücs'), Js('Szabó'), Js('Kende'), Js('Szalai'), Js('Szekeres'), Js('Szilágyi'), Js('Szőke'), Js('Szűts'), Js('Tóth'), Js('Török'), Js('Takács'), Js('Tamás'), Js('Váradi'), Js('Kapolcs'), Js('Zobor'), Js('Vörös'), Js('Varga'), Js('Vass'), Js('Veres'), Js('Vincze'), Js('Virág')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm3').get(var.get('rnd2'))+Js(' '))+var.get('nm2').get(var.get('rnd'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm3').get(var.get('rnd2'))+Js(' '))+var.get('nm1').get(var.get('rnd'))))
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
hungarianNames = var.to_python()