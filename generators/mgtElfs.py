__all__ = ['mgtElfs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm18', 'nm14', 'nm17', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
            var.put('lName', ((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd5'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    while PyJsStrictEq(var.get('nm10').get(var.get('rnd5')),var.get('nm8').get(var.get('rnd3'))):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        while PyJsStrictEq(var.get('nm9').get(var.get('rnd7')),var.get('nm8').get(var.get('rnd3'))):
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', ((((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                        var.put('names', ((var.get('nm17').get(var.get('rnd'))+Js(' '))+var.get('nm18').get(var.get('rnd2'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                        while PyJsStrictEq(var.get('nm15').get(var.get('rnd')),var.get('nm16').get(var.get('rnd2'))):
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                        var.put('names', (((var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2')))+Js(' '))+var.get('nm18').get(var.get('rnd3'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    while PyJsStrictEq(var.get('nm5').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        while PyJsStrictEq(var.get('nm4').get(var.get('rnd7')),var.get('nm3').get(var.get('rnd3'))):
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                        var.put('names', ((var.get('nm17').get(var.get('rnd'))+Js(' '))+var.get('nm18').get(var.get('rnd2'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                        while PyJsStrictEq(var.get('nm15').get(var.get('rnd')),var.get('nm16').get(var.get('rnd2'))):
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                        var.put('names', (((var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2')))+Js(' '))+var.get('nm18').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('d'), Js('j'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('rh'), Js('th'), Js('v')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('e'), Js('a'), Js('o'), Js('eo'), Js('ea'), Js('aa')]))
var.put('nm3', Js([Js('f'), Js('g'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('s'), Js('ss'), Js('v'), Js('z'), Js('dr'), Js('f'), Js('g'), Js('l'), Js('ll'), Js('lm'), Js('ln'), Js('m'), Js('mn'), Js('n'), Js('nm'), Js('r'), Js('rl'), Js('s'), Js('ss'), Js('v'), Js('z')]))
var.put('nm4', Js([Js('d'), Js('ll'), Js('ld'), Js('ln'), Js('lm'), Js('mn'), Js('mr'), Js('nr'), Js('s'), Js('r'), Js('v'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('l'), Js('ll'), Js('ld'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('s'), Js('th')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('dw'), Js('gl'), Js('gw'), Js('h'), Js('k'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('t'), Js('th'), Js('y')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('ae'), Js('ea'), Js('ia')]))
var.put('nm8', Js([Js('dh'), Js('ff'), Js('l'), Js('lv'), Js('lr'), Js('lm'), Js('ll'), Js('m'), Js('mm'), Js('n'), Js('nh'), Js('nn'), Js('ny'), Js('ph'), Js('s'), Js('ss'), Js('sh'), Js('shm'), Js('th'), Js('v'), Js('vr'), Js('y'), Js('ys')]))
var.put('nm9', Js([Js('l'), Js('ll'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('t'), Js('y'), Js('z')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('n'), Js('s'), Js('th')]))
var.put('nm11', Js([Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm12', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i')]))
var.put('nm13', Js([Js('g'), Js('gg'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('v'), Js('vv'), Js('z'), Js('zz'), Js('gr'), Js('gn'), Js('hr'), Js('hn'), Js('ldr'), Js('ld'), Js('lr'), Js('ln'), Js('lm'), Js('mr'), Js('mdr'), Js('mv'), Js('mn'), Js('nd'), Js('nr'), Js('nm'), Js('ngr'), Js('ndr'), Js('rdr'), Js('rl'), Js('rg'), Js('rgr'), Js('rv'), Js('st'), Js('sk'), Js('sl'), Js('str'), Js('tr'), Js('thr'), Js('vr'), Js('vn'), Js('zr'), Js('zdr'), Js('zd')]))
var.put('nm14', Js([Js('g'), Js('l'), Js('n'), Js('s'), Js('t'), Js('th')]))
var.put('nm15', Js([Js('alder'), Js('alpen'), Js('amber'), Js('autumn'), Js('beech'), Js('birch'), Js('bitter'), Js('blight'), Js('blood'), Js('border'), Js('boulder'), Js('bramble'), Js('bright'), Js('bronze'), Js('cedar'), Js('cliff'), Js('cloud'), Js('copper'), Js('coven'), Js('crag'), Js('crest'), Js('dark'), Js('dawn'), Js('deep'), Js('dense'), Js('dew'), Js('dream'), Js('dusk'), Js('elm'), Js('ever'), Js('eye'), Js('fall'), Js('far'), Js('fern'), Js('fir'), Js('flint'), Js('fore'), Js('free'), Js('glade'), Js('glow'), Js('gnarl'), Js('gold'), Js('grand'), Js('grass'), Js('great'), Js('green'), Js('grove'), Js('hallow'), Js('hard'), Js('haven'), Js('hazel'), Js('heart'), Js('high'), Js('keen'), Js('knot'), Js('larch'), Js('life'), Js('light'), Js('lone'), Js('long'), Js('low'), Js('luna'), Js('lunar'), Js('maple'), Js('marsh'), Js('meadow'), Js('mild'), Js('moon'), Js('moss'), Js('nettle'), Js('night'), Js('noble'), Js('nor'), Js('oak'), Js('oaken'), Js('oat'), Js('peace'), Js('pine'), Js('plain'), Js('pride'), Js('proud'), Js('pyre'), Js('rapid'), Js('rich'), Js('rover'), Js('scrub'), Js('seed'), Js('silver'), Js('sky'), Js('snow'), Js('solar'), Js('splinter'), Js('spring'), Js('spruce'), Js('stag'), Js('star'), Js('still'), Js('stone'), Js('storm'), Js('stout'), Js('strong'), Js('summer'), Js('sun'), Js('swift'), Js('terra'), Js('thistle'), Js('thorn'), Js('thunder'), Js('timber'), Js('tree'), Js('true'), Js('tusk'), Js('vast'), Js('vine'), Js('weather'), Js('whit'), Js('wild'), Js('willow'), Js('wind'), Js('wire'), Js('wise'), Js('wood'), Js('yew')]))
var.put('nm16', Js([Js('arrow'), Js('bane'), Js('bark'), Js('bellow'), Js('bender'), Js('binder'), Js('blade'), Js('blight'), Js('bloom'), Js('blossom'), Js('bluff'), Js('bough'), Js('bow'), Js('braid'), Js('bramble'), Js('branch'), Js('brand'), Js('breath'), Js('breeze'), Js('brook'), Js('brow'), Js('caller'), Js('chaser'), Js('cloud'), Js('copse'), Js('cover'), Js('covert'), Js('cradle'), Js('crag'), Js('crest'), Js('crown'), Js('dancer'), Js('dew'), Js('down'), Js('draft'), Js('drifter'), Js('eye'), Js('fall'), Js('fern'), Js('fir'), Js('flare'), Js('force'), Js('forge'), Js('gaze'), Js('glade'), Js('gleam'), Js('glide'), Js('glory'), Js('glove'), Js('glow'), Js('grip'), Js('grove'), Js('guard'), Js('gust'), Js('hand'), Js('hart'), Js('haven'), Js('heart'), Js('hide'), Js('hilt'), Js('horn'), Js('hunter'), Js('husk'), Js('lance'), Js('land'), Js('larch'), Js('lash'), Js('leaf'), Js('light'), Js('limb'), Js('lore'), Js('mane'), Js('mantle'), Js('mark'), Js('more'), Js('needle'), Js('nettle'), Js('pike'), Js('ridge'), Js('root'), Js('runner'), Js('scape'), Js('seed'), Js('shade'), Js('shadow'), Js('shard'), Js('shine'), Js('shroud'), Js('shrub'), Js('side'), Js('soil'), Js('spire'), Js('spring'), Js('surge'), Js('sworn'), Js('talon'), Js('tender'), Js('thorn'), Js('trunk'), Js('vine'), Js('watch'), Js('weald'), Js('wind'), Js('wood'), Js('woods')]))
var.put('nm17', Js([Js('Acclaimed'), Js('Adept'), Js('Advanced'), Js('Agile'), Js('Ambush'), Js('Arbor'), Js('Armored'), Js('Athletic'), Js('Attentive'), Js('Aura'), Js('Aurora'), Js('Blind'), Js('Bloom'), Js('Boreal'), Js('Bright'), Js('Brilliant'), Js('Bruised'), Js('Calm'), Js('Carapace'), Js('Careful'), Js('Cautious'), Js('Composed'), Js('Crafty'), Js('Crazed'), Js('Dapper'), Js('Deadly'), Js('Defiant'), Js('Determined'), Js('Devoted'), Js('Diligent'), Js('Discrete'), Js('Eager'), Js('Essence'), Js('Exalted'), Js('Exemplary'), Js('False'), Js('Famous'), Js('Fauna'), Js('Fearless'), Js('Feisty'), Js('Fierce'), Js('Flora'), Js('Focused'), Js('Forsaken'), Js('Frontier'), Js('Gifted'), Js('Grand'), Js('Great'), Js('Grim'), Js('Hidden'), Js('Honored'), Js('Illustrious'), Js('Infamous'), Js('Keen'), Js('Light'), Js('Loyal'), Js('Menacing'), Js('Mysterious'), Js('Powerful'), Js('Prestigious'), Js('Prime'), Js('Quick'), Js('Quiet'), Js('Radiant'), Js('Reckless'), Js('Renegade'), Js('Savant'), Js('Shady'), Js('Silent'), Js('Suspicious'), Js('Swift'), Js('Trained'), Js('Vengeful'), Js('Vicious'), Js('Vigilant'), Js('Violent'), Js('Wicked'), Js('Wrathful'), Js('Wretched')]))
var.put('nm18', Js([Js('Acolyte'), Js('Animist'), Js('Archdruid'), Js('Archer'), Js('Architect'), Js('Archmage'), Js('Artisan'), Js('Assassin'), Js('Barbarian'), Js('Bard'), Js('Battalion'), Js('Battlemage'), Js('Battlerider'), Js('Battlewarden'), Js('Beastcaller'), Js('Beastmaster'), Js('Berserker'), Js('Biomancer'), Js('Blademaster'), Js('Bladesinger'), Js('Bowmaster'), Js('Branchbender'), Js('Branchcaller'), Js('Brigade'), Js('Cavalier'), Js('Cavalry'), Js('Champion'), Js('Channeler'), Js('Commander'), Js('Conduit'), Js('Courier'), Js('Crafter'), Js('Cultivator'), Js('Dancer'), Js('Denizen'), Js('Druid'), Js('Elder'), Js('Elite'), Js('Emissary'), Js('Empath'), Js('Enforcer'), Js('Entourage'), Js('Exiled'), Js('Explorer'), Js('Forger'), Js('Gamekeeper'), Js('Gatekeeper'), Js('Guardian'), Js('Guide'), Js('Guildmage'), Js('Handservant'), Js('Harbinger'), Js('Healer'), Js('Herald'), Js('Herder'), Js('Hero'), Js('Hexhunter'), Js('Hivemaster'), Js('Hunter'), Js('Initiate'), Js('Knight'), Js('Leader'), Js('Ledgewalker'), Js('Lookout'), Js('Lorebearer'), Js('Mage'), Js('Magistrate'), Js('Messenger'), Js('Mystic'), Js('Operative'), Js('Oracle'), Js('Outrider'), Js('Paragon'), Js('Pathcutter'), Js('Pathfinder'), Js('Pathwarden'), Js('Patrol'), Js('Pioneer'), Js('Piper'), Js('Preserver'), Js('Priest'), Js('Ranger'), Js('Rider'), Js('Rogue'), Js('Rootbreeder'), Js('Rootcaller'), Js('Rootspeaker'), Js('Runner'), Js('Sage'), Js('Savage'), Js('Scout'), Js('Scrapper'), Js('Seeker'), Js('Seer'), Js('Sentinel'), Js('Sentry'), Js('Servant'), Js('Shaman'), Js('Shepherd'), Js('Skyrider'), Js('Skysweeper'), Js('Spirit Guide'), Js('Spy'), Js('Spymaster'), Js('Strider'), Js('Summoner'), Js('Sunsinger'), Js('Swordmaster'), Js('Tender'), Js('Tracer'), Js('Tracker'), Js('Trailblazer'), Js('Trapper'), Js('Treespeaker'), Js('Trooper'), Js('Vanguard'), Js('Vinebender'), Js('Vinebreeder'), Js('Vinecaller'), Js('Vinespeaker'), Js('Visionary'), Js('Wanderer'), Js('Warcaller'), Js('Warden'), Js('Warrior'), Js('Watcher'), Js('Wayfinder'), Js('Whisperer'), Js('Wolf-Rider'), Js('Woodcloaker'), Js('Zealot')]))
pass
pass


# Add lib to the module scope
mgtElfs = var.to_python()