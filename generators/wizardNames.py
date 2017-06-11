__all__ = ['wizardNames']

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
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm8').get(var.get('rnd6'))))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm8').get(var.get('rnd6'))))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                            var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm8').get(var.get('rnd6'))))
                        else:
                            if (var.get('i')<Js(8.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                                var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm8').get(var.get('rnd6'))))
                            else:
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                                var.put('names', ((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6'))))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6'))))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                            var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6'))))
                        else:
                            if (var.get('i')<Js(8.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                                var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6'))))
                            else:
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                                var.put('names', ((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('b'), Js('br'), Js('c'), Js('cr'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('kn'), Js('p'), Js('pr'), Js('q'), Js('qr'), Js('r'), Js('st'), Js('str'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('bahn'), Js('barin'), Js('beus'), Js('bin'), Js('bus'), Js('dalf'), Js('del'), Js('dium'), Js('dore'), Js('dus'), Js('farihm'), Js('faris'), Js('feus'), Js('flyn'), Js('forn'), Js('gast'), Js('geor'), Js('gorim'), Js('groln'), Js('grur'), Js('hagan'), Js('harad'), Js('haris'), Js('hith'), Js('hone'), Js('jahr'), Js('jamar'), Js('jeik'), Js('jest'), Js('jor'), Js('kalis'), Js('key'), Js('kius'), Js('kore'), Js('kron'), Js('lenor'), Js('leus'), Js('lin'), Js('lius'), Js('lore'), Js('maex'), Js('marim'), Js('mazz'), Js('monar'), Js('morn'), Js('naxx'), Js('neus'), Js('nior'), Js('nitor'), Js('norim'), Js('pan'), Js('phior'), Js('pius'), Js('pniar'), Js('prix'), Js('qiohr'), Js('qium'), Js('qor'), Js('qrax'), Js('quam'), Js('ras'), Js('rhan'), Js('rius'), Js('ronin'), Js('rune'), Js('shan'), Js('sim'), Js('sior'), Js('sorin'), Js('strum'), Js('tarum'), Js('taz'), Js('thar'), Js('tior'), Js('trix'), Js('veus'), Js('viar'), Js('vior'), Js('vius'), Js('vras'), Js('wahl'), Js('wix'), Js('wras'), Js('wrick'), Js('wyn'), Js('xarif'), Js('xeor'), Js('xium'), Js('xius'), Js('xon'), Js('ydor'), Js('ynas'), Js('yorn'), Js('yrin'), Js('yus'), Js('zahr'), Js('zax'), Js('zif'), Js('zohr'), Js('zor')]))
var.put('nm6', Js([Js('b'), Js('bl'), Js('c'), Js('cl'), Js('d'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gl'), Js('gn'), Js('h'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pl'), Js('ph'), Js('q'), Js('s'), Js('st'), Js('sl'), Js('t'), Js('v'), Js('vl'), Js('w'), Js('z')]))
var.put('nm7', Js([Js('b'), Js('c'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('w')]))
var.put('nm8', Js([Js('belle'), Js('baris'), Js('beus'), Js('bine'), Js('beus'), Js('dali'), Js('delis'), Js('disum'), Js('dores'), Js('deis'), Js('faeh'), Js('faris'), Js('fea'), Js('fyne'), Js('fora'), Js('gaell'), Js('georis'), Js('gis'), Js('garis'), Js('grith'), Js('haen'), Js('harith'), Js('harise'), Js('hith'), Js('hione'), Js('jelle'), Js('jes'), Js('jyll'), Js('jiane'), Js('jior'), Js('kealis'), Js('key'), Js('kely'), Js('kora'), Js('kon'), Js('lyn'), Js('leas'), Js('lune'), Js('laes'), Js('lore'), Js('maev'), Js('mari'), Js('meazz'), Js('monora'), Js('morith'), Js('naxix'), Js('neas'), Js('nilor'), Js('nirn'), Js('nora'), Js('paen'), Js('phi'), Js('pianne'), Js('pyx'), Js('prixys'), Js('qiohn'), Js('qille'), Js('qora'), Js('qix'), Js('qian'), Js('ras'), Js('rihan'), Js('ris'), Js('ro'), Js('rune'), Js('shan'), Js('saem'), Js('sinor'), Js('soph'), Js('strea'), Js('taris'), Js('taz'), Js('thal'), Js('tosh'), Js('trix'), Js('veus'), Js('via'), Js('vira'), Js('vys'), Js('vae'), Js('weahl'), Js('wix'), Js('wrys'), Js('waelle'), Js('wyn'), Js('xaryl'), Js('xea'), Js('xis'), Js('xyll'), Js('xone'), Js('ydae'), Js('yna'), Js('yora'), Js('yrin'), Js('yeas'), Js('zahn'), Js('zyxi'), Js('zif'), Js('zohra'), Js('zora')]))
var.put('nm9', Js([Js('b'), Js('bl'), Js('c'), Js('cl'), Js('d'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gl'), Js('gn'), Js('h'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pl'), Js('ph'), Js('q'), Js('s'), Js('st'), Js('sl'), Js('t'), Js('v'), Js('vl'), Js('w'), Js('z')]))
pass
pass


# Add lib to the module scope
wizardNames = var.to_python()