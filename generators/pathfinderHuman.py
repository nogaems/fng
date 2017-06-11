__all__ = ['pathfinderHuman']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm1', 'nm11', 'nm24', 'nm29', 'nm56', 'nm16', 'nm47', 'nm49', 'nm23', 'nm31', 'nm63', 'nm3', 'nm62', 'nm33', 'nm34', 'nm41', 'nm44', 'nm48', 'nm51', 'nm2', 'nm27', 'nm26', 'nm54', 'nm30', 'nm36', 'nm39', 'nm22', 'nm14', 'nm59', 'nm7', 'nm10', 'nm21', 'nm25', 'nm40', 'nm42', 'nm45', 'nm15', 'nm20', 'nm64', 'nm58', 'nm43', 'nm55', 'nm12', 'nm32', 'nm5', 'nm65', 'nm60', 'nm6', 'nm35', 'nm46', 'nm4', 'nameGen', 'nm8', 'nm28', 'nm18', 'nm37', 'nm17', 'nm13', 'nm9', 'nm38', 'nm50', 'nm57', 'nm52', 'nm61', 'nm53'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(12.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                        var.put('names', (((((((var.get('nm12').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd3')))+var.get('nm13').get(var.get('rnd4')))+var.get('nm15').get(var.get('rnd5')))+Js(' '))+var.get('nm16').get(var.get('rnd6')))+var.get('nm17').get(var.get('rnd7'))))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm23').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm23').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length'))))
                            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm29').get('length'))))
                            def PyJs_LONG_0_(var=var):
                                return var.put('names', ((((((((((var.get('nm22').get(var.get('rnd'))+var.get('nm23').get(var.get('rnd2')))+var.get('nm24').get(var.get('rnd3')))+var.get('nm23').get(var.get('rnd4')))+var.get('nm25').get(var.get('rnd5')))+Js(' '))+var.get('nm26').get(var.get('rnd6')))+var.get('nm27').get(var.get('rnd7')))+var.get('nm28').get(var.get('rnd8')))+var.get('nm27').get(var.get('rnd9')))+var.get('nm28').get(var.get('rnd10'))))
                            PyJs_LONG_0_()
                        else:
                            if (var.get('i')<Js(8.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm34').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm35').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm36').get('length'))))
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm35').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm37').get('length'))))
                                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm38').get('length'))))
                                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm39').get('length'))))
                                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm40').get('length'))))
                                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm39').get('length'))))
                                var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm41').get('length'))))
                                def PyJs_LONG_1_(var=var):
                                    return var.put('names', ((((((((((var.get('nm34').get(var.get('rnd'))+var.get('nm35').get(var.get('rnd2')))+var.get('nm36').get(var.get('rnd3')))+var.get('nm35').get(var.get('rnd4')))+var.get('nm37').get(var.get('rnd5')))+Js(' '))+var.get('nm38').get(var.get('rnd6')))+var.get('nm39').get(var.get('rnd7')))+var.get('nm40').get(var.get('rnd8')))+var.get('nm39').get(var.get('rnd9')))+var.get('nm41').get(var.get('rnd10'))))
                                PyJs_LONG_1_()
                            else:
                                if (var.get('i')<Js(10.0)):
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm46').get('length'))))
                                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm47').get('length'))))
                                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm48').get('length'))))
                                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm47').get('length'))))
                                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm49').get('length'))))
                                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm50').get('length'))))
                                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm51').get('length'))))
                                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm52').get('length'))))
                                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm51').get('length'))))
                                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm53').get('length'))))
                                    def PyJs_LONG_2_(var=var):
                                        return var.put('names', ((((((((((var.get('nm46').get(var.get('rnd'))+var.get('nm47').get(var.get('rnd2')))+var.get('nm48').get(var.get('rnd3')))+var.get('nm47').get(var.get('rnd4')))+var.get('nm49').get(var.get('rnd5')))+Js(' '))+var.get('nm50').get(var.get('rnd6')))+var.get('nm51').get(var.get('rnd7')))+var.get('nm52').get(var.get('rnd8')))+var.get('nm51').get(var.get('rnd9')))+var.get('nm53').get(var.get('rnd10'))))
                                    PyJs_LONG_2_()
                                else:
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm58').get('length'))))
                                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm59').get('length'))))
                                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm60').get('length'))))
                                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm59').get('length'))))
                                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm61').get('length'))))
                                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm62').get('length'))))
                                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm63').get('length'))))
                                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm64').get('length'))))
                                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm63').get('length'))))
                                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm65').get('length'))))
                                    def PyJs_LONG_3_(var=var):
                                        return var.put('names', ((((((((((var.get('nm58').get(var.get('rnd'))+var.get('nm59').get(var.get('rnd2')))+var.get('nm60').get(var.get('rnd3')))+var.get('nm59').get(var.get('rnd4')))+var.get('nm61').get(var.get('rnd5')))+Js(' '))+var.get('nm62').get(var.get('rnd6')))+var.get('nm63').get(var.get('rnd7')))+var.get('nm64').get(var.get('rnd8')))+var.get('nm63').get(var.get('rnd9')))+var.get('nm65').get(var.get('rnd10'))))
                                    PyJs_LONG_3_()
            else:
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                        var.put('names', (((((((var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5')))+Js(' '))+var.get('nm16').get(var.get('rnd6')))+var.get('nm17').get(var.get('rnd7'))))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length'))))
                            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm29').get('length'))))
                            def PyJs_LONG_4_(var=var):
                                return var.put('names', ((((((((((var.get('nm18').get(var.get('rnd'))+var.get('nm19').get(var.get('rnd2')))+var.get('nm20').get(var.get('rnd3')))+var.get('nm19').get(var.get('rnd4')))+var.get('nm21').get(var.get('rnd5')))+Js(' '))+var.get('nm26').get(var.get('rnd6')))+var.get('nm27').get(var.get('rnd7')))+var.get('nm28').get(var.get('rnd8')))+var.get('nm27').get(var.get('rnd9')))+var.get('nm28').get(var.get('rnd10'))))
                            PyJs_LONG_4_()
                        else:
                            if (var.get('i')<Js(8.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm30').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm31').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm32').get('length'))))
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm31').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm33').get('length'))))
                                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm38').get('length'))))
                                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm39').get('length'))))
                                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm40').get('length'))))
                                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm39').get('length'))))
                                var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm41').get('length'))))
                                def PyJs_LONG_5_(var=var):
                                    return var.put('names', ((((((((((var.get('nm30').get(var.get('rnd'))+var.get('nm31').get(var.get('rnd2')))+var.get('nm32').get(var.get('rnd3')))+var.get('nm31').get(var.get('rnd4')))+var.get('nm33').get(var.get('rnd5')))+Js(' '))+var.get('nm38').get(var.get('rnd6')))+var.get('nm39').get(var.get('rnd7')))+var.get('nm40').get(var.get('rnd8')))+var.get('nm39').get(var.get('rnd9')))+var.get('nm41').get(var.get('rnd10'))))
                                PyJs_LONG_5_()
                            else:
                                if (var.get('i')<Js(10.0)):
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm42').get('length'))))
                                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm43').get('length'))))
                                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm44').get('length'))))
                                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm43').get('length'))))
                                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm45').get('length'))))
                                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm50').get('length'))))
                                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm51').get('length'))))
                                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm52').get('length'))))
                                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm51').get('length'))))
                                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm53').get('length'))))
                                    def PyJs_LONG_6_(var=var):
                                        return var.put('names', ((((((((((var.get('nm42').get(var.get('rnd'))+var.get('nm43').get(var.get('rnd2')))+var.get('nm44').get(var.get('rnd3')))+var.get('nm43').get(var.get('rnd4')))+var.get('nm45').get(var.get('rnd5')))+Js(' '))+var.get('nm50').get(var.get('rnd6')))+var.get('nm51').get(var.get('rnd7')))+var.get('nm52').get(var.get('rnd8')))+var.get('nm51').get(var.get('rnd9')))+var.get('nm53').get(var.get('rnd10'))))
                                    PyJs_LONG_6_()
                                else:
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm54').get('length'))))
                                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm55').get('length'))))
                                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm56').get('length'))))
                                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm55').get('length'))))
                                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm57').get('length'))))
                                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm62').get('length'))))
                                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm63').get('length'))))
                                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm64').get('length'))))
                                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm63').get('length'))))
                                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm65').get('length'))))
                                    def PyJs_LONG_7_(var=var):
                                        return var.put('names', ((((((((((var.get('nm54').get(var.get('rnd'))+var.get('nm55').get(var.get('rnd2')))+var.get('nm56').get(var.get('rnd3')))+var.get('nm55').get(var.get('rnd4')))+var.get('nm57').get(var.get('rnd5')))+Js(' '))+var.get('nm62').get(var.get('rnd6')))+var.get('nm63').get(var.get('rnd7')))+var.get('nm64').get(var.get('rnd8')))+var.get('nm63').get(var.get('rnd9')))+var.get('nm65').get(var.get('rnd10'))))
                                    PyJs_LONG_7_()
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('g'), Js('k'), Js('kr'), Js('p'), Js('pr'), Js('q'), Js('r'), Js('str'), Js('t'), Js('tr'), Js('v')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('l'), Js('ld'), Js('lb'), Js('lk'), Js('lr'), Js('m'), Js('ml'), Js('n'), Js('nd'), Js('nk'), Js('r'), Js('rk'), Js('rc'), Js('rd'), Js('rl')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('n'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js('b'), Js('bh'), Js('d'), Js('dh'), Js('h'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('th'), Js('v'), Js('y')]))
var.put('nm6', Js([Js('d'), Js('ll'), Js('lb'), Js('ld'), Js('lr'), Js('l'), Js('lk'), Js('m'), Js('n'), Js('nn'), Js('nr'), Js('nd'), Js('nk'), Js('r'), Js('rr'), Js('rl'), Js('rn'), Js('rm'), Js('rd')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js('h'), Js('n'), Js('s'), Js('t')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bj'), Js('br'), Js('f'), Js('fr'), Js('g'), Js('gr'), Js('h'), Js('hr'), Js('hj'), Js('j'), Js('k'), Js('kr'), Js('m'), Js('r'), Js('s'), Js('st'), Js('sv'), Js('sk'), Js('t'), Js('th'), Js('v'), Js('y')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ei'), Js('uu'), Js('ae')]))
var.put('nm10', Js([Js('bj'), Js('d'), Js('ddv'), Js('dg'), Js('dm'), Js('dv'), Js('g'), Js('gb'), Js('gbj'), Js('gf'), Js('gg'), Js('gn'), Js('gnv'), Js('k'), Js('ks'), Js('lb'), Js('lbj'), Js('ld'), Js('ldm'), Js('lk'), Js('ll'), Js('lld'), Js('m'), Js('n'), Js('nd'), Js('ng'), Js('ngv'), Js('nk'), Js('nn'), Js('nv'), Js('p'), Js('r'), Js('rg'), Js('rl'), Js('rn'), Js('rnl'), Js('rr'), Js('rs'), Js('rt'), Js('rv'), Js('sg'), Js('sk'), Js('st'), Js('th'), Js('tv'), Js('v'), Js('w'), Js('x'), Js('z')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('g'), Js('gg'), Js('gr'), Js('k'), Js('ld'), Js('lf'), Js('lfr'), Js('ll'), Js('m'), Js('n'), Js('nd'), Js('ndr'), Js('nn'), Js('r'), Js('rk'), Js('rl'), Js('rn'), Js('rr'), Js('rth'), Js('st'), Js('t')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('l'), Js('lj'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sv'), Js('th'), Js('t'), Js('v')]))
var.put('nm13', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('y'), Js('au'), Js('ie'), Js('ae')]))
var.put('nm14', Js([Js('bj'), Js('d'), Js('df'), Js('dg'), Js('dh'), Js('dl'), Js('dn'), Js('dr'), Js('fl'), Js('g'), Js('gd'), Js('gn'), Js('gv'), Js('ld'), Js('lk'), Js('ll'), Js('llg'), Js('lv'), Js('m'), Js('n'), Js('nd'), Js('nfr'), Js('ng'), Js('nj'), Js('nng'), Js('nnv'), Js('r'), Js('rd'), Js('rf'), Js('rg'), Js('rgr'), Js('rl'), Js('rn'), Js('sfr'), Js('sg'), Js('sl'), Js('str'), Js('th'), Js('thr')]))
var.put('nm15', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('f'), Js('g'), Js('ld'), Js('lf'), Js('n'), Js('nn'), Js('rd'), Js('rg'), Js('s'), Js('th')]))
var.put('nm16', Js([Js('Amber'), Js('Arm'), Js('Ash'), Js('Autumn'), Js('Battle'), Js('Bear'), Js('Black'), Js('Blaze'), Js('Blood'), Js('Boar'), Js('Boulder'), Js('Brawl'), Js('Bright'), Js('Bronze'), Js('Bull'), Js('Cinder'), Js('Cloud'), Js('Cold'), Js('Common'), Js('Dark'), Js('Dawn'), Js('Dead'), Js('Doom'), Js('Dream'), Js('Dusk'), Js('Dust'), Js('Ember'), Js('Even'), Js('Fine'), Js('Forest'), Js('Free'), Js('Frost'), Js('Frozen'), Js('Gloom'), Js('Gold'), Js('Grand'), Js('Great'), Js('Grim'), Js('Grizzly'), Js('Hallow'), Js('Hell'), Js('High'), Js('Honey'), Js('Horn'), Js('Ice'), Js('Iron'), Js('Keen'), Js('Light'), Js('Lone'), Js('Long'), Js('Mighty'), Js('Mist'), Js('Moss'), Js('Mountain'), Js('Night'), Js('Noble'), Js('Pale'), Js('Plain'), Js('Pride'), Js('Proud'), Js('Quick'), Js('Rage'), Js('Rapid'), Js('Raven'), Js('River'), Js('Rock'), Js('Rune'), Js('Shadow'), Js('Sharp'), Js('Silent'), Js('Silver'), Js('Smoke'), Js('Snow'), Js('Soft'), Js('Spirit'), Js('Star'), Js('Steel'), Js('Stone'), Js('Storm'), Js('Strong'), Js('Summer'), Js('Swift'), Js('Thunder'), Js('Troll'), Js('True'), Js('War'), Js('Wild'), Js('Wind'), Js('Winter'), Js('Wolf')]))
var.put('nm17', Js([Js('arm'), Js('arrow'), Js('bane'), Js('bash'), Js('bear'), Js('blade'), Js('brace'), Js('brand'), Js('breaker'), Js('breath'), Js('brew'), Js('caller'), Js('cleaver'), Js('crest'), Js('crusher'), Js('cut'), Js('cutter'), Js('dream'), Js('eye'), Js('eyes'), Js('fall'), Js('fire'), Js('fist'), Js('flame'), Js('force'), Js('forge'), Js('fury'), Js('gaze'), Js('gleam'), Js('grip'), Js('guard'), Js('hair'), Js('hall'), Js('hammer'), Js('hand'), Js('heart'), Js('hunter'), Js('killer'), Js('lash'), Js('mane'), Js('mantle'), Js('mark'), Js('maul'), Js('rage'), Js('reaper'), Js('reaver'), Js('rider'), Js('ripper'), Js('roar'), Js('rock'), Js('root'), Js('scar'), Js('scream'), Js('shield'), Js('shout'), Js('slayer'), Js('snarl'), Js('song'), Js('spirit'), Js('splitter'), Js('star'), Js('stride'), Js('sun'), Js('sword'), Js('thorn'), Js('tongue'), Js('walker'), Js('ward'), Js('watcher'), Js('wind'), Js('wine'), Js('wolf')]))
var.put('nm18', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('r'), Js('s'), Js('tr'), Js('v'), Js('y')]))
var.put('nm19', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ua'), Js('eo'), Js('oi'), Js('ia')]))
var.put('nm20', Js([Js('b'), Js('br'), Js('bg'), Js('c'), Js('d'), Js('dg'), Js('dr'), Js('ds'), Js('k'), Js('l'), Js('ld'), Js('lp'), Js('m'), Js('n'), Js('nd'), Js('ndr'), Js('nn'), Js('r'), Js('rdr'), Js('rg'), Js('rn'), Js('rr'), Js('sm'), Js('sn'), Js('ss'), Js('st'), Js('v'), Js('vr'), Js('vg'), Js('vd')]))
var.put('nm21', Js([Js(''), Js(''), Js(''), Js('c'), Js('k'), Js('l'), Js('ll'), Js('n'), Js('r'), Js('rd'), Js('rt'), Js('s'), Js('sk'), Js('v')]))
var.put('nm22', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('v'), Js('z')]))
var.put('nm23', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('ya'), Js('uu'), Js('ie'), Js('ei'), Js('ia'), Js('eo'), Js('ae')]))
var.put('nm24', Js([Js('d'), Js('ff'), Js('f'), Js('fr'), Js('fl'), Js('j'), Js('l'), Js('ld'), Js('ll'), Js('lm'), Js('lr'), Js('ls'), Js('lt'), Js('m'), Js('mm'), Js('ms'), Js('mr'), Js('ns'), Js('nr'), Js('n'), Js('nd'), Js('nn'), Js('ph'), Js('r'), Js('rl'), Js('rh'), Js('rm'), Js('rn'), Js('s'), Js('sh'), Js('sk'), Js('sr'), Js('ss'), Js('sl'), Js('th'), Js('tl'), Js('v'), Js('x')]))
var.put('nm25', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('k'), Js('n'), Js('r'), Js('s')]))
var.put('nm26', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('cz'), Js('d'), Js('f'), Js('fr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kl'), Js('m'), Js('mv'), Js('p'), Js('r'), Js('s'), Js('ts'), Js('v'), Js('vh'), Js('w'), Js('z')]))
var.put('nm27', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ai'), Js('io'), Js('ae'), Js('aa'), Js('oo')]))
var.put('nm28', Js([Js('cc'), Js('d'), Js('ddr'), Js('dm'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('l'), Js('ld'), Js('ll'), Js('m'), Js('ml'), Js('n'), Js('nd'), Js('ndl'), Js('ng'), Js('nj'), Js('nn'), Js('nt'), Js('r'), Js('rdr'), Js('rk'), Js('rr'), Js('rs'), Js('shk'), Js('sht'), Js('sk'), Js('st'), Js('t'), Js('th'), Js('ttl'), Js('v'), Js('zm'), Js('zn'), Js('zz')]))
var.put('nm29', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('kz'), Js('kcz'), Js('l'), Js('lf'), Js('n'), Js('r'), Js('rc'), Js('rd'), Js('rk'), Js('s'), Js('t'), Js('v')]))
var.put('nm30', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('cr'), Js('c'), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('m'), Js('n'), Js('nh'), Js('r'), Js('x'), Js('z'), Js('zr')]))
var.put('nm31', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ou')]))
var.put('nm32', Js([Js('b'), Js('br'), Js('bz'), Js('c'), Js('cr'), Js('d'), Js('dr'), Js('dl'), Js('gh'), Js('gg'), Js('gr'), Js('gn'), Js('gm'), Js('k'), Js('kk'), Js('kn'), Js('km'), Js('kr'), Js('lr'), Js('lm'), Js('ln'), Js('lb'), Js('lg'), Js('ld'), Js('m'), Js('md'), Js('mz'), Js('mr'), Js('mg'), Js('n'), Js('nd'), Js('ng'), Js('nd'), Js('nr'), Js('r'), Js('rg'), Js('rgh'), Js('rp'), Js('rr'), Js('rz'), Js('th')]))
var.put('nm33', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('g'), Js('l'), Js('n'), Js('r'), Js('s'), Js('sh')]))
var.put('nm34', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('ch'), Js('d'), Js('dh'), Js('g'), Js('h'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('nh'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v')]))
var.put('nm35', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('ea')]))
var.put('nm36', Js([Js('d'), Js('dr'), Js('dh'), Js('f'), Js('ff'), Js('g'), Js('gg'), Js('gn'), Js('gm'), Js('gh'), Js('gl'), Js('h'), Js('hh'), Js('l'), Js('ll'), Js('llm'), Js('ls'), Js('lz'), Js('lm'), Js('ln'), Js('lg'), Js('ld'), Js('m'), Js('mm'), Js('mn'), Js('ms'), Js('mz'), Js('ml'), Js('n'), Js('nn'), Js('nl'), Js('ns'), Js('nr'), Js('r'), Js('rs'), Js('rr'), Js('rl'), Js('rsh'), Js('s'), Js('ss'), Js('sh'), Js('sr'), Js('t'), Js('v'), Js('zn')]))
var.put('nm37', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('st'), Js('th')]))
var.put('nm38', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('st'), Js('t'), Js('th'), Js('v'), Js('x'), Js('z')]))
var.put('nm39', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm40', Js([Js('d'), Js('dr'), Js('f'), Js('g'), Js('gg'), Js('gr'), Js('gh'), Js('gm'), Js('j'), Js('k'), Js('kk'), Js('kr'), Js('kn'), Js('kl'), Js('l'), Js('ll'), Js('ld'), Js('lg'), Js('lb'), Js('lm'), Js('ln'), Js('m'), Js('mm'), Js('md'), Js('mb'), Js('mr'), Js('ml'), Js('n'), Js('nn'), Js('nb'), Js('nl'), Js('ng'), Js('ngr'), Js('nr'), Js('r'), Js('rs'), Js('rr'), Js('rb'), Js('rg'), Js('rl'), Js('ss'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm41', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('g'), Js('ll'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('st'), Js('th')]))
var.put('nm42', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('dh'), Js('f'), Js('gh'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('x'), Js('w'), Js('z')]))
var.put('nm43', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('i'), Js('i'), Js('u'), Js('aa'), Js('ya'), Js('eo'), Js('ee'), Js('oo'), Js('ai')]))
var.put('nm44', Js([Js('b'), Js('d'), Js('dd'), Js('dh'), Js('dr'), Js('dw'), Js('f'), Js('g'), Js('h'), Js('hr'), Js('hs'), Js('j'), Js('k'), Js('km'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('n'), Js('ns'), Js('q'), Js('qd'), Js('qm'), Js('r'), Js('rb'), Js('rf'), Js('rg'), Js('rh'), Js('rr'), Js('rw'), Js('s'), Js('sf'), Js('sh'), Js('sm'), Js('ss'), Js('st'), Js('z')]))
var.put('nm45', Js([Js(''), Js(''), Js('b'), Js('d'), Js('dh'), Js('f'), Js('j'), Js('jh'), Js('k'), Js('l'), Js('lf'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('th'), Js('wz'), Js('z')]))
var.put('nm46', Js([Js(''), Js(''), Js(''), Js('f'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('w'), Js('z')]))
var.put('nm47', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('u'), Js('i'), Js('y'), Js('ya'), Js('aa'), Js('ai'), Js('iya'), Js('ee')]))
var.put('nm48', Js([Js('b'), Js('br'), Js('d'), Js('dh'), Js('f'), Js('fl'), Js('fn'), Js('h'), Js('hd'), Js('hj'), Js('hm'), Js('j'), Js('km'), Js('l'), Js('lm'), Js('m'), Js('mt'), Js('n'), Js('nt'), Js('ph'), Js('q'), Js('r'), Js('rh'), Js('s'), Js('sf'), Js('sh'), Js('shm'), Js('sm'), Js('t'), Js('th'), Js('z')]))
var.put('nm49', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('l'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm50', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('d'), Js('f'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('m'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('vr'), Js('y'), Js('z')]))
var.put('nm51', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('i'), Js('i'), Js('ee'), Js('aa'), Js('ou'), Js('ei')]))
var.put('nm52', Js([Js('b'), Js('bb'), Js('d'), Js('dd'), Js('dr'), Js('f'), Js('h'), Js('hr'), Js('j'), Js('k'), Js('l'), Js('lk'), Js('ll'), Js('lm'), Js('m'), Js('n'), Js('nb'), Js('nl'), Js('ns'), Js('r'), Js('rw'), Js('s'), Js('sh'), Js('sm'), Js('sp'), Js('sr'), Js('ss'), Js('st'), Js('th'), Js('tt'), Js('v'), Js('w'), Js('z')]))
var.put('nm53', Js([Js(''), Js(''), Js(''), Js('d'), Js('h'), Js('j'), Js('kh'), Js('l'), Js('lm'), Js('m'), Js('n'), Js('r'), Js('s')]))
var.put('nm54', Js([Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm55', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ae'), Js('eu'), Js('aa'), Js('ui')]))
var.put('nm56', Js([Js('b'), Js('ch'), Js('dr'), Js('f'), Js('fm'), Js('g'), Js('h'), Js('hbr'), Js('hm'), Js('k'), Js('kh'), Js('kht'), Js('l'), Js('m'), Js('mm'), Js('ms'), Js('n'), Js('nh'), Js('nk'), Js('nkh'), Js('nm'), Js('nn'), Js('nr'), Js('ns'), Js('nt'), Js('p'), Js('ph'), Js('ps'), Js('pt'), Js('r'), Js('rg'), Js('rk'), Js('rm'), Js('rp'), Js('rph'), Js('rr'), Js('rs'), Js('rt'), Js('s'), Js('sk'), Js('skh'), Js('ss'), Js('st'), Js('t'), Js('thr'), Js('zgh')]))
var.put('nm57', Js([Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('f'), Js('ff'), Js('h'), Js('ln'), Js('nn'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('x')]))
var.put('nm58', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('cl'), Js('h'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('z')]))
var.put('nm59', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('ia'), Js('au'), Js('eo'), Js('ei')]))
var.put('nm60', Js([Js('b'), Js('c'), Js('fs'), Js('h'), Js('hm'), Js('k'), Js('kh'), Js('kr'), Js('kt'), Js('l'), Js('m'), Js('mm'), Js('n'), Js('nk'), Js('nkh'), Js('nn'), Js('ns'), Js('nt'), Js('p'), Js('pp'), Js('q'), Js('r'), Js('rm'), Js('rs'), Js('s'), Js('sh'), Js('st'), Js('t'), Js('th'), Js('tm'), Js('tr'), Js('z')]))
var.put('nm61', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm62', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('cl'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm63', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ae'), Js('eu'), Js('aa'), Js('ui'), Js('ee'), Js('ia'), Js('au'), Js('eo'), Js('ei')]))
var.put('nm64', Js([Js('b'), Js('c'), Js('ch'), Js('dr'), Js('f'), Js('fm'), Js('fs'), Js('g'), Js('h'), Js('hbr'), Js('hm'), Js('k'), Js('kh'), Js('kht'), Js('kr'), Js('kt'), Js('l'), Js('m'), Js('mm'), Js('ms'), Js('n'), Js('nh'), Js('nk'), Js('nkh'), Js('nm'), Js('nn'), Js('nr'), Js('ns'), Js('nt'), Js('p'), Js('ph'), Js('pp'), Js('ps'), Js('pt'), Js('q'), Js('r'), Js('rg'), Js('rk'), Js('rm'), Js('rp'), Js('rph'), Js('rr'), Js('rs'), Js('rt'), Js('s'), Js('sh'), Js('sk'), Js('skh'), Js('ss'), Js('st'), Js('t'), Js('th'), Js('thr'), Js('tm'), Js('tr'), Js('z'), Js('zgh')]))
var.put('nm65', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('f'), Js('ff'), Js('h'), Js('l'), Js('ln'), Js('m'), Js('n'), Js('nn'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('x')]))
pass
pass


# Add lib to the module scope
pathfinderHuman = var.to_python()