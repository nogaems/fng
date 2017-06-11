__all__ = ['waterfallNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Angel Wing'), Js('Bat Cove'), Js('Beaver'), Js('Beaver Brook'), Js('Big Baron'), Js('Big Rock'), Js('Blackwater'), Js('Blue Water'), Js('Broken Window'), Js('Bronze Boulder'), Js('Butterfly'), Js('Cannonball'), Js('Cascading'), Js('Clearwater'), Js('Copper Creek'), Js('Crescent'), Js('Crescent Moon'), Js('Crimson'), Js('Crystal'), Js('Crystal Creek'), Js('Crystal Shower'), Js('Crystalized'), Js('Deadly'), Js('Death'), Js('Diamond Creek'), Js('Dragon'), Js('Dragonfly'), Js('Dual Branch'), Js('Eagle Cliff'), Js('Eagle Eye'), Js('Eagle Feather'), Js('Ebony'), Js('Echo'), Js('Emerald'), Js('Emerald Lake'), Js('Emperor'), Js('Eternal Drop'), Js('Eternal Fog'), Js('Fairy'), Js('Fall River'), Js('Feather'), Js('Five'), Js('Forest'), Js('Forestsong'), Js('Forgotten'), Js('Four'), Js('Foxtail'), Js('Frozen Lake'), Js('Golden Cliff'), Js('Golden Gate'), Js('Golden Nugget'), Js('Golden Strand'), Js('Grizzly Creek'), Js('Heavenly'), Js('Hidden'), Js('Hidden Cave'), Js('Hidden Rock'), Js('Hidden Rogue'), Js('Hollow Point'), Js('Hollow Rock'), Js('Horseshoe'), Js('Horsetail'), Js('Hourglass'), Js('Hunter'), Js('Iron Lake'), Js('Ivory'), Js('Ivory Cliff'), Js('Jade'), Js('Jade Glacier'), Js("King's Cloak"), Js('Laughing'), Js('Leaping Frog'), Js('Liberty'), Js('Lily Pond'), Js('Little Creek'), Js('Little Rock'), Js('Little Spring'), Js('Livingstone'), Js('Lonely Creek'), Js('Marble'), Js('Meadow Brook'), Js('Meteor'), Js('Middle Brook'), Js('Middle Stream'), Js('Mirror'), Js('Mirror Pools'), Js('Misty'), Js('Moonshadow'), Js('Mosquito'), Js('Mountain River'), Js('Mystic'), Js('Narrow'), Js('New Rainbow'), Js('New Water'), Js('Oaken'), Js('Obsidian'), Js('Onyx'), Js('Paradise'), Js('Phantom'), Js('Pirate Cove'), Js("Queen's Veil"), Js('Razorrock'), Js('Red Ribbon'), Js('River Rock'), Js('Ruby'), Js('Salmon'), Js('Salt River'), Js('Sapphire'), Js('Serpent'), Js('Serpentine'), Js('Seven Stones'), Js('Shadow'), Js('Silent Glacier'), Js('Silk Ribbon'), Js('Silken Cloak'), Js('Silken Veil'), Js('Silver Shower'), Js('Silver Wolf'), Js('Silverband'), Js('Silverstone'), Js('Silverthread'), Js('Single Branch'), Js('Sister'), Js('Sleepy'), Js('Sliding Rock'), Js('Slumbering'), Js('Spring Blossom'), Js('Spring Meadow'), Js('Spring River'), Js('Stoney Creek'), Js('Storm Peak'), Js('Summerset'), Js('Sunny Point'), Js('Surprise'), Js('Surprise Creek'), Js('The'), Js('Triplet'), Js('Turtleshell'), Js('Twin Mountain'), Js('Twin Sisters'), Js('Twister'), Js('Umbrella'), Js('Vanishing'), Js('Virgin'), Js('Virgin Valley'), Js('Whispering'), Js('Whisperwind'), Js('Whitewater'), Js('Willowwood'), Js('Young River')]))
var.put('nm2', Js([Js('Falls'), Js('Cascades'), Js('Rapids'), Js('Falls'), Js('Falls'), Js('Falls')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js(''), Js(''), Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
waterfallNames = var.to_python()