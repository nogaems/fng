__all__ = ['templeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'names9', 'nameGen', 'names6', 'names5', 'names8', 'names2', 'names10', 'names11', 'names3', 'names12', 'names1', 'names7'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('names', ((var.get('names5').get(var.get('rnd'))+Js(' of '))+var.get('names6').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names9').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names10').get('length'))))
                    var.put('names', (((((var.get('names5').get(var.get('rnd'))+Js(' of '))+var.get('names7').get(var.get('rnd2')))+var.get('names8').get(var.get('rnd3')))+var.get('names9').get(var.get('rnd4')))+var.get('names10').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names11').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names12').get('length'))))
                        var.put('names', (((Js('The ')+var.get('names11').get(var.get('rnd')))+Js(' '))+var.get('names12').get(var.get('rnd2'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                        if (var.get('rnd')<Js(20.0)):
                            while (var.get('rnd3')>Js(14.0)):
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                        if (var.get('rnd2')>Js(4.0)):
                            while (var.get('rnd4')>Js(4.0)):
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                        var.put('names', (((((Js('The ')+var.get('names1').get(var.get('rnd')))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names2').get(var.get('rnd4')))+var.get('names4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('pr'), Js('tr'), Js('str'), Js('vr'), Js('bl'), Js('cl'), Js('gl'), Js('kl'), Js('pl'), Js('sl'), Js('ch'), Js('sh'), Js('th'), Js('ph'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ea'), Js('eo'), Js('ai')]))
var.put('names3', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('w'), Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('pr'), Js('tr'), Js('str'), Js('vr'), Js('bl'), Js('cl'), Js('gl'), Js('kl'), Js('pl'), Js('sl'), Js('ch'), Js('sh'), Js('th'), Js('ph')]))
var.put('names4', Js([Js('bania'), Js('bara'), Js('ceris'), Js('cise'), Js('cys'), Js('dahre'), Js('dana'), Js('daris'), Js('deia'), Js('dhari'), Js('dhuru'), Js('firi'), Js('fys'), Js('geris'), Js('gura'), Js('hagar'), Js('haja'), Js('hara'), Js('hari'), Js('hati'), Js('hava'), Js('haya'), Js('jia'), Js('kami'), Js('kata'), Js('kaya'), Js('keria'), Js('laris'), Js('leia'), Js('leian'), Js('leion'), Js('lerion'), Js('levia'), Js('loka'), Js('luna'), Js('mana'), Js('mano'), Js('mao'), Js('mena'), Js('mina'), Js('nero'), Js('neron'), Js('nesh'), Js('neya'), Js('nira'), Js('nis'), Js('nora'), Js('nova'), Js('nuga'), Js('peron'), Js('phenia'), Js('polis'), Js('porith'), Js('ppeion'), Js('qira'), Js('rana'), Js('reon'), Js('ris'), Js('shara'), Js('szara'), Js('talis'), Js('taris'), Js('tera'), Js('theion'), Js('thenon'), Js('theoa'), Js('theon'), Js('vana'), Js('veras'), Js('vira'), Js('wani'), Js('weia'), Js('za'), Js('zaki'), Js('zale')]))
var.put('names5', Js([Js('Altar'), Js('Chapel'), Js('Church'), Js('House'), Js('Mosque'), Js('Monastery'), Js('Pagoda'), Js('Pantheon'), Js('Pantheon'), Js('Sanctuary'), Js('Sanctuary'), Js('Sanctum'), Js('Shrine'), Js('Shrine'), Js('Sanctum'), Js('Synagogue'), Js('Temple'), Js('Temple')]))
var.put('names6', Js([Js('Agony'), Js('Air'), Js('Allegiance'), Js('Ambition'), Js('Amnesia'), Js('Ancestors'), Js('Anguish'), Js('Answers'), Js('Aspiration'), Js('Ataraxia'), Js('Blight'), Js('Bliss'), Js('Bonds'), Js('Braveness'), Js('Chance'), Js('Clairvoyance'), Js('Coincidences'), Js('Chaos'), Js('Collapse'), Js('Comfort'), Js('Confessions'), Js('Confidence'), Js('Connections'), Js('Consequences'), Js('Contemplation'), Js('Conviction'), Js('Corruption'), Js('Courage'), Js('Creed'), Js('Darkness'), Js('Death'), Js('Decay'), Js('Dedication'), Js('Defeat'), Js('Delight'), Js('Demise'), Js('Desire'), Js('Despair'), Js('Destinations'), Js('Destinies'), Js('Determination'), Js('Devotion'), Js('Disaster'), Js('Discipline'), Js('Divine Will'), Js('Divinity'), Js('Doom'), Js('Dreams'), Js('Earth'), Js('Emergencies'), Js('Emotions'), Js('Endurance'), Js('Enlightenment'), Js('Equality'), Js('Equanimity'), Js('Eternity'), Js('Exile'), Js('Exiles'), Js('Exodus'), Js('Exploration'), Js('Extinction'), Js('Faith'), Js('Fate'), Js('Fealty'), Js('Felicity'), Js('Fire'), Js('Foresight'), Js('Forgiveness'), Js('Fortune'), Js('Frenzy'), Js('Friendship'), Js('Grace'), Js('Grief'), Js('Harm'), Js('Healing'), Js('Honor'), Js('Hope'), Js('Humility'), Js('Hunger'), Js('Ice'), Js('Infinity'), Js('Insight'), Js('Integrity'), Js('Introspection'), Js('Isolation'), Js('Judgement'), Js('Karma'), Js('Kinship'), Js('Knowledge'), Js('Lament'), Js('Legends'), Js('Life'), Js('Light'), Js('Lore'), Js('Loss'), Js('Love'), Js('Luck'), Js('Meditation'), Js('Mending'), Js('Mercy'), Js('Mourning'), Js('Myths'), Js('Nature'), Js('Necrosis'), Js('Oblivion'), Js('Opportunities'), Js('Paradise'), Js('Passion'), Js('Patience'), Js('Peace'), Js('Perception'), Js('Perfection'), Js('Perpetuity'), Js('Placidity'), Js('Pledges'), Js('Plight'), Js('Possibilities'), Js('Order'), Js('Premonitions'), Js('Probabilities'), Js('Promise'), Js('Prospects'), Js('Purgatory'), Js('Purpose'), Js('Pursuance'), Js('Pursuit'), Js('Quests'), Js('Quietude'), Js('Reflection'), Js('Refugees'), Js('Regrets'), Js('Rejuvenation'), Js('Reliance'), Js('Remorse'), Js('Repose'), Js('Resolutions'), Js('Resolve'), Js('Restoration'), Js('Revelations'), Js('Reverence'), Js('Reverie'), Js('Revival'), Js('Sagas'), Js('Sanctity'), Js('Seclusion'), Js('Secrets'), Js('Sentiment'), Js('Serenity'), Js('Silence'), Js('Snow'), Js('Solitude'), Js('Souls'), Js('Spirits'), Js('Tenacity'), Js('Termination'), Js('Thirst'), Js('Time'), Js('Tolerance'), Js('Tragedy'), Js('Tranquility'), Js('Triumph'), Js('Truth'), Js('Twilight'), Js('Utopia'), Js('Verdicts'), Js('Vigor'), Js('Visions'), Js('Vitality'), Js('Vows'), Js('Water'), Js('Willpower'), Js('Wisdom'), Js('Withdrawal'), Js('Zeal'), Js('the Afterlife'), Js('the Blessed'), Js('the Brave'), Js('the Eclipse'), Js('the Forest'), Js('the Forsaken'), Js('the Future'), Js('the Lake'), Js('the Light'), Js('the Mountain'), Js('the Night'), Js('the Ocean'), Js('the Oracle'), Js('the Outcasts'), Js('the Past'), Js('the Present'), Js('the Prophet'), Js('the River'), Js('the Sea'), Js('the Senses'), Js('the Shadows'), Js('the Solstice'), Js('the Universe'), Js('the Void'), Js('the Volcano'), Js('the World'), Js('the Ancients')]))
var.put('names7', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names8', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('y')]))
var.put('names9', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names10', Js([Js('agi'), Js('aldir'), Js('aos'), Js('arus'), Js('borh'), Js('bris'), Js('bum'), Js('bus'), Js('dall'), Js('dar'), Js('darr'), Js('des'), Js('dis'), Js('dite'), Js('dohr'), Js('don'), Js('dos'), Js('dros'), Js('dum'), Js('dur'), Js('emis'), Js('enar'), Js('esis'), Js('eus'), Js('eyar'), Js('eyr'), Js('her'), Js('ion'), Js('ione'), Js('ius'), Js('jun'), Js('ldir'), Js('lios'), Js('lo'), Js('lous'), Js('mes'), Js('mir'), Js('mjir'), Js('mos'), Js('mus'), Js('nia'), Js('nir'), Js('nos'), Js('nus'), Js('ohr'), Js('orr'), Js('rasil'), Js('reus'), Js('ros'), Js('ruer'), Js('rus'), Js('ses'), Js('stus'), Js('tar'), Js('tarr'), Js('teus'), Js('thar'), Js('ther'), Js('tia'), Js('ton'), Js('tos'), Js('tyx'), Js('ysus')]))
var.put('names11', Js([Js('Amaranthine'), Js('Ancestral'), Js('Ancient'), Js('Angel'), Js('Angelic'), Js('Animus'), Js('Argent'), Js('Astral'), Js('August'), Js('Azure'), Js('Blessed'), Js('Blue'), Js('Bright'), Js('Cardinal'), Js('Celestial'), Js('Ceremonial'), Js('Ceremony'), Js('Cerulean'), Js('Clairvoyance'), Js('Corrupted'), Js('Crying'), Js('Dark'), Js('Death'), Js('Devout'), Js('Divine'), Js('Elder'), Js('Eternal'), Js('Ethereal'), Js('Exalted'), Js('Fading'), Js('Father'), Js('Foul'), Js('Ghost'), Js('Glowing'), Js('Golden'), Js('Guilty'), Js('Hallowed'), Js('Harbinger'), Js('Heavenly'), Js('Herald'), Js('Holy'), Js('Honor'), Js('Immortal'), Js('Impious'), Js('Impure'), Js('Ivory'), Js('Legendary'), Js('Light'), Js('Lucent'), Js('Luminescent'), Js('Matriarch'), Js('Mirror'), Js('Mother'), Js('Mythic'), Js('Noble'), Js('Omen'), Js('Oracle'), Js('Origin'), Js('Pale'), Js('Parent'), Js('Patriarch'), Js('Pearl'), Js('Perpetual'), Js('Phantom'), Js('Phoenix'), Js('Pious'), Js('Premonition'), Js('Primal'), Js('Prophecy'), Js('Prophet'), Js('Pure'), Js('Putrid'), Js('Radiant'), Js('Red'), Js('Revelation'), Js('Revered'), Js('Righteous'), Js('Sacred'), Js('Sanctified'), Js('Sanguine'), Js('Shadow'), Js('Silver'), Js('Solemn'), Js('Soul'), Js('Source'), Js('Spirit'), Js('Tainted'), Js('Timeless'), Js('Tribal'), Js('True'), Js('Twin'), Js('Unholy'), Js('Venerable'), Js('Vile'), Js('Virtuous'), Js('Vitality'), Js('Weeping'), Js('White'), Js('Wicked'), Js('Wisdom')]))
var.put('names12', Js([Js('Altar'), Js('Basin'), Js('Beach'), Js('Boulder'), Js('Brook'), Js('Burials'), Js('Catacombs'), Js('Cave'), Js('Cavern'), Js('Chamber'), Js('Chapel'), Js('Church'), Js('Cliff'), Js('Coast'), Js('Column'), Js('Crag'), Js('Creek'), Js('Crypts'), Js('Crystal'), Js('Den'), Js('Enclave'), Js('Estuary'), Js('Field'), Js('Fjord'), Js('Flowers'), Js('Forest'), Js('Fountain'), Js('Garden'), Js('Gazebo'), Js('Geyser'), Js('Grave'), Js('Graves'), Js('Grotto'), Js('Grove'), Js('Hill'), Js('Hot Spring'), Js('Island'), Js('Isle'), Js('Jungle'), Js('Lagoon'), Js('Lake'), Js('Maple'), Js('Marsh'), Js('Meadow'), Js('Menhir'), Js('Monolith'), Js('Monument'), Js('Mosque'), Js('Mountain'), Js('Oak'), Js('Oasis'), Js('Obelisk'), Js('Orchard'), Js('Pagoda'), Js('Pantheon'), Js('Pasture'), Js('Peak'), Js('Pillar'), Js('Pillars'), Js('Pinnacle'), Js('Pond'), Js('Pool'), Js('Pyramid'), Js('Realm'), Js('Reef'), Js('Reliquary'), Js('Ridge'), Js('River'), Js('Rock'), Js('Rocks'), Js('Sanctuary'), Js('Sanctum'), Js('Shore'), Js('Shrine'), Js('Slab'), Js('Statue'), Js('Stone'), Js('Summit'), Js('Synagogue'), Js('Temple'), Js('Terrace'), Js('Thicket'), Js('Tomb'), Js('Topiary'), Js('Totem'), Js('Tower'), Js('Tree'), Js('Trees'), Js('Vertex'), Js('Willow'), Js('Woods'), Js('Yew')]))
pass
pass


# Add lib to the module scope
templeNames = var.to_python()