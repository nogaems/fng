__all__ = ['tuaregNames']

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
    var.registers(['nm1', 'nm2', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Abahag'), Js('Abidine'), Js('Aboura'), Js('Adebir'), Js('Aflan'), Js('Agag'), Js('Ahag'), Js('Ahmed'), Js('Ahmedu'), Js('Ahu'), Js('Aitarel'), Js('Akhemouk'), Js('Akhiou'), Js('Akorebi'), Js('Akrud'), Js('Alemhok'), Js('Allgoui'), Js('Amanrassa'), Js("Amar'l"), Js('Amastame'), Js('Amayas'), Js('Amder'), Js('Amellal'), Js('Amer'), Js('Amjer'), Js('Amma'), Js('Amoud'), Js('Anaba'), Js('Ansar'), Js('Aqqasen'), Js('Askiou'), Js('Attici'), Js('Aziouel'), Js('Baba'), Js('Badjhoud'), Js('Bay'), Js('Beh'), Js('Beketa'), Js('Bekkai'), Js('Biska'), Js('Bouhen'), Js('Brahim'), Js('Bubekir'), Js('Buzin'), Js('Chekkadh'), Js('Chikat'), Js('Danguchi'), Js('Echerif'), Js('Ehenkouen'), Js('Ehenu'), Js('El Boghari'), Js('El Hamous'), Js('El Hosseyni'), Js('El Khir'), Js('El Kounti'), Js('El Menir'), Js('El Mokhtar'), Js('El Mostafa'), Js('El Mouden'), Js('Elwafil'), Js('Goma'), Js('Hama'), Js('Heguir'), Js('Hosseyni'), Js('Howedi'), Js('Ibrahim'), Js('Ihemma'), Js('Ihemod'), Js('Iherhe'), Js('Ikemma'), Js('Ikhenoukhen'), Js('Iklan'), Js('Ilaman'), Js('Ilbak'), Js('Ilou'), Js('Kenan'), Js('Keneiss'), Js('Keradji'), Js('Khabte'), Js('Khebbi'), Js('Khelba'), Js('Khemidou'), Js('Khyar'), Js('Lamine'), Js('Louen'), Js('Louki'), Js('Makhia'), Js('Mama'), Js('Marli'), Js('Mellou'), Js('Meslar'), Js('Mohammed'), Js('Moussa'), Js('Musa'), Js('Okha'), Js('Othman'), Js('Ou-Fenait'), Js('Ould'), Js('Ourzig'), Js('Rali'), Js('Rezkou'), Js('Salah'), Js('Salla'), Js("Ser'ada"), Js('Sid Ahmed'), Js('Sidi'), Js('Sidi Mohammed'), Js('Souri'), Js('Tamaklast'), Js('Tinekerbas'), Js('Tissi'), Js('Uksem'), Js('Uray'), Js('Yakhia'), Js('Younes')]))
    var.put('nm2', Js([Js('Aisha'), Js('Amena'), Js('Baya'), Js('Bella'), Js('Dasha'), Js('Dassine'), Js('Demu'), Js('Dhabba'), Js('El Jamit'), Js('El Kubra'), Js('El Mamoum'), Js('Eljamit'), Js('Elkubra'), Js('Elmamoum'), Js('Essebet'), Js('Fadimata'), Js('Fatma'), Js('Feduda'), Js('Hadada'), Js('Hadeja'), Js('Hariza'), Js('Hashisha'), Js('Kahina'), Js('Kana'), Js('Katouh'), Js('Kella'), Js('Khaouila'), Js('Khatti'), Js('Kodda'), Js('Lalla'), Js('Lella'), Js('Lemtuna'), Js('Malla'), Js('Meriama'), Js('Mimi'), Js('Raeraou'), Js('Rahma'), Js('Rahmadu'), Js('Raisha'), Js('Ratma'), Js('Raysha'), Js('Rayshabu'), Js('Regida'), Js('Seda'), Js('Sekata'), Js('Shemama'), Js('Sherifa'), Js('Sheyma'), Js('Tabehaout'), Js("Taber'ourt"), Js('Tagouzamt'), Js('Tahat'), Js('Tahe'), Js('Tahenkot'), Js('Tahyart'), Js('Takama'), Js('Tamagit'), Js('Tamat'), Js('Tamerouelt'), Js('Tamu'), Js('Tandarine'), Js('Tanelhir'), Js('Tanermat'), Js('Tanloubouh'), Js("Tar'aoussit"), Js('Tebeshit'), Js('Tebubirt'), Js('Tekawilt'), Js('Tiguent'), Js('Tihit'), Js('Tinhert'), Js('Tinhinan'), Js('Tioueyin'), Js('Umeyda'), Js('Wertenezzu'), Js('Zahara')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' ult '))+var.get('nm1').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' ag '))+var.get('nm1').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm1').callprop('splice', var.get('rnd2'), Js(1.0))
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
tuaregNames = var.to_python()