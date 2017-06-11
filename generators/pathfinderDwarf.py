__all__ = ['pathfinderDwarf']

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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if (PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)) and ((var.get('i')%Js(2.0))!=Js(0.0))):
                var.put('nameLast', ((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd10'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('nameLast', (var.get('nm13').get(var.get('rnd9'))+var.get('nm14').get(var.get('rnd10'))))
                else:
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('nameLast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(6.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('nameLast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('nameLast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('m'), Js('r'), Js('sr'), Js('st'), Js('str'), Js('t'), Js('tr'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('y'), Js('y'), Js('aa'), Js('ai'), Js('oo'), Js('uu'), Js('io'), Js('io')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bm'), Js('bn'), Js('cr'), Js('cd'), Js('cn'), Js('cm'), Js('d'), Js('dd'), Js('dg'), Js('dn'), Js('dm'), Js('g'), Js('gr'), Js('gn'), Js('gm'), Js('gr'), Js('gg'), Js('gd'), Js('k'), Js('kk'), Js('kl'), Js('kn'), Js('l'), Js('ld'), Js('lb'), Js('lbr'), Js('ldr'), Js('lg'), Js('lgr'), Js('lm'), Js('lk'), Js('mg'), Js('md'), Js('n'), Js('nf'), Js('nm'), Js('nth'), Js('ng'), Js('ngr'), Js('ndr'), Js('nr'), Js('r'), Js('rg'), Js('rgr'), Js('rs'), Js('rst'), Js('rd'), Js('rb'), Js('v'), Js('zm'), Js('zb'), Js('zd')]))
var.put('nm4', Js([Js('c'), Js('ck'), Js('d'), Js('dd'), Js('g'), Js('k'), Js('l'), Js('ls'), Js('ld'), Js('m'), Js('n'), Js('r'), Js('rd'), Js('rsk'), Js('rg'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('gh'), Js('h'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sr'), Js('t'), Js('thr'), Js('y'), Js('v'), Js('w')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm7', Js([Js('bn'), Js('bh'), Js('bb'), Js('b'), Js('cw'), Js('cn'), Js('d'), Js('dw'), Js('dn'), Js('dg'), Js('dd'), Js('dr'), Js('dl'), Js('h'), Js('hn'), Js('hl'), Js('hg'), Js('gn'), Js('gl'), Js('gw'), Js('gr'), Js('gv'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('ld'), Js('lw'), Js('lgr'), Js('lgw'), Js('lb'), Js('lk'), Js('m'), Js('mm'), Js('mw'), Js('mgw'), Js('mr'), Js('n'), Js('nd'), Js('ng'), Js('ngr'), Js('ngv'), Js('nn'), Js('nngv'), Js('nw'), Js('r'), Js('rg'), Js('rgw'), Js('rl'), Js('rb'), Js('s'), Js('ss'), Js('tr'), Js('v'), Js('vr'), Js('vl'), Js('z'), Js('zl'), Js('zw')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('mn'), Js('s'), Js('r'), Js('t'), Js('th')]))
var.put('nm9', Js([Js('b'), Js('br'), Js('bh'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sr'), Js('st'), Js('str'), Js('t'), Js('thr'), Js('tr'), Js('v'), Js('w'), Js('y'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('y'), Js('y')]))
var.put('nm11', Js([Js('b'), Js('bb'), Js('bh'), Js('bm'), Js('bn'), Js('br'), Js('cd'), Js('cm'), Js('cn'), Js('cr'), Js('cw'), Js('d'), Js('dd'), Js('dg'), Js('dl'), Js('dm'), Js('dn'), Js('dr'), Js('dw'), Js('g'), Js('gd'), Js('gg'), Js('gl'), Js('gm'), Js('gn'), Js('gr'), Js('gv'), Js('gw'), Js('h'), Js('hg'), Js('hl'), Js('hn'), Js('k'), Js('kk'), Js('kl'), Js('kn'), Js('l'), Js('lb'), Js('lbr'), Js('ld'), Js('ldr'), Js('lg'), Js('lgr'), Js('lgw'), Js('lk'), Js('ll'), Js('lm'), Js('lw'), Js('m'), Js('md'), Js('mg'), Js('mgw'), Js('mm'), Js('mr'), Js('mw'), Js('n'), Js('nd'), Js('ndr'), Js('nf'), Js('ng'), Js('ngr'), Js('ngv'), Js('nm'), Js('nn'), Js('nngv'), Js('nr'), Js('nth'), Js('nw'), Js('r'), Js('rb'), Js('rd'), Js('rg'), Js('rgr'), Js('rgw'), Js('rl'), Js('rs'), Js('rst'), Js('s'), Js('ss'), Js('tr'), Js('v'), Js('vl'), Js('vr'), Js('z'), Js('zb'), Js('zd'), Js('zl'), Js('zm'), Js('zw')]))
var.put('nm12', Js([Js('b'), Js('c'), Js('ck'), Js('d'), Js('dd'), Js('g'), Js('h'), Js('k'), Js('l'), Js('ll'), Js('ls'), Js('ld'), Js('m'), Js('n'), Js('mn'), Js('r'), Js('rd'), Js('rsk'), Js('rg'), Js('s'), Js('t'), Js('th')]))
var.put('nm13', Js([Js('Amber'), Js('Axe'), Js('Battle'), Js('Black'), Js('Blaze'), Js('Boulder'), Js('Bright'), Js('Bronze'), Js('Cinder'), Js('Cloud'), Js('Cold'), Js('Common'), Js('Crag'), Js('Dark'), Js('Deep'), Js('Dew'), Js('Earth'), Js('Ember'), Js('Fair'), Js('Fire'), Js('Fist'), Js('Flame'), Js('Flat'), Js('Flint'), Js('Free'), Js('Full'), Js('Fuse'), Js('Gold'), Js('Grand'), Js('Great'), Js('Hammer'), Js('Hard'), Js('Heavy'), Js('High'), Js('Humble'), Js('Iron'), Js('Keen'), Js('Lone'), Js('Low'), Js('Molten'), Js('Noble'), Js('Plain'), Js('Pride'), Js('Proud'), Js('Pyre'), Js('Rock'), Js('Rumble'), Js('Shield'), Js('Silent'), Js('Simple'), Js('Single'), Js('Soft'), Js('Solid'), Js('Steel'), Js('Stern'), Js('Stone'), Js('Storm'), Js('Stout'), Js('Strong'), Js('Terra'), Js('Thunder'), Js('Titan'), Js('True'), Js('War'), Js('Wild'), Js('Winter'), Js('Wise')]))
var.put('nm14', Js([Js('arm'), Js('bash'), Js('beam'), Js('beard'), Js('belly'), Js('bend'), Js('blaze'), Js('bluff'), Js('bough'), Js('brace'), Js('brand'), Js('breath'), Js('brew'), Js('brow'), Js('crest'), Js('crusher'), Js('dew'), Js('fall'), Js('fell'), Js('flare'), Js('flow'), Js('force'), Js('forge'), Js('fury'), Js('gaze'), Js('gem'), Js('gleam'), Js('glide'), Js('glow'), Js('grip'), Js('guard'), Js('gut'), Js('hair'), Js('hand'), Js('heart'), Js('helm'), Js('hide'), Js('horn'), Js('ingot'), Js('mane'), Js('mantle'), Js('maul'), Js('might'), Js('more'), Js('pelt'), Js('punch'), Js('ridge'), Js('roar'), Js('scar'), Js('shade'), Js('shadow'), Js('shard'), Js('shot'), Js('shout'), Js('sky'), Js('snow'), Js('spark'), Js('steam'), Js('strength'), Js('stride'), Js('strike'), Js('surge'), Js('sword'), Js('thorn'), Js('track'), Js('ward')]))
pass
pass


# Add lib to the module scope
pathfinderDwarf = var.to_python()