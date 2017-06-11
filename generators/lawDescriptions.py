__all__ = ['lawDescriptions']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'rnd15', 'rnd11', 'rnd8', 'name', 'name7', 'nm3', 'rnd14', 'name3', 'name6', 'name9', 'rnd2', 'br', 'name2', 'name4', 'rnd5', 'rnd4', 'rnd7', 'name8', 'result', 'rnd6', 'rnd13', 'rnd3', 'name5', 'rnd10', 'rnd9', 'rnd12', 'rnd1'])
    var.put('nm1', Js([Js('local'), Js('federal'), Js('state'), Js('national'), Js('regional'), Js('international'), Js('provincial'), Js('territorial'), Js('community')]))
    var.put('nm3', Js([Js('a brief prison sentence'), Js('a high fine'), Js('a long term exile'), Js('a long term prison sentence'), Js('a low fine'), Js('a moderate fine'), Js('a moderate term exile'), Js('a moderate term prison sentence'), Js('a paddling'), Js('a short term exile'), Js('a short term prison sentence'), Js('a stern warning'), Js('a warning'), Js("an 'eye for an eye'"), Js('bodily harm'), Js('branding'), Js('brief public service'), Js('compensation to the victims in cash'), Js('compensation to the victims in servitude'), Js('execution'), Js('exile for life'), Js('imprisonment for life'), Js('incapacitation that prevent repeats of this crime'), Js('long term forced rehabilitation'), Js('long term public service'), Js('long term servitude'), Js('loss of civil privileges'), Js('medium term forced rehabilitation'), Js('long term solitary confinement'), Js('medium term solitary confinement'), Js('short term solitary confinement'), Js('moderate term public service'), Js('moderate term servitude'), Js('public humiliation'), Js('short term forced rehabilitation'), Js('short term public service'), Js('short term servitude'), Js('whatever the wheel of justice lands on')]))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('name', ((((((Js('This ')+var.get('nm1').get(var.get('rnd1')))+Js(' law dictates all those found guilty of '))+var.get('nm2').get(var.get('rnd2')))+Js(' will face the punishment of '))+var.get('nm3').get(var.get('rnd3')))+Js('.')))
    var.put('name2', Js('----------------------------'))
    var.put('name3', ((((((Js('This ')+var.get('nm1').get(var.get('rnd4')))+Js(' law dictates all those found guilty of '))+var.get('nm2').get(var.get('rnd5')))+Js(' will face the punishment of '))+var.get('nm3').get(var.get('rnd6')))+Js('.')))
    var.put('name4', Js('----------------------------'))
    var.put('name5', ((((((Js('This ')+var.get('nm1').get(var.get('rnd7')))+Js(' law dictates all those found guilty of '))+var.get('nm2').get(var.get('rnd8')))+Js(' will face the punishment of '))+var.get('nm3').get(var.get('rnd9')))+Js('.')))
    var.put('name6', Js('----------------------------'))
    var.put('name7', ((((((Js('This ')+var.get('nm1').get(var.get('rnd10')))+Js(' law dictates all those found guilty of '))+var.get('nm2').get(var.get('rnd11')))+Js(' will face the punishment of '))+var.get('nm3').get(var.get('rnd12')))+Js('.')))
    var.put('name8', Js('----------------------------'))
    var.put('name9', ((((((Js('This ')+var.get('nm1').get(var.get('rnd13')))+Js(' law dictates all those found guilty of '))+var.get('nm2').get(var.get('rnd14')))+Js(' will face the punishment of '))+var.get('nm3').get(var.get('rnd15')))+Js('.')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(8.0)):
        try:
            pass
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
lawDescriptions = var.to_python()