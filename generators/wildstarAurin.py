__all__ = ['wildstarAurin']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            while PyJsStrictEq(var.get('nm8').get(var.get('rnd6')),var.get('nm9').get(var.get('rnd7'))):
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('lname', (var.get('nm8').get(var.get('rnd6'))+var.get('nm9').get(var.get('rnd7'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(' '))+var.get('lname')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lname')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('d'), Js('f'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('r'), Js('t'), Js('v')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('y')]))
var.put('nm3', Js([Js('b'), Js('ff'), Js('h'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('r'), Js('rv'), Js('rl'), Js('v'), Js('w'), Js('z')]))
var.put('nm4', Js([Js('l'), Js('ll'), Js('n'), Js('nn'), Js('r'), Js('s')]))
var.put('nm5', Js([Js('d'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('w')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('ya'), Js('ia')]))
var.put('nm7', Js([Js('h'), Js('ff'), Js('hn'), Js('hl'), Js('l'), Js('ll'), Js('ln'), Js('lm'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('r'), Js('rs'), Js('rl'), Js('rn'), Js('rm'), Js('s'), Js('sh'), Js('ss'), Js('w')]))
var.put('nm8', Js([Js('amber'), Js('autumn'), Js('blue'), Js('bright'), Js('comet'), Js('dawn'), Js('day'), Js('dew'), Js('dusk'), Js('ember'), Js('even'), Js('ever'), Js('far'), Js('feather'), Js('fire'), Js('flame'), Js('fog'), Js('forest'), Js('green'), Js('lake'), Js('leaf'), Js('light'), Js('luna'), Js('lunar'), Js('mirth'), Js('mist'), Js('moon'), Js('morning'), Js('moss'), Js('night'), Js('ocean'), Js('opal'), Js('rain'), Js('red'), Js('river'), Js('rose'), Js('ruby'), Js('shadow'), Js('silver'), Js('sky'), Js('solar'), Js('stem'), Js('still'), Js('storm'), Js('summer'), Js('sun'), Js('twilight'), Js('water'), Js('wild'), Js('wind'), Js('winter'), Js('wood')]))
var.put('nm9', Js([Js('bloom'), Js('blossom'), Js('blower'), Js('branch'), Js('breath'), Js('breeze'), Js('brook'), Js('cloud'), Js('clouds'), Js('dance'), Js('drift'), Js('fall'), Js('flame'), Js('flock'), Js('flower'), Js('gaze'), Js('gazer'), Js('grass'), Js('heart'), Js('lead'), Js('leaf'), Js('mind'), Js('petal'), Js('root'), Js('shade'), Js('shine'), Js('sky'), Js('snow'), Js('song'), Js('spirit'), Js('spyre'), Js('stalk'), Js('star'), Js('strike'), Js('swift'), Js('thorn'), Js('vale'), Js('walk'), Js('watch'), Js('whisper'), Js('wing')]))
pass
pass


# Add lib to the module scope
wildstarAurin = var.to_python()