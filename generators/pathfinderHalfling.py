__all__ = ['pathfinderHalfling']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if (PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)) and ((var.get('i')%Js(2.0))!=Js(0.0))):
                var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd16', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('nameLast', ((((((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm10').get(var.get('rnd14')))+var.get('nm11').get(var.get('rnd15')))+var.get('nm10').get(var.get('rnd16')))+var.get('nm12').get(var.get('rnd12'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('nameLast', (var.get('nm13').get(var.get('rnd13'))+var.get('nm14').get(var.get('rnd14'))))
                else:
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('nameLast', ((((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm10').get(var.get('rnd14')))+var.get('nm12').get(var.get('rnd12'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(2.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(3.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('nameLast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('f'), Js('h'), Js('j'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('x')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa')]))
var.put('nm3', Js([Js('b'), Js('b'), Js('d'), Js('d'), Js('f'), Js('f'), Js('g'), Js('g'), Js('k'), Js('k'), Js('l'), Js('l'), Js('lb'), Js('ld'), Js('m'), Js('m'), Js('mr'), Js('mg'), Js('n'), Js('n'), Js('nd'), Js('ng'), Js('nk'), Js('nt'), Js('r'), Js('r'), Js('rb'), Js('rc'), Js('rg'), Js('rr'), Js('rk'), Js('sg'), Js('sk'), Js('st'), Js('v'), Js('v'), Js('x'), Js('x')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('k'), Js('l'), Js('m'), Js('n'), Js('nd'), Js('pp'), Js('r'), Js('rd'), Js('rn'), Js('s'), Js('th')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('f'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('pr'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('iu'), Js('io'), Js('oe'), Js('ai'), Js('ia'), Js('ae')]))
var.put('nm7', Js([Js('dg'), Js('f'), Js('f'), Js('hs'), Js('hr'), Js('hn'), Js('hj'), Js('l'), Js('l'), Js('lc'), Js('lk'), Js('ll'), Js('lm'), Js('ln'), Js('ld'), Js('lr'), Js('m'), Js('m'), Js('mb'), Js('n'), Js('n'), Js('nt'), Js('nth'), Js('nr'), Js('r'), Js('r'), Js('rl'), Js('rr'), Js('s'), Js('s'), Js('ss'), Js('st'), Js('str'), Js('t'), Js('t'), Js('th'), Js('tt'), Js('v'), Js('v'), Js('y'), Js('y'), Js('z'), Js('z')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('n'), Js('s'), Js('t'), Js('th')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('c'), Js('d'), Js('f'), Js('g'), Js('gl'), Js('gn'), Js('h'), Js('k'), Js('kl'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('vl')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ia'), Js('ae'), Js('ea'), Js('ai')]))
var.put('nm11', Js([Js('bl'), Js('br'), Js('bbl'), Js('dl'), Js('dn'), Js('dr'), Js('ffl'), Js('ggl'), Js('gr'), Js('gdd'), Js('gn'), Js('l'), Js('ld'), Js('lb'), Js('lv'), Js('ln'), Js('lm'), Js('lr'), Js('lz'), Js('lv'), Js('m'), Js('mb'), Js('md'), Js('n'), Js('nd'), Js('ng'), Js('nb'), Js('nv'), Js('nch'), Js('nd'), Js('r'), Js('rb'), Js('rd'), Js('rw'), Js('s'), Js('sr'), Js('sb'), Js('sd'), Js('sl'), Js('v'), Js('vr'), Js('vl'), Js('wh'), Js('zr'), Js('zz')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js('g'), Js('l'), Js('lk'), Js('n'), Js('nch'), Js('nd'), Js('r'), Js('rd'), Js('rg'), Js('s'), Js('th'), Js('x')]))
var.put('nm13', Js([Js('Amber'), Js('Arms'), Js('Ash'), Js('Autumn'), Js('Bard'), Js('Black'), Js('Blaze'), Js('Blossom'), Js('Bright'), Js('Bronze'), Js('Cask'), Js('Cinder'), Js('Cliff'), Js('Cloud'), Js('Cold'), Js('Common'), Js('Coven'), Js('Crag'), Js('Dark'), Js('Dawn'), Js('Day'), Js('Deep'), Js('Dew'), Js('Down'), Js('Dream'), Js('Dusk'), Js('Dust'), Js('Earth'), Js('Even'), Js('Ever'), Js('Far'), Js('Feather'), Js('Fern'), Js('Flame'), Js('Flat'), Js('Flint'), Js('Fog'), Js('Forest'), Js('Free'), Js('Frost'), Js('Full'), Js('Gold'), Js('Grand'), Js('Grass'), Js('Gray'), Js('Green'), Js('Hard'), Js('Haven'), Js('Haze'), Js('Heart'), Js('High'), Js('Hill'), Js('Honor'), Js('Humble'), Js('Iron'), Js('Keen'), Js('Leaf'), Js('Light'), Js('Lone'), Js('Long'), Js('Low'), Js('Meadow'), Js('Mild'), Js('Mist'), Js('Moon'), Js('Moss'), Js('Never'), Js('Night'), Js('Noble'), Js('Orb'), Js('Pale'), Js('Pine'), Js('Plain'), Js('Rain'), Js('Red'), Js('Rich'), Js('River'), Js('Rumble'), Js('Shadow'), Js('Silent'), Js('Simple'), Js('Single'), Js('Snow'), Js('Soft'), Js('Spirit'), Js('Spring'), Js('Star'), Js('Still'), Js('Stone'), Js('Summer'), Js('Sun'), Js('Swift'), Js('Tree'), Js('True'), Js('Truth'), Js('Turn'), Js('Water'), Js('Whit'), Js('Wind'), Js('Winter'), Js('Wise'), Js('Wood')]))
var.put('nm14', Js([Js('arm'), Js('beam'), Js('bend'), Js('blaze'), Js('bloom'), Js('blossom'), Js('bough'), Js('brace'), Js('branch'), Js('brand'), Js('breath'), Js('breeze'), Js('brook'), Js('brow'), Js('cloud'), Js('coin'), Js('creek'), Js('crest'), Js('dew'), Js('down'), Js('draft'), Js('dream'), Js('fall'), Js('flaw'), Js('flow'), Js('flower'), Js('force'), Js('gaze'), Js('gazer'), Js('gem'), Js('glade'), Js('gleam'), Js('glide'), Js('glow'), Js('grain'), Js('grip'), Js('guard'), Js('hair'), Js('hand'), Js('heart'), Js('helm'), Js('horn'), Js('keep'), Js('leaf'), Js('less'), Js('light'), Js('more'), Js('orb'), Js('peak'), Js('ridge'), Js('root'), Js('run'), Js('shine'), Js('shot'), Js('soar'), Js('song'), Js('spark'), Js('stream'), Js('stride'), Js('sun'), Js('surge'), Js('sword'), Js('sworn'), Js('thorn'), Js('tide'), Js('track'), Js('vale'), Js('valor'), Js('ward'), Js('water'), Js('whirl'), Js('wing'), Js('with'), Js('worth')]))
pass
pass


# Add lib to the module scope
pathfinderHalfling = var.to_python()