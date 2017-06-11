__all__ = ['portNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2'])
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
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd7')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Albatross Point'), Js('Anchorage'), Js('Angel'), Js('Angelwood'), Js('Arrow Point'), Js('Ashland'), Js('Avalon'), Js('Barnacle Bay'), Js('Barnacle Point'), Js('Baymouth'), Js('Bayport'), Js('Bayside'), Js('Blackbeard'), Js('Blackrock'), Js('Blue Lagoon'), Js('Blue River'), Js('Breakwater'), Js('Broken Reef'), Js('Candlelight'), Js('Cedar Creek'), Js('Claremont'), Js('Clearwater'), Js('Coal'), Js('Cocaobeach'), Js('Coconut'), Js('Crescent Moon'), Js('Dames Point'), Js('Driftwood'), Js('Dry River'), Js('Eagle Rock'), Js('Eastport'), Js('Echo Bay'), Js('Echo Bluff'), Js('Edgewater'), Js('Fair Isle'), Js('Fallen Oak'), Js('False River'), Js('Flamingo Bay'), Js('Forestville'), Js('Golden Beach'), Js('Golden Springs'), Js('Grand Bank'), Js('Grand Canal'), Js('Grand Island'), Js('Grand River'), Js('Greencoast'), Js('Greenport'), Js('Greymouth'), Js('Hallowind'), Js('Heaven Beach'), Js('Heaven Gate'), Js('Hermite'), Js('Hermite Creek'), Js('High Tide'), Js('Hope'), Js('Hopewell'), Js('Hunter'), Js('Huntersville'), Js('Hurricane'), Js('Imperial Beach'), Js('Iron Isle'), Js('Kings Bay'), Js('Kings Cove'), Js('Kingshill'), Js('Kingsville'), Js('Knightstone'), Js('Little Oak'), Js('Little River'), Js('Little Rock'), Js('Lobster Bay'), Js('Long Beach'), Js('Main Brook'), Js('Marblerock'), Js('Mermaid'), Js('Nemo'), Js('New Gardens'), Js('New Haven'), Js('New Hope'), Js('New Meadow'), Js('New Moon'), Js('New Point'), Js('New Wave'), Js('Newcastle'), Js('Newhaven'), Js('Newland Bay'), Js('Nightingale'), Js('No Name'), Js('North Fork'), Js('Northwest'), Js('Oak Island'), Js('Oakland'), Js('Oakwood'), Js('Ocean City'), Js('Ocean Fall'), Js('Ocean Reef'), Js('Oceanside'), Js('Oceansong'), Js('Oceanview'), Js('Old Port'), Js('Oyster'), Js('Oyster Pearl'), Js('Pelican Beach'), Js('Pine Key'), Js('Portsmouth'), Js('Prisoner Point'), Js('Redwood'), Js('Riverfall'), Js('Rivermouth'), Js('Riverport'), Js('Salmon Bay'), Js('Salmon Falls'), Js('Salmonville'), Js('Saltend'), Js('Saltlake'), Js('Saltstone'), Js('Seabreeze'), Js('Seashell Bay'), Js('Settlers Point'), Js('Seven Lake'), Js('Shark Bay'), Js('Shark River'), Js('Silver Bluff'), Js('Silvercove'), Js('Silvercreek'), Js('Silvermoon'), Js('South Fork'), Js('South Point'), Js('Southeast'), Js('Stormbreaker'), Js('Stormfury'), Js('Summer Isle'), Js('Sunken Reef'), Js('Sunset Beach'), Js('Sunset Point'), Js('Thunder Bay'), Js('Torch Key'), Js('Tortoise'), Js('Tortoise Shell'), Js('Tradepost'), Js('Turtle Bay'), Js('Victoria'), Js('Waterfalls'), Js('Westport'), Js('Whale'), Js('Whale Water'), Js('Whalehunter'), Js('Whisperwind'), Js('White Cliff'), Js('Whitehaven'), Js('Winterfall')]))
var.put('nm2', Js([Js('Harbor'), Js('Wharf'), Js('Piers'), Js('Landing'), Js('Harbor'), Js('Port')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm7', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
portNames = var.to_python()