__all__ = ['schoolUniformDescriptions']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm1', 'nm11', 'nm16', 'nm3', 'nm16s', 'nm2', 'nm14', 'nm7', 'nm10', 'nm21', 'nm15', 'nm20', 'nm12', 'nm3s', 'nm5', 'nm8b', 'nm6', 'nm4', 'nameGen', 'nm8', 'nm18', 'nm17', 'nm13', 'nm9'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['rnd19', 'rnd18', 'rnd15', 'rnd11', 'rnd8', 'name', 'rnd14', 'name3', 'rnd17', 'name6', 'rnd8b', 'rnd9b', 'rnd2', 'br', 'name2', 'name4', 'rnd21', 'rnd3s', 'rnd14b', 'rnd5', 'rnd14c', 'rnd4', 'rnd10b', 'rnd7', 'rnd5b', 'result', 'rnd13b', 'rnd6', 'rnd20', 'rnd13', 'rnd16s', 'rnd3', 'rnd12b', 'name5', 'rnd16', 'rnd10', 'rnd9', 'rnd12', 'rnd1'])
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd3s', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3s').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd5b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    var.put('rnd8b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8b').get('length')))))
    var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length')))))
    var.put('rnd9b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length')))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
    var.put('rnd10b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
    var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    var.put('rnd12b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    var.put('rnd13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    var.put('rnd13b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    var.put('rnd14b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    var.put('rnd14c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length')))))
    var.put('rnd16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    var.put('rnd16s', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16s').get('length')))))
    var.put('rnd17', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd18', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    var.put('rnd19', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length')))))
    var.put('rnd20', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length')))))
    var.put('rnd21', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length')))))
    var.put('name', ((((((((((Js('The boys in this school wear ')+var.get('nm1').get(var.get('rnd1')))+Js(', '))+var.get('nm2').get(var.get('rnd2')))+Js(' trousers that reach '))+var.get('nm3').get(var.get('rnd3')))+Js(' their '))+var.get('nm3s').get(var.get('rnd3s')))+Js(', all of which are colored '))+var.get('nm5').get(var.get('rnd5')))+Js('.')))
    var.put('name2', ((((((((Js(" They're paired with ")+var.get('nm6').get(var.get('rnd6')))+Js(', '))+var.get('nm14').get(var.get('rnd14')))+Js(' socks '))+var.get('nm7').get(var.get('rnd7')))+Js('colored '))+var.get('nm5').get(var.get('rnd5b')))+Js('.')))
    def PyJs_LONG_0_(var=var):
        return ((((((((((((var.get('nm8').get(var.get('rnd8'))+Js(' '))+var.get('nm8b').get(var.get('rnd8b')))+Js(' shirt is '))+var.get('nm9').get(var.get('rnd9')))+Js(' their trousers and covered with a '))+var.get('nm10').get(var.get('rnd10')))+Js(' jacket. A '))+var.get('nm11').get(var.get('rnd11')))+Js(' tie '))+var.get('nm12').get(var.get('rnd12')))+Js(' the middle of their '))+var.get('nm13').get(var.get('rnd13')))
    var.put('name3', (((((((PyJs_LONG_0_()+Js(' jacket and is '))+var.get('nm14').get(var.get('rnd14b')))+Js(' in '))+var.get('nm5').get(var.get('rnd5')))+Js(' and '))+var.get('nm5').get(var.get('rnd5b')))+Js('.')))
    def PyJs_LONG_1_(var=var):
        return (((((((((((((Js('The girls wear ')+var.get('nm15').get(var.get('rnd15')))+Js(' skirts in '))+var.get('nm5').get(var.get('rnd5')))+Js(' and they '))+var.get('nm16').get(var.get('rnd16')))+Js(". They're paired with "))+var.get('nm17').get(var.get('rnd17')))+Js(' socks and '))+var.get('nm16s').get(var.get('rnd16s')))+Js(' colored in '))+var.get('nm5').get(var.get('rnd5b')))+Js(' and '))+var.get('nm5').get(var.get('rnd5')))
    var.put('name4', (PyJs_LONG_1_()+Js(' respectively.')))
    def PyJs_LONG_2_(var=var):
        return ((((((((((Js('Like the boys the girls wear ')+var.get('nm8b').get(var.get('rnd8b')))+Js(' shirts, which are usually '))+var.get('nm9').get(var.get('rnd9b')))+Js(' their skirts and are covered with a '))+var.get('nm10').get(var.get('rnd10b')))+Js(' jacket. They too wear a tie that '))+var.get('nm12').get(var.get('rnd12b')))+Js(' the middle of their often '))+var.get('nm13').get(var.get('rnd13b')))+Js(' jackets and is '))
    var.put('name5', ((PyJs_LONG_2_()+var.get('nm14').get(var.get('rnd14c')))+Js(' in the same colors.')))
    var.put('name6', ((((((((Js('All jackets ')+var.get('nm21').get(var.get('rnd21')))+Js(' and, '))+var.get('nm18').get(var.get('rnd18')))+Js(', many students wear '))+var.get('nm19').get(var.get('rnd19')))+Js(' accessoires, '))+var.get('nm20').get(var.get('rnd20')))+Js('.')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(7.0)):
        try:
            pass
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('straight'), Js('striped'), Js('lined'), Js('finely striped'), Js('thickly striped'), Js('plain'), Js('checkered'), Js('loose fitting'), Js('narrow fitting')]))
var.put('nm2', Js([Js('Dacron'), Js('cotton'), Js('nylon'), Js('polycotton'), Js('polyester'), Js('cotton'), Js('nylon')]))
var.put('nm3', Js([Js('down to about their calves and thus reveal'), Js('down to just above'), Js('down to just under their knees, clearly revealing'), Js('down to just above their ankles and reveal'), Js('all the way down and partially cover'), Js('down to well below their knees and clearly reveal')]))
var.put('nm3s', Js([Js('loafers'), Js('single strap shoes'), Js('double strap shoes'), Js('triple strap shoes'), Js('sporty loafers'), Js('lace-up shoes'), Js('slip-in shoes'), Js('Chelsea boots')]))
var.put('nm4', Js([Js('both of which are colored'), Js('each respectively colored')]))
var.put('nm5', Js([Js('almond'), Js('amber'), Js('apricot'), Js('aquamarine'), Js('auburn'), Js('azure'), Js('baby blue'), Js('beige'), Js('black'), Js('bronze'), Js('brown'), Js('burgundy'), Js('cardinal'), Js('cerulean'), Js('cobalt'), Js('crimson'), Js('denim'), Js('forest green'), Js('ginger'), Js('indigo'), Js('jade'), Js('jasmine'), Js('jasper'), Js('khaki'), Js('lavender'), Js('lilac'), Js('mahogany'), Js('maroon'), Js('navy'), Js('ochre'), Js('onyx'), Js('orchid'), Js('peach'), Js('rosewood'), Js('russet'), Js('scarlet'), Js('sepia'), Js('sienna'), Js('sinopia'), Js('tangerine'), Js('tawny'), Js('teal'), Js('vanilla'), Js('vermilion'), Js('viridian'), Js('wheat')]))
var.put('nm6', Js([Js('long'), Js('short'), Js('regular')]))
var.put('nm7', Js([Js('and a simple belt '), Js('and a thick belt '), Js(' and a regular belt '), Js(''), Js('')]))
var.put('nm8', Js([Js('A white'), Js('An almond'), Js('A beige'), Js('A cream'), Js('A floral white'), Js('A ghost white'), Js('An ivory')]))
var.put('nm8b', Js([Js('long sleeved'), Js('short sleeved'), Js('fairly short sleeved'), Js('long sleeved')]))
var.put('nm9', Js([Js('neatly tucked into'), Js('gently tucked into'), Js('almost perfectly tucked into'), Js('barely tucked into'), Js('roughly tucked into'), Js('loosely hanging over'), Js('neatly hanging over'), Js('playfully hanging over'), Js('somewhat messily hanging over'), Js('carelessly hanging over')]))
var.put('nm10', Js([Js('basic'), Js('charming'), Js('classic'), Js('clear-cut'), Js('comfortable'), Js('diligent'), Js('discrete'), Js('fairly long'), Js('fancy'), Js('formal'), Js('graceful'), Js('heavy'), Js('humble'), Js('lavish'), Js('light'), Js('lined'), Js('long'), Js('loose'), Js('luxurious'), Js('moderate'), Js('modest'), Js('mundane'), Js('narrow'), Js('navy'), Js('neat'), Js('plain'), Js('regular'), Js('short'), Js('simple'), Js('slim'), Js('standard'), Js('stylish'), Js('thick'), Js('thin'), Js('tight'), Js('wide')]))
var.put('nm11', Js([Js('long'), Js('short'), Js('thin'), Js('wide'), Js('narrow'), Js('slim'), Js('lean'), Js('light'), Js('fine'), Js('broad')]))
var.put('nm12', Js([Js('splits right down'), Js('hangs gently in'), Js('playfully dangles in'), Js('neatly rests in'), Js('divides'), Js('neatly splits'), Js('drops freely down'), Js('hangs neatly in'), Js('playfully hangs in'), Js('hangs down'), Js('is tucked in'), Js('is neatly tucked behind')]))
var.put('nm13', Js([Js('buttoned up'), Js('half buttoned up'), Js('unbuttoned'), Js('mostly buttoned up'), Js('barely buttoned up'), Js('rarely buttoned up'), Js('often unbottoned'), Js('half unbottoned')]))
var.put('nm14', Js([Js('striped'), Js('dotted'), Js('thinly striped'), Js('broadly striped'), Js('thinly dotted'), Js('diagonally striped'), Js('horizontally striped'), Js('vertically striped'), Js('gingerly dotted'), Js('moderately dotted'), Js('patterned'), Js('checkered'), Js('broadly checkered'), Js('thinly checkered'), Js('crisscrossed'), Js('broadly crisscrossed'), Js('thinly crisscrossed'), Js('plain and undecorated')]))
var.put('nm15', Js([Js('straight'), Js('circle'), Js('accordion'), Js('pleated'), Js('box pleated'), Js('paneled'), Js('wrap'), Js('bubble'), Js('layered'), Js('tiered'), Js('pencil')]))
var.put('nm16', Js([Js('reach down to just above their calves'), Js('dangle down to just below their knees'), Js('reach down to just above their ankles'), Js('dangle all the way down to their feet'), Js('cover the entirety of their legs'), Js('reveal their legs from the knees down'), Js('just reveal their calves'), Js('reach down to well below their knees'), Js('dangle down to about their calves'), Js('reach to just above their ankles'), Js('dangle down to about their ankles')]))
var.put('nm16s', Js([Js('Mary Jane shoes'), Js('toe cap shoes'), Js('brogue shoes'), Js('plimsolls'), Js('pumps'), Js('wedge shoes')]))
var.put('nm17', Js([Js('knee high'), Js('striped'), Js('dotted'), Js('crisscrossed'), Js('regular'), Js('over the calf'), Js('thigh high')]))
var.put('nm18', Js([Js('while not mandatory'), Js('although slightly frowned upon'), Js('although forbidden by regulations'), Js('while not really encouraged'), Js('although discouraged by teachers'), Js("while it's completely up to them"), Js('although completely optional'), Js('while up to their discretion'), Js('although non-compulsory'), Js('although slightly disapproved')]))
var.put('nm19', Js([Js('school-colored'), Js('all sorts of'), Js('varied'), Js('matching'), Js('uniform matching'), Js('various'), Js('distinct'), Js('individual'), Js('separate'), Js('corresponding')]))
var.put('nm20', Js([Js('mostly as a form of self expression'), Js('in some cases purely to be somewhat rebellious'), Js('often as a way to show their school spirit'), Js('often because this is the only part of their clothing they have any say over'), Js('sometimes somewhat as an act of defiance'), Js('in some cases simply to make a statement'), Js('often to create a new style within the standard uniform'), Js('usually to identify themselves as being part of a specific group'), Js('usually to bring some form of their own identity into the standard uniform'), Js("mostly because many think the standard uniform's too dull"), Js('many do it to add a personal touch to the otherwise identical uniform'), Js('some do it simply to avoid being confused for somebody else'), Js("it's an easy way to express themselves at least a little"), Js("for some it's a means to stand out from the crowd"), Js("often it's done through forms of group expression")]))
var.put('nm21', Js([Js('are emblazoned with the school logo'), Js('have a line around all edges in the school color'), Js('have two lines around all edges in the school color'), Js('are adorned with a small school logo'), Js('have buttons with the school symbol on them'), Js('have the school symbol on the breast pockets'), Js('have colored lines around the sleeves'), Js('have been left plain and undecorated'), Js('have a line in the school color at the bottom'), Js('have school colored accents on all edges')]))
pass
pass


# Add lib to the module scope
schoolUniformDescriptions = var.to_python()