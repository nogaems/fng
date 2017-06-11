__all__ = ['mutantSpecies']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('names', (Js('The ')+var.get('names1').get(var.get('rnd'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('names', (var.get('names2').get(var.get('rnd'))+var.get('names3').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    if (var.get('rnd3')>Js(64.0)):
                        var.put('rnd4', Js(0.0))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('names', ((((var.get('names4').get(var.get('rnd'))+var.get('names5').get(var.get('rnd2')))+var.get('names6').get(var.get('rnd3')))+var.get('names7').get(var.get('rnd4')))+var.get('names3').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Aberrations'), Js('Abnormalities'), Js('Invincible'), Js('Abominations'), Js('Anomalies'), Js('Blessed'), Js('Chosen Ones'), Js('Cleansed'), Js('Enigmas'), Js('Eternals'), Js('Freaks'), Js('Giants'), Js('Gifted'), Js('Horned Ones'), Js('Impure'), Js('Infected'), Js('Lost Ones'), Js('Lost Souls'), Js('Miracles'), Js('Monsters'), Js('Newmans'), Js('Paragons'), Js('Phantoms'), Js('Phoenixes'), Js('Stalkers'), Js('Tails'), Js('Walkers'), Js('Transparent'), Js('Translucent'), Js('Luminescent'), Js('Green Skins'), Js('Triclopses'), Js('Cyclopses'), Js('Beaks'), Js('Fins'), Js('Wings'), Js('Fangs'), Js('Claws'), Js('Pelts'), Js('Behemoths'), Js('Fiends'), Js('Savages'), Js('Unnaturals'), Js('Miscreants'), Js('Miscreations'), Js('Grotesque'), Js('Misshapen'), Js('Gills'), Js('Hellions'), Js('Horrors'), Js('Pincers'), Js('Eyeless'), Js('Faceless'), Js('Rock Skins'), Js('Leather Skins'), Js('Dwellers'), Js('Otherworldly'), Js('Forsaken'), Js('Upgraded'), Js('Beasts'), Js('Creatures'), Js('Missfits'), Js('Howlers'), Js('Scales'), Js('Scaled Ones'), Js('Tentacles'), Js('Tentacled'), Js('Silver Eyes'), Js('Burdened'), Js('Marked'), Js('Horns'), Js('Horned Ones'), Js('Maniacs'), Js('Bugs'), Js('Creeps'), Js('Sirens'), Js('Finned Ones'), Js('Fins'), Js('Bended'), Js('Four Legged'), Js('Quadrupeds'), Js('Decapeds'), Js('Armored'), Js('Blue Skins'), Js('Black Skins'), Js('Serpents'), Js('Arachnids'), Js('Arachnumans'), Js('Serpumans'), Js('Hogmen'), Js('Demons'), Js('Evolved'), Js('Devolved'), Js('Deviants'), Js('Perverse'), Js('Irregularities'), Js('Synthetics'), Js('Nonentities'), Js('Beings'), Js('Entities'), Js('Creatures'), Js('Critters'), Js('Seedlings'), Js('Shrubs'), Js('Weeds'), Js('Vines'), Js('Progressed'), Js('Aquatic'), Js('Aquas'), Js('Aerials'), Js('Avians'), Js('Aviumans'), Js('Transformed'), Js('Furs'), Js('Shells'), Js('Shelled Ones')]))
var.put('names2', Js([Js('Abna'), Js('Abno'), Js('Ani'), Js('Ano'), Js('Arach'), Js('Arthro'), Js('Ave'), Js('Avi'), Js('Barba'), Js('Bea'), Js('Beas'), Js('Behe'), Js('Bru'), Js('Canin'), Js('Car'), Js('Care'), Js('Carni'), Js('Chi'), Js('Chime'), Js('Chiro'), Js('Cla'), Js('Crea'), Js('Cree'), Js('Crit'), Js('Cro'), Js('Croco'), Js('Crus'), Js('Cryp'), Js('Dasy'), Js('Devi'), Js('Dice'), Js('Felin'), Js('Gas'), Js('Gil'), Js('Heli'), Js('Inno'), Js('Levi'), Js('Loxo'), Js('Lupu'), Js('Modi'), Js('Mus'), Js('Muscu'), Js('Mut'), Js('Nea'), Js('Neo'), Js('Pan'), Js('Permu'), Js('Prima'), Js('Probo'), Js('Psy'), Js('Rufu'), Js('Serpen'), Js('Strigi'), Js('Tigri'), Js('Ur'), Js('Ursi'), Js('Ver'), Js('Vermi'), Js('Vici'), Js('Vul')]))
var.put('names3', Js([Js('barias'), Js('bines'), Js('bites'), Js('crians'), Js('cries'), Js('crites'), Js('garians'), Js('garis'), Js('gees'), Js('gians'), Js('gites'), Js('narians'), Js('neans'), Js('nees'), Js('nians'), Js('nines'), Js('nirians'), Js('nites'), Js('ratis'), Js('rees'), Js('sees'), Js('sias'), Js('tarians'), Js('tasians'), Js('teans'), Js('tees'), Js('tians'), Js('tines'), Js('tirians'), Js('tites')]))
var.put('names4', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z')]))
var.put('names5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('names6', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names7', Js([Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
pass
pass


# Add lib to the module scope
mutantSpecies = var.to_python()