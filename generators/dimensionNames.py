__all__ = ['dimensionNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names5', 'names2', 'names3', 'names1'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('names', ((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('names', ((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names2').get(var.get('rnd4')))+var.get('names4').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('names', ((Js('The ')+var.get('names5').get(var.get('rnd')))+Js(' Dimension')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('ch'), Js('cw'), Js('cr'), Js('cy'), Js('cl'), Js('br'), Js('by'), Js('bl'), Js('dr'), Js('dy'), Js('dl'), Js('fr'), Js('fy'), Js('fl'), Js('gr'), Js('gy'), Js('gl'), Js('gn'), Js('gh'), Js('kr'), Js('kh'), Js('kl'), Js('ky'), Js('kn'), Js('lh'), Js('ly'), Js('my'), Js('ny'), Js('ph'), Js('pr'), Js('pl'), Js('py'), Js('pn'), Js('rh'), Js('ry'), Js('sh'), Js('sr'), Js('str'), Js('st'), Js('sn'), Js('sm'), Js('sl'), Js('sw'), Js('th'), Js('tr'), Js('thr')]))
var.put('names2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('eo'), Js('eu'), Js('ei'), Js('ee'), Js('ia'), Js('io'), Js('iu'), Js('ie'), Js('ae'), Js('ao'), Js('ai'), Js('aa'), Js('ua'), Js('ui'), Js('ue'), Js('oi'), Js('oo'), Js('ou'), Js('oe')]))
var.put('names3', Js([Js('sh'), Js('ch'), Js('ph'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('st'), Js('str'), Js('cl'), Js('gl'), Js('kl'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('bb'), Js('cc'), Js('dd'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt')]))
var.put('names4', Js([Js('bith'), Js('ch'), Js('cyl'), Js('cyn'), Js('cys'), Js('cire'), Js('din'), Js('dynn'), Js('dale'), Js('dea'), Js('dor'), Js('dore'), Js('dath'), Js('dag'), Js('gath'), Js('gor'), Js('glyn'), Js('gwyn'), Js('ghon'), Js('gor'), Js('gaz'), Js('jax'), Js('gax'), Js('glin'), Js('lax'), Js('lix'), Js('lan'), Js('lahr'), Js('lyn'), Js('lag'), Js('laq'), Js('myn'), Js('myhr'), Js('myth'), Js('mix'), Js('myx'), Js('max'), Js('maq'), Js('mhaz'), Js('nos'), Js('noth'), Js('nix'), Js('nith'), Js('nyl'), Js('nif'), Js('nor'), Js('nore'), Js('nox'), Js('noxis'), Js('phis'), Js('phas'), Js('phara'), Js('phere'), Js('phire'), Js('phaire'), Js('pix'), Js('para'), Js('pale'), Js('pea'), Js('prea'), Js('qir'), Js('qira'), Js('qur'), Js('que'), Js('qia'), Js('qin'), Js('qis'), Js('qith'), Js('qoth'), Js('rire'), Js('roth'), Js('raz'), Js('riq'), Js('raq'), Js('raqa'), Js('rhan'), Js('ril'), Js('rix'), Js('riz'), Js('roth'), Js('rath'), Js('syn'), Js('sh'), Js('six'), Js('san'), Js('sol'), Js('sos'), Js('sox'), Js('th'), Js('x'), Js('pis'), Js('pith'), Js('tea'), Js('tix'), Js('toq'), Js('tire'), Js('tore'), Js('tale'), Js('thal'), Js('tis'), Js('til'), Js('tur'), Js('tig'), Js('vys'), Js('vyn'), Js('vox'), Js('via'), Js('vil'), Js('xin'), Js('xas'), Js('xar'), Js('zal'), Js('zar')]))
var.put('names5', Js([Js('Ageless'), Js('Amber'), Js('Amnesia'), Js('Ancestral'), Js('Ancient'), Js('Angel'), Js('Anima'), Js('Ash'), Js('Astral'), Js('Autumn'), Js('Barbaric'), Js('Barren'), Js('Behemoth'), Js('Berserk'), Js('Blessed'), Js('Blind'), Js('Blood'), Js('Blood Magic'), Js('Bone'), Js('Brutal'), Js('Burning'), Js('Cannibal'), Js('Celestial'), Js('Cerulean'), Js('Clone'), Js('Cosmic'), Js('Cosmos'), Js('Crimson'), Js('Cyber'), Js('Dark'), Js('Dark Magic'), Js('Day'), Js('Daydream'), Js('Dead'), Js('Death'), Js('Deception'), Js('Demon'), Js('Deranged'), Js('Desolate'), Js('Destiny'), Js('Diabolical'), Js('Divine'), Js('Doom'), Js('Dragon'), Js('Dream'), Js('Ebon'), Js('Echo'), Js('Elder'), Js('Elemental'), Js('Elysian'), Js('Emerald'), Js('Empty'), Js('Eternal'), Js('Ethereal'), Js('Fade'), Js('Fallow'), Js('False'), Js('Fire'), Js('First'), Js('Flame'), Js('Forged'), Js('Forsaken'), Js('Fossil'), Js('Freak'), Js('Free'), Js('Frozen'), Js('Fury'), Js('Future'), Js('Gateway'), Js('Ghost'), Js('Giants'), Js('Gloom'), Js('God'), Js('Godly'), Js('Golden'), Js('Gray'), Js('Green'), Js('Grim'), Js('Hallowed'), Js('Hallucination'), Js('Healing'), Js('Heaven'), Js('Hell'), Js('Hollow'), Js('Holy'), Js('Horror'), Js('Hungry'), Js('Hysteria'), Js('Ice'), Js('Illusion'), Js('Immortal'), Js('Impure'), Js('Infernal'), Js('Inferno'), Js('Infinite'), Js('Insane'), Js('Isolated'), Js('Ivory'), Js('Last'), Js('Legend'), Js('Lifeless'), Js('Light'), Js('Limbo'), Js('Lonely'), Js('Lost'), Js('Lunar'), Js('Mad'), Js('Magic'), Js('Malevolent'), Js('Master'), Js('Maze'), Js('Mime'), Js('Mimic'), Js('Mind'), Js('Miracle'), Js('Mirage'), Js('Mirror'), Js('Mist'), Js('Monster'), Js('Mortal'), Js('Mutant'), Js('Mystery'), Js('Myth'), Js('Mythical'), Js('Necrotic'), Js('Nether'), Js('Night'), Js('Nightmare'), Js('Oblivion'), Js('Obsidian'), Js('Oracle'), Js('Outcast'), Js('Pandora'), Js('Parallel'), Js('Peace'), Js('Phantom'), Js('Placid'), Js('Plague'), Js('Portal'), Js('Primal'), Js('Prime'), Js('Primeval'), Js('Pristine'), Js('Pure'), Js('Rage'), Js('Rainbow'), Js('Reflection'), Js('Relic'), Js('Rogue'), Js('Ruined'), Js('Sacred'), Js('Sanctuary'), Js('Sanguine'), Js('Sapphire'), Js('Savage'), Js('Serene'), Js('Shade'), Js('Shadow'), Js('Shattered'), Js('Silver'), Js('Skeletal'), Js('Snow'), Js('Solar'), Js('Solitary'), Js('Solstice'), Js('Soul'), Js('Soulless'), Js('Spirit'), Js('Spring'), Js('Starfall'), Js('Storm'), Js('Summer'), Js('Temporal'), Js('Terror'), Js('Thunder'), Js('Time Lost'), Js('Timeless'), Js('Titan'), Js('Tranquil'), Js('Trickster'), Js('Twilight'), Js('Twin'), Js('Unborn'), Js('Undead'), Js('Universe'), Js('Unstable'), Js('Utopian'), Js('Vacuum'), Js('Virtual'), Js('Vision'), Js('Voiceless'), Js('Void'), Js('War'), Js('Water'), Js('Whisper'), Js('White'), Js('Wicked'), Js('Winter'), Js('Wish'), Js('Wither')]))
pass
pass


# Add lib to the module scope
dimensionNames = var.to_python()