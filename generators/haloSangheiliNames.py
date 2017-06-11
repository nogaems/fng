__all__ = ['haloSangheiliNames']

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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+Js(" '"))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js(" '"))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('gr'), Js('j'), Js('k'), Js('kh'), Js('l'), Js('mr'), Js("n'th"), Js('r'), Js('rt'), Js('s'), Js('t'), Js('th'), Js('v'), Js('x'), Js('z'), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm3', Js([Js('da'), Js('do'), Js('g'), Js('ga'), Js('ha'), Js('ka'), Js('kan'), Js('ko'), Js('l'), Js('la'), Js('pa'), Js('po'), Js('r'), Js('ra'), Js('re'), Js('ro'), Js('s'), Js('sa'), Js('san'), Js('so'), Js('sze'), Js('t'), Js('ta'), Js('tan'), Js('to'), Js('va'), Js('vo'), Js('vu'), Js('za'), Js('ze'), Js('zo')]))
var.put('nm4', Js([Js('Cha'), Js('Da'), Js('Dra'), Js('Ga'), Js('Go'), Js('Ha'), Js('Ka'), Js('Ko'), Js('Kra'), Js('Ku'), Js('La'), Js('Lo'), Js('Lu'), Js('Ma'), Js('Mda'), Js('Mo'), Js('Mu'), Js('Na'), Js('Nra'), Js('Nu'), Js('Ra'), Js('Re'), Js('Ro'), Js('Sa'), Js('Sra'), Js('Su'), Js('Ta'), Js('Te'), Js('Tra'), Js('Tu'), Js('Va'), Js('Vo'), Js('Vra'), Js('Vu'), Js('Wa'), Js('Za'), Js('Zo'), Js('Zu')]))
var.put('nm5', Js([Js('cam'), Js('dam'), Js('dom'), Js('dum'), Js('fam'), Js('fum'), Js('gam'), Js('gram'), Js('gum'), Js('ham'), Js('hom'), Js('kam'), Js('lcam'), Js('lkam'), Js('ma'), Js('man'), Js('nam'), Js('ngam'), Js('nom'), Js('ntak'), Js('ralum'), Js('ram'), Js('rom'), Js('rum'), Js('sam'), Js('sov'), Js('sum'), Js('tam'), Js('tan'), Js('ttin'), Js('tum'), Js('vam'), Js('vum'), Js('zam'), Js('zum')]))
var.put('nm6', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('h'), Js('g'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('sh'), Js('s'), Js('t'), Js('th'), Js('v'), Js('x'), Js('z')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('o'), Js('u')]))
var.put('nm8', Js([Js('ea'), Js('ha'), Js('he'), Js('ia'), Js('ie'), Js('io'), Js('la'), Js('le'), Js('lo'), Js('ma'), Js('me'), Js('mi'), Js('mo'), Js('n'), Js('na'), Js('ne'), Js('pa'), Js('sa'), Js('se'), Js('sha'), Js('she'), Js('so'), Js('wa'), Js('we'), Js('xa'), Js('xe'), Js('xi'), Js('ya'), Js('ye'), Js('yo')]))
var.put('nm9', Js([Js(''), Js(''), Js('ee'), Js(''), Js('ai')]))
pass
pass


# Add lib to the module scope
haloSangheiliNames = var.to_python()