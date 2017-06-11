__all__ = ['dndTieflingNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameFem', 'nm4', 'nameGen', 'nm5', 'nm3', 'nameMas', 'nm2'])
@Js
def PyJsHoisted_nameFem_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    if (var.get('i')<Js(7.0)):
        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
        var.put('nMs', (var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2'))))
        var.get('testSwear')(var.get('nMs'))
    else:
        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
        var.put('nMs', var.get('nm3').get(var.get('rnd')))
PyJsHoisted_nameFem_.func_name = 'nameFem'
var.put('nameFem', PyJsHoisted_nameFem_)
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    if (var.get('i')<Js(7.0)):
        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
        var.put('nMs', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
        var.get('testSwear')(var.get('nMs'))
    else:
        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
        var.put('nMs', var.get('nm3').get(var.get('rnd')))
PyJsHoisted_nameMas_.func_name = 'nameMas'
var.put('nameMas', PyJsHoisted_nameMas_)
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
                var.get('nameFem')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameFem')()
            else:
                var.get('nameMas')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameMas')()
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aet'), Js('Ak'), Js('Am'), Js('Aran'), Js('And'), Js('Ar'), Js('Ark'), Js('Bar'), Js('Car'), Js('Cas'), Js('Dam'), Js('Dhar'), Js('Eb'), Js('Ek'), Js('Er'), Js('Gar'), Js('Gu'), Js('Gue'), Js('Hor'), Js('Ia'), Js('Ka'), Js('Kai'), Js('Kar'), Js('Kil'), Js('Kos'), Js('Ky'), Js('Loke'), Js('Mal'), Js('Male'), Js('Mav'), Js('Me'), Js('Mor'), Js('Neph'), Js('Oz'), Js('Ral'), Js('Re'), Js('Rol'), Js('Sal'), Js('Sha'), Js('Sir'), Js('Ska'), Js('The'), Js('Thy'), Js('Thyne'), Js('Ur'), Js('Uri'), Js('Val'), Js('Xar'), Js('Zar'), Js('Zer'), Js('Zher'), Js('Zor')]))
var.put('nm2', Js([Js('adius'), Js('akas'), Js('akos'), Js('char'), Js('cis'), Js('cius'), Js('dos'), Js('emon'), Js('ichar'), Js('il'), Js('ilius'), Js('ira'), Js('lech'), Js('lius'), Js('lyre'), Js('marir'), Js('menos'), Js('meros'), Js('mir'), Js('mong'), Js('mos'), Js('mus'), Js('non'), Js('rai'), Js('rakas'), Js('rakir'), Js('reus'), Js('rias'), Js('ris'), Js('rius'), Js('ron'), Js('ros'), Js('rus'), Js('rut'), Js('shoon'), Js('thor'), Js('thos'), Js('thus'), Js('us'), Js('venom'), Js('vir'), Js('vius'), Js('xes'), Js('xik'), Js('xikas'), Js('xire'), Js('xius'), Js('xus'), Js('zer'), Js('zire')]))
var.put('nm3', Js([Js('Achievement'), Js('Adventure'), Js('Aid'), Js('Anguish'), Js('Art'), Js('Ashes'), Js('Atonement'), Js('Awe'), Js('Bliss'), Js('Bright'), Js('Carrion'), Js('Chant'), Js('Cheer'), Js('Cherish'), Js('Closed'), Js('Comfort'), Js('Compassion'), Js('Confidence'), Js('Content'), Js('Courage'), Js('Cunning'), Js('Darkness'), Js('Deceit'), Js('Delight'), Js('Desire'), Js('Despair'), Js('Devotion'), Js('Dexterity'), Js('Different'), Js('Dread'), Js('Ecstasy'), Js('End'), Js('Enduring'), Js('Essential'), Js('Esteem'), Js('Eternal'), Js('Euphoria'), Js('Exceptional'), Js('Exciting'), Js('Expert'), Js('Expertise'), Js('Expressive'), Js('Extreme'), Js('Faith'), Js('Fear'), Js('Flawed'), Js('Free'), Js('Freedom'), Js('Fresh'), Js('Gentle'), Js('Gladness'), Js('Glee'), Js('Gloom'), Js('Happiness'), Js('Happy'), Js('Harmony'), Js('Hatred'), Js('Hero'), Js('Hope'), Js('Hunt'), Js('Hymn'), Js('Ideal'), Js('Immortal'), Js('Innovation'), Js('Interesting'), Js('Journey'), Js('Joy'), Js('Laughter'), Js('Life'), Js('Light'), Js('Love'), Js('Loyal'), Js('Mantra'), Js('Master'), Js('Mastery'), Js('Misery'), Js('Music'), Js('Normal'), Js('Nowhere'), Js('Odd'), Js('Open'), Js('Optimal'), Js('Panic'), Js('Perfect'), Js('Piety'), Js('Pleasure'), Js('Poetry'), Js('Possession'), Js('Promise'), Js('Psalm'), Js('Pure'), Js('Quest'), Js('Random'), Js('Rare'), Js('Recovery'), Js('Redemption'), Js('Regular'), Js('Relentless'), Js('Respect'), Js('Reverence'), Js('Sadness'), Js('Sanctity'), Js('Silence'), Js('Skilled'), Js('Sly'), Js('Song'), Js('Sorrow'), Js('Suffering'), Js('Terror'), Js('Timeless'), Js('Torment'), Js('Trickery'), Js('Trouble'), Js('Trust'), Js('Truth'), Js('Uncommon'), Js('Unlocked'), Js('Void'), Js('Voyage'), Js('Weary'), Js('Winning'), Js('Woe')]))
var.put('nm4', Js([Js('Af'), Js('Agne'), Js('Ani'), Js('Ara'), Js('Ari'), Js('Aria'), Js('Bel'), Js('Bri'), Js('Cre'), Js('Da'), Js('Di'), Js('Dim'), Js('Dor'), Js('Ea'), Js('Fri'), Js('Gri'), Js('His'), Js('In'), Js('Ini'), Js('Kal'), Js('Le'), Js('Lev'), Js('Lil'), Js('Ma'), Js('Mar'), Js('Mis'), Js('Mith'), Js('Na'), Js('Nat'), Js('Ne'), Js('Neth'), Js('Nith'), Js('Ori'), Js('Pes'), Js('Phe'), Js('Qu'), Js('Ri'), Js('Ro'), Js('Sa'), Js('Sar'), Js('Seiri'), Js('Sha'), Js('Val'), Js('Vel'), Js('Ya'), Js('Yora'), Js('Yu'), Js('Za'), Js('Zai'), Js('Ze')]))
var.put('nm5', Js([Js('bis'), Js('borys'), Js('cria'), Js('cyra'), Js('dani'), Js('doris'), Js('faris'), Js('firith'), Js('goria'), Js('grea'), Js('hala'), Js('hiri'), Js('karia'), Js('ki'), Js('laia'), Js('lia'), Js('lies'), Js('lista'), Js('lith'), Js('loth'), Js('lypsis'), Js('lyvia'), Js('maia'), Js('meia'), Js('mine'), Js('narei'), Js('nirith'), Js('nise'), Js('phi'), Js('pione'), Js('punith'), Js('qine'), Js('rali'), Js('rissa'), Js('seis'), Js('solis'), Js('spira'), Js('tari'), Js('tish'), Js('uphis'), Js('vari'), Js('vine'), Js('wala'), Js('wure'), Js('xibis'), Js('xori'), Js('yis'), Js('yola'), Js('za'), Js('zes')]))
pass
pass
pass
pass


# Add lib to the module scope
dndTieflingNames = var.to_python()