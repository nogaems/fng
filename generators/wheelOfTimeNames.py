__all__ = ['wheelOfTimeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
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
            if PyJsStrictEq(var.get('type'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', ((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+Js(' '))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ad'), Js('Al'), Js('Ar'), Js('Art'), Js('B'), Js('Ben'), Js('Ber'), Js('Bin'), Js('C'), Js('Cal'), Js('Coul'), Js('Cul'), Js('Eam'), Js('El'), Js('Er'), Js('Ert'), Js('G'), Js('Gaid'), Js('Galv'), Js('Gar'), Js('J'), Js('Jan'), Js('Jand'), Js('Jul'), Js('K'), Js('Kal'), Js('Ken'), Js('L'), Js('Laer'), Js('Lan'), Js('Lest'), Js('Mas'), Js('Mat'), Js('Matt'), Js('Maz'), Js('Nad'), Js('Nal'), Js('Ner'), Js('Nor'), Js('Ol'), Js('Olv'), Js('Ond'), Js('Os'), Js('P'), Js('Pad'), Js('Pel'), Js('Per'), Js('R'), Js('Ran'), Js('Reld'), Js('Rh'), Js('S'), Js('Sal'), Js('Sar'), Js('Sil'), Js('T'), Js('Th'), Js('Ther'), Js('Tor'), Js('Val'), Js('Vend'), Js('Ver'), Js('Vor'), Js('Z'), Js('Zan'), Js('Zol'), Js('Zor')]))
var.put('nm2', Js([Js('adin'), Js('ain'), Js('al'), Js('am'), Js('an'), Js('and'), Js('ar'), Js('as'), Js('ath'), Js('aul'), Js('ean'), Js('el'), Js('em'), Js('ema'), Js('en'), Js('eon'), Js('er'), Js('erin'), Js('esean'), Js('eth'), Js('ian'), Js('il'), Js('im'), Js('in'), Js('inan'), Js('inean'), Js('inen'), Js('ion'), Js('iren'), Js('is'), Js('od'), Js('oial'), Js('ol'), Js('om'), Js('on'), Js('orin'), Js('orn'), Js('oth'), Js('oul'), Js('ovin'), Js('ral'), Js('ran'), Js('ren'), Js('rim'), Js('ris'), Js('uan'), Js('uarc'), Js('uen'), Js('uin'), Js('ulin'), Js('um'), Js('un'), Js('ur'), Js('us'), Js('uth'), Js('yas'), Js('yel'), Js('yin'), Js('yom'), Js('yor')]))
var.put('nm3', Js([Js('Al'), Js('Am'), Js('Ar'), Js('Av'), Js('B'), Js('Bel'), Js('Birg'), Js('Brin'), Js('Cads'), Js('Cel'), Js('Ch'), Js('Cyn'), Js('Den'), Js('Dil'), Js('Dol'), Js('Dyn'), Js('Egw'), Js('El'), Js('En'), Js('Er'), Js('F'), Js('Fel'), Js('Fern'), Js('Fil'), Js('Gem'), Js('Gil'), Js('Gin'), Js('Gwen'), Js('Haen'), Js('Han'), Js('Hel'), Js('Hin'), Js('Ien'), Js('Il'), Js('In'), Js('Ir'), Js('Kel'), Js('Ken'), Js('Khon'), Js('Kis'), Js('Lem'), Js('Len'), Js('Lis'), Js('Lor'), Js('M'), Js('Mel'), Js('Mor'), Js('Morg'), Js('Nel'), Js('Nic'), Js('Nor'), Js('Nyn'), Js('Rel'), Js('Ren'), Js('Rin'), Js('Ros'), Js('S'), Js('Sel'), Js('Set'), Js('Som'), Js('Sor'), Js('T'), Js('Ten'), Js('Ther'), Js('Tigr'), Js('V'), Js('Vel'), Js('Vil'), Js('Von'), Js('Zar'), Js('Zel'), Js('Zer'), Js('Zon')]))
var.put('nm4', Js([Js('aeve'), Js('aida'), Js('aile'), Js('ain'), Js('aine'), Js('alle'), Js('ase'), Js('athera'), Js('ava'), Js('ayne'), Js('ela'), Js('elle'), Js('ena'), Js('ene'), Js('enya'), Js('era'), Js('erava'), Js('esh'), Js('eshta'), Js('eth'), Js('ia'), Js('iad'), Js('iendha'), Js('ilea'), Js('in'), Js('inea'), Js('ith'), Js('itte'), Js('iuan'), Js('ivia'), Js('oane'), Js('oell'), Js('ois'), Js('oith'), Js('ola'), Js('one'), Js('ora'), Js('osa'), Js('ovi'), Js('oyin'), Js('ua'), Js('uane'), Js('ucia'), Js('uel'), Js('uena'), Js('uene'), Js('uis'), Js('ulin'), Js('uon'), Js('ush'), Js('yana'), Js('yela'), Js('yena'), Js('yesh'), Js('yla'), Js('ymis'), Js('yna'), Js('yra'), Js('ys'), Js('yth')]))
var.put('nm5', Js([Js('Ald'), Js('An'), Js('Ath'), Js('Ay'), Js('Bach'), Js('Ban'), Js('Bash'), Js('Bryn'), Js('C'), Js('Cauth'), Js('Char'), Js('Cran'), Js('D'), Js('Daen'), Js('Dag'), Js('Dam'), Js('F'), Js('Fal'), Js('Farsh'), Js('Fon'), Js('Gam'), Js('Gan'), Js('Gor'), Js('Gryn'), Js('Haen'), Js('Hag'), Js('Har'), Js('Hon'), Js('Kash'), Js('Ken'), Js('Kir'), Js('Kryn'), Js('Lam'), Js('Lan'), Js('Lin'), Js('Loth'), Js('Mach'), Js('Man'), Js('Mant'), Js('Math'), Js('Mel'), Js('Merr'), Js('Moer'), Js('Naer'), Js('Nam'), Js('Nil'), Js('Nor'), Js('P'), Js('Paen'), Js('Pem'), Js('Pran'), Js('Sal'), Js('San'), Js('Sol'), Js('Step'), Js('T'), Js('Tel'), Js('Tor'), Js('Trak'), Js('Val'), Js('Varn'), Js('Vel'), Js('Vyn'), Js("a'D"), Js("a'L"), Js("a'M"), Js("a'N"), Js("a'R"), Js("al'D"), Js("al'M"), Js("al'R"), Js("al'Th"), Js("al'V")]))
var.put('nm6', Js([Js('aem'), Js('aera'), Js('ag'), Js('agar'), Js('agin'), Js('aidhrin'), Js('aim'), Js('ain'), Js('alda'), Js('alin'), Js('amon'), Js('an'), Js('anche'), Js('and'), Js('aneos'), Js('ar'), Js('ara'), Js('arin'), Js('athor'), Js('aw'), Js('ear'), Js('ed'), Js('elle'), Js('enne'), Js('eos'), Js('era'), Js('eran'), Js('ere'), Js('eron'), Js('evron'), Js('iar'), Js('iaw'), Js('iaya'), Js('ilin'), Js('in'), Js('inas'), Js('ind'), Js('ineos'), Js('ira'), Js('iros'), Js('odred'), Js('ogan'), Js('oihan'), Js('olin'), Js('olrin'), Js('on'), Js('onche'), Js('onne'), Js('or'), Js('oron'), Js('yan'), Js('yl'), Js('ynar'), Js('yne'), Js('yr'), Js('yrag'), Js('yran'), Js('yron'), Js('yros'), Js('ys')]))
pass
pass


# Add lib to the module scope
wheelOfTimeNames = var.to_python()