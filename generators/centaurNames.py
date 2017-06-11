__all__ = ['centaurNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        def PyJs_LONG_0_(var=var):
            return var.put('names4', Js([Js('a'), Js('acea'), Js('aea'), Js('aenna'), Js('aeno'), Js('aia'), Js('alia'), Js('allo'), Js('ania'), Js('anke'), Js('aope'), Js('apso'), Js('ar'), Js('arge'), Js('astea'), Js('ato'), Js('e'), Js('ea'), Js('eia'), Js('eis'), Js('eles'), Js('elete'), Js('eme'), Js('emis'), Js('ena'), Js('ene'), Js('enope'), Js('era'), Js('eria'), Js('eris'), Js('erope'), Js('eros'), Js('ese'), Js('esia'), Js('eso'), Js('eta'), Js('ete'), Js('ethe'), Js('etis'), Js('etna'), Js('eto'), Js('etope'), Js('ia'), Js('iae'), Js('idia'), Js('ieia'), Js('inoe'), Js('inthe'), Js('io'), Js('ione'), Js('iope'), Js('is'), Js('ite'), Js('ithea'), Js('o'), Js('oe'), Js('oebe'), Js('oina'), Js('ois'), Js('ole'), Js('olpe'), Js('on'), Js('ona'), Js('one'), Js('onis'), Js('oosa'), Js('ope'), Js('orie'), Js('oris'), Js('osia'), Js('osie'), Js('osyne'), Js('othoe'), Js('ousa'), Js('us'), Js('ybia'), Js('yia'), Js('ylla'), Js('ynome'), Js('yo'), Js('yone'), Js('ypso'), Js('ys'), Js('ytie'), Js('yx')]))
        PyJs_LONG_0_()
        def PyJs_LONG_1_(var=var):
            return var.put('names5', Js([Js('belle'), Js('bes'), Js('both'), Js('cris'), Js('cith'), Js('cise'), Js('dine'), Js('dim'), Js('dol'), Js('flin'), Js('fone'), Js('fran'), Js('grin'), Js('gone'), Js('gana'), Js('hine'), Js('hoth'), Js('hante'), Js('kine'), Js('kres'), Js('koe'), Js('lynn'), Js('lore'), Js('less'), Js('melle'), Js('mine'), Js('mare'), Js('nine'), Js('nith'), Js('nys'), Js('pris'), Js('plix'), Js('pione'), Js('phine'), Js('phes'), Js('phe'), Js('renne'), Js('rila'), Js('rone'), Js('syla'), Js('sin'), Js('sane'), Js('trix'), Js('tyne'), Js('toph'), Js('vina'), Js('vera'), Js('vin'), Js('wyn'), Js('wane'), Js('woth'), Js('zyna'), Js('zora'), Js('zith')]))
        PyJs_LONG_1_()
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((var.get('nm6').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('A'), Js('Ar'), Js('Al'), Js('B'), Js('Br'), Js('Bl'), Js('C'), Js('Cr'), Js('Cl'), Js('D'), Js('Dl'), Js('Dr'), Js('E'), Js('Er'), Js('El'), Js('F'), Js('Fl'), Js('G'), Js('Gl'), Js('Gr'), Js('H'), Js('I'), Js('Il'), Js('J'), Js('K'), Js('Kl'), Js('Kr'), Js('L'), Js('M'), Js('N'), Js('O'), Js('Or'), Js('Ol'), Js('P'), Js('Pl'), Js('Ph'), Js('Pr'), Js('R'), Js('S'), Js('Sl'), Js('Str'), Js('T'), Js('Tr'), Js('U'), Js('Ur'), Js('Ul'), Js('V'), Js('Vr'), Js('W'), Js('Wr'), Js('X'), Js('Z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z')]))
var.put('nm4', Js([Js('aemon'), Js('aenon'), Js('aeon'), Js('aestus'), Js('aeus'), Js('agos'), Js('aios'), Js('anes'), Js('anos'), Js('antos'), Js('aon'), Js('arus'), Js('as'), Js('ates'), Js('atos'), Js('aumas'), Js('eas'), Js('eidon'), Js('er'), Js('erion'), Js('erus'), Js('es'), Js('etheus'), Js('etus'), Js('eus'), Js('ias'), Js('ibos'), Js('ion'), Js('ios'), Js('is'), Js('iton'), Js('ius'), Js('o'), Js('oeis'), Js('oeus'), Js('olus'), Js('on'), Js('onos'), Js('or'), Js('os'), Js('oteus'), Js('otos'), Js('otus'), Js('ous'), Js('us'), Js('yrus'), Js('ys'), Js('ytion')]))
var.put('nm5', Js([Js('bor'), Js('ban'), Js('bran'), Js('cron'), Js('carn'), Js('crin'), Js('dral'), Js('dor'), Js('dall'), Js('fin'), Js('furn'), Js('fan'), Js('gran'), Js('gone'), Js('glan'), Js('hum'), Js('hurn'), Js('harm'), Js('krol'), Js('kall'), Js('kule'), Js('lorn'), Js('lans'), Js('lath'), Js('moth'), Js('morn'), Js('merth'), Js('nirn'), Js('noth'), Js('nall'), Js('pas'), Js('poth'), Js('pos'), Js('rall'), Js('roth'), Js('rorn'), Js('sal'), Js('sor'), Js('sul'), Js('stral'), Js('storn'), Js('stag'), Js('thorn'), Js('tral'), Js('turn'), Js('vral'), Js('vor'), Js('vil'), Js('will'), Js('wor'), Js('warn'), Js('zran'), Js('zorn'), Js('zark')]))
var.put('nm6', Js([Js('A'), Js('Ar'), Js('Al'), Js('B'), Js('Br'), Js('Bl'), Js('C'), Js('Cr'), Js('Cl'), Js('D'), Js('Dr'), Js('E'), Js('Er'), Js('El'), Js('F'), Js('Fl'), Js('G'), Js('Gl'), Js('Gr'), Js('H'), Js('I'), Js('Il'), Js('J'), Js('K'), Js('Kl'), Js('Kr'), Js('L'), Js('M'), Js('N'), Js('O'), Js('Or'), Js('Ol'), Js('P'), Js('Pl'), Js('Ph'), Js('Pr'), Js('R'), Js('S'), Js('Sl'), Js('Str'), Js('T'), Js('Tr'), Js('U'), Js('Ur'), Js('Ul'), Js('V'), Js('Vr'), Js('W'), Js('Wr'), Js('X'), Js('Z')]))
var.put('nm7', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
centaurNames = var.to_python()