__all__ = ['mgtSphinx']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm6').get(var.get('rnd')),var.get('nm8').get(var.get('rnd3'))):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm10').get(var.get('rnd5')),var.get('nm8').get(var.get('rnd3'))):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(2.0)):
                        var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm8').get(var.get('rnd3'))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        if (var.get('i')<Js(4.0)):
                            var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd5'))))
                        else:
                            var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm11').get(var.get('rnd'))+Js(' '))+var.get('nm12').get(var.get('rnd2'))))
                    else:
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                        var.put('names', (Js('Sphinx ')+var.get('nm13').get(var.get('rnd'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm5').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(2.0)):
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3'))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        if (var.get('i')<Js(4.0)):
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
                        else:
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm11').get(var.get('rnd'))+Js(' '))+var.get('nm12').get(var.get('rnd2'))))
                    else:
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                        var.put('names', (Js('Sphinx ')+var.get('nm13').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('h'), Js('kh'), Js('m'), Js('ms'), Js('n'), Js('ng'), Js('ps'), Js('r'), Js('s'), Js('t'), Js('ts'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('ai')]))
var.put('nm3', Js([Js('b'), Js('ch'), Js('d'), Js('g'), Js('h'), Js('hm'), Js('ht'), Js('k'), Js('kh'), Js('lh'), Js('m'), Js('n'), Js('nh'), Js('nkh'), Js('nm'), Js('nn'), Js('p'), Js('ph'), Js('r'), Js('rj'), Js('rp'), Js('rs'), Js('rt'), Js('sht'), Js('ss'), Js('t'), Js('z')]))
var.put('nm4', Js([Js('b'), Js('ch'), Js('h'), Js('hb'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('mh'), Js('mm'), Js('n'), Js('p'), Js('ph'), Js('r'), Js('rr'), Js('s'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('b'), Js('f'), Js('kh'), Js('n'), Js('nk'), Js('pt'), Js('r'), Js('s'), Js('t')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('h'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('z')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('uu'), Js('ii')]))
var.put('nm8', Js([Js('d'), Js('h'), Js('hm'), Js('ht'), Js('k'), Js('m'), Js('mm'), Js('n'), Js('nk'), Js('nkh'), Js('nn'), Js('nq'), Js('nqt'), Js('p'), Js('r'), Js('rb'), Js('rs'), Js('s'), Js('sht'), Js('sm'), Js('sn'), Js('sp'), Js('st'), Js('t'), Js('z')]))
var.put('nm9', Js([Js('c'), Js('h'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('mn'), Js('n'), Js('nh'), Js('p'), Js('pp'), Js('r'), Js('s'), Js('t'), Js('tt')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('l'), Js('m'), Js('s'), Js('ts'), Js('th')]))
var.put('nm11', Js([Js('Ageless'), Js('Analytic'), Js('Anchored'), Js('Ancient'), Js('Angelic'), Js('Argent'), Js('Austere'), Js('Azure'), Js('Basilica'), Js('Behemoth'), Js('Belltower'), Js('Beryl'), Js('Brilliant'), Js('Campanile'), Js('Carmine'), Js('Cathedral'), Js('Cenotaph'), Js('Cerulean'), Js('Charade'), Js('Charm'), Js('Cobalt'), Js('Colossal'), Js('Consecrated'), Js('Conundrum'), Js('Courteous'), Js('Crimson'), Js('Crux'), Js('Cryptogram'), Js('Defiant'), Js('Diligent'), Js('Distant'), Js('Dutiful'), Js('Ecstatic'), Js('Edifice'), Js('Elated'), Js('Elegant'), Js('Elemental'), Js('Enigma'), Js('Enlightened'), Js('Esteemed'), Js('Eternal'), Js('Fearless'), Js('Feline'), Js('Flawed'), Js('Flawless'), Js('Gargantuan'), Js('Gifted'), Js('Goliath'), Js('Graceful'), Js('Gracious'), Js('Grand'), Js('Grandiose'), Js('Harmonious'), Js('Hex'), Js('Hieroglyph'), Js('Horizon'), Js('Humongous'), Js('Hymn'), Js('Idle'), Js('Indigo'), Js('Infinite'), Js('Infinity'), Js('Intrepid'), Js('Juvenile'), Js('Knot'), Js('Leviathan'), Js('Magister'), Js('Majestic'), Js('Malachite'), Js('Mindful'), Js('Miniature'), Js('Monolith'), Js('Motionless'), Js('Mysterious'), Js('Mystery'), Js('Mystic'), Js('Mythic'), Js('Mythical'), Js('Obelisk'), Js('Observatory'), Js('Obsidian'), Js('Onyx'), Js('Oracle'), Js('Oratory'), Js('Ornate'), Js('Parable'), Js('Pictograph'), Js('Pleased'), Js('Poised'), Js('Predicament'), Js('Prestigious'), Js('Primal'), Js('Prime'), Js('Prognostic'), Js('Proud'), Js('Pyramid'), Js('Rebus'), Js('Reckless'), Js('Riddle'), Js('Rune'), Js('Sanctuary'), Js('Sandstone'), Js('Sanguine'), Js('Secret'), Js('Sharding'), Js('Shrine'), Js('Silver'), Js('Spire'), Js('Supreme'), Js('Swift'), Js('Symbol'), Js('Synagogue'), Js('Temple'), Js('Timeless'), Js('Titan'), Js('Tomb'), Js('Tremendous'), Js('Twin'), Js('Twister'), Js('Verdigris'), Js('Vermilion'), Js('Vigilant'), Js('Watchful')]))
var.put('nm12', Js([Js('Abettor'), Js('Academic'), Js('Adjudicator'), Js('Agent'), Js('Ambassador'), Js('Appraiser'), Js('Arbiter'), Js('Attendant'), Js('Augur'), Js('Avenger'), Js('Cerberus'), Js('Champion'), Js('Chancellor'), Js('Chaperon'), Js('Conservator'), Js('Consul'), Js('Council'), Js('Curator'), Js('Defender'), Js('Dignitary'), Js('Diplomat'), Js('Disciple'), Js('Emissary'), Js('Envoy'), Js('Guard'), Js('Guardian'), Js('Handler'), Js('Judge'), Js('Keeper'), Js('Magister'), Js('Magistrate'), Js('Marshal'), Js('Master'), Js('Maven'), Js('Mediator'), Js('Moderator'), Js('Negotiator'), Js('Oracle'), Js('Preserver'), Js('Prophet'), Js('Protector'), Js('Reconciler'), Js('Sage'), Js('Savant'), Js('Scholar'), Js('Sentinel'), Js('Sentry'), Js('Servant'), Js('Shepherd'), Js('Sphinx'), Js('Steward'), Js('Treasurer'), Js('Warden'), Js('Watcher')]))
var.put('nm13', Js([Js('Abettor'), Js('Academic'), Js('Adjudicator'), Js('Agent'), Js('Ambassador'), Js('Appraiser'), Js('Arbiter'), Js('Attendant'), Js('Augur'), Js('Avenger'), Js('Cerberus'), Js('Champion'), Js('Chancellor'), Js('Chaperon'), Js('Conservator'), Js('Consul'), Js('Council'), Js('Curator'), Js('Defender'), Js('Dignitary'), Js('Diplomat'), Js('Disciple'), Js('Emissary'), Js('Envoy'), Js('Guard'), Js('Guardian'), Js('Judge'), Js('Keeper'), Js('Magister'), Js('Magistrate'), Js('Marshal'), Js('Master'), Js('Maven'), Js('Mediator'), Js('Moderator'), Js('Negotiator'), Js('Oracle'), Js('Preserver'), Js('Prophet'), Js('Protector'), Js('Reconciler'), Js('Sage'), Js('Savant'), Js('Scholar'), Js('Sentinel'), Js('Sentry'), Js('Servant'), Js('Shepherd'), Js('Steward'), Js('Treasurer'), Js('Warden'), Js('Watcher'), Js('of Advice'), Js('of Cryptograms'), Js('of Discovery'), Js('of Eternity'), Js('of Fiction'), Js('of Games'), Js('of Gifts'), Js('of Gold'), Js('of Grace'), Js('of Great Minds'), Js('of Harmony'), Js('of Hymns'), Js('of Ideals'), Js('of Infinity'), Js('of Invention'), Js('of Jewels'), Js('of Journeys'), Js('of Judgment'), Js('of Justice'), Js('of Knowledge'), Js('of Language'), Js('of Masks'), Js('of Memories'), Js('of Minds'), Js('of Music'), Js('of Mysteries'), Js('of Observation'), Js('of Obsidian'), Js('of Onyx'), Js('of Oracles'), Js('of Pride'), Js('of Prophecies'), Js('of Prosperity'), Js('of Puzzles'), Js('of Riddles'), Js('of Rumors'), Js('of Sapphire'), Js('of Secrets'), Js('of Teachings'), Js('of Theories'), Js('of Time'), Js('of Truth'), Js('of Voices'), Js('of Whispers'), Js('of Wisdom'), Js('of the Ages'), Js('of the Basilica'), Js('of the Cathedral'), Js('of the Chimes'), Js('of the Crown'), Js('of the Crypt'), Js('of the Enigma'), Js('of the Flame'), Js('of the Flock'), Js('of the Library'), Js('of the Monolith'), Js('of the Obelisk'), Js('of the Observatory'), Js('of the Pinnacle'), Js('of the Pyramid'), Js('of the Shrine'), Js('of the Spires'), Js('of the Temple'), Js('of the Tomb'), Js('of the Tower'), Js('of the Zephyr')]))
pass
pass


# Add lib to the module scope
mgtSphinx = var.to_python()