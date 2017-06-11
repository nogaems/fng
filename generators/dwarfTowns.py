__all__ = ['dwarfTowns']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('D'), Js('Dh'), Js('Bh'), Js('G'), Js('H'), Js('K'), Js('Kh'), Js('M'), Js('N'), Js('Th'), Js('V')]))
var.put('nm2', Js([Js('ag'), Js('agh'), Js('al'), Js('am'), Js('an'), Js('ar'), Js('arn'), Js('eg'), Js('egh'), Js('el'), Js('em'), Js('en'), Js('er'), Js('ern'), Js('ig'), Js('igh'), Js('il'), Js('im'), Js('in'), Js('ir'), Js('irn'), Js('og'), Js('ogh'), Js('ol'), Js('om'), Js('on'), Js('or'), Js('orn'), Js('ug'), Js('ugh'), Js('ul'), Js('um'), Js('un'), Js('ur'), Js('urn')]))
var.put('nm3', Js([Js(' Badihr'), Js(' Badir'), Js(' Baduhr'), Js(' Badur'), Js(' Boldahr'), Js(' Boldar'), Js(' Boldihr'), Js(' Boldir'), Js(' Boldohr'), Js(' Boldor'), Js(' Boram'), Js(' Boramm'), Js(' Borim'), Js(' Borimm'), Js(' Buldahr'), Js(' Buldar'), Js(' Buldihr'), Js(' Buldohr'), Js(' Buldor'), Js(' Burim'), Js(' Burimm'), Js(' Darahl'), Js(' Daral'), Js(' Darihm'), Js(' Darim'), Js(' Darohm'), Js(' Darom'), Js(' Daruhl'), Js(' Daruhm'), Js(' Darul'), Js(' Darum'), Js(' Dorahl'), Js(' Doral'), Js(' Doruhl'), Js(' Dorul'), Js(' Durahl'), Js(' Dural'), Js(' Faldihr'), Js(' Faldir'), Js(' Falduhr'), Js(' Faldur'), Js(' Faruhm'), Js(' Farum'), Js(' Furuhm'), Js(' Furum'), Js(' Garohm'), Js(' Garom'), Js(' Garuhm'), Js(' Garum'), Js(' Gurihm'), Js(' Guruhm'), Js(' Gurum'), Js(' Kahldur'), Js(' Kalduhr'), Js(' Kohldur'), Js(' Kolduhr'), Js(' Kuldihr'), Js(' Kuldir'), Js(' Kuldohr'), Js(' Kuldor'), Js(' Laduhr'), Js(' Ladur'), Js(' Lodahr'), Js(' Lodar'), Js(' Lodihr'), Js(' Lodir'), Js(' Loduhr'), Js(' Lodur'), Js(' Maldir'), Js(' Malduhr'), Js(' Maldur'), Js(' Moldir'), Js(' Molduhr'), Js(' Moldur'), Js(' Olihm'), Js(' Oluhm'), Js(' Tarihr'), Js(' Taruhm'), Js(' Taruhr'), Js(' Tarum'), Js(' Tharim'), Js(' Tharum'), Js(' Thoram'), Js(' Thorim'), Js(' Thorum'), Js(' Thurim'), Js(' Thurum'), Js(' Todihr'), Js(' Todir'), Js(' Toduhr'), Js(' Todur'), Js(' Toruhm'), Js(' Torum'), Js(' Turuhm'), Js(' Turum'), Js(' Ulihm'), Js(' Uluhm'), Js(' Ulum'), Js(' Wahrum'), Js(' Wohrum'), Js(' Wuhrum'), Js('ahm'), Js('alduhr'), Js('aldur'), Js('am'), Js('aruhm'), Js('arum'), Js('badihr'), Js('badir'), Js('baduhr'), Js('badur'), Js('bihr'), Js('bohr'), Js('boldahr'), Js('boldar'), Js('boldihr'), Js('boldir'), Js('boldohr'), Js('boldor'), Js('bor'), Js('boram'), Js('boramm'), Js('borim'), Js('borimm'), Js('buhr'), Js('buldahr'), Js('buldar'), Js('buldihr'), Js('buldohr'), Js('buldor'), Js('bur'), Js('burim'), Js('burimm'), Js('dahn'), Js('dan'), Js('darahl'), Js('daral'), Js('darihm'), Js('darim'), Js('darohm'), Js('darom'), Js('darth'), Js('daruhl'), Js('daruhm'), Js('darul'), Js('darum'), Js('dihm'), Js('dihr'), Js('dim'), Js('dirth'), Js('dohr'), Js('dor'), Js('dorahl'), Js('doral'), Js('dorth'), Js('doruhl'), Js('dorul'), Js('duahr'), Js('duar'), Js('duhm'), Js('duhn'), Js('duhr'), Js('dum'), Js('dun'), Js('dur'), Js('durahl'), Js('dural'), Js('eduhr'), Js('edur'), Js('elduhr'), Js('eldur'), Js('eruhm'), Js('erum'), Js('faldihr'), Js('faldir'), Js('falduhr'), Js('faldur'), Js('faruhm'), Js('farum'), Js('fuhn'), Js('furuhm'), Js('furum'), Js('galir'), Js('galor'), Js('gan'), Js('gari'), Js('garohm'), Js('garom'), Js('garuhm'), Js('garum'), Js('golar'), Js('golir'), Js('gon'), Js('gran'), Js('grim'), Js('grin'), Js('grom'), Js('gron'), Js('grum'), Js('grun'), Js('gulir'), Js('gulor'), Js('gurihm'), Js('guruhm'), Js('gurum'), Js('heim'), Js('kahldur'), Js('kahm'), Js('kalduhr'), Js('kihm'), Js('kohldur'), Js('kohm'), Js('kolduhr'), Js('kuhm'), Js('kuldihr'), Js('kuldir'), Js('kuldohr'), Js('kuldor'), Js('laduhr'), Js('ladur'), Js('lodahr'), Js('lodar'), Js('lodihr'), Js('lodir'), Js('loduhr'), Js('lodur'), Js('olduhr'), Js('oldur'), Js('olihm'), Js('oluhm'), Js('oluhr'), Js('olur'), Js('ragh'), Js('rahm'), Js('ram'), Js('rhia'), Js('ria'), Js('righ'), Js('rihm'), Js('rim'), Js('rogh'), Js('rugh'), Js('ruhm'), Js('rum'), Js('tarihr'), Js('taruhm'), Js('taruhr'), Js('tarum'), Js('thiad'), Js('thiod'), Js('tihrm'), Js('tirm'), Js('todihr'), Js('todir'), Js('toduhr'), Js('todur'), Js('torhm'), Js('torm'), Js('toruhm'), Js('torum'), Js('tuhrm'), Js('turm'), Js('turuhm'), Js('turum'), Js('uhm'), Js('ulihm'), Js('ulihr'), Js('ulir'), Js('uluhm'), Js('uluhr'), Js('ulum'), Js('ulur'), Js('um'), Js('wahr'), Js('wahrum'), Js('wihr'), Js('wohr'), Js('wohrum'), Js('wuhr'), Js('wuhrum'), Js('yahr'), Js('yar'), Js('yaruhm'), Js('yuhr'), Js('yur')]))
pass
pass


# Add lib to the module scope
dwarfTowns = var.to_python()