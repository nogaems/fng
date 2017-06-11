__all__ = ['mgtHorror']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm14', 'nm17', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm4').get(var.get('rnd5'))):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm7').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd'))):
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm7').get(var.get('rnd3')),var.get('nm8').get(var.get('rnd5'))):
                            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                        var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5'))))
                    else:
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm11').get(var.get('rnd3')),var.get('nm9').get(var.get('rnd'))):
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm11').get(var.get('rnd3')),var.get('nm12').get(var.get('rnd5'))):
                            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm13').get(var.get('rnd7')),var.get('nm12').get(var.get('rnd5'))):
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                        var.put('names', ((((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm10').get(var.get('rnd6')))+var.get('nm13').get(var.get('rnd7'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm14').get(var.get('rnd')),var.get('nm15').get(var.get('rnd2'))):
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm16').get('length'))|Js(0.0)))
                    var.put('names', (((var.get('nm14').get(var.get('rnd'))+var.get('nm15').get(var.get('rnd2')))+Js(' '))+var.get('nm16').get(var.get('rnd3'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm17').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm16').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm17').get(var.get('rnd'))+Js(' '))+var.get('nm16').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('br'), Js('cr'), Js('ch'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('k'), Js('kr'), Js('n'), Js('q'), Js('qr'), Js('r'), Js('s'), Js('sr'), Js('str'), Js('t'), Js('tr'), Js('v'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('ee'), Js('ai'), Js('au'), Js('ao'), Js('ou'), Js('ei')]))
var.put('nm3', Js([Js('dn'), Js('dl'), Js('dr'), Js('dd'), Js('gn'), Js('gl'), Js('gd'), Js('k'), Js('kk'), Js('kl'), Js('kn'), Js('kr'), Js('lr'), Js('ln'), Js('ld'), Js('ldr'), Js('lg'), Js('lgr'), Js('lk'), Js('lkr'), Js('m'), Js('mk'), Js('md'), Js('mg'), Js('mgr'), Js('mdr'), Js('ng'), Js('ngr'), Js('nd'), Js('ndr'), Js('nk'), Js('nkr'), Js('nr'), Js('nz'), Js('r'), Js('rg'), Js('rl'), Js('rk'), Js('rd'), Js('rdr'), Js('rgr'), Js('rb'), Js('rbr'), Js('s'), Js('sg'), Js('sgr'), Js('sl'), Js('sr'), Js('st'), Js('str'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vr'), Js('vl'), Js('vk'), Js('z'), Js('zg'), Js('zgr'), Js('zd'), Js('zdr'), Js('zl'), Js('zk'), Js('zkr')]))
var.put('nm4', Js([Js('c'), Js('ch'), Js('d'), Js('l'), Js('m'), Js('n'), Js('t'), Js('x'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('br'), Js('dr'), Js('g'), Js('gr'), Js('l'), Js('m'), Js('n'), Js('q'), Js('qr'), Js('r'), Js('t'), Js('tr'), Js('th'), Js('v'), Js('y'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('u')]))
var.put('nm7', Js([Js('d'), Js('g'), Js('j'), Js('m'), Js('n'), Js('r'), Js('s'), Js('st'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('y')]))
var.put('nm8', Js([Js('g'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('x'), Js('z')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('h'), Js('k'), Js('l'), Js('n'), Js('m'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o')]))
var.put('nm11', Js([Js('c'), Js('ch'), Js('g'), Js('j'), Js('k'), Js('n'), Js('q'), Js('t'), Js('v'), Js('x'), Js('z')]))
var.put('nm12', Js([Js('c'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v'), Js('x'), Js('z')]))
var.put('nm13', Js([Js('c'), Js('d'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th'), Js('x')]))
var.put('nm14', Js([Js('amber'), Js('arc'), Js('ash'), Js('bale'), Js('barb'), Js('bitter'), Js('blaze'), Js('blister'), Js('blood'), Js('blunt'), Js('bone'), Js('boulder'), Js('brick'), Js('broad'), Js('cave'), Js('chaos'), Js('chasm'), Js('cinder'), Js('crag'), Js('creak'), Js('crypt'), Js('dark'), Js('dawn'), Js('dead'), Js('death'), Js('dirge'), Js('doom'), Js('dread'), Js('dusk'), Js('dust'), Js('ember'), Js('fire'), Js('flame'), Js('flesh'), Js('flint'), Js('fore'), Js('forge'), Js('fright'), Js('frost'), Js('fuse'), Js('gloom'), Js('gnarl'), Js('gore'), Js('gray'), Js('great'), Js('grey'), Js('grim'), Js('haze'), Js('hell'), Js('horn'), Js('krag'), Js('lash'), Js('lone'), Js('long'), Js('mind'), Js('mist'), Js('molten'), Js('moon'), Js('mourn'), Js('mud'), Js('murk'), Js('myco'), Js('necro'), Js('nether'), Js('night'), Js('onyx'), Js('pyre'), Js('rage'), Js('rapid'), Js('rough'), Js('saur'), Js('shade'), Js('shadow'), Js('silent'), Js('skull'), Js('slate'), Js('spell'), Js('spells'), Js('stitch'), Js('stone'), Js('storm'), Js('strom'), Js('tall'), Js('tangle'), Js('thunder'), Js('twilight'), Js('under'), Js('wild'), Js('wood')]))
var.put('nm15', Js([Js('bane'), Js('bash'), Js('bender'), Js('blaze'), Js('blight'), Js('blood'), Js('bone'), Js('born'), Js('bough'), Js('bound'), Js('breaker'), Js('bringer'), Js('brow'), Js('burn'), Js('claw'), Js('cleaver'), Js('copse'), Js('crag'), Js('crawler'), Js('crest'), Js('crown'), Js('crusher'), Js('doom'), Js('fall'), Js('fang'), Js('fiend'), Js('fire'), Js('flame'), Js('flaw'), Js('force'), Js('forge'), Js('fury'), Js('gaze'), Js('gen'), Js('growl'), Js('growth'), Js('grub'), Js('gut'), Js('head'), Js('heart'), Js('hell'), Js('horn'), Js('howl'), Js('husk'), Js('kirk'), Js('kite'), Js('lash'), Js('leech'), Js('rage'), Js('reaper'), Js('reaver'), Js('run'), Js('scar'), Js('shadow'), Js('shard'), Js('shell'), Js('spark'), Js('spine'), Js('stalk'), Js('stalker'), Js('stand'), Js('strike'), Js('striker'), Js('stub'), Js('synth'), Js('thorn'), Js('weed'), Js('wing'), Js('wood'), Js('wrack'), Js('wraith'), Js('writher')]))
var.put('nm16', Js([Js('Aberration'), Js('Abomination'), Js('Annihilator'), Js('Barbarian'), Js('Brute'), Js('Butcher'), Js('Champion'), Js('Conduit'), Js('Corrupter'), Js('Courier'), Js('Crawler'), Js('Creation'), Js('Creeper'), Js('Crusher'), Js('Destroyer'), Js('Devourer'), Js('Dreadlord'), Js('Driller'), Js('Emissary'), Js('Enforcer'), Js('Eviscerator'), Js('Fiend'), Js('Form'), Js('Gargantuan'), Js('Gatekeeper'), Js('Gorger'), Js('Gouger'), Js('Harvester'), Js('Hatchling'), Js('Horror'), Js('Host'), Js('Howler'), Js('Infiltrator'), Js('Intimidator'), Js('Mangler'), Js('Mass'), Js('Mauler'), Js('Maw'), Js('Monster'), Js('Monstrosity'), Js('Negator'), Js('Nemesis'), Js('Nomad'), Js('Obliterator'), Js('Oppressor'), Js('Overlord'), Js('Parasite'), Js('Pest'), Js('Phalanx'), Js('Prowler'), Js('Rager'), Js('Raker'), Js('Reaper'), Js('Reaver'), Js('Remains'), Js('Reveler'), Js('Ruinator'), Js('Scavenger'), Js('Scourge'), Js('Scudder'), Js('Shambler'), Js('Shedder'), Js('Skulker'), Js('Slag'), Js('Slasher'), Js('Slaver'), Js('Spitter'), Js('Stinger'), Js('Swarm'), Js('Swarmlord'), Js('Thing'), Js('Tormenter'), Js('Tyrant')]))
var.put('nm17', Js([Js('Abyss'), Js('Abyssal'), Js('Acidic'), Js('Advanced'), Js('Anchored'), Js('Animated'), Js('Arid'), Js('Awoken'), Js('Blind'), Js('Bony'), Js('Broken'), Js('Careless'), Js('Chasm'), Js('Chittering'), Js('Colossal'), Js('Core'), Js('Corrupt'), Js('Corrupted'), Js('Cosmic'), Js('Crazed'), Js('Crooked'), Js('Cruel'), Js('Cursed'), Js('Damaged'), Js('Dark'), Js('Deaf'), Js('Delirious'), Js('Despair'), Js('Dire'), Js('Disfigured'), Js('Dread'), Js('Droopy'), Js('Enslaved'), Js('Eternal'), Js('Eyeless'), Js('Faceless'), Js('Fading'), Js('Faint'), Js('Feisty'), Js('Fickle'), Js('Filthy'), Js('Flickering'), Js('Forgotten'), Js('Forsaken'), Js('Foul'), Js('Fume'), Js('Gloomy'), Js('Grave'), Js('Greater'), Js('Grief'), Js('Grim'), Js('Growing'), Js('Guilt'), Js('Hidden'), Js('Hollow'), Js('Horrible'), Js('Huge'), Js('Hungry'), Js('Inferior'), Js('Infernal'), Js('Infinite'), Js('Lanky'), Js('Lesser'), Js('Limping'), Js('Livid'), Js('Lone'), Js('Lopsided'), Js('Meager'), Js('Meaty'), Js('Menacing'), Js('Mesmeric'), Js('Mindless'), Js('Monstrous'), Js('Murky'), Js('Mysterious'), Js('Nether'), Js('Night'), Js('Nightmare'), Js('Noxious'), Js('Organic'), Js('Partial'), Js('Pit'), Js('Plague'), Js('Possessed'), Js('Powerful'), Js('Prime'), Js('Primeval'), Js('Pungent'), Js('Putrid'), Js('Ragged'), Js('Reckless'), Js('Ridged'), Js('Rotten'), Js('Rotting'), Js('Savage'), Js('Scaly'), Js('Scrawny'), Js('Sewer'), Js('Shady'), Js('Shrill'), Js('Sinuous'), Js('Skeletal'), Js('Skittering'), Js('Skulking'), Js('Slimy'), Js('Slippery'), Js('Slithering'), Js('Slithery'), Js('Sludge'), Js('Slum'), Js('Slumbering'), Js('Slushy'), Js('Smog'), Js('Smoldering'), Js('Soggy'), Js('Sorrow'), Js('Spiked'), Js('Stitched'), Js('Storm'), Js('Sweltering'), Js('Tangle'), Js('Tangled'), Js('Thorny'), Js('Thunderous'), Js('Vicious'), Js('Viscous'), Js('Void'), Js('Warped'), Js('Wicked'), Js('Wilted'), Js('Winged'), Js('Worn'), Js('Wrathful'), Js('Wretched'), Js('Writing')]))
pass
pass


# Add lib to the module scope
mgtHorror = var.to_python()