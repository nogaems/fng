__all__ = ['mgtGolem']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd')),var.get('nm5').get(var.get('rnd2'))):
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('names', (((var.get('nm5').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+Js(' '))+var.get('nm6').get(var.get('rnd3'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm7').get(var.get('rnd'))+Js(' '))+var.get('nm6').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('j'), Js('k'), Js('q'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('e'), Js('i')]))
var.put('nm3', Js([Js('cc'), Js('dd'), Js('gg'), Js('gh'), Js('lc'), Js('lg'), Js('lk'), Js('lm'), Js('ln'), Js('nd'), Js('ng'), Js('nk'), Js('nq'), Js('nt'), Js('rb'), Js('rd'), Js('rc'), Js('rg'), Js('rk'), Js('rm'), Js('rn'), Js('rr'), Js('rt'), Js('sc'), Js('sh'), Js('sk'), Js('st'), Js('th')]))
var.put('nm4', Js([Js('amber'), Js('arc'), Js('ash'), Js('blight'), Js('boulder'), Js('bright'), Js('bronze'), Js('cinder'), Js('clear'), Js('cold'), Js('crystal'), Js('dark'), Js('ember'), Js('even'), Js('flame'), Js('flint'), Js('fore'), Js('full'), Js('fuse'), Js('glass'), Js('glow'), Js('grand'), Js('great'), Js('hard'), Js('haze'), Js('hex'), Js('high'), Js('iron'), Js('keen'), Js('light'), Js('micro'), Js('molten'), Js('moon'), Js('mourn'), Js('nehter'), Js('plain'), Js('pure'), Js('pyre'), Js('rough'), Js('rumble'), Js('rune'), Js('saber'), Js('shadow'), Js('soft'), Js('solid'), Js('soul'), Js('steel'), Js('stone'), Js('storm'), Js('strong'), Js('terra'), Js('thunder'), Js('twilight'), Js('void')]))
var.put('nm5', Js([Js('bane'), Js('bash'), Js('beam'), Js('bend'), Js('bough'), Js('bound'), Js('braid'), Js('brand'), Js('brow'), Js('claw'), Js('crest'), Js('crown'), Js('dust'), Js('fist'), Js('flaw'), Js('force'), Js('forge'), Js('forged'), Js('fury'), Js('glow'), Js('grip'), Js('guard'), Js('hammer'), Js('helm'), Js('husk'), Js('limb'), Js('mane'), Js('mark'), Js('maul'), Js('might'), Js('plate'), Js('ridge'), Js('shard'), Js('shield'), Js('spark'), Js('spine'), Js('splint'), Js('stalk'), Js('stand'), Js('steel'), Js('stride'), Js('surge'), Js('synth'), Js('tether'), Js('ward'), Js('watch')]))
var.put('nm6', Js([Js('Attendant'), Js('Automaton'), Js('Beast'), Js('Beast of Burden'), Js('Brawler'), Js('Bruiser'), Js('Champion'), Js('Colossus'), Js('Construct'), Js('Curator'), Js('Custodian'), Js('Drifter'), Js('Golem'), Js('Guard'), Js('Guardian'), Js('Herald'), Js('Hulk'), Js('Keeper'), Js('Monstrosity'), Js('Nomad'), Js('Overseer'), Js('Pilgrim'), Js('Protector'), Js('Rambler'), Js('Reclaimer'), Js('Retainer'), Js('Roamer'), Js('Sentinel'), Js('Shepherd'), Js('Statue'), Js('Stroller'), Js('Titan'), Js('Vagabond'), Js('Voyager'), Js('Wanderer'), Js('Warden'), Js('Warrior'), Js('Watcher'), Js('Golem'), Js('Golem'), Js('Golem'), Js('Golem'), Js('Golem'), Js('Golem'), Js('Golem'), Js('Construct'), Js('Construct'), Js('Construct')]))
var.put('nm7', Js([Js('Acidic'), Js('Advanced'), Js('Alabaster'), Js('Alloy'), Js('Altar'), Js('Ancestral'), Js('Anchored'), Js('Ancient'), Js('Animated'), Js('Basalt'), Js('Battered'), Js('Brass'), Js('Broken'), Js('Bruised'), Js('Buoyant'), Js('Clay'), Js('Cobalt'), Js('Complex'), Js('Corrupt'), Js('Corrupted'), Js('Crimson'), Js('Crumbling'), Js('Crystal'), Js('Defiant'), Js('Dense'), Js('Emblazoned'), Js('Enchanted'), Js('Etched'), Js('Flint'), Js('Frost'), Js('Frozen'), Js('Gaseous'), Js('Glass'), Js('Gold'), Js('Grand'), Js('Grave'), Js('Grim'), Js('Hematite'), Js('Hollow'), Js('Igneous'), Js('Iron'), Js('Jade'), Js('Jagged'), Js('Junk'), Js('Lead'), Js('Limestone'), Js('Lodestone'), Js('Lunar'), Js('Malachite'), Js('Monstrous'), Js('Mossy'), Js('Motionless'), Js('Obedient'), Js('Obsidian'), Js('Onyx'), Js('Opal'), Js('Ornate'), Js('Platinum'), Js('Primal'), Js('Prime'), Js('Pristine'), Js('Pungent'), Js('Radiant'), Js('Ruby'), Js('Rusted'), Js('Sand'), Js('Sandstone'), Js('Sanguine'), Js('Sapphire'), Js('Shadow'), Js('Shadowy'), Js('Silent'), Js('Silver'), Js('Skeletal'), Js('Solar'), Js('Spire'), Js('Steel'), Js('Straw'), Js('Titanium'), Js('Twin'), Js('Vacant'), Js('Vibrant'), Js('Volatile'), Js('Winged')]))
pass
pass


# Add lib to the module scope
mgtGolem = var.to_python()