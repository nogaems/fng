__all__ = ['gangNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
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
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (((((Js('The ')+var.get('nm1').get(var.get('rnd0')))+Js(' '))+var.get('nm2').get(var.get('rnd1')))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd0')))+Js(' '))+var.get('nm3').get(var.get('rnd1'))))
                else:
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', (Js('The ')+var.get('nm5').get(var.get('rnd0'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('azure'), Js('black'), Js('blue'), Js('brass'), Js('bronze'), Js('brown'), Js('cardinal'), Js('cobalt'), Js('copper'), Js('crimson'), Js('crystal'), Js('demon'), Js('denim'), Js('diamond'), Js('ebony'), Js('electric'), Js('emerald'), Js('fire'), Js('flame'), Js('gold'), Js('green'), Js('grey'), Js('grizzly'), Js('ice'), Js('ivory'), Js('jade'), Js('onyx'), Js('orange'), Js('red'), Js('royal'), Js('ruby'), Js('sanguine'), Js('sapphire'), Js('scarlet'), Js('thunder'), Js('violet'), Js('white'), Js('yellow'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('alien'), Js('alligator'), Js('angel'), Js('badger'), Js('banner'), Js('bat'), Js('bear'), Js('blood'), Js('blooddrop'), Js('blossom'), Js('boar'), Js('bull'), Js('bulldog'), Js('butterfly'), Js('chainsaw'), Js('cobra'), Js('coyote'), Js('crocodile'), Js('cross'), Js('crow'), Js('death'), Js('demon'), Js('devil'), Js('dragon'), Js('dragonfly'), Js('dragontooth'), Js('dwarf'), Js('eagle'), Js('elephant'), Js('enigma'), Js('fang'), Js('forsaken'), Js('ghost'), Js('gorilla'), Js('hand'), Js('hog'), Js('honey badger'), Js('horn'), Js('jackal'), Js('knife'), Js('knuckle'), Js('leopard'), Js('lily'), Js('lion'), Js('liontooth'), Js('mamba'), Js('mammoth'), Js('monkey'), Js('moth'), Js('needle'), Js('owl'), Js('phantom'), Js('pygmy'), Js('pincer'), Js('pistol'), Js('rat'), Js('raven'), Js('ravenclaw'), Js('razor'), Js('reaper'), Js('rebel'), Js('rider'), Js('rose'), Js('saber'), Js('sabortooth'), Js('serpent'), Js('shark'), Js('sharkfin'), Js('sharktooth'), Js('skeleton'), Js('skull'), Js('snake'), Js('spider'), Js('sword'), Js('tear'), Js('thorn'), Js('tiger'), Js('toad'), Js('troll'), Js('undead'), Js('viper'), Js('vulture'), Js('warthog'), Js('water'), Js('wolf'), Js('wolverine')]))
var.put('nm3', Js([Js('aliens'), Js('alligators'), Js('angels'), Js('badgers'), Js('bats'), Js('bears'), Js('blooddrops'), Js('bloods'), Js('blossoms'), Js('boars'), Js('bulldogs'), Js('bulls'), Js('butterflies'), Js('chainsaws'), Js('cobras'), Js('coyotes'), Js('crocs'), Js('crosses'), Js('crows'), Js('demons'), Js('devils'), Js('dragonflies'), Js('dragons'), Js('dwarves'), Js('eagles'), Js('elephants'), Js('enigmas'), Js('fangs'), Js('forsaken'), Js('ghosts'), Js('gorillas'), Js('growlers'), Js('hogs'), Js('honey badgers'), Js('horns'), Js('jackals'), Js('knives'), Js('knuckles'), Js('leopards'), Js('lilies'), Js('lions'), Js('mambas'), Js('mammoths'), Js('monkeys'), Js('moths'), Js('needles'), Js('owls'), Js('phantoms'), Js('pigmies'), Js('pillagers'), Js('pincers'), Js('pistols'), Js('plunderers'), Js('rats'), Js('ravenclaws'), Js('ravens'), Js('razors'), Js('reapers'), Js('rebels'), Js('riders'), Js('roses'), Js('sabors'), Js('seals'), Js('serpents'), Js('sharkfins'), Js('sharks'), Js('sharkteeth'), Js('skeletons'), Js('skulls'), Js('slicers'), Js('snakes'), Js('spiders'), Js('swords'), Js('takers'), Js('tears'), Js('thorns'), Js('tigers'), Js('toads'), Js('trolls'), Js('undead'), Js('vipers'), Js('vultures'), Js('warthogs'), Js('wolverines'), Js('wolves')]))
var.put('nm4', Js([Js('association'), Js('band'), Js('brotherhood'), Js('clan'), Js('company'), Js('crew'), Js('gang'), Js('posse'), Js('riders'), Js('soldiers'), Js('squad'), Js('syndicate'), Js('tribe')]))
var.put('nm5', Js([Js('abandoned'), Js('anarchists'), Js('anonymous'), Js('chargers'), Js('damnation'), Js('day walkers'), Js('dead eyes'), Js('destroyers'), Js('disciples'), Js('doom bringers'), Js('dreamers'), Js('liberated'), Js('liberation front'), Js('empty eyes'), Js('eternals'), Js('faceless ones'), Js('fallen angels'), Js('forsaken'), Js('grim reapers'), Js('hopeless'), Js('hopeless ones'), Js('hunters'), Js('idealists'), Js('immortals'), Js('invincibles'), Js('invisibles'), Js('kings'), Js('life takers'), Js('loners'), Js('men of limbo'), Js('men of the night'), Js('women of limbo'), Js('women of the night'), Js('mob'), Js('nameless'), Js('night stalkers'), Js('poison ivies'), Js('purgatory'), Js('ravagers'), Js('risen demons'), Js('salvation'), Js('shadows'), Js('silence'), Js('silent death'), Js('silent footsteps'), Js('soul stealers'), Js('soulless ones'), Js('united front'), Js('unseen'), Js('untamed'), Js('voiceless ones'), Js('void'), Js('whisperers'), Js('wild ones'), Js('wildlings')]))
pass
pass


# Add lib to the module scope
gangNames = var.to_python()