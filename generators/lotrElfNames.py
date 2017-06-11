__all__ = ['lotrElfNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['lastChar', 'nm1', 'nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'br', 'type'])
    var.put('tp', var.get('type'))
    var.put('br', Js([]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(5.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('lastChar', var.get('nm1').get(var.get('rnd')).get('0').callprop('substr', (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                var.put('lastTwoChar', var.get('nm1').get(var.get('rnd')).get('0').callprop('substr', (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(2.0))))
                if PyJsStrictEq(var.get('tp'),Js(1.0)):
                    while 1:
                        SWITCHED = False
                        CONDITION = (var.get('lastChar'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('a')):
                            SWITCHED = True
                            def PyJs_LONG_0_(var=var):
                                return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('el'), Js('Female'), Js('el')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('sell'), Js('Girl'), Js('ahel')]), Js([Js('gwend'), Js('Maiden'), Js('awen')]), Js([Js('neth'), Js('Girl'), Js('aneth')]), Js([Js('dîs'), Js('Bride'), Js('anis')]), Js([Js('dess'), Js('Woman'), Js('anes')]), Js([Js('nîth'), Js('Sister'), Js('anith')]), Js([Js('thêl'), Js('Sister'), Js('athel')]), Js([Js('bess'), Js('Wife'), Js('aves')])]))
                            PyJs_LONG_0_()
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('e')):
                            SWITCHED = True
                            def PyJs_LONG_1_(var=var):
                                return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('el'), Js('Female'), Js('el')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('sell'), Js('Girl'), Js('ehel')]), Js([Js('gwend'), Js('Maiden'), Js('ewen')]), Js([Js('neth'), Js('Girl'), Js('eneth')]), Js([Js('dîs'), Js('Bride'), Js('enis')]), Js([Js('dess'), Js('Woman'), Js('enes')]), Js([Js('nîth'), Js('Sister'), Js('enith')]), Js([Js('thêl'), Js('Sister'), Js('ethel')]), Js([Js('bess'), Js('Wife'), Js('eves')])]))
                            PyJs_LONG_1_()
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('i')):
                            SWITCHED = True
                            def PyJs_LONG_2_(var=var):
                                return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('el'), Js('Female'), Js('el')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('sell'), Js('Girl'), Js('ihel')]), Js([Js('gwend'), Js('Maiden'), Js('iwen')]), Js([Js('neth'), Js('Girl'), Js('ineth')]), Js([Js('dîs'), Js('Bride'), Js('inis')]), Js([Js('dess'), Js('Woman'), Js('ines')]), Js([Js('nîth'), Js('Sister'), Js('inith')]), Js([Js('thêl'), Js('Sister'), Js('ithel')]), Js([Js('bess'), Js('Wife'), Js('ives')])]))
                            PyJs_LONG_2_()
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('o')):
                            SWITCHED = True
                            def PyJs_LONG_3_(var=var):
                                return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('el'), Js('Female'), Js('el')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('sell'), Js('Girl'), Js('ohel')]), Js([Js('gwend'), Js('Maiden'), Js('owen')]), Js([Js('neth'), Js('Girl'), Js('oneth')]), Js([Js('dîs'), Js('Bride'), Js('onis')]), Js([Js('dess'), Js('Woman'), Js('ones')]), Js([Js('nîth'), Js('Sister'), Js('onith')]), Js([Js('thêl'), Js('Sister'), Js('othel')]), Js([Js('bess'), Js('Wife'), Js('oves')])]))
                            PyJs_LONG_3_()
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('u')):
                            SWITCHED = True
                            def PyJs_LONG_4_(var=var):
                                return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('el'), Js('Female'), Js('el')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('sell'), Js('Girl'), Js('uhel')]), Js([Js('gwend'), Js('Maiden'), Js('uwen')]), Js([Js('neth'), Js('Girl'), Js('uneth')]), Js([Js('dîs'), Js('Bride'), Js('unis')]), Js([Js('dess'), Js('Woman'), Js('unes')]), Js([Js('nîth'), Js('Sister'), Js('unith')]), Js([Js('thêl'), Js('Sister'), Js('uthel')]), Js([Js('bess'), Js('Wife'), Js('uves')])]))
                            PyJs_LONG_4_()
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('b')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('el'), Js('Female'), Js('el')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('bess'), Js('Wife'), Js('es')])]))
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('c')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('geth')]), Js([Js('el'), Js('Female'), Js('gel')]), Js([Js('il'), Js('Female'), Js('gil')]), Js([Js('ien'), Js('Daughter of'), Js('gien')]), Js([Js('iell'), Js('Daughter of'), Js('giel')]), Js([Js('gwend'), Js('Maiden'), Js('gwen')])]))
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('d')):
                            SWITCHED = True
                            if PyJsStrictEq(var.get('lastTwoChar'),Js('nd')):
                                def PyJs_LONG_5_(var=var):
                                    return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('neth')]), Js([Js('el'), Js('Female'), Js('nel')]), Js([Js('il'), Js('Female'), Js('nil')]), Js([Js('ien'), Js('Daughter of'), Js('nien')]), Js([Js('iell'), Js('Daughter of'), Js('niel')]), Js([Js('sell'), Js('Girl'), Js('hel')]), Js([Js('gwend'), Js('Maiden'), Js('gwen')]), Js([Js('neth'), Js('Girl'), Js('neth')]), Js([Js('dîs'), Js('Bride'), Js('dis')]), Js([Js('dess'), Js('Woman'), Js('des')]), Js([Js('nîth'), Js('Sister'), Js('nith')]), Js([Js('thêl'), Js('Sister'), Js('thel')]), Js([Js('bess'), Js('Wife'), Js('bes')])]))
                                PyJs_LONG_5_()
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            else:
                                def PyJs_LONG_6_(var=var):
                                    return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('deth')]), Js([Js('el'), Js('Female'), Js('del')]), Js([Js('il'), Js('Female'), Js('dil')]), Js([Js('ien'), Js('Daughter of'), Js('dien')]), Js([Js('iell'), Js('Daughter of'), Js('diel')]), Js([Js('sell'), Js('Girl'), Js('ssel')]), Js([Js('gwend'), Js('Maiden'), Js('dwen')]), Js([Js('dîs'), Js('Bride'), Js('dis')]), Js([Js('dess'), Js('Woman'), Js('des')])]))
                                PyJs_LONG_6_()
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('f')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('veth')]), Js([Js('el'), Js('Female'), Js('vel')]), Js([Js('il'), Js('Female'), Js('vil')]), Js([Js('ien'), Js('Daughter of'), Js('vien')]), Js([Js('iell'), Js('Daughter of'), Js('viel')]), Js([Js('bess'), Js('Wife'), Js('ves')])]))
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('g')):
                            SWITCHED = True
                            def PyJs_LONG_7_(var=var):
                                return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('geth')]), Js([Js('el'), Js('Female'), Js('gel')]), Js([Js('il'), Js('Female'), Js('gil')]), Js([Js('ien'), Js('Daughter of'), Js('gien')]), Js([Js('iell'), Js('Daughter of'), Js('giel')]), Js([Js('sell'), Js('Girl'), Js('gel')]), Js([Js('gwend'), Js('Maiden'), Js('gwen')]), Js([Js('neth'), Js('Girl'), Js('gneth')]), Js([Js('dîs'), Js('Bride'), Js('gnis')]), Js([Js('dess'), Js('Woman'), Js('gnes')]), Js([Js('nîth'), Js('Sister'), Js('gnith')]), Js([Js('thêl'), Js('Sister'), Js('cthel')])]))
                            PyJs_LONG_7_()
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('h')):
                            SWITCHED = True
                            if PyJsStrictEq(var.get('lastTwoChar'),Js('ch')):
                                var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('sell'), Js('Girl'), Js('el')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                            else:
                                var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('es')]), Js([Js('el'), Js('Female'), Js('el')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('sell'), Js('Girl'), Js('el')]), Js([Js('thêl'), Js('Sister'), Js('el')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('l')):
                            SWITCHED = True
                            if PyJsStrictEq(var.get('lastTwoChar'),Js('ll')):
                                def PyJs_LONG_8_(var=var):
                                    return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('el'), Js('Female'), Js('el')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('sell'), Js('Girl'), Js('hel')]), Js([Js('gwend'), Js('Maiden'), Js('wen')]), Js([Js('neth'), Js('Girl'), Js('neth')]), Js([Js('dîs'), Js('Bride'), Js('dis')]), Js([Js('dess'), Js('Woman'), Js('des')]), Js([Js('nîth'), Js('Sister'), Js('nith')]), Js([Js('thêl'), Js('Sister'), Js('thel')]), Js([Js('bess'), Js('Wife'), Js('bes')])]))
                                PyJs_LONG_8_()
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            else:
                                def PyJs_LONG_9_(var=var):
                                    return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('el'), Js('Female'), Js('el')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('sell'), Js('Girl'), Js('hel')]), Js([Js('gwend'), Js('Maiden'), Js('wen')]), Js([Js('neth'), Js('Girl'), Js('neth')]), Js([Js('dîs'), Js('Bride'), Js('dis')]), Js([Js('dess'), Js('Woman'), Js('des')]), Js([Js('nîth'), Js('Sister'), Js('nith')]), Js([Js('thêl'), Js('Sister'), Js('thel')]), Js([Js('bess'), Js('Wife'), Js('bes')])]))
                                PyJs_LONG_9_()
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('m')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('el'), Js('Female'), Js('el')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('dîs'), Js('Bride'), Js('dis')]), Js([Js('dess'), Js('Woman'), Js('des')]), Js([Js('bess'), Js('Wife'), Js('bes')])]))
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('n')):
                            SWITCHED = True
                            def PyJs_LONG_10_(var=var):
                                return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('neth')]), Js([Js('el'), Js('Female'), Js('nel')]), Js([Js('il'), Js('Female'), Js('nil')]), Js([Js('ien'), Js('Daughter of'), Js('nien')]), Js([Js('iell'), Js('Daughter of'), Js('niel')]), Js([Js('sell'), Js('Girl'), Js('ssel')]), Js([Js('gwend'), Js('Maiden'), Js('ngwen')]), Js([Js('neth'), Js('Girl'), Js('neth')]), Js([Js('dîs'), Js('Bride'), Js('ndis')]), Js([Js('dess'), Js('Woman'), Js('ndes')]), Js([Js('nîth'), Js('Sister'), Js('nith')]), Js([Js('thêl'), Js('Sister'), Js('nthel')]), Js([Js('bess'), Js('Wife'), Js('mes')])]))
                            PyJs_LONG_10_()
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('p')):
                            SWITCHED = True
                            if PyJsStrictEq(var.get('lastTwoChar'),Js('mp')):
                                def PyJs_LONG_11_(var=var):
                                    return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('meth')]), Js([Js('el'), Js('Female'), Js('mel')]), Js([Js('il'), Js('Female'), Js('mil')]), Js([Js('ien'), Js('Daughter of'), Js('mien')]), Js([Js('iell'), Js('Daughter of'), Js('miel')]), Js([Js('sell'), Js('Girl'), Js('hel')]), Js([Js('dîs'), Js('Bride'), Js('dis')]), Js([Js('dess'), Js('Woman'), Js('des')]), Js([Js('bess'), Js('Wife'), Js('bes')])]))
                                PyJs_LONG_11_()
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            else:
                                var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('beth')]), Js([Js('el'), Js('Female'), Js('bel')]), Js([Js('il'), Js('Female'), Js('bil')]), Js([Js('ien'), Js('Daughter of'), Js('bien')]), Js([Js('iell'), Js('Daughter of'), Js('biel')]), Js([Js('bess'), Js('Wife'), Js('bes')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('r')):
                            SWITCHED = True
                            def PyJs_LONG_12_(var=var):
                                return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('el'), Js('Female'), Js('el')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('sell'), Js('Girl'), Js('hel')]), Js([Js('gwend'), Js('Maiden'), Js('wen')]), Js([Js('neth'), Js('Girl'), Js('neth')]), Js([Js('dîs'), Js('Bride'), Js('dis')]), Js([Js('dess'), Js('Woman'), Js('des')]), Js([Js('nîth'), Js('Sister'), Js('nith')]), Js([Js('thêl'), Js('Sister'), Js('thel')]), Js([Js('bess'), Js('Wife'), Js('bes')])]))
                            PyJs_LONG_12_()
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('s')):
                            SWITCHED = True
                            if PyJsStrictEq(var.get('lastTwoChar'),Js('ss')):
                                def PyJs_LONG_13_(var=var):
                                    return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('seth')]), Js([Js('el'), Js('Female'), Js('sel')]), Js([Js('il'), Js('Female'), Js('sil')]), Js([Js('ien'), Js('Daughter of'), Js('sien')]), Js([Js('iell'), Js('Daughter of'), Js('siel')]), Js([Js('sell'), Js('Girl'), Js('sel')]), Js([Js('gwend'), Js('Maiden'), Js('sengwen')]), Js([Js('neth'), Js('Girl'), Js('seneth')]), Js([Js('dîs'), Js('Bride'), Js('sendis')]), Js([Js('dess'), Js('Woman'), Js('sendes')]), Js([Js('nîth'), Js('Sister'), Js('senith')]), Js([Js('thêl'), Js('Sister'), Js('senthel')]), Js([Js('bess'), Js('Wife'), Js('semes')])]))
                                PyJs_LONG_13_()
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            else:
                                def PyJs_LONG_14_(var=var):
                                    return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('seth')]), Js([Js('el'), Js('Female'), Js('sel')]), Js([Js('il'), Js('Female'), Js('sil')]), Js([Js('ien'), Js('Daughter of'), Js('sien')]), Js([Js('iell'), Js('Daughter of'), Js('siel')]), Js([Js('sell'), Js('Girl'), Js('sel')]), Js([Js('dîs'), Js('Bride'), Js('dis')]), Js([Js('dess'), Js('Woman'), Js('des')]), Js([Js('bess'), Js('Wife'), Js('bes')])]))
                                PyJs_LONG_14_()
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('t')):
                            SWITCHED = True
                            if PyJsStrictEq(var.get('lastTwoChar'),Js('lt')):
                                def PyJs_LONG_15_(var=var):
                                    return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('eth')]), Js([Js('il'), Js('Female'), Js('il')]), Js([Js('ien'), Js('Daughter of'), Js('ien')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('gwend'), Js('Maiden'), Js('wen')]), Js([Js('neth'), Js('Girl'), Js('neth')]), Js([Js('dîs'), Js('Bride'), Js('dis')]), Js([Js('dess'), Js('Woman'), Js('des')]), Js([Js('nîth'), Js('Sister'), Js('nith')]), Js([Js('bess'), Js('Wife'), Js('ves')])]))
                                PyJs_LONG_15_()
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            else:
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('nt')):
                                    def PyJs_LONG_16_(var=var):
                                        return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('nneth')]), Js([Js('el'), Js('Female'), Js('nnel')]), Js([Js('il'), Js('Female'), Js('nnil')]), Js([Js('ien'), Js('Daughter of'), Js('nnien')]), Js([Js('iell'), Js('Daughter of'), Js('nniel')]), Js([Js('sell'), Js('Girl'), Js('nthel')]), Js([Js('gwend'), Js('Maiden'), Js('ngwen')]), Js([Js('neth'), Js('Girl'), Js('nneth')]), Js([Js('dîs'), Js('Bride'), Js('ndis')]), Js([Js('dess'), Js('Woman'), Js('ndes')]), Js([Js('nîth'), Js('Sister'), Js('nnith')]), Js([Js('bess'), Js('Wife'), Js('mbes')])]))
                                    PyJs_LONG_16_()
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(2.0))))
                                else:
                                    var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('teth')]), Js([Js('el'), Js('Female'), Js('tel')]), Js([Js('il'), Js('Female'), Js('til')]), Js([Js('ien'), Js('Daughter of'), Js('tien')]), Js([Js('iell'), Js('Daughter of'), Js('tiel')]), Js([Js('sell'), Js('Girl'), Js('sel')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('w')):
                            SWITCHED = True
                            def PyJs_LONG_17_(var=var):
                                return var.put('nm3', Js([Js([Js('eth'), Js('Female'), Js('weth')]), Js([Js('el'), Js('Female'), Js('wel')]), Js([Js('il'), Js('Female'), Js('wil')]), Js([Js('ien'), Js('Daughter of'), Js('wien')]), Js([Js('iell'), Js('Daughter of'), Js('wiel')]), Js([Js('sell'), Js('Girl'), Js('hel')]), Js([Js('gwend'), Js('Maiden'), Js('wen')]), Js([Js('neth'), Js('Girl'), Js('neth')]), Js([Js('dîs'), Js('Bride'), Js('nis')]), Js([Js('dess'), Js('Woman'), Js('nes')]), Js([Js('nîth'), Js('Sister'), Js('nith')]), Js([Js('thêl'), Js('Sister'), Js('thel')]), Js([Js('bess'), Js('Wife'), Js('ves')])]))
                            PyJs_LONG_17_()
                            var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        SWITCHED = True
                        break
                else:
                    if PyJsStrictEq(var.get('tp'),Js(2.0)):
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get('lastChar'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('a')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('ben')]), Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('e')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('ben')]), Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('i')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('ben')]), Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('o')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('ben')]), Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('u')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('ben')]), Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('b')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('en')]), Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('c')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('d')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('nd')):
                                    var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('mben')]), Js([Js(''), Js(''), Js('nd')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(2.0))))
                                else:
                                    var.put('nm3', Js([Js([Js(''), Js(''), Js('')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('f')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('phen')]), Js([Js(''), Js(''), Js('f')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('g')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('h')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('ch')):
                                    var.put('nm3', Js([Js([Js(''), Js(''), Js('')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                else:
                                    var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('ben')]), Js([Js(''), Js(''), Js('')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('l')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('ll')):
                                    var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('ben')]), Js([Js(''), Js(''), Js('')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                else:
                                    var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('ben')]), Js([Js(''), Js(''), Js('')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('m')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('ben')]), Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('n')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('mben')]), Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('p')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('mp')):
                                    var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('ben')]), Js([Js(''), Js(''), Js('')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                else:
                                    var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('en')]), Js([Js(''), Js(''), Js('')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('r')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('phen')]), Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('s')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('ss')):
                                    var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('pen')]), Js([Js(''), Js(''), Js('')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                else:
                                    var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('pen')]), Js([Js(''), Js(''), Js('')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('t')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('lt')):
                                    var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('ben')]), Js([Js(''), Js(''), Js('')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                else:
                                    if PyJsStrictEq(var.get('lastTwoChar'),Js('nt')):
                                        var.put('nm3', Js([Js([Js('pen'), Js('Person'), Js('mben')]), Js([Js(''), Js(''), Js('')])]))
                                        var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(2.0))))
                                    else:
                                        var.put('nm3', Js([Js([Js(''), Js(''), Js('')])]))
                                        var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('w')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js(''), Js(''), Js('')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            SWITCHED = True
                            break
                    else:
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get('lastChar'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('a')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('daer'), Js('Groom'), Js('naer')]), Js([Js('dir'), Js('Man'), Js('nir')]), Js([Js('benn'), Js('Husband'), Js('ven')]), Js([Js('tôr'), Js('Brother'), Js('dor')]), Js([Js('hawn'), Js('Brother'), Js('chon')]), Js([Js('hanar'), Js('Brother'), Js('chanar')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('e')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('daer'), Js('Groom'), Js('naer')]), Js([Js('dir'), Js('Man'), Js('nir')]), Js([Js('benn'), Js('Husband'), Js('ven')]), Js([Js('tôr'), Js('Brother'), Js('dor')]), Js([Js('hawn'), Js('Brother'), Js('chon')]), Js([Js('hanar'), Js('Brother'), Js('chanar')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('i')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('daer'), Js('Groom'), Js('naer')]), Js([Js('dir'), Js('Man'), Js('nir')]), Js([Js('benn'), Js('Husband'), Js('ven')]), Js([Js('tôr'), Js('Brother'), Js('dor')]), Js([Js('hawn'), Js('Brother'), Js('chon')]), Js([Js('hanar'), Js('Brother'), Js('chanar')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('o')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('daer'), Js('Groom'), Js('naer')]), Js([Js('dir'), Js('Man'), Js('nir')]), Js([Js('benn'), Js('Husband'), Js('ven')]), Js([Js('tôr'), Js('Brother'), Js('dor')]), Js([Js('hawn'), Js('Brother'), Js('chon')]), Js([Js('hanar'), Js('Brother'), Js('chanar')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('u')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('daer'), Js('Groom'), Js('naer')]), Js([Js('dir'), Js('Man'), Js('nir')]), Js([Js('benn'), Js('Husband'), Js('ven')]), Js([Js('tôr'), Js('Brother'), Js('dor')]), Js([Js('hawn'), Js('Brother'), Js('chon')]), Js([Js('hanar'), Js('Brother'), Js('chanar')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('b')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('on')]), Js([Js('ion'), Js('Son of'), Js('ion')]), Js([Js('benn'), Js('Husband'), Js('en')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('c')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('gon')]), Js([Js('ion'), Js('Son of'), Js('gion')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('d')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('nd')):
                                    var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('nnor')]), Js([Js('ion'), Js('Son of'), Js('nnion')]), Js([Js('daer'), Js('Groom'), Js('ndaer')]), Js([Js('dir'), Js('Man'), Js('ndir')]), Js([Js('benn'), Js('Husband'), Js('mben')]), Js([Js('tôr'), Js('Brother'), Js('ndor')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(2.0))))
                                else:
                                    var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('on')]), Js([Js('ion'), Js('Son of'), Js('ion')]), Js([Js('daer'), Js('Groom'), Js('aer')]), Js([Js('dir'), Js('Man'), Js('ir')]), Js([Js('benn'), Js('Husband'), Js('ben')]), Js([Js('tôr'), Js('Brother'), Js('or')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('f')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('von')]), Js([Js('ion'), Js('Son of'), Js('vion')]), Js([Js('benn'), Js('Husband'), Js('ven')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('g')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('gon')]), Js([Js('ion'), Js('Son of'), Js('gion')]), Js([Js('dir'), Js('Man'), Js('gnir')]), Js([Js('hawn'), Js('Brother'), Js('chon')]), Js([Js('hanar'), Js('Brother'), Js('chanar')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('h')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('on')]), Js([Js('ion'), Js('Son of'), Js('ion')]), Js([Js('hawn'), Js('Brother'), Js('on')]), Js([Js('hanar'), Js('Brother'), Js('anar')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('l')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('ll')):
                                    var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('on')]), Js([Js('ion'), Js('Son of'), Js('ion')]), Js([Js('daer'), Js('Groom'), Js('daer')]), Js([Js('dir'), Js('Man'), Js('dir')]), Js([Js('benn'), Js('Husband'), Js('ben')]), Js([Js('tôr'), Js('Brother'), Js('dor')]), Js([Js('hawn'), Js('Brother'), Js('chon')]), Js([Js('hanar'), Js('Brother'), Js('chanar')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                else:
                                    var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('on')]), Js([Js('ion'), Js('Son of'), Js('ion')]), Js([Js('daer'), Js('Groom'), Js('daer')]), Js([Js('dir'), Js('Man'), Js('dir')]), Js([Js('benn'), Js('Husband'), Js('ben')]), Js([Js('tôr'), Js('Brother'), Js('dor')]), Js([Js('hawn'), Js('Brother'), Js('chon')]), Js([Js('hanar'), Js('Brother'), Js('chanar')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('m')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('on')]), Js([Js('ion'), Js('Son of'), Js('ion')]), Js([Js('daer'), Js('Groom'), Js('daer')]), Js([Js('dir'), Js('Man'), Js('dir')]), Js([Js('benn'), Js('Husband'), Js('ben')]), Js([Js('tôr'), Js('Brother'), Js('dor')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('n')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('nor')]), Js([Js('ion'), Js('Son of'), Js('nion')]), Js([Js('daer'), Js('Groom'), Js('ndaer')]), Js([Js('dir'), Js('Man'), Js('ndir')]), Js([Js('benn'), Js('Husband'), Js('men')]), Js([Js('tôr'), Js('Brother'), Js('thor')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('p')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('mp')):
                                    var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('mon')]), Js([Js('ion'), Js('Son of'), Js('mion')]), Js([Js('daer'), Js('Groom'), Js('daer')]), Js([Js('dir'), Js('Man'), Js('dir')]), Js([Js('benn'), Js('Husband'), Js('ben')]), Js([Js('tôr'), Js('Brother'), Js('dor')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                else:
                                    var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('bon')]), Js([Js('ion'), Js('Son of'), Js('bion')]), Js([Js('benn'), Js('Husband'), Js('ben')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('r')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('on')]), Js([Js('ion'), Js('Son of'), Js('ion')]), Js([Js('daer'), Js('Groom'), Js('daer')]), Js([Js('dir'), Js('Man'), Js('dir')]), Js([Js('benn'), Js('Husband'), Js('ben')]), Js([Js('tôr'), Js('Brother'), Js('dor')]), Js([Js('hawn'), Js('Brother'), Js('chon')]), Js([Js('hanar'), Js('Brother'), Js('chanar')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('s')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('ss')):
                                    var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('son')]), Js([Js('ion'), Js('Son of'), Js('sion')]), Js([Js('daer'), Js('Groom'), Js('sendaer')]), Js([Js('dir'), Js('Man'), Js('sendir')]), Js([Js('benn'), Js('Husband'), Js('semen')]), Js([Js('tôr'), Js('Brother'), Js('tor')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                else:
                                    var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('son')]), Js([Js('ion'), Js('Son of'), Js('sion')]), Js([Js('daer'), Js('Groom'), Js('daer')]), Js([Js('dir'), Js('Man'), Js('dir')]), Js([Js('benn'), Js('Husband'), Js('ben')]), Js([Js('tôr'), Js('Brother'), Js('tor')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('t')):
                                SWITCHED = True
                                if PyJsStrictEq(var.get('lastTwoChar'),Js('lt')):
                                    var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('on')]), Js([Js('ion'), Js('Son of'), Js('ion')]), Js([Js('daer'), Js('Groom'), Js('daer')]), Js([Js('dir'), Js('Man'), Js('dir')]), Js([Js('benn'), Js('Husband'), Js('ven')]), Js([Js('tôr'), Js('Brother'), Js('dor')]), Js([Js('hawn'), Js('Brother'), Js('chon')]), Js([Js('hanar'), Js('Brother'), Js('chanar')])]))
                                    var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                else:
                                    if PyJsStrictEq(var.get('lastTwoChar'),Js('nt')):
                                        var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('nnor')]), Js([Js('ion'), Js('Son of'), Js('nnion')]), Js([Js('daer'), Js('Groom'), Js('ndaer')]), Js([Js('dir'), Js('Man'), Js('ndir')]), Js([Js('benn'), Js('Husband'), Js('mben')]), Js([Js('tôr'), Js('Brother'), Js('ndor')])]))
                                        var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(2.0))))
                                    else:
                                        var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('on')]), Js([Js('ion'), Js('Son of'), Js('ion')]), Js([Js('tôr'), Js('Brother'), Js('or')])]))
                                        var.put('name1', var.get('nm1').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('w')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('won')]), Js([Js('ion'), Js('Son of'), Js('wion')]), Js([Js('daer'), Js('Groom'), Js('naer')]), Js([Js('dir'), Js('Man'), Js('nir')]), Js([Js('benn'), Js('Husband'), Js('ven')]), Js([Js('tôr'), Js('Brother'), Js('dor')]), Js([Js('hawn'), Js('Brother'), Js('chon')]), Js([Js('hanar'), Js('Brother'), Js('chanar')])]))
                                var.put('name1', var.get('nm1').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm1').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            SWITCHED = True
                            break
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names1', (var.get('name1')+var.get('nm3').get(var.get('rnd2')).get('2')))
                var.put('names2', ((((((((Js('(')+var.get('nm1').get(var.get('rnd')).get('0'))+Js(' ('))+var.get('nm1').get(var.get('rnd')).get('1'))+Js(') + '))+var.get('nm3').get(var.get('rnd2')).get('0'))+Js(' ('))+var.get('nm3').get(var.get('rnd2')).get('1'))+Js('))')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('lastChar', var.get('nm2').get(var.get('rnd')).get('0').callprop('substr', (var.get('nm2').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                var.put('lastTwoChar', var.get('nm2').get(var.get('rnd')).get('0').callprop('substr', (var.get('nm2').get(var.get('rnd')).get('0').get('length')-Js(2.0))))
                if PyJsStrictEq(var.get('tp'),Js(1.0)):
                    while 1:
                        SWITCHED = False
                        CONDITION = (var.get('lastChar'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('a')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('ril'), Js('Female'), Js('ril')]), Js([Js('dis'), Js('Female'), Js('adis')]), Js([Js('iell'), Js('Daughter of'), Js('riel')]), Js([Js('ien'), Js('Daughter of'), Js('rien')])]))
                            var.put('name2', var.get('nm2').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm2').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('b')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('h')):
                            SWITCHED = True
                            pass
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('w')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('ril'), Js('Female'), Js('ril')]), Js([Js('dis'), Js('Female'), Js('edis')]), Js([Js('iell'), Js('Daughter of'), Js('riel')]), Js([Js('ien'), Js('Daughter of'), Js('rien')])]))
                            var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('d')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('ril'), Js('Female'), Js('ril')]), Js([Js('dis'), Js('Female'), Js('is')]), Js([Js('iell'), Js('Daughter of'), Js('issiel')]), Js([Js('ien'), Js('Daughter of'), Js('issien')]), Js([Js('iell'), Js('Daughter of'), Js('riel')]), Js([Js('ien'), Js('Daughter of'), Js('rien')])]))
                            var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('f')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('ril'), Js('Female'), Js('vril')]), Js([Js('dis'), Js('Female'), Js('vedis')]), Js([Js('iell'), Js('Daughter of'), Js('vriel')]), Js([Js('ien'), Js('Daughter of'), Js('vrien')])]))
                            var.put('name2', var.get('nm2').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm2').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('g')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('ril'), Js('Female'), Js('ril')]), Js([Js('dis'), Js('Female'), Js('nis')]), Js([Js('iell'), Js('Daughter of'), Js('nissiel')]), Js([Js('ien'), Js('Daughter of'), Js('nissien')]), Js([Js('iell'), Js('Daughter of'), Js('riel')]), Js([Js('ien'), Js('Daughter of'), Js('rien')])]))
                            var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('l')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('ril'), Js('Female'), Js('lil')]), Js([Js('dis'), Js('Female'), Js('dis')]), Js([Js('iell'), Js('Daughter of'), Js('liel')]), Js([Js('ien'), Js('Daughter of'), Js('lien')]), Js([Js('iell'), Js('Daughter of'), Js('dissiel')]), Js([Js('ien'), Js('Daughter of'), Js('dissien')])]))
                            var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('n')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('ril'), Js('Female'), Js('dhril')]), Js([Js('dis'), Js('Female'), Js('ndis')]), Js([Js('iell'), Js('Daughter of'), Js('ndissiel')]), Js([Js('ien'), Js('Daughter of'), Js('ndissien')]), Js([Js('iell'), Js('Daughter of'), Js('dhriel')]), Js([Js('ien'), Js('Daughter of'), Js('dhrien')])]))
                            var.put('name2', var.get('nm2').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm2').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('r')):
                            SWITCHED = True
                            var.put('nm3', Js([Js([Js('ril'), Js('Female'), Js('il')]), Js([Js('dis'), Js('Female'), Js('dis')]), Js([Js('iell'), Js('Daughter of'), Js('iel')]), Js([Js('ien'), Js('Daughter of'), Js('ien')])]))
                            var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                            break
                        SWITCHED = True
                        break
                else:
                    if PyJsStrictEq(var.get('tp'),Js(2.0)):
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get('lastChar'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('a')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('or'), Js('Person'), Js('or')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm2').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('b')):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('h')):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('w')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('or'), Js('Person'), Js('or')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('d')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('or'), Js('Person'), Js('or')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('f')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('or'), Js('Person'), Js('vor')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm2').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('g')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('or'), Js('Person'), Js('or')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('l')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('or'), Js('Person'), Js('or')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('n')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('or'), Js('Person'), Js('or')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('r')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('or'), Js('Person'), Js('or')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                                break
                            SWITCHED = True
                            break
                    else:
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get('lastChar'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('a')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('on')]), Js([Js('dir'), Js('Male'), Js('edir')]), Js([Js('ron'), Js('Male'), Js('on')]), Js([Js('ion'), Js('Son of'), Js('ion')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm2').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('b')):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('h')):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('w')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('on'), Js('Male'), Js('edon')]), Js([Js('dir'), Js('Male'), Js('edir')]), Js([Js('ron'), Js('Male'), Js('ron')]), Js([Js('ion'), Js('Son of'), Js('rion')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('d')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('ion'), Js('Son of'), Js('irion')]), Js([Js('dir'), Js('Male'), Js('ir')]), Js([Js('ron'), Js('Male'), Js('ron')]), Js([Js('ion'), Js('Son of'), Js('rion')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('f')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('dir'), Js('Male'), Js('vedir')]), Js([Js('ron'), Js('Male'), Js('vron')]), Js([Js('ion'), Js('Son of'), Js('vrion')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm2').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('g')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('ion'), Js('Son of'), Js('nirion')]), Js([Js('dir'), Js('Male'), Js('nir')]), Js([Js('ron'), Js('Male'), Js('ron')]), Js([Js('ion'), Js('Son of'), Js('rion')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('l')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('ion'), Js('Son of'), Js('lion')]), Js([Js('dir'), Js('Male'), Js('dir')]), Js([Js('ron'), Js('Male'), Js('lon')]), Js([Js('ion'), Js('Son of'), Js('dirion')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('n')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('ion'), Js('Son of'), Js('dhrion')]), Js([Js('dir'), Js('Male'), Js('ndir')]), Js([Js('ron'), Js('Male'), Js('dhron')]), Js([Js('ion'), Js('Son of'), Js('ndirion')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0').callprop('slice', Js(0.0), (var.get('nm2').get(var.get('rnd')).get('0').get('length')-Js(1.0))))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js('r')):
                                SWITCHED = True
                                var.put('nm3', Js([Js([Js('ion'), Js('Son of'), Js('ion')]), Js([Js('dir'), Js('Male'), Js('dir')]), Js([Js('ron'), Js('Male'), Js('on')]), Js([Js('ion'), Js('Son of'), Js('dirion')])]))
                                var.put('name2', var.get('nm2').get(var.get('rnd')).get('0'))
                                break
                            SWITCHED = True
                            break
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names1', (var.get('name2')+var.get('nm3').get(var.get('rnd2')).get('2')))
                var.put('names2', ((((((((Js('(')+var.get('nm2').get(var.get('rnd')).get('0'))+Js(' ('))+var.get('nm2').get(var.get('rnd')).get('1'))+Js(') + '))+var.get('nm3').get(var.get('rnd2')).get('0'))+Js(' ('))+var.get('nm3').get(var.get('rnd2')).get('1'))+Js('))')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js([Js('Âr'), Js('Royal/Noble')]), Js([Js('Êg'), Js('Thorn')]), Js([Js('Êl'), Js('Star')]), Js([Js('Îdh'), Js('Rest/Repose')]), Js([Js('Îr'), Js('Sexual Disire')]), Js([Js('Óleryd'), Js('Dream of Mountains')]), Js([Js('Ôl'), Js('Dream')]), Js([Js('Úan'), Js('Monster')]), Js([Js('Úhael'), Js('Unwise')]), Js([Js('Úlloth'), Js('Flower Scent')]), Js([Js('Úthaes'), Js('Temptation')]), Js([Js('Ûn'), Js('Creature')]), Js([Js('Ûr'), Js('Fire')]), Js([Js('Ûr'), Js('Wide/Heat')]), Js([Js('Ýridhren'), Js('Wise Course')]), Js([Js('Ablad'), Js('Prohibition/Refusal')]), Js([Js('Acharn'), Js('Vengeance')]), Js([Js('Achas'), Js('Dread/Fear')]), Js([Js('Adab'), Js('Building/House')]), Js([Js('Aduial'), Js('Evendim')]), Js([Js('Aear'), Js('Sea')]), Js([Js('Aearon'), Js('Ocean')]), Js([Js('Aeg'), Js('Sharp Point')]), Js([Js('Aeglos'), Js('Icicle')]), Js([Js('Ael'), Js('Lake/Pool')]), Js([Js('Aen'), Js('Holy')]), Js([Js('Aer'), Js('Holy')]), Js([Js('Aer'), Js('Sea')]), Js([Js('Aew'), Js('Small Bird')]), Js([Js('Aewen'), Js('Of Birds')]), Js([Js('Agar'), Js('Blood')]), Js([Js('Agarwaen'), Js('Bloodstained')]), Js([Js('Aglar'), Js('Glory/Brilliance')]), Js([Js('Aglareb'), Js('Glorious')]), Js([Js('Agor'), Js('Narrow')]), Js([Js('Aith'), Js('Spearpoint')]), Js([Js('Alag'), Js('Rushing/Impetuous')]), Js([Js('Alagos'), Js('Wind Storm')]), Js([Js('Alph'), Js('Swan')]), Js([Js('Amar'), Js('Earth')]), Js([Js('Amarth'), Js('Fate/Doom')]), Js([Js('Amath'), Js('Shield')]), Js([Js('Amlug'), Js('Dragon')]), Js([Js('Amon'), Js('Hill')]), Js([Js('Amrûn'), Js('East')]), Js([Js('And'), Js('Long')]), Js([Js('Ang'), Js('Iron')]), Js([Js('Angol'), Js('Deep Lore/Magic')]), Js([Js('Angol'), Js('Stench')]), Js([Js('Angwedh'), Js('Chain')]), Js([Js('Annúngil'), Js('West Star')]), Js([Js('Annûn'), Js('West/Sunset')]), Js([Js('Annon'), Js('Door/Gate')]), Js([Js('Annui'), Js('Western')]), Js([Js('Ant'), Js('Gift')]), Js([Js('Anu'), Js('Masculine')]), Js([Js('Aradhel'), Js('Royal Terror')]), Js([Js('Arahael'), Js('Noble and Wise')]), Js([Js('Aras'), Js('Deer')]), Js([Js('Arn'), Js('Royal')]), Js([Js('Arod'), Js('Noble')]), Js([Js('Arrad'), Js('Without a Path')]), Js([Js('Arth'), Js('Exalted')]), Js([Js('Aur'), Js('Day/Sunlight')]), Js([Js('Auth'), Js('Spectral/Apparition')]), Js([Js('Auth'), Js('War/Battle')]), Js([Js('Avorn'), Js('Staying/Fast')]), Js([Js('Bôr'), Js('Faithful Man/Vassal')]), Js([Js('Bachor'), Js('Pedlar')]), Js([Js('Bain'), Js('Beautiful')]), Js([Js('Baingol'), Js('Fair and Wise')]), Js([Js('Balch'), Js('Cruel')]), Js([Js('Ballin'), Js('Divine')]), Js([Js('Balrant'), Js('Powerful Course')]), Js([Js('Band'), Js('Prison')]), Js([Js('Bar'), Js('Dwelling/Home')]), Js([Js('Bara'), Js('Fiery')]), Js([Js('Barad'), Js('Doomed')]), Js([Js('Barad'), Js('Tower/Fortress')]), Js([Js('Baralin'), Js('Fiery Gleam in the Eyes')]), Js([Js('Baran'), Js('Brown')]), Js([Js('Barhador'), Js('One Faithful to Home')]), Js([Js('Baudh'), Js('Judgement')]), Js([Js('Baug'), Js('Tyrannous/Cruel')]), Js([Js('Baul'), Js('Torment')]), Js([Js('Baur'), Js('Need')]), Js([Js('Beleg'), Js('Great/Mighty')]), Js([Js('Belegorn'), Js('Mighty Tree')]), Js([Js('Belegur'), Js('Great Heart')]), Js([Js('Belt'), Js('Strong')]), Js([Js('Beren'), Js('Bold')]), Js([Js('Born'), Js('Fiery Red')]), Js([Js('Bornif'), Js('Fiery Red Face')]), Js([Js('Both'), Js('Puddle/Small Pool')]), Js([Js('Brêg'), Js('Violent/Sudden/Fierce')]), Js([Js('Brûn'), Js('Old')]), Js([Js('Bragol'), Js('Sudden')]), Js([Js('Braig'), Js('Wild/Fierce')]), Js([Js('Brand'), Js('High/Noble/Fine')]), Js([Js('Brass'), Js('White Heat')]), Js([Js('Breged'), Js('Violence/Suddenness')]), Js([Js('Bregol'), Js('Violent/Fierce')]), Js([Js('Brethil'), Js('Beech')]), Js([Js('Bronad'), Js('Survival')]), Js([Js('Bronwe'), Js('Endurance/Faith')]), Js([Js('Brui'), Js('Loud/Noisy')]), Js([Js('Cîl'), Js('Cleft/Gorge')]), Js([Js('Cîl'), Js('Renewal')]), Js([Js('Cîr'), Js('Renewed')]), Js([Js('Cîw'), Js('Fresh/New')]), Js([Js('Côf'), Js('Bay')]), Js([Js('Côl'), Js('Gold')]), Js([Js('Cû'), Js('Bow')]), Js([Js('Cûn'), Js('Bow-shaped/Bent')]), Js([Js('Cadu'), Js('Shaped/Formed')]), Js([Js('Cadwor'), Js('Shapely')]), Js([Js('Cae'), Js('Earth')]), Js([Js('Cael'), Js('Sickness')]), Js([Js('Caeleb'), Js('Bedridden/Sick')]), Js([Js('Caew'), Js('Lair')]), Js([Js('Cai'), Js('Hedge')]), Js([Js('Cail'), Js('Sharp Fence')]), Js([Js('Cair'), Js('Ship')]), Js([Js('Calad'), Js('Light')]), Js([Js('Calaer'), Js('Light of the Sea')]), Js([Js('Calar'), Js('Lamp')]), Js([Js('Calardan'), Js('Lampwright')]), Js([Js('Caledhel'), Js('Light Elf')]), Js([Js('Calemir'), Js('Green Jewel')]), Js([Js('Calen'), Js('Green')]), Js([Js('Calithil'), Js('Moon Light')]), Js([Js('Callon'), Js('Hero')]), Js([Js('Calph'), Js('Water-Vessel')]), Js([Js('Camaen'), Js('Skilled Hand')]), Js([Js('Cand'), Js('Bold')]), Js([Js('Caran'), Js('Red')]), Js([Js('Carandol'), Js('Red Head')]), Js([Js('Caranor'), Js('Red Fire')]), Js([Js('Caraphind'), Js('Red Hair')]), Js([Js('Caras'), Js('City')]), Js([Js('Cast'), Js('Cape/Cove')]), Js([Js('Caun'), Js('Valor')]), Js([Js('Cef'), Js('Soil')]), Js([Js('Celair'), Js('Brilliant')]), Js([Js('Celeb'), Js('Silver')]), Js([Js('Celeblas'), Js('Silver Leaf')]), Js([Js('Celebren'), Js('Silvery')]), Js([Js('Celeg'), Js('Swift/Agile/Hasty')]), Js([Js('Celephind'), Js('Silver Tresses')]), Js([Js('Cellin'), Js('Flowing Music')]), Js([Js('Celon'), Js('River')]), Js([Js('Cennan'), Js('Potter')]), Js([Js('Ceven'), Js('Earthen')]), Js([Js('Claur'), Js('Splendour/Glory')]), Js([Js('Colfind'), Js('Gold Hair')]), Js([Js('Coll'), Js('Golden Red')]), Js([Js('Corch'), Js('Crow')]), Js([Js('Coru'), Js('Cunning')]), Js([Js('Cost'), Js('Quarrel')]), Js([Js('Coth'), Js('Enemy')]), Js([Js('Craban'), Js('Raven')]), Js([Js('Cugu'), Js('Dove')]), Js([Js('Curu'), Js('Skilled')]), Js([Js('Curulaer'), Js('Song Skill')]), Js([Js('Dílloth'), Js('Silent Flower')]), Js([Js('Dínen'), Js('Silent')]), Js([Js('Dôl'), Js('Hill/Mountain')]), Js([Js('Dúlind'), Js('Nightingale')]), Js([Js('Dúven'), Js('Southern')]), Js([Js('Dû'), Js('Nightfall')]), Js([Js('Dûr'), Js('Dark')]), Js([Js('Dûr'), Js('Somber')]), Js([Js('Dae'), Js('Shadow')]), Js([Js('Daedhel'), Js('Shadow of Horror')]), Js([Js('Daedhrog'), Js('Shadow Wolf')]), Js([Js('Daer'), Js('Great')]), Js([Js('Dam'), Js('Hammer')]), Js([Js('Dath'), Js('Hole/Pit/Abyss')]), Js([Js('Daug'), Js('Warrior/Soldier')]), Js([Js('Daw'), Js('Night/Gloom')]), Js([Js('Del'), Js('Fear/Disgust')]), Js([Js('Deldhin'), Js('Silent Horror')]), Js([Js('Deleb'), Js('Horrible/Loathsome')]), Js([Js('Delgaran'), Js('Red Horror')]), Js([Js('Delos'), Js('Detestation/Loathing')]), Js([Js('Delu'), Js('Hateful/Deadly/Fell')]), Js([Js('Dem'), Js('Sad/Gloomy')]), Js([Js('Dimaethor'), Js('Silence Warrior')]), Js([Js('Dinalagos'), Js('Silent Storm')]), Js([Js('Doll'), Js('Dark/Dusky')]), Js([Js('Doron'), Js('Oak')]), Js([Js('Draug'), Js('Wolf')]), Js([Js('Dringol'), Js('Wise Hammerer')]), Js([Js('Duin'), Js('River')]), Js([Js('Duinen'), Js('Flood/High Tide')]), Js([Js('Duirro'), Js('River-Bank')]), Js([Js('Duvain'), Js('Beautiful Darkness')]), Js([Js('Ech'), Js('Spine')]), Js([Js('Echad'), Js('Camp')]), Js([Js('Echui'), Js('Awakening')]), Js([Js('Ecthel'), Js('Spearpoint')]), Js([Js('Eden'), Js('New')]), Js([Js('Edlen'), Js('Exiled')]), Js([Js('Edraith'), Js('Saving')]), Js([Js('Eglan'), Js('Forsaken')]), Js([Js('Egnas'), Js('Sharp Point')]), Js([Js('Eiliant'), Js('Rainbow')]), Js([Js('Elhael'), Js('Wise Elf')]), Js([Js('Ellavorn'), Js('Staying Elf')]), Js([Js('Elu'), Js('Light Blue')]), Js([Js('Emlin'), Js('Yellow Bird')]), Js([Js('Ened'), Js('Centre/Middle')]), Js([Js('Ephel'), Js('Outer Fence')]), Js([Js('Erch'), Js('Prickle')]), Js([Js('Eredh'), Js('Seed')]), Js([Js('Erist'), Js('Lone Lore')]), Js([Js('Erthor'), Js('Uniter')]), Js([Js('Eru'), Js('Waste/Desert')]), Js([Js('Erwarth'), Js('Lone Betrayer')]), Js([Js('Eryn'), Js('Woods')]), Js([Js('Esgal'), Js('Screen/Veil')]), Js([Js('Esgalnor'), Js('Hiding Fire')]), Js([Js('Esgalwath'), Js('Hiding Shadow')]), Js([Js('Esgar'), Js('Shore')]), Js([Js('Estel'), Js('Hope/Trust')]), Js([Js('Estelmist'), Js('Lost Hope')]), Js([Js('Estent'), Js('Short')]), Js([Js('Estolad'), Js('Encampment')]), Js([Js('Ethir'), Js('River Mouth/Estuary')]), Js([Js('Ethir'), Js('Spy')]), Js([Js('Fân'), Js('Bright Figure/Veil/White Cloud')]), Js([Js('Fêr'), Js('Beech-Tree')]), Js([Js('Faeg'), Js('Bad/Mean/Poor')]), Js([Js('Fael'), Js('Generous')]), Js([Js('Faen'), Js('Radiant White')]), Js([Js('Faerdhinen'), Js('Silent Spirit')]), Js([Js('Faerthurin'), Js('Secret Spirit')]), Js([Js('Faervel'), Js('Strong Spirit')]), Js([Js('Faerveren'), Js('Joyous Spirit')]), Js([Js('Fain'), Js('Cloud')]), Js([Js('Fain'), Js('White')]), Js([Js('Falas'), Js('Beach')]), Js([Js('Falch'), Js('Ravine')]), Js([Js('Fang'), Js('Beard')]), Js([Js('Far'), Js('Sufficient')]), Js([Js('Fast'), Js('Shaggy Hair')]), Js([Js('Faug'), Js('Thirsty')]), Js([Js('Faun'), Js('Cloud')]), Js([Js('Faur'), Js('Beach/Shore')]), Js([Js('Fela'), Js('Cave')]), Js([Js('Fend'), Js('Door/Threshold')]), Js([Js('Fileg'), Js('Little Birds')]), Js([Js('Fim'), Js('Slender')]), Js([Js('Fingaer'), Js('Coppery Red Hair')]), Js([Js('Forn'), Js('North')]), Js([Js('Forod'), Js('North')]), Js([Js('Forven'), Js('North')]), Js([Js('Fuin'), Js('Night/Darkness')]), Js([Js('Fuir'), Js('North')]), Js([Js('Gûd'), Js('Foe')]), Js([Js('Gûl'), Js('Sorcery')]), Js([Js('Gûr'), Js('Death')]), Js([Js('Gûr'), Js('Heart/Counsel')]), Js([Js('Gador'), Js('Prison/Dungeon')]), Js([Js('Gae'), Js('Dread')]), Js([Js('Gaear'), Js('Sea')]), Js([Js('Gael'), Js('Pale/Glimmering')]), Js([Js('Gaer'), Js('Coppery Red')]), Js([Js('Gaer'), Js('Dreadful')]), Js([Js('Gaer'), Js('Sea')]), Js([Js('Gaeralagos'), Js('Sea Storm')]), Js([Js('Gaeruil'), Js('Seaweed')]), Js([Js('Gail'), Js('Star/Bright Light')]), Js([Js('Gal'), Js('Light')]), Js([Js('Galad'), Js('Light/Radiance')]), Js([Js('Galadh'), Js('Tree')]), Js([Js('Galas'), Js('Plant')]), Js([Js('Galenas'), Js('Pipeweed')]), Js([Js('Galu'), Js('Good Fortune')]), Js([Js('Gamp'), Js('Hook/Claw')]), Js([Js('Gannel'), Js('Harp')]), Js([Js('Garaf'), Js('Wolf')]), Js([Js('Garth'), Js('Fortress')]), Js([Js('Gas'), Js('Hole')]), Js([Js('Gath'), Js('Cavern')]), Js([Js('Gathrod'), Js('Cave')]), Js([Js('Gaud'), Js('Machine')]), Js([Js('Gaul'), Js('Wolf-Howl')]), Js([Js('Gaur'), Js('Werewolf')]), Js([Js('Gaw'), Js('Void')]), Js([Js('Gawad'), Js('Howling')]), Js([Js('Gelinnas'), Js('Joyful Will')]), Js([Js('Gell'), Js('Joy/Triumph')]), Js([Js('Gellam'), Js('Jubilation')]), Js([Js('Gellui'), Js('Triumphant')]), Js([Js('Gem'), Js('Sickly')]), Js([Js('Gern'), Js('Old/Decripit')]), Js([Js('Gilorn'), Js('Star Tree')]), Js([Js('Girith'), Js('Shuddering/Horror')]), Js([Js('Glân'), Js('White')]), Js([Js('Glî'), Js('Honey')]), Js([Js('Glîn'), Js('Gleam/Glint')]), Js([Js('Glîr'), Js('Song')]), Js([Js('Glûdh'), Js('Soap')]), Js([Js('Glaew'), Js('Salve')]), Js([Js('Glam'), Js('Shouting/Uproar')]), Js([Js('Glamor'), Js('Echo')]), Js([Js('Glamren'), Js('Echoing')]), Js([Js('Glass'), Js('Joy')]), Js([Js('Glaur'), Js('Golden Light')]), Js([Js('Glavrol'), Js('Babbling')]), Js([Js('Glaw'), Js('Radiance')]), Js([Js('Glawar'), Js('Sunlight/Radiance')]), Js([Js('Gloss'), Js('Snow-White')]), Js([Js('Gobel'), Js('Town')]), Js([Js('Goe'), Js('Terror')]), Js([Js('Goeol'), Js('Dreadful/Terrifying')]), Js([Js('Golf'), Js('Branch')]), Js([Js('Goll'), Js('Wise')]), Js([Js('Gollor'), Js('Magician')]), Js([Js('Golwen'), Js('Wise')]), Js([Js('Gond'), Js('Stone/Rock')]), Js([Js('Gorf'), Js('Vigor')]), Js([Js('Gorfuin'), Js('Dreaded Gloom')]), Js([Js('Gorn'), Js('Impetuous/Valor')]), Js([Js('Gorog'), Js('Horror')]), Js([Js('Goroth'), Js('Horror')]), Js([Js('Gorth'), Js('Horror')]), Js([Js('Gorthad'), Js('Barrow')]), Js([Js('Gortheb'), Js('Horrible')]), Js([Js('Gost'), Js('Dread')]), Js([Js('Gowest'), Js('Contract/Treaty')]), Js([Js('Graw'), Js('Bear')]), Js([Js('Grond'), Js('Club')]), Js([Js('Groth'), Js('Cave/Tunnel')]), Js([Js('Gruin'), Js('Ruddy')]), Js([Js('Guldur'), Js('Black Magic')]), Js([Js('Gurgaran'), Js('Red Death')]), Js([Js('Gurth'), Js('Death')]), Js([Js('Guruth'), Js('Death')]), Js([Js('Gwî'), Js('Net/Web')]), Js([Js('Gwaedh'), Js('Bond/Oath')]), Js([Js('Gwael'), Js('Gull')]), Js([Js('Gwaen'), Js('Stained')]), Js([Js('Gwaeren'), Js('Windy')]), Js([Js('Gwaew'), Js('Wind')]), Js([Js('Gwain'), Js('New')]), Js([Js('Gwas'), Js('Stain')]), Js([Js('Gwastar'), Js('Hummock')]), Js([Js('Gwath'), Js('Shade/Shadow')]), Js([Js('Gwaun'), Js('Goose')]), Js([Js('Gwaur'), Js('Soiled/Dirty')]), Js([Js('Gwedh'), Js('Bond')]), Js([Js('Gwelu'), Js('Air')]), Js([Js('Gwend'), Js('Bond/Friendship')]), Js([Js('Gwilith'), Js('Air')]), Js([Js('Gwilwileth'), Js('Butterfly')]), Js([Js('Gwing'), Js('Spindrift/Foam')]), Js([Js('Hâdh'), Js('Cleaver')]), Js([Js('Hâl'), Js('Fish')]), Js([Js('Hîw'), Js('Sticky')]), Js([Js('Hû'), Js('Dog')]), Js([Js('Hûb'), Js('Haven/Harbor/Bay')]), Js([Js('Hûl'), Js('Battle Cry')]), Js([Js('Hûr'), Js('Vigour/Fiery Spirit')]), Js([Js('Habad'), Js('Shoe')]), Js([Js('Hadlath'), Js('Sling')]), Js([Js('Hae'), Js('Far/Remote/Distant')]), Js([Js('Haedirn'), Js('Remote Watcher')]), Js([Js('Haered'), Js('Remote Distance')]), Js([Js('Haerel'), Js('Distant Star')]), Js([Js('Haeron'), Js('Far/Remote/Distant')]), Js([Js('Haew'), Js('Custom/Habit')]), Js([Js('Half'), Js('Seashell')]), Js([Js('Hall'), Js('Exalted')]), Js([Js('Hall'), Js('Tall/Hidden')]), Js([Js('Halloth'), Js('Hiding Flower')]), Js([Js('Ham'), Js('Chair')]), Js([Js('Hand'), Js('Intelligent')]), Js([Js('Harad'), Js('South')]), Js([Js('Haradren'), Js('Southern')]), Js([Js('Harn'), Js('Helmet')]), Js([Js('Harn'), Js('Southern')]), Js([Js('Harn'), Js('Wounded')]), Js([Js('Haru'), Js('Wound')]), Js([Js('Hast'), Js('Axe-Stroke')]), Js([Js('Hathol'), Js('Blade/Axe')]), Js([Js('Haudh'), Js('Tomb')]), Js([Js('Haust'), Js('Bed')]), Js([Js('Helch'), Js('Bitter Cold')]), Js([Js('Heledh'), Js('Glass')]), Js([Js('Heledir'), Js('Kingfisher')]), Js([Js('Heleg'), Js('Ice')]), Js([Js('Heleth'), Js('Fur/Fur-Coat')]), Js([Js('Helf'), Js('Fur')]), Js([Js('Hell'), Js('Naked')]), Js([Js('Henneth'), Js('Window')]), Js([Js('Hethurin'), Js('Secret Child')]), Js([Js('Him'), Js('Cold')]), Js([Js('Him'), Js('Steadfast/Abiding')]), Js([Js('Himel'), Js('Cold Star')]), Js([Js('Hinnor'), Js('Fire Eyes')]), Js([Js('Hissael'), Js('Wise Eyes')]), Js([Js('Hith'), Js('Mist/Fog')]), Js([Js('Hithaer'), Js('Sea Mist')]), Js([Js('Hithfaer'), Js('Mist Spirit')]), Js([Js('Hithu'), Js('Fog')]), Js([Js('Horn'), Js('Driven/Impelled')]), Js([Js('Hwest'), Js('Breeze')]), Js([Js('Hwind'), Js('Twirling/Whirling')]), Js([Js('Iâ'), Js('Abyss')]), Js([Js('Iâr'), Js('Blood')]), Js([Js('Iôl'), Js('Flood Plain')]), Js([Js('Iûl'), Js('Embers')]), Js([Js('Iach'), Js('Ford/Crossing')]), Js([Js('Iaew'), Js('Mocking/Scorn')]), Js([Js('Ial'), Js('Call/Cry')]), Js([Js('Iant'), Js('Bridge')]), Js([Js('Ianu'), Js('Yoke')]), Js([Js('Iau'), Js('Corn')]), Js([Js('Iau'), Js('Ravine/Gulf')]), Js([Js('Iaun'), Js('Sanctuary')]), Js([Js('Iaur'), Js('Ancient/Old')]), Js([Js('Idhren'), Js('Wise/Thoughtful')]), Js([Js('Iest'), Js('Wish')]), Js([Js('Inc'), Js('Guess/Idea/Notion')]), Js([Js('Ind'), Js('Inner Thought/Meaning/Heart')]), Js([Js('Ingem'), Js('Old/Year-Sick')]), Js([Js('Inu'), Js('Feminine')]), Js([Js('Iorist'), Js('Ancient Lore')]), Js([Js('Iorthon'), Js('Old Pine')]), Js([Js('Iphant'), Js('Aged/Old')]), Js([Js('Ist'), Js('Knowledge/Lore')]), Js([Js('Istui'), Js('Learned')]), Js([Js('Ivor'), Js('Crystal')]), Js([Js('Lîn'), Js('Pool')]), Js([Js('Lîr'), Js('Song/Poem')]), Js([Js('Lô'), Js('Shallow Lake/Marshland')]), Js([Js('Lûg'), Js('Snake/Serpent')]), Js([Js('Lûth'), Js('Spell/Charm')]), Js([Js('Lach'), Js('Flame')]), Js([Js('Lad'), Js('Plain/Valley')]), Js([Js('Ladrengil'), Js('Valley of Stars')]), Js([Js('Laeb'), Js('Fresh')]), Js([Js('Laeg'), Js('Green')]), Js([Js('Laeg'), Js('Keen/Sharp/Acute')]), Js([Js('Laer'), Js('Song')]), Js([Js('Laergul'), Js('Song of Sorcery')]), Js([Js('Laerorn'), Js('Tree Song')]), Js([Js('Lagorúth'), Js('Swift Anger')]), Js([Js('Lagor'), Js('Swift/Rapid')]), Js([Js('Lain'), Js('Free')]), Js([Js('Lain'), Js('Thread')]), Js([Js('Lalf'), Js('Elm')]), Js([Js('Lamaen'), Js('Clever Tongue')]), Js([Js('Lanc'), Js('Naked')]), Js([Js('Land'), Js('Wide/Broad')]), Js([Js('Lang'), Js('Cutlass/Sword')]), Js([Js('Lant'), Js('Clearing')]), Js([Js('Lant'), Js('Fall')]), Js([Js('Lanthir'), Js('Waterfall')]), Js([Js('Lass'), Js('Leaf')]), Js([Js('Laug'), Js('Warm')]), Js([Js('Lavan'), Js('Animal')]), Js([Js('Leithian'), Js('Release/Freeing')]), Js([Js('Lend'), Js('Journey')]), Js([Js('Lend'), Js('Tuneful/Sweet')]), Js([Js('Lest'), Js('Girdle')]), Js([Js('Lhê'), Js('Thread')]), Js([Js('Lhîw'), Js('Sickness')]), Js([Js('Lhaew'), Js('Sickly/Ill')]), Js([Js('Lhain'), Js('Lean/Thin')]), Js([Js('Lhind'), Js('Fine/Slender')]), Js([Js('Lhing'), Js('Spider/Spiderweb')]), Js([Js('Lhoss'), Js('Whisper/Rustle')]), Js([Js('Lif'), Js('Link')]), Js([Js('Lim'), Js('Clear/Sparkling')]), Js([Js('Lim'), Js('Fish')]), Js([Js('Limlug'), Js('Seaserpent')]), Js([Js('Limp'), Js('Wet')]), Js([Js('Lith'), Js('Ash/Sand/Dust')]), Js([Js('Lithui'), Js('Ashen/Dusty')]), Js([Js('Lobor'), Js('Horse')]), Js([Js('Loeg'), Js('Pool')]), Js([Js('Loen'), Js('Soaking Wet/Swamped')]), Js([Js('Lom'), Js('Weary')]), Js([Js('Long'), Js('Heavy')]), Js([Js('Lorn'), Js('Harbour')]), Js([Js('Loss'), Js('Snow')]), Js([Js('Lossam'), Js('Empty Chamber')]), Js([Js('Lossen'), Js('Snowy')]), Js([Js('Lost'), Js('Empty')]), Js([Js('Loth'), Js('Flower')]), Js([Js('Lothuial'), Js('Twilight Blossom')]), Js([Js('Luin'), Js('Blue')]), Js([Js('Lum'), Js('Shade')]), Js([Js('Lumorn'), Js('Tree Shade')]), Js([Js('Mâl'), Js('Pollen')]), Js([Js('Mírdan'), Js('Jewel Smith')]), Js([Js('Míresgal'), Js('Hidden Jewel')]), Js([Js('Mîl'), Js('Love/Affection')]), Js([Js('Mîr'), Js('Jewel/Treasure')]), Js([Js('Mîw'), Js('Small/Tiny/Frail')]), Js([Js('Môr'), Js('Darkness/Night')]), Js([Js('Mûl'), Js('Slave')]), Js([Js('Mae'), Js('Soft')]), Js([Js('Maeas'), Js('Dough')]), Js([Js('Maecheneb'), Js('Sharp-Eyed')]), Js([Js('Maed'), Js('Shapely')]), Js([Js('Maegorod'), Js('Sharp Mountain')]), Js([Js('Mael'), Js('Lust')]), Js([Js('Mael'), Js('Stain/Stained')]), Js([Js('Maen'), Js('Skilled/Clever')]), Js([Js('Maer'), Js('Good/Useful/Fit')]), Js([Js('Maeth'), Js('Battle/Fight')]), Js([Js('Maew'), Js('Sea Gull')]), Js([Js('Magol'), Js('Sword')]), Js([Js('Magor'), Js('Swordsman')]), Js([Js('Maidh'), Js('Pale')]), Js([Js('Malen'), Js('Yellow')]), Js([Js('Malfind'), Js('Gold Hair')]), Js([Js('Malgelir'), Js('Golden Happy Person')]), Js([Js('Mallos'), Js('Golden Flower')]), Js([Js('Malt'), Js('Gold')]), Js([Js('Malu'), Js('Fallow/Pale')]), Js([Js('Manadh'), Js('Doom/Fate/Fortune')]), Js([Js('Maur'), Js('Gloom')]), Js([Js('Maw'), Js('Soil/Stain')]), Js([Js('Medlí'), Js('Bear')]), Js([Js('Medlin'), Js('Bearlike')]), Js([Js('Megilagor'), Js('Rapid Sword')]), Js([Js('Megor'), Js('Sharp/Pointed')]), Js([Js('Melch'), Js('Greedy')]), Js([Js('Mell'), Js('Dear')]), Js([Js('Melui'), Js('Lovely/Sweet')]), Js([Js('Men'), Js('Way/Road')]), Js([Js('Ment'), Js('Point')]), Js([Js('Meren'), Js('Festive/Joyous')]), Js([Js('Meril'), Js('Rose')]), Js([Js('Merilin'), Js('Nightingale')]), Js([Js('Midh'), Js('Dew')]), Js([Js('Milui'), Js('Friendly/Loving/Kind')]), Js([Js('Minas'), Js('Tower')]), Js([Js('Mindon'), Js('Hill/Tower')]), Js([Js('Mist'), Js('Straying/Error')]), Js([Js('Mist'), Js('Wandering')]), Js([Js('Mith'), Js('Grey')]), Js([Js('Mith'), Js('White Fog/Wet Mist')]), Js([Js('Mithril'), Js('True-Silver')]), Js([Js('Morfind'), Js('Black Haired')]), Js([Js('Morgul'), Js('Black Magic/Necromancy')]), Js([Js('Mormeril'), Js('Black Rose')]), Js([Js('Morn'), Js('Black')]), Js([Js('Muil'), Js('Drear')]), Js([Js('Muin'), Js('Dear/Beloved')]), Js([Js('Mund'), Js('Bull')]), Js([Js('Myl'), Js('Gull')]), Js([Js('Nínim'), Js('Snowdrop')]), Js([Js('Nîd'), Js('Tearful')]), Js([Js('Nîd'), Js('Wet')]), Js([Js('Nîdh'), Js('Honeycomb')]), Js([Js('Nîn'), Js('Tear')]), Js([Js('Nîn'), Js('Watery')]), Js([Js('Nîr'), Js('Tear/Weeping')]), Js([Js('Nórui'), Js('Sunny')]), Js([Js('Nûr'), Js('Sad')]), Js([Js('Nadhor'), Js('Pasture')]), Js([Js('Naer'), Js('Sad/Lamentable')]), Js([Js('Nan'), Js('Grassland/Valley')]), Js([Js('Nardh'), Js('Knot')]), Js([Js('Naru'), Js('Red')]), Js([Js('Naruthir'), Js('Red Face')]), Js([Js('Nath'), Js('Web')]), Js([Js('Naud'), Js('Bound')]), Js([Js('Naur'), Js('Fire')]), Js([Js('Nell'), Js('Bell')]), Js([Js('Nemir'), Js('Water Jewel')]), Js([Js('Nen'), Js('Water')]), Js([Js('Nend'), Js('Wet')]), Js([Js('Nengel'), Js('Water Joy')]), Js([Js('Neth'), Js('Young')]), Js([Js('Niben'), Js('Small')]), Js([Js('Nimp'), Js('Small/Frail')]), Js([Js('Nimp'), Js('White')]), Js([Js('Ninael'), Js('Tears of a Pool')]), Js([Js('Nind'), Js('Slender')]), Js([Js('Ningaear'), Js('Tears of the Sea')]), Js([Js('Ningannel'), Js('Tears of a Harp')]), Js([Js('Ninniach'), Js('Rainbow')]), Js([Js('Nirorn'), Js('Tear Tree')]), Js([Js('Norawarth'), Js('Forsaking Fire')]), Js([Js('Norgalad'), Js('Fire Radiance')]), Js([Js('Noruinif'), Js('Sunny Face')]), Js([Js('Ogol'), Js('Wicked/Evil')]), Js([Js('Oldhin'), Js('Dream of Silence')]), Js([Js('Oll'), Js('Stream')]), Js([Js('Orchal'), Js('Superior/Lofty')]), Js([Js('Orchal'), Js('Tall')]), Js([Js('Orel'), Js('Morning Star')]), Js([Js('Orn'), Js('Tree')]), Js([Js('Orod'), Js('Mountain')]), Js([Js('Osp'), Js('Reek')]), Js([Js('Osp'), Js('Smoke')]), Js([Js('Pâd'), Js('Way/Path')]), Js([Js('Pant'), Js('Full')]), Js([Js('Parch'), Js('Dry')]), Js([Js('Parf'), Js('Book')]), Js([Js('Parth'), Js('Fenced Field')]), Js([Js('Path'), Js('Smooth')]), Js([Js('Pe-lam'), Js('Without Language')]), Js([Js('Pe-phennas'), Js('No Past')]), Js([Js('Peg'), Js('Spot/Dot')]), Js([Js('Pel'), Js('Fenced Field')]), Js([Js('Pelilas'), Js('Fading Leaf')]), Js([Js('Pelinel'), Js('Fading Star')]), Js([Js('Pelingil'), Js('Fading Star')]), Js([Js('Pen-estel'), Js('Hopeless')]), Js([Js('Peng'), Js('Bow')]), Js([Js('Pent'), Js('Tale')]), Js([Js('Perchalad'), Js('Half Tall')]), Js([Js('Peth'), Js('Word')]), Js([Js('Pigen'), Js('Tiny')]), Js([Js('Puig'), Js('Clean')]), Js([Js('Râd'), Js('Path/Track')]), Js([Js('Rî'), Js('Crown/Garland')]), Js([Js('Rîl'), Js('Brilliance')]), Js([Js('Rîn'), Js('Crowned')]), Js([Js('Rîn'), Js('Remembrance')]), Js([Js('Rûdh'), Js('Bald')]), Js([Js('Rûth'), Js('Anger')]), Js([Js('Raef'), Js('Net')]), Js([Js('Raeg'), Js('Crooked')]), Js([Js('Raeg'), Js('Wrong')]), Js([Js('Raen'), Js('Crooked')]), Js([Js('Raen'), Js('Nettled/Enlaced')]), Js([Js('Rain'), Js('Erratic Wandering')]), Js([Js('Ram'), Js('Wall')]), Js([Js('Rant'), Js('Riverbed')]), Js([Js('Raph'), Js('Rope')]), Js([Js('Ravon'), Js('Wing')]), Js([Js('Raw'), Js('Lion')]), Js([Js('Raw'), Js('Riverbank')]), Js([Js('Rem'), Js('Mesh/Net')]), Js([Js('Remlas'), Js('Joy Net')]), Js([Js('Rhaw'), Js('Wild/Untamed')]), Js([Js('Rhosg'), Js('Brown')]), Js([Js('Rhossolas'), Js('Rustling Folliage')]), Js([Js('Rhovan'), Js('Wilderness')]), Js([Js('Rim'), Js('Cold Mountain Pool')]), Js([Js('Ring'), Js('Cold')]), Js([Js('Riros'), Js('Red Crown')]), Js([Js('Rivalt'), Js('Gold Crown')]), Js([Js('Rivorn'), Js('Black Crown')]), Js([Js('Roch'), Js('Horse')]), Js([Js('Rom'), Js('Horn/Trumpet')]), Js([Js('Ross'), Js('Rain')]), Js([Js('Ross'), Js('Red-Haired')]), Js([Js('Rothruin'), Js('Fiery Red-Haired')]), Js([Js('Rui'), Js('Hunting')]), Js([Js('Ruin'), Js('Fiery Red')]), Js([Js('Ruindol'), Js('Fiery Red Head')]), Js([Js('Rusc'), Js('Fox')]), Js([Js('Rust'), Js('Copper')]), Js([Js('Ryn'), Js('Hound')]), Js([Js('Sírdhem'), Js('River of Sadness')]), Js([Js('Sîdh'), Js('Peace')]), Js([Js('Sîr'), Js('River')]), Js([Js('Sûl'), Js('Wind')]), Js([Js('Sael'), Js('Wise')]), Js([Js('Saeledhel'), Js('Wise Elf')]), Js([Js('Saer'), Js('Bitter')]), Js([Js('Saew'), Js('Poison')]), Js([Js('Sain'), Js('New')]), Js([Js('Salab'), Js('Herb')]), Js([Js('Sarn'), Js('Pebble/Stone')]), Js([Js('Sereg'), Js('Blood')]), Js([Js('Seregruth'), Js('Blood Anger')]), Js([Js('Seron'), Js('Lover')]), Js([Js('Silef'), Js('Shining White Crystal')]), Js([Js('Silevren'), Js('Glittering')]), Js([Js('Solch'), Js('Root')]), Js([Js('Tû'), Js('Strength')]), Js([Js('Tûg'), Js('Thick/Fat')]), Js([Js('Tûr'), Js('Mastery/Victory')]), Js([Js('Taen'), Js('Long and Thin')]), Js([Js('Taer'), Js('Straight')]), Js([Js('Talagan'), Js('Harper')]), Js([Js('Talath'), Js('Flatland/Plain')]), Js([Js('Talf'), Js('Flatland/Field')]), Js([Js('Tara'), Js('Tough/Stiff')]), Js([Js('Tathar'), Js('Willow')]), Js([Js('Taur'), Js('Forest')]), Js([Js('Tavor'), Js('Woodpecker')]), Js([Js('Taw'), Js('Wool')]), Js([Js('Tegilbor'), Js('Writer')]), Js([Js('Tegol'), Js('Pen')]), Js([Js('Thâr'), Js('Stiff Grass')]), Js([Js('Thîn'), Js('Evening')]), Js([Js('Thôn'), Js('Pine')]), Js([Js('Thôr'), Js('Eagle')]), Js([Js('Thala'), Js('Stalwart/Steady')]), Js([Js('Thalawest'), Js('Steady Oath')]), Js([Js('Thand'), Js('Firm/True')]), Js([Js('Thand'), Js('Shield')]), Js([Js('Thangur'), Js('True Heart')]), Js([Js('Tharbad'), Js('Crossroad')]), Js([Js('Tharn'), Js('Stiff/Rigid/Withered')]), Js([Js('Thaur'), Js('Abominable/Abhorrent')]), Js([Js('Thaw'), Js('Corrupt/Rotten')]), Js([Js('Thent'), Js('Short')]), Js([Js('Thind'), Js('Pale/Grey')]), Js([Js('Thirist'), Js('Cut Face')]), Js([Js('Thond'), Js('Root')]), Js([Js('Thurilost'), Js('Empty Secret')]), Js([Js('Thurin'), Js('Secret')]), Js([Js('Thurin'), Js('Secret/Hidden')]), Js([Js('Tinc'), Js('Metal')]), Js([Js('Tinnu'), Js('Twilight')]), Js([Js('Tint'), Js('Spark')]), Js([Js('Tinu'), Js('Spark')]), Js([Js('Tinu'), Js('Star')]), Js([Js('Tirnel'), Js('Star Gazer')]), Js([Js('Tithen'), Js('Little/Tiny')]), Js([Js('Tol'), Js('Island')]), Js([Js('Tond'), Js('Tall')]), Js([Js('Toss'), Js('Bush')]), Js([Js('Trîw'), Js('Fine/Slender')]), Js([Js('Triwath'), Js('Slender Shadow')]), Js([Js('Tuiw'), Js('Sprout/Bud')]), Js([Js('Tulus'), Js('Poplar-Tree')]), Js([Js('Tund'), Js('Hill/Mound')]), Js([Js('Uial'), Js('Twilight')]), Js([Js('Uil'), Js('Seaweed')]), Js([Js('Uilos'), Js('Everwhite')]), Js([Js('Uir'), Js('Eternity')]), Js([Js('Uireb'), Js('Eternal')]), Js([Js('Ulund'), Js('Monster')]), Js([Js('Um'), Js('Bad/Evil')]), Js([Js('Ungol'), Js('Spider')]), Js([Js('Yr'), Js('River Course')])]))
var.put('nm2', Js([Js([Js('Gal'), Js('To Shine Clear')]), Js([Js('Gwathra'), Js('To Overshadow')]), Js([Js('Míria'), Js('To Shine')]), Js([Js('Síla'), Js('To Shine White')]), Js([Js('Thilia'), Js('To Glisten')]), Js([Js('Tinna'), Js('To Glint')]), Js([Js('Banga'), Js('To Trade')]), Js([Js('Achar'), Js('To Avenge')]), Js([Js('Adertha'), Js('To Reunite')]), Js([Js('Aphada'), Js('To Follow')]), Js([Js('Beria'), Js('To Protect')]), Js([Js('Brona'), Js('To Survive')]), Js([Js('Northa'), Js('To Make Run/Ride')]), Js([Js('Suila'), Js('To Greet')]), Js([Js('Toltha'), Js('To Fetch/Make Come')]), Js([Js('Tortha'), Js('To Wield/Control')]), Js([Js('Bartha'), Js('To Doom')]), Js([Js('Trasta'), Js('To Harass/Trouble')]), Js([Js('Trenar'), Js('To Recount')]), Js([Js('Trevad'), Js('To Traverse')]), Js([Js('Tir'), Js('To Watch/Gaze')]), Js([Js('Feira'), Js('To Suffice')]), Js([Js('Taetha'), Js('To Fasten/Tie')]), Js([Js('Fara'), Js('To Hunt')]), Js([Js('Tangada'), Js('To Make Firm')]), Js([Js('Toba'), Js('To Cover/Roof')]), Js([Js('Telia'), Js('To Play')]), Js([Js('Ertha'), Js('To Unite')]), Js([Js('Heria'), Js('To Have an Impulse')]), Js([Js('Tog'), Js('To Lead/Bring')]), Js([Js('Than'), Js('To Kindle')]), Js([Js('Nasta'), Js('To Prick/Thrust')]), Js([Js('Teitha'), Js('To Draw/Write')]), Js([Js('Hwinia'), Js('To Twirl/Whirl')]), Js([Js('Theria'), Js('To Dread/Fear')]), Js([Js('Theria'), Js('To Florish')]), Js([Js('Thosta'), Js('To Stink')]), Js([Js('Henia'), Js('To Understand')]), Js([Js('Sog'), Js('To Drink')]), Js([Js('Ran'), Js('To Wander/Stray')]), Js([Js('Rosta'), Js('To Hollow Out')]), Js([Js('Nella'), Js('To Ring Bells')]), Js([Js('Ruthra'), Js('To Rage')]), Js([Js('Rista'), Js('To Rend/Rip/Cut/Cleave')]), Js([Js('Ritha'), Js('To Jerk/Twitch/Snatch')]), Js([Js('Redh'), Js('To Sow')]), Js([Js('Rib'), Js('To Rush/Fly/Fling')]), Js([Js('Renia'), Js('To Stray/Wander')]), Js([Js('Revia'), Js('To Fly/Sail/Wander')]), Js([Js('Oltha'), Js('To Dream')]), Js([Js('Raitha'), Js('To Strive')]), Js([Js('Pada'), Js('To Walk')]), Js([Js('Rada'), Js('To Make/Find a Way')]), Js([Js('Raeda'), Js('To Catch in a Net')]), Js([Js('Penia'), Js('To Fix/Set')]), Js([Js('Presta'), Js('To Affect/Disrupt')]), Js([Js('Pel'), Js('To Fade/Wither')]), Js([Js('Padra'), Js('To Walk')]), Js([Js('Lacha'), Js('To Burn')]), Js([Js('Ped'), Js('To Say/Speak')]), Js([Js('Nesta'), Js('To Heal')]), Js([Js('Nod'), Js('To Tie/Bind')]), Js([Js('Orthel'), Js('To Roof')]), Js([Js('Orthor'), Js('To Master/Conquer')]), Js([Js('Osgar'), Js('To Amputate')]), Js([Js('Nor'), Js('To Run')]), Js([Js('Nautha'), Js('To Conceive a Thought')]), Js([Js('Nedia'), Js('To Count')]), Js([Js('Neitha'), Js('To Wrong/Deprive')]), Js([Js('Hortha'), Js('To Urge On/Impel')]), Js([Js('Lasta'), Js('To Listen')]), Js([Js('Maetha'), Js('To Fight')]), Js([Js('Maetha'), Js('To Handle/Wield')]), Js([Js('Dew'), Js('To Fail')]), Js([Js('Nartha'), Js('To Kindle')]), Js([Js('Muda'), Js('To Labor/Work')]), Js([Js('Naegra'), Js('To Cause Pain')]), Js([Js('Nara'), Js('To Narrate/Tell a Story')]), Js([Js('Narcha'), Js('To Rend/Rip/Tear')]), Js([Js('Mad'), Js('To Eat')]), Js([Js('Ialla'), Js('To Call/Yell')]), Js([Js('Nag'), Js('To Bite')]), Js([Js('Nalla'), Js('To Cry Out/Shout')]), Js([Js('Iuitha'), Js('To Use')]), Js([Js('Mista'), Js('To Stray/Be Mistaken')]), Js([Js('Leitha'), Js('To Set Free')]), Js([Js('Loda'), Js('To Float')]), Js([Js('Linna'), Js('To Chant'), Js(' Sing')]), Js([Js('Liria'), Js('To Sing')]), Js([Js('Laba'), Js('To Hop')]), Js([Js('Ista'), Js('To Know')]), Js([Js('Gad'), Js('To Catch')]), Js([Js('Gonod'), Js('To Count Up/Sum Up')]), Js([Js('Glavra'), Js('To Babble')]), Js([Js('Lútha'), Js('To Enchant')]), Js([Js('Gweria'), Js('To Betray/Cheat')]), Js([Js('Heb'), Js('To Keep')]), Js([Js('Harna'), Js('To Wound')]), Js([Js('Hartha'), Js('To Hope')]), Js([Js('Hasta'), Js('To Hack Through')]), Js([Js('Gwesta'), Js('To Swear/Oath')]), Js([Js('Can'), Js('To Shout')]), Js([Js('Groga'), Js('To be Terrified')]), Js([Js('Had'), Js('To Hurl/Throw/Sling')]), Js([Js('Basta'), Js('To Bake Bread')]), Js([Js('Gruitha'), Js('To Terrify')]), Js([Js('Gwedh'), Js('To Bind')]), Js([Js('Gladh'), Js('To Laugh')]), Js([Js('Gosta'), Js('To Fear')]), Js([Js('Carva'), Js('To Talk')]), Js([Js('Glir'), Js('To Sing/Recite Poetry')]), Js([Js('Gala'), Js('To Grow/Cultivate')]), Js([Js('Ganna'), Js('To Play a Harp')]), Js([Js('Feria'), Js('To Prepare')]), Js([Js('Doltha'), Js('To Conceal')]), Js([Js('Gir'), Js('To Shudder/Tremble')]), Js([Js('Esta'), Js('To Name/Call')]), Js([Js('Critha'), Js('To Reap')]), Js([Js('Elia'), Js('To Bless/Help Out')]), Js([Js('Draf'), Js('To Hew')]), Js([Js('Echad'), Js('To Make/Fashion')]), Js([Js('Eitha'), Js('To Ease/Assist')]), Js([Js('Eitha'), Js('To Prick/Insult')]), Js([Js('Egleria'), Js('To Praise')]), Js([Js('Def'), Js('To Try')]), Js([Js('Dreg'), Js('To Flee/Run Away')]), Js([Js('Dringa'), Js('To Beat')]), Js([Js('Damma'), Js('To Hammer')]), Js([Js('Delia'), Js('To Conceal')]), Js([Js('Cen'), Js('To See')]), Js([Js('Brenia'), Js('To Endure')]), Js([Js('Bertha'), Js('To Dare')]), Js([Js('Dag'), Js('To Slay')]), Js([Js('Cab'), Js('To Leap')]), Js([Js('Aphed'), Js('To Answer')]), Js([Js('Amartha'), Js('To Decree')]), Js([Js('Awartha'), Js('To Forsake/Abandon')]), Js([Js('Adleg'), Js('To Loose/Release')])]))
var.put('nm3', Js([Js([Js(''), Js(''), Js('')])]))
var.put('lastChar', Js(''))
pass
pass


# Add lib to the module scope
lotrElfNames = var.to_python()