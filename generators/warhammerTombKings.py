__all__ = ['warhammerTombKings']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('nameL', (Js(' the ')+var.get('nm8').get(var.get('rnd'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nameL')))
                else:
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nameL')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('rnd')<Js(4.0)):
                    while (var.get('rnd5')<Js(2.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nameL')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+var.get('nameL')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('f'), Js('h'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('i'), Js('i')]))
var.put('nm3', Js([Js('b'), Js('ch'), Js('f'), Js('h'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('mh'), Js('n'), Js('p'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('y'), Js('b'), Js('bd'), Js('ch'), Js('ct'), Js('f'), Js('h'), Js('k'), Js('kh'), Js('kht'), Js('kt'), Js('l'), Js('m'), Js('mh'), Js('mkh'), Js('mt'), Js('n'), Js('nkh'), Js('ns'), Js('p'), Js('ph'), Js('phk'), Js('phr'), Js('pht'), Js('pr'), Js('pth'), Js('r'), Js('rkh'), Js('rs'), Js('rt'), Js('s'), Js('sf'), Js('sh'), Js('shk'), Js('skh'), Js('sph'), Js('ss'), Js('st'), Js('t'), Js('th'), Js('tm'), Js('tr'), Js('ttr'), Js('y')]))
var.put('nm4', Js([Js(''), Js(''), Js('f'), Js('h'), Js('kh'), Js('m'), Js('n'), Js('nb'), Js('p'), Js('ph'), Js('r'), Js('rs'), Js('s')]))
var.put('nm5', Js([Js('b'), Js('h'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('o')]))
var.put('nm7', Js([Js('b'), Js('d'), Js('f'), Js('fr'), Js('g'), Js('gt'), Js('gh'), Js('h'), Js('k'), Js('kh'), Js('kt'), Js('l'), Js('m'), Js('mkh'), Js('mph'), Js('n'), Js('nkh'), Js('nph'), Js('nth'), Js('nkhn'), Js('ns'), Js('nt'), Js('p'), Js('ph'), Js('phr'), Js('pth'), Js('r'), Js('rh'), Js('rm'), Js('rt'), Js('ry'), Js('s'), Js('st'), Js('t'), Js('tr'), Js('th'), Js('thy'), Js('y'), Js('z'), Js('zh')]))
var.put('nm8', Js([Js('Academic'), Js('Acclaimed'), Js('Adept'), Js('Ambitious'), Js('Ancient'), Js('Architect'), Js('Artist'), Js('Austere'), Js('Black'), Js('Blessed'), Js('Bright'), Js('Brilliant'), Js('Celebrated'), Js('Chaste'), Js('Composed'), Js('Conjurer'), Js('Content'), Js('Crimson'), Js('Cunning'), Js('Devoted'), Js('Diligent'), Js('Earnest'), Js('Educated'), Js('Elegant'), Js('Enchanted'), Js('Enlightened'), Js('Euphoric'), Js('Exalted'), Js('Flawless'), Js('Generous'), Js('Gifted'), Js('Giving'), Js('Glorious'), Js('Graceful'), Js('Grand'), Js('Great'), Js('Hallowed'), Js('Herald'), Js('Hierpohant'), Js('Holy'), Js('Honorable'), Js('Honored'), Js('Humble'), Js('Idealist'), Js('Illustrious'), Js('Immortal'), Js('Imperishable'), Js('Incredible'), Js('Infinite'), Js('Knowing'), Js('Learned'), Js('Light'), Js('Loyal'), Js('Magnificent'), Js('Majestic'), Js('Marvelous'), Js('Oracle'), Js('Paragon'), Js('Patient'), Js('Powerful'), Js('Prestigious'), Js('Prime'), Js('Prophet'), Js('Soothsayer'), Js('Sophisticated'), Js('Terrific'), Js('Treasure'), Js('Treasured'), Js('Valiant'), Js('Visionary'), Js('Watcher'), Js('White'), Js('Zealous')]))
pass
pass


# Add lib to the module scope
warhammerTombKings = var.to_python()