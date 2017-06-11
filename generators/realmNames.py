__all__ = ['realmNames']

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
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                if (var.get('rnd')>Js(41.0)):
                    while (var.get('rnd3')<Js(12.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names4').get(var.get('rnd4')))+var.get('names5').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                var.put('names', (((Js('The ')+var.get('names6').get(var.get('rnd')))+Js(' '))+var.get('names7').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('ch'), Js('sh'), Js('ph'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('pr'), Js('str'), Js('vr'), Js('wr'), Js('st'), Js('bl'), Js('cl'), Js('gl'), Js('fl'), Js('kl'), Js('pl'), Js('sl')]))
var.put('names2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('eo'), Js('ia'), Js('io'), Js('ae')]))
var.put('names3', Js([Js('sh'), Js('ch'), Js('ph'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('st'), Js('str'), Js('cl'), Js('gl'), Js('kl'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('bb'), Js('cc'), Js('dd'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt')]))
var.put('names4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('eo'), Js('ia'), Js('io')]))
var.put('names5', Js([Js('bis'), Js('chaeus'), Js('cia'), Js('cion'), Js('cyre'), Js('dalar'), Js('dale'), Js('dell'), Js('din'), Js('dolon'), Js('dore'), Js('dran'), Js('du'), Js('gana'), Js('gar'), Js('garth'), Js('ghar'), Js('goth'), Js('gus'), Js('jan'), Js('la'), Js('lan'), Js('lar'), Js('las'), Js('lion'), Js('lon'), Js('lyn'), Js('mar'), Js('mel'), Js('melan'), Js('mond'), Js('mos'), Js('mund'), Js('nara'), Js('nary'), Js('nata'), Js('nem'), Js('net'), Js('nia'), Js('nica'), Js('nium'), Js('non'), Js('nor'), Js('nys'), Js('phere'), Js('pia'), Js('qar'), Js('que'), Js('rah'), Js('ran'), Js('rant'), Js('rat'), Js('rath'), Js('rea'), Js('rene'), Js('rhia'), Js('ria'), Js('rial'), Js('riel'), Js('rim'), Js('rion'), Js('ron'), Js('rona'), Js('ros'), Js('roth'), Js('rune'), Js('rus'), Js('rynn'), Js('ryon'), Js('sia'), Js('sos'), Js('spea'), Js('tall'), Js('tara'), Js('terra'), Js('tha'), Js('thae'), Js('thaer'), Js('than'), Js('thas'), Js('ther'), Js('this'), Js('thra'), Js('tia'), Js('tika'), Js('tion'), Js('tis'), Js('tope'), Js('topia'), Js('tora'), Js('tria'), Js('tuary'), Js('var'), Js('ven'), Js('ver'), Js('vion'), Js('xar'), Js('xath'), Js('xus'), Js('zan')]))
var.put('names6', Js([Js('Abandoned'), Js('Abyss'), Js('Ageless'), Js('All'), Js('Amber'), Js('Ancestor'), Js('Ancient'), Js('Animated'), Js('Aquamarine'), Js('Arctic'), Js('Argent'), Js('Ash'), Js('August'), Js('Autumn'), Js('Azure'), Js('Barbarian'), Js('Barren'), Js('Black'), Js('Boiling'), Js('Bone'), Js('Broken'), Js('Burning'), Js('Calm'), Js('Celestial'), Js('Center'), Js('Cerulean'), Js('Cinder'), Js('Cloud'), Js('Conjured'), Js('Conscious'), Js('Cosmic'), Js('Covert'), Js('Crimson'), Js('Cyber'), Js('Dead'), Js('Delusion'), Js('Demi'), Js('Desolate'), Js('Destiny'), Js('Divine'), Js('Dormant'), Js('Double'), Js('Dragon'), Js('Dream'), Js('Dual'), Js('Dying'), Js('Ebon'), Js('Echo'), Js('Eclipse'), Js('Edge'), Js('Elder'), Js('Ember'), Js('Emerald'), Js('Empty'), Js('Enchanted'), Js('Enigma'), Js('Eternal'), Js('Ethereal'), Js('Ever'), Js('Everday'), Js('Fading'), Js('Fantasy'), Js('Fate'), Js('Feral'), Js('Fierce'), Js('Final'), Js('Flaming'), Js('Floating'), Js('Flowing'), Js('Forged'), Js('Forsaken'), Js('Fortune'), Js('Fractioned'), Js('Frenzied'), Js('Frozen'), Js('Future'), Js('Gentle'), Js('Ghost'), Js('Giant'), Js('Glowing'), Js('God'), Js('Golden'), Js('Hallowed'), Js('Harsh'), Js('Hell'), Js('Hibernating'), Js('Hidden'), Js('Hollow'), Js('Howling'), Js('Ice'), Js('Illusion'), Js('Imagined'), Js('Immortal'), Js('Infernal'), Js('Inferno'), Js('Injured'), Js('Invisible'), Js('Iron'), Js('Ivory'), Js('Jade'), Js('Legend'), Js('Lifeless'), Js('Limbo'), Js('Living'), Js('Lonely'), Js('Lunar'), Js('Lush'), Js('Lustrous'), Js('Mad'), Js('Magic'), Js('Malachite'), Js('Mammoth'), Js('Manifested'), Js('Maroon'), Js('Merciless'), Js('Migrating'), Js('Mimic'), Js('Miniature'), Js('Miracle'), Js('Mirage'), Js('Mirror'), Js('Mist'), Js('Mock'), Js('Monster'), Js('Mortal'), Js('Moving'), Js('Multi'), Js('Mythic'), Js('Nebula'), Js('Nether'), Js('Never'), Js('Night'), Js('Nightmare'), Js('Nimbus'), Js('Noble'), Js('Oblivion'), Js('Obscure'), Js('Obsidian'), Js('Onyx'), Js('Oracle'), Js('Paralyzed'), Js('Parallel'), Js('Past'), Js('Patriarch'), Js('Peaceful'), Js('Perfect'), Js('Perpetual'), Js('Phantom'), Js('Portal'), Js('Pure'), Js('Rabid'), Js('Rain'), Js('Regal'), Js('Riddle'), Js('Rune'), Js('Sacred'), Js('Sanguine'), Js('Sapphire'), Js('Savage'), Js('Scarlet'), Js('Second'), Js('Severed'), Js('Shadow'), Js('Shattered'), Js('Shifting'), Js('Shivering'), Js('Shrouded'), Js('Silver'), Js('Single'), Js('Sinking'), Js('Skeletal'), Js('Sky'), Js('Slumbering'), Js('Snow'), Js('Solar'), Js('Solitary'), Js('Soul'), Js('Specter'), Js('Spirit'), Js('Spring'), Js('Steam'), Js('Sterile'), Js('Storm'), Js('Summer'), Js('Tamed'), Js('Tempest'), Js('Temporary'), Js('Terminal'), Js('Thunder'), Js('Timeless'), Js('Titan'), Js('Trance'), Js('Transient'), Js('Treacherous'), Js('Trial'), Js('Twilight'), Js('Twin'), Js('Undying'), Js('Utopia'), Js('Virtual'), Js('Vision'), Js('Void'), Js('Wandering'), Js('White'), Js('Whole'), Js('Wild'), Js('Windy'), Js('Winter'), Js('Wonder')]))
var.put('names7', Js([Js('Country'), Js('Domain'), Js('Dominion'), Js('Earth'), Js('Empire'), Js('Expanse'), Js('Fields'), Js('Forest'), Js('Isle'), Js('Isles'), Js('Lake'), Js('Land'), Js('Lands'), Js('Moon'), Js('Nation'), Js('Nexus'), Js('Ocean'), Js('Plane'), Js('Planet'), Js('Province'), Js('Reach'), Js('Realm'), Js('Realms'), Js('Region'), Js('Sanctuary'), Js('Sanctum'), Js('Sea'), Js('Terrain'), Js('Territories'), Js('Territory'), Js('Universe'), Js('Vale'), Js('Vales'), Js('Valley'), Js('World'), Js('Yonder')]))
pass
pass


# Add lib to the module scope
realmNames = var.to_python()