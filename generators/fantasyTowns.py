__all__ = ['fantasyTowns']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm2').get(var.get('rnd2'))):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('amber'), Js('angel'), Js('spirit'), Js('basin'), Js('lagoon'), Js('basin'), Js('arrow'), Js('autumn'), Js('bare'), Js('bay'), Js('beach'), Js('bear'), Js('bell'), Js('black'), Js('bleak'), Js('blind'), Js('bone'), Js('boulder'), Js('bridge'), Js('brine'), Js('brittle'), Js('bronze'), Js('castle'), Js('cave'), Js('chill'), Js('clay'), Js('clear'), Js('cliff'), Js('cloud'), Js('cold'), Js('crag'), Js('crow'), Js('crystal'), Js('curse'), Js('dark'), Js('dawn'), Js('dead'), Js('deep'), Js('deer'), Js('demon'), Js('dew'), Js('dim'), Js('dire'), Js('dirt'), Js('dog'), Js('dragon'), Js('dry'), Js('dusk'), Js('dust'), Js('eagle'), Js('earth'), Js('east'), Js('ebon'), Js('edge'), Js('elder'), Js('ember'), Js('ever'), Js('fair'), Js('fall'), Js('false'), Js('far'), Js('fay'), Js('fear'), Js('flame'), Js('flat'), Js('frey'), Js('frost'), Js('ghost'), Js('glimmer'), Js('gloom'), Js('gold'), Js('grass'), Js('gray'), Js('green'), Js('grim'), Js('grime'), Js('hazel'), Js('heart'), Js('high'), Js('hollow'), Js('honey'), Js('hound'), Js('ice'), Js('iron'), Js('kil'), Js('knight'), Js('lake'), Js('last'), Js('light'), Js('lime'), Js('little'), Js('lost'), Js('mad'), Js('mage'), Js('maple'), Js('mid'), Js('might'), Js('mill'), Js('mist'), Js('moon'), Js('moss'), Js('mud'), Js('mute'), Js('myth'), Js('never'), Js('new'), Js('night'), Js('north'), Js('oaken'), Js('ocean'), Js('old'), Js('ox'), Js('pearl'), Js('pine'), Js('pond'), Js('pure'), Js('quick'), Js('rage'), Js('raven'), Js('red'), Js('rime'), Js('river'), Js('rock'), Js('rogue'), Js('rose'), Js('rust'), Js('salt'), Js('sand'), Js('scorch'), Js('shade'), Js('shadow'), Js('shimmer'), Js('shroud'), Js('silent'), Js('silk'), Js('silver'), Js('sleek'), Js('sleet'), Js('sly'), Js('small'), Js('smooth'), Js('snake'), Js('snow'), Js('south'), Js('spring'), Js('stag'), Js('star'), Js('steam'), Js('steel'), Js('steep'), Js('still'), Js('stone'), Js('storm'), Js('summer'), Js('sun'), Js('swamp'), Js('swan'), Js('swift'), Js('thorn'), Js('timber'), Js('trade'), Js('west'), Js('whale'), Js('whit'), Js('white'), Js('wild'), Js('wilde'), Js('wind'), Js('winter'), Js('wolf')]))
var.put('nm2', Js([Js('acre'), Js('band'), Js('barrow'), Js('bay'), Js('bell'), Js('born'), Js('borough'), Js('bourne'), Js('breach'), Js('break'), Js('brook'), Js('burgh'), Js('burn'), Js('bury'), Js('cairn'), Js('call'), Js('chill'), Js('cliff'), Js('coast'), Js('crest'), Js('cross'), Js('dale'), Js('denn'), Js('drift'), Js('fair'), Js('fall'), Js('falls'), Js('fell'), Js('field'), Js('ford'), Js('forest'), Js('fort'), Js('front'), Js('frost'), Js('garde'), Js('gate'), Js('glen'), Js('grasp'), Js('grave'), Js('grove'), Js('guard'), Js('gulch'), Js('gulf'), Js('hall'), Js('hallow'), Js('ham'), Js('hand'), Js('harbor'), Js('haven'), Js('helm'), Js('hill'), Js('hold'), Js('holde'), Js('hollow'), Js('horn'), Js('host'), Js('keep'), Js('land'), Js('light'), Js('maw'), Js('meadow'), Js('mere'), Js('mire'), Js('mond'), Js('moor'), Js('more'), Js('mount'), Js('mouth'), Js('pass'), Js('peak'), Js('point'), Js('pond'), Js('port'), Js('post'), Js('reach'), Js('rest'), Js('rock'), Js('run'), Js('scar'), Js('shade'), Js('shear'), Js('shell'), Js('shield'), Js('shore'), Js('shire'), Js('side'), Js('spell'), Js('spire'), Js('stall'), Js('wich'), Js('minster'), Js('star'), Js('storm'), Js('strand'), Js('summit'), Js('tide'), Js('town'), Js('vale'), Js('valley'), Js('vault'), Js('vein'), Js('view'), Js('ville'), Js('wall'), Js('wallow'), Js('ward'), Js('watch'), Js('water'), Js('well'), Js('wharf'), Js('wick'), Js('wind'), Js('wood'), Js('yard')]))
pass
pass


# Add lib to the module scope
fantasyTowns = var.to_python()