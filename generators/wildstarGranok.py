__all__ = ['wildstarGranok']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            while PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm10').get(var.get('rnd7'))):
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('lname', (var.get('nm9').get(var.get('rnd6'))+var.get('nm10').get(var.get('rnd7'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(' '))+var.get('lname')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+Js(' '))+var.get('lname')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lname')))
                else:
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lname')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('br'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('q'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('g'), Js('gg'), Js('gn'), Js('k'), Js('kn'), Js('kk'), Js('lk'), Js('lg'), Js('r'), Js('rr'), Js('rk'), Js('rg'), Js('rv'), Js('rz'), Js('rd'), Js('rb'), Js('v'), Js('z'), Js('zk'), Js('zg')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('ll'), Js('r'), Js('s'), Js('z')]))
var.put('nm5', Js([Js('ch'), Js('d'), Js('f'), Js('h'), Js('j'), Js('k'), Js('l'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('o')]))
var.put('nm7', Js([Js('dk'), Js('dr'), Js('fk'), Js('fr'), Js('gn'), Js('kn'), Js('kr'), Js('kz'), Js('x'), Js('lk'), Js('lr'), Js('lg'), Js('lz'), Js('rv'), Js('rs'), Js('rz'), Js('rd'), Js('rb'), Js('sk'), Js('sh'), Js('sv'), Js('st'), Js('sr'), Js('v'), Js('vk'), Js('z'), Js('zk')]))
var.put('nm8', Js([Js('h'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('s'), Js('ss'), Js('t'), Js('tt'), Js('z')]))
var.put('nm9', Js([Js('blast'), Js('bleak'), Js('bone'), Js('boulder'), Js('brutal'), Js('bulk'), Js('burst'), Js('cold'), Js('crack'), Js('crag'), Js('crash'), Js('dark'), Js('deep'), Js('doom'), Js('ember'), Js('fight'), Js('fire'), Js('firm'), Js('fist'), Js('flame'), Js('force'), Js('frost'), Js('grand'), Js('grim'), Js('hard'), Js('ice'), Js('iron'), Js('long'), Js('metal'), Js('power'), Js('red'), Js('rigid'), Js('shadow'), Js('slab'), Js('slam'), Js('slate'), Js('smash'), Js('stark'), Js('steel'), Js('stern'), Js('stone'), Js('stout'), Js('strong'), Js('stubborn'), Js('ten'), Js('thunder'), Js('timber'), Js('titan'), Js('tough'), Js('vault')]))
var.put('nm10', Js([Js('bend'), Js('blaze'), Js('blight'), Js('bough'), Js('breaker'), Js('brow'), Js('burst'), Js('buster'), Js('clash'), Js('crag'), Js('crest'), Js('crusher'), Js('cut'), Js('down'), Js('dream'), Js('fall'), Js('flake'), Js('force'), Js('fury'), Js('grip'), Js('guard'), Js('heart'), Js('horn'), Js('hunter'), Js('keep'), Js('keeper'), Js('lash'), Js('mark'), Js('master'), Js('might'), Js('more'), Js('prime'), Js('quake'), Js('rage'), Js('reaper'), Js('rend'), Js('ridge'), Js('right'), Js('roar'), Js('runner'), Js('shade'), Js('shadow'), Js('shard'), Js('shatter'), Js('shout'), Js('sky'), Js('sliver'), Js('smasher'), Js('snap'), Js('song'), Js('sorrow'), Js('spell'), Js('spire'), Js('spirit'), Js('splinter'), Js('split'), Js('splitter'), Js('storm'), Js('stride'), Js('strike'), Js('thorn'), Js('track'), Js('trap'), Js('valor'), Js('walker'), Js('ward'), Js('watcher')]))
pass
pass


# Add lib to the module scope
wildstarGranok = var.to_python()