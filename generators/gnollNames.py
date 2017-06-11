__all__ = ['gnollNames']

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
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
            var.put('rnd22', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
            var.put('nmLast', (var.get('nm13').get(var.get('rnd12'))+var.get('nm14').get(var.get('rnd22'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('rnd')<Js(5.0)):
                    while (var.get('rnd3')<Js(5.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+Js(' '))+var.get('nmLast')))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd3')))+Js(' '))+var.get('nmLast')))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    if (var.get('rnd')<Js(5.0)):
                        while (var.get('rnd3')<Js(5.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    if (var.get('i')<Js(5.0)):
                        var.put('names', ((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd3')))+Js(' '))+var.get('nmLast')))
                    else:
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('names', ((((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd5')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd3')))+Js(' '))+var.get('nmLast')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('rnd')<Js(5.0)):
                        while (var.get('rnd3')<Js(5.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(5.0)):
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+Js(' '))+var.get('nmLast')))
                    else:
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd3')))+Js(' '))+var.get('nmLast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('br'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('gh'), Js('gn'), Js('k'), Js('kh'), Js('kr'), Js('m'), Js('r'), Js('rr'), Js('t'), Js('th'), Js('tr'), Js('thr'), Js('v'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y'), Js('y'), Js('aa'), Js('ei'), Js('ia'), Js('ou'), Js('ua'), Js('uo')]))
var.put('nm3', Js([Js('br'), Js('g'), Js('gr'), Js('gn'), Js('gl'), Js('gz'), Js('gv'), Js('gg'), Js('grr'), Js('ghr'), Js('hr'), Js('hg'), Js('kz'), Js('kr'), Js('kn'), Js('kz'), Js('kk'), Js('lg'), Js('lz'), Js('lk'), Js('lr'), Js('mk'), Js('mm'), Js('mr'), Js('ng'), Js('nr'), Js('ngr'), Js('ndr'), Js('nk'), Js('nkr'), Js('r'), Js('rr'), Js('rg'), Js('rgr'), Js('rk'), Js('rkr'), Js('x'), Js('xx'), Js('v'), Js('vk'), Js('vg'), Js('zg'), Js('zz'), Js('zr')]))
var.put('nm4', Js([Js('r'), Js('rr'), Js('rg'), Js('rrg'), Js('rk'), Js('c'), Js('k'), Js('kk'), Js('x'), Js('kx'), Js('z'), Js('zz'), Js('t'), Js('h'), Js('n')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gl'), Js('gr'), Js('grr'), Js('gn'), Js('h'), Js('hr'), Js('kh'), Js('kn'), Js('l'), Js('m'), Js('mr'), Js('n'), Js('p'), Js('r'), Js('rh'), Js('rr'), Js('rrh'), Js('s'), Js('sh'), Js('sr'), Js('sn'), Js('sz'), Js('t'), Js('th'), Js('tr'), Js('trr'), Js('ts'), Js('v'), Js('z'), Js('zh')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('aa'), Js('ae'), Js('ai'), Js('ea'), Js('ei'), Js('ie'), Js('ia'), Js('ui')]))
var.put('nm7', Js([Js('b'), Js('bn'), Js('bl'), Js('d'), Js('dd'), Js('dn'), Js('g'), Js('gh'), Js('gg'), Js('gz'), Js('gr'), Js('hr'), Js('hz'), Js('hg'), Js('hn'), Js('hl'), Js('hrr'), Js('l'), Js('ll'), Js('lr'), Js('lm'), Js('ln'), Js('lg'), Js('lz'), Js('lv'), Js('mn'), Js('mv'), Js('ms'), Js('ng'), Js('nk'), Js('nr'), Js('nz'), Js('nv'), Js('r'), Js('rr'), Js('rh'), Js('rg'), Js('rt'), Js('rtr'), Js('rth'), Js('rx'), Js('s'), Js('ss'), Js('sz'), Js('sr'), Js('szr'), Js('str'), Js('sl'), Js('sn'), Js('sg'), Js('sh'), Js('szh'), Js('t'), Js('th'), Js('thr'), Js('ts'), Js('thn'), Js('tn'), Js('tz'), Js('tzs'), Js('tsz'), Js('tsh'), Js('thv'), Js('thg'), Js('thm'), Js('thn'), Js('w'), Js('wv'), Js('vn'), Js('vg'), Js('vl'), Js('vr'), Js('zr'), Js('zn'), Js('zl'), Js('zh'), Js('zs'), Js('zsh')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('r'), Js('rh'), Js('hr'), Js('h'), Js('hn'), Js('s'), Js('sh'), Js('z'), Js('hz'), Js('th'), Js('rth')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('g'), Js('gn'), Js('gr'), Js('k'), Js('kr'), Js('kn'), Js('m'), Js('r'), Js('rr'), Js('s'), Js('sz'), Js('sr'), Js('t'), Js('th'), Js('tr'), Js('thr'), Js('v'), Js('x'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('aa'), Js('ei'), Js('ou'), Js('ua'), Js('ue'), Js('ei'), Js('ai'), Js('ia')]))
var.put('nm11', Js([Js('b'), Js('bb'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('gr'), Js('gn'), Js('gl'), Js('gv'), Js('grr'), Js('ghr'), Js('hr'), Js('hg'), Js('hn'), Js('hl'), Js('hz'), Js('l'), Js('ll'), Js('lg'), Js('lz'), Js('lv'), Js('lk'), Js('lm'), Js('m'), Js('mm'), Js('mr'), Js('mv'), Js('mk'), Js('mg'), Js('nk'), Js('nn'), Js('nz'), Js('nv'), Js('ng'), Js('ngr'), Js('r'), Js('rr'), Js('rg'), Js('rh'), Js('rhg'), Js('rn'), Js('rm'), Js('rl'), Js('rz'), Js('x'), Js('xr'), Js('z'), Js('zz'), Js('zs'), Js('zn'), Js('zl'), Js('zg')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js('c'), Js('l'), Js('n'), Js('m'), Js('h'), Js('r'), Js('rr'), Js('th'), Js('t')]))
var.put('nm13', Js([Js('Ash'), Js('Blight'), Js('Blood'), Js('Boom'), Js('Brine'), Js('Broken'), Js('Burst'), Js('Clay'), Js('Crack'), Js('Cracked'), Js('Damp'), Js('Dead'), Js('Dirt'), Js('Dreck'), Js('Dregs'), Js('Dust'), Js('Fail'), Js('Far'), Js('Fast'), Js('Filth'), Js('Fizz'), Js('Fizzle'), Js('Foam'), Js('Froth'), Js('Fungi'), Js('Fungus'), Js('Glop'), Js('Gold'), Js('Goo'), Js('Gore'), Js('Grapple'), Js('Grease'), Js('Grime'), Js('Ground'), Js('Gunk'), Js('Lard'), Js('Loose'), Js('Lump'), Js('Mire'), Js('Mole'), Js('Muck'), Js('Mucus'), Js('Mud'), Js('Murk'), Js('Ooze'), Js('Pebble'), Js('Pest'), Js('Rent'), Js('River'), Js('Rot'), Js('Salt'), Js('Sand'), Js('Scourge'), Js('Scum'), Js('Scuz'), Js('Silt'), Js('Slab'), Js('Sleaze'), Js('Slime'), Js('Sludge'), Js('Snore'), Js('Snot'), Js('Soil'), Js('Soot'), Js('Sore'), Js('Split'), Js('Stain'), Js('Sweat'), Js('Tame'), Js('Woe'), Js('Zest')]))
var.put('nm14', Js([Js('barb'), Js('bash'), Js('basher'), Js('beam'), Js('blase'), Js('blast'), Js('bolt'), Js('boot'), Js('brass'), Js('cast'), Js('cheek'), Js('clash'), Js('claw'), Js('cloak'), Js('club'), Js('crook'), Js('dance'), Js('death'), Js('dent'), Js('ear'), Js('ears'), Js('eye'), Js('eyes'), Js('face'), Js('fang'), Js('fangs'), Js('feet'), Js('finger'), Js('fingers'), Js('fist'), Js('fists'), Js('foot'), Js('frown'), Js('fuse'), Js('gall'), Js('gaze'), Js('gleam'), Js('glob'), Js('gob'), Js('grapnel'), Js('grappler'), Js('grin'), Js('grinder'), Js('guard'), Js('guise'), Js('hallow'), Js('hammer'), Js('hand'), Js('hands'), Js('head'), Js('hook'), Js('hunter'), Js('knob'), Js('knuckle'), Js('mask'), Js('maw'), Js('mouth'), Js('mug'), Js('nail'), Js('nails'), Js('nose'), Js('paw'), Js('pince'), Js('pincer'), Js('pinch'), Js('scowl'), Js('scrap'), Js('shrapnel'), Js('skin'), Js('smile'), Js('smirk'), Js('snag'), Js('spear'), Js('stick'), Js('talon'), Js('teeth'), Js('thumb'), Js('tine'), Js('toe'), Js('toes'), Js('tongue'), Js('tooth'), Js('tusk'), Js('watch'), Js('wizzle')]))
pass
pass


# Add lib to the module scope
gnollNames = var.to_python()