__all__ = ['dwarfWowNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', (((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Am'), Js('Arm'), Js('Bal'), Js('Ban'), Js('Bar'), Js('Bel'), Js('Beng'), Js('Bhal'), Js('Bhar'), Js('Bhel'), Js('Bram'), Js('Bran'), Js('Brom'), Js('Brum'), Js('Bun'), Js('Dal'), Js('Dar'), Js('Dol'), Js('Dram'), Js('Drom'), Js('Drum'), Js('Dul'), Js('Em'), Js('Erm'), Js('Gal'), Js('Gar'), Js('Ger'), Js('Gim'), Js('Gir'), Js('Gol'), Js('Gor'), Js('Gral'), Js('Gram'), Js('Gran'), Js('Grem'), Js('Gren'), Js('Gril'), Js('Grim'), Js('Grom'), Js('Grul'), Js('Grum'), Js('Grun'), Js('Gry'), Js('Gul'), Js('Har'), Js('Hjal'), Js('Hjol'), Js('Hjul'), Js('Hor'), Js('Hulf'), Js('Hur'), Js('Irom'), Js('Iron'), Js('Jar'), Js('Jor'), Js('Kar'), Js('Khar'), Js('Kram'), Js('Krom'), Js('Krum'), Js('Mag'), Js('Mal'), Js('Mel'), Js('Muir'), Js('Mur'), Js('Ol'), Js('Orim'), Js('Orm'), Js('Rag'), Js('Reg'), Js('Rot'), Js('Shel'), Js('Sog'), Js('Sogn'), Js('Sug'), Js('Sugn'), Js('Thal'), Js('Thar'), Js('Thel'), Js('Ther'), Js('Tho'), Js('Thor'), Js('Thul'), Js('Thur'), Js('Thy'), Js('Tor'), Js('Ty'), Js('Um'), Js('Urm')]))
var.put('nm2', Js([Js('o'), Js('a'), Js('u'), Js('i'), Js('ia'), Js('iu'), Js('ou'), Js('ua'), Js('ah'), Js('uh'), Js('oh'), Js('ihr'), Js('ahr'), Js('ohr'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm3', Js([Js('brek'), Js('dahr'), Js('dan'), Js('dar'), Js('dir'), Js('dohr'), Js('donore'), Js('dor'), Js('dram'), Js('dren'), Js('drom'), Js('drum'), Js('drus'), Js('duhr'), Js('dur'), Js('dus'), Js('edon'), Js('g'), Js('garn'), Js('gas'), Js('gorn'), Js('gos'), Js('gram'), Js('gran'), Js('grom'), Js('gron'), Js('grum'), Js('grun'), Js('gurn'), Js('gus'), Js('han'), Js('hann'), Js('hun'), Js('hunn'), Js('iggs'), Js('kahm'), Js('kam'), Js('kohm'), Js('kom'), Js('kuhm'), Js('kum'), Js('kyl'), Js('m'), Js('man'), Js('mand'), Js('mar'), Js('mek'), Js('miir'), Js('min'), Js('mir'), Js('mond'), Js('mor'), Js('mun'), Js('mund'), Js('mur'), Js('mus'), Js('myl'), Js('myr'), Js('n'), Js('nam'), Js('nar'), Js('ni'), Js('nik'), Js('nir'), Js('nom'), Js('nu'), Js('num'), Js('nur'), Js('nus'), Js('nyl'), Js('ram'), Js('ren'), Js('rig'), Js('rigg'), Js('rim'), Js('rom'), Js('ron'), Js('rum'), Js('rus'), Js('ruuk'), Js('ryl'), Js('tharm'), Js('tharn'), Js('thorm'), Js('thorn'), Js('thran'), Js('throm'), Js('thron'), Js('thrum'), Js('thrun'), Js('thurm'), Js('thurn'), Js('thus'), Js('yth')]))
var.put('nm4', Js([Js('Ang'), Js('Angr'), Js('Bel'), Js('Bell'), Js('Bon'), Js('Bonn'), Js('Braen'), Js('Bral'), Js('Brall'), Js('Bran'), Js('Bril'), Js('Brill'), Js('Bren'), Js('Bret'), Js('Brett'), Js('Brol'), Js('Broll'), Js('Bron'), Js('Brul'), Js('Brull'), Js('Bryl'), Js('Bryll'), Js('Bryn'), Js('Bryt'), Js('Byl'), Js('Byll'), Js('Daer'), Js('Dear'), Js('Dim'), Js('Ed'), Js('Ein'), Js('Eyn'), Js('Gwan'), Js('Gwen'), Js('Gwin'), Js('Gwyn'), Js('Gim'), Js('Gym'), Js('Ing'), Js('Ingr'), Js('Jen'), Js('Jenn'), Js('Jin'), Js('Jinn'), Js('Jyn'), Js('Jynn'), Js('Kait'), Js('Kar'), Js('Kat'), Js('Ket'), Js('Las'), Js('Lass'), Js('Les'), Js('Less'), Js('Lyes'), Js('Lys'), Js('Lyss'), Js('Maev'), Js('Mar'), Js('Mis'), Js('Mist'), Js('Myr'), Js('Mys'), Js('Myss'), Js('Myst'), Js('Nal'), Js('Nas'), Js('Nass'), Js('Nes'), Js('Ness'), Js('Nis'), Js('Niss'), Js('Nys'), Js('Nyss'), Js('Ong'), Js('Ongr'), Js('Ov'), Js('Raen'), Js('Ran'), Js('Red'), Js('Reyn'), Js('Run'), Js('Ryn'), Js('Sar'), Js('Sol'), Js('Tas'), Js('Taz'), Js('Tis'), Js('Tish'), Js('Tiz'), Js('Tys'), Js('Tysh'), Js('Ung'), Js('Ungr')]))
var.put('nm5', Js([Js('o'), Js('a'), Js('i'), Js('ia'), Js('io'), Js('ou'), Js('ua'), Js('ah'), Js('um'), Js('oh'), Js('ir'), Js('ar'), Js('or'), Js('un'), Js('eo'), Js('ea'), Js('in'), Js('im'), Js('an'), Js('am'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('leil'), Js('nar'), Js('nyl'), Js('myl'), Js('lyl'), Js('dyl'), Js('ris'), Js('ras'), Js('res'), Js('ros'), Js('win'), Js('wyn'), Js('waen'), Js('whin'), Js('whyn'), Js('whaen'), Js('tin'), Js('tyn'), Js('lyn'), Js('lin'), Js('lynn'), Js('linn'), Js('wynn'), Js('va'), Js('van'), Js('rin'), Js('ryn'), Js('ryl'), Js('nas'), Js('nan'), Js('ria'), Js('nia'), Js('ri'), Js('rip'), Js('nip'), Js('dora'), Js('leen'), Js('len'), Js('ma'), Js('la'), Js('mora'), Js('mura'), Js('mera'), Js('nura'), Js('nera'), Js('nora'), Js('glia'), Js('glian'), Js('giel'), Js('thiel'), Js('diel'), Js('thel'), Js('nis'), Js('niss'), Js('nys'), Js('nyss')]))
var.put('nm7', Js([Js('Barley'), Js('Battle'), Js('Black'), Js('Bone'), Js('Boulder'), Js('Bright'), Js('Bronze'), Js('Cask'), Js('Cliff'), Js('Cold'), Js('Crag'), Js('Dark'), Js('Deep'), Js('Dirge'), Js('Doom'), Js('Fire'), Js('Flint'), Js('Frost'), Js('Fuse'), Js('Gold'), Js('Hammer'), Js('High'), Js('Iron'), Js('Long'), Js('Marble'), Js('Molten'), Js('Mountain'), Js('Pale'), Js('Red'), Js('Slate'), Js('Snow'), Js('Steel'), Js('Stern'), Js('Stone'), Js('Storm'), Js('Stout'), Js('Thunder')]))
var.put('nm8', Js([Js('arm'), Js('axe'), Js('beard'), Js('belly'), Js('blade'), Js('braid'), Js('branch'), Js('brand'), Js('breaker'), Js('brew'), Js('brow'), Js('crag'), Js('dust'), Js('fall'), Js('fist'), Js('flayer'), Js('forge'), Js('fury'), Js('gem'), Js('grip'), Js('hammer'), Js('hand'), Js('helm'), Js('mane'), Js('mantle'), Js('ore'), Js('pike'), Js('river'), Js('roar'), Js('rock'), Js('shaper'), Js('shield'), Js('shout'), Js('steel'), Js('stone'), Js('toe')]))
pass
pass


# Add lib to the module scope
dwarfWowNames = var.to_python()