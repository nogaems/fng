__all__ = ['freecityNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('names', ((((var.get('names3').get(var.get('rnd'))+var.get('names4').get(var.get('rnd2')))+Js(' '))+var.get('names5').get(var.get('rnd3')))+var.get('names6').get(var.get('rnd4'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+Js(' '))+var.get('names5').get(var.get('rnd3')))+var.get('names6').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Adar'), Js('Aer'), Js('Ar'), Js('Ball'), Js('Bel'), Js('Brach'), Js('Daar'), Js('Don'), Js('Draq'), Js('Garr'), Js('Goran'), Js('Gyll'), Js('Har'), Js('Harl'), Js('Hor'), Js('Ill'), Js('Inn'), Js('Irr'), Js('Jaer'), Js('Jaq'), Js('Jor'), Js('Laraz'), Js('Laz'), Js('Lys'), Js('Maerr'), Js('Mal'), Js('Mar'), Js('Nak'), Js('Nor'), Js('Nyess'), Js('Sall'), Js('Stall'), Js('Syr'), Js('Thor'), Js('Treg'), Js('Tych'), Js('Var'), Js('Varg'), Js('Vog'), Js('Vyr')]))
var.put('names2', Js([Js('adhor'), Js('an'), Js('ano'), Js('aphos'), Js('aquo'), Js('ar'), Js('ario'), Js('aro'), Js('apho'), Js('arro'), Js('ello'), Js('elos'), Js('en'), Js('enhor'), Js('enno'), Js('eo'), Js('eqor'), Js('ero'), Js('esso'), Js('icho'), Js('idos'), Js('illos'), Js('io'), Js('iphos'), Js('iros'), Js('o'), Js('odos'), Js('onar'), Js('onno'), Js('onos'), Js('oquo'), Js('or'), Js('orno'), Js('oros'), Js('os'), Js('yllo'), Js('ynno'), Js('yrio'), Js('yros'), Js('ys')]))
var.put('names3', Js([Js('Ahr'), Js('Aren'), Js('Daen'), Js('Dil'), Js('Dor'), Js('Erin'), Js('Erl'), Js('Faey'), Js('Fer'), Js('Firan'), Js('Harr'), Js('Hel'), Js('Hen'), Js('Il'), Js('Iner'), Js('Laen'), Js('Ler'), Js('Less'), Js('Mel'), Js('Mesh'), Js('Min'), Js('Nes'), Js('Nil'), Js('Noar'), Js('Onal'), Js('Or'), Js('Phen'), Js('Phir'), Js('Sael'), Js('Ser'), Js('Sir'), Js('Taen'), Js('Tir'), Js('Triann'), Js('Vaer'), Js('Vell'), Js('Vor'), Js('Waer'), Js('Wen'), Js('Wyn')]))
var.put('names4', Js([Js('a'), Js('aena'), Js('aerah'), Js('ala'), Js('aleah'), Js('anah'), Js('anea'), Js('aria'), Js('asha'), Js('aya'), Js('eah'), Js('ela'), Js('ella'), Js('elna'), Js('era'), Js('erah'), Js('esa'), Js('esha'), Js('eya'), Js('eyana'), Js('ianna'), Js('ila'), Js('ina'), Js('ira'), Js('irah'), Js('issa'), Js('ola'), Js('olana'), Js('olla'), Js('ona'), Js('ora'), Js('oreah'), Js('orlah'), Js('osha'), Js('ylea'), Js('ylla'), Js('yna'), Js('ynea'), Js('ysa'), Js('ysha')]))
var.put('names5', Js([Js('Aen'), Js('Ahr'), Js('Aner'), Js('Baerr'), Js('Bah'), Js('Bren'), Js('Dirr'), Js('Drenn'), Js('Dyn'), Js('Enn'), Js('Eran'), Js('Ess'), Js('Faen'), Js('Flaer'), Js('For'), Js('Fyll'), Js('Hart'), Js('Hest'), Js('Hot'), Js('Iran'), Js('Irn'), Js('Irr'), Js('Maeg'), Js('Mar'), Js('Mop'), Js('Naer'), Js('Nah'), Js('Nest'), Js('Orl'), Js('Orm'), Js('Ost'), Js('Paen'), Js('Pahr'), Js('Phass'), Js('San'), Js('Sorr'), Js('Stass'), Js('Vhass'), Js('Voll'), Js('Vyn')]))
var.put('names6', Js([Js('aan'), Js('aar'), Js('aenor'), Js('ah'), Js('ahran'), Js('anar'), Js('ar'), Js('aris'), Js('assar'), Js('atis'), Js('el'), Js('elar'), Js('elion'), Js('en'), Js('enohr'), Js('erah'), Js('erion'), Js('erris'), Js('in'), Js('inar'), Js('ion'), Js('ios'), Js('irah'), Js('iris'), Js('iros'), Js('ohr'), Js('ohrin'), Js('olis'), Js('onnis'), Js('oran'), Js('oris'), Js('orlan'), Js('os'), Js('oyor'), Js('yl'), Js('ymion'), Js('yr'), Js('yrion'), Js('yris'), Js('ys')]))
pass
pass


# Add lib to the module scope
freecityNames = var.to_python()