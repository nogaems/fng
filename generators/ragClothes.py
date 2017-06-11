__all__ = ['ragClothes']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'nm11', 'rnd15', 'rnd11', 'nm16', 'rnd8', 'name', 'nm3', 'rnd14', 'name3', 'rnd17', 'name6', 'nm2', 'rnd2', 'w', 'br', 'type', 'z', 'nm14', 'tp', 'nm7', 'nm10', 'name4', 'v', 'nm15', 'rnd5', 'nm12', 'nm5', 'rnd4', 'rnd7', 'result', 'nm6', 'rnd6', 'rnd13', 'nm4', 'rnd3', 'name5', 'y', 'nm17', 'nm13', 'nm9', 'rnd10', 'rnd16', 'rnd9', 'rnd12', 'rnd1', 'x'])
    var.put('tp', var.get('type'))
    var.put('nm1', Js([Js('Her'), Js('She'), Js('her'), Js('she'), Js('her'), Js('His'), Js('He'), Js('his'), Js('he'), Js('him')]))
    var.put('nm2', Js([Js('shirt'), Js('t-shirt')]))
    var.put('nm3', Js([Js('merely a dirt stained piece of fabric, hanging from one of'), Js('barely a piece of clothing at all, the dirt stained fabric hangs onto'), Js('nothing more than pieces of fabric held barely together, it hangs from'), Js('a torn, dirt stained shadow of its former self, only barely able to hang from'), Js('a gross, tattered home to lice and dirt, hanging from one of'), Js('a dirty, flimsy piece of fabric, held together by a handful of fibers hanging from'), Js('a dirty, tattered mess of fibers and fabric, only barely able to hang from'), Js('a ruffled mess of loose fibers, dirt stains and holes, it barely manages to hang from'), Js('a collection of dirt, lice and who knows what else, it barely manages to hang from'), Js('nothing more than a collection of dirt, loose pieces of fabric and holes, only barely able to hang from'), Js('a vile collection of pieces of dirty fabric, grime and muck, it barely manages to hang from'), Js('nothing more than a crummy old piece of fabric full of holes and stained with dirt, it barely manages to hang from'), Js('a nasty mess of holes, muck and dirty stains, hanging from one of'), Js('a foul collection of raggedy pieces of fabric, dirt and holes, barely able to hang from'), Js('nothing more than dirty pieces of fabric barely held together, hanging from')]))
    var.put('nm4', Js([Js("There's a massive tear on the right side, which leaves much of"), Js('There are holes all over it. Big, small and anything in between, leaving much of'), Js("There's a huge tear on the left side, which leaves much of"), Js("The bottom's worn and tattered and there's a huge hole in the front, leaving much of"), Js('There are more holes than fabric at this point, leaving much of'), Js("It's filled with holes which have grown over time, leaving much of"), Js('Part of the bottom has been torns of and the sleeves are worn away, leaving much of'), Js("There's a huge hole in one of the shoulders which reaches almost all the way down, leaving much of"), Js('Insects or rodents have chewed hundreds of small holes in it, leaving much of'), Js('Holes and tears are scattered all over and leave much of'), Js("There's a big tear across the backside and holes all over the front, leaving much of"), Js('Both of the sides are torn and worn out, leaving much of'), Js('A big piece has been ripped from the right side and there are holes all over, leaving much of'), Js('A big chunk of fabric has been torn from the left side and there are holes and tears all over, leaving much of'), Js('The neck has been torn on one side and there are dozens of holes, leaving much of')]))
    var.put('nm5', Js([Js('a tattered'), Js('a ripped'), Js('a worn out'), Js('an old'), Js('a scraggy'), Js('a rugged')]))
    var.put('nm6', Js([Js('vest'), Js('poncho'), Js('hoody'), Js('jacket'), Js('fleece'), Js('coat')]))
    var.put('nm7', Js([Js("It's far too big and stained with who knows what"), Js("It's too big, torn and very dirty"), Js("It's dirty, it's torn and it's worn out"), Js("It's a size too small, stained and dirty"), Js("It's too small, dirty and it smells"), Js("It smells, it's dirty and full of stains"), Js("It's in relative good condition apart from the holes"), Js("It's in a fairly good condition, apart from the tears and stains"), Js("It's a size too large, it's dirty and it's torn"), Js("It's worn out, dirty and stained with grime"), Js("It's almost the right size, but dirty, smelly and torn"), Js("It's a torn, dirty, stinking mess"), Js("It's filthy, flimsy and worn out"), Js("It's greasy, full of stains and torn"), Js("It's a nasty mess of stains and dirt")]))
    var.put('nm9', Js([Js("aren't in great shape either"), Js("aren't much better either"), Js('are in terrible shape as well'), Js("aren't what they used to be either"), Js('are a mess as well'), Js('are just as bad'), Js("aren't looking great either"), Js('have seen better times as well')]))
    var.put('nm10', Js([Js('Holes everywhere and the legs have been shortened by wear and tear'), Js('The right side is nothing more than a bunch of shreds'), Js('The left side is torn up and nothing more than a bunch shreds'), Js("There are holes all over the bottom part and there's a big tear on the right side"), Js('Dirt stains, holes and tears are scattered all over'), Js("There are holes all over the right side and what's left is covered in stains"), Js('Rips and tears have turned these pants into a dirt stained mess of shreds'), Js("There's a big tear at the backside and holes all across the sides"), Js('A big tear has split the left leg in two and the right leg is full of smaller tears as well'), Js('The pants are covered in small tears and covered in unknown stains'), Js('Wear and tear has turned what were once small tears into big gaping holes'), Js("There's a big tear on the left side which runs from the top to almost the bottom"), Js('Dirt and other substances have stained these pants and gave them a new color'), Js('The right leg has been torn at the knee and the left leg is full of holes'), Js('The knees are torn and there are plenty of other small tears all over')]))
    var.put('nm11', Js([Js('old'), Js('dirty'), Js('worn out'), Js('broken'), Js('missing laces'), Js('tattered'), Js('ragged'), Js('grimy'), Js('stained'), Js('murky')]))
    var.put('nm12', Js([Js('a size too small'), Js('a size too big'), Js('way too big'), Js('a little too small'), Js('barely the right size'), Js('only just the right size'), Js('a little too big')]))
    var.put('nm13', Js([Js('a hole in the sole of the right shoe lets in water and dirt'), Js('a hole in the sole of the left shoe lets in water and dirt'), Js('the heel of the left shoe is worn far more than the right'), Js('the outer fabric is tattered, worn and missing in some places'), Js('the outer sole of the left shoe has long been lost'), Js('the outer sole of the right shoe has long been lost'), Js('the right toebox has come loose from the sole'), Js('the left toebox has come loose from the sole'), Js('the sole of the right shoe has come loose at the heel'), Js('the sole of the left shoe has come loose at the heel'), Js('the soles are worn to barely a sliver of what they were'), Js('there are holes in the right side of the left shoe'), Js('there are holes in the right side of the right shoe'), Js("there's a hole in the left heel which lets in water and dirt"), Js("there's a hole in the left toebox which lets in water and dirt"), Js("there's a hole in the right heel which lets in water and dirt"), Js("there's a hole in the right toebox which lets in water and dirt")]))
    var.put('nm14', Js([Js('large scarf'), Js('small scarf'), Js('scarf'), Js('bandana')]))
    var.put('nm15', Js([Js('face to just below the nose'), Js('face to just below the eyes'), Js('face in a way that covers the chin')]))
    var.put('nm16', Js([Js("dirty and shoddy, but at least it doesn't smell"), Js('old and ragged, but relatively clean'), Js('torn and worn, but otherwise in a decent shape'), Js("ragged and stained, but at least it's not smelly"), Js('full of holes, but still holding together'), Js('old and worn, but otherwise in a good condition'), Js('torn and slightly stained, but otherwise in a decent shape'), Js('worn out, but still holding together')]))
    var.put('nm17', Js([Js("beanie, there was once a small pom pom on the top, but all that's left now is a small piece of yarn"), Js("beanie, there's a hole in the top, but that's pretty much its only flaw"), Js("beanie, it's in suprisingly good condition. It's old, but there are no holes or stains"), Js("beanie, which may be old and worn out, but it's still in a relatively good and clean condition"), Js("beanie, there's a small dirt stain on one of the sides, but that's its only real flaw"), Js("bandana, there's a hole at the front, but other than that it's in pretty good shape"), Js("bandana, it's old and ragged, but otherwise in a good and relatively clean condition"), Js("bandana, there are a few small stains here and there, but it's otherwise in a relatively great condition"), Js("bandana, there's a couple of small holes here and there, but it's relatively clean and in a decent condition"), Js('bandana, surprisingly there are no holes or stains or any other major flaws besides its age')]))
    var.put('v', Js(5.0))
    var.put('w', Js(6.0))
    var.put('x', Js(7.0))
    var.put('y', Js(8.0))
    var.put('z', Js(9.0))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('v', Js(0.0))
        var.put('w', Js(1.0))
        var.put('x', Js(2.0))
        var.put('y', Js(3.0))
        var.put('z', Js(4.0))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    if (var.get('rnd1')<Js(5.0)):
        var.put('nm2', Js([Js('shirt'), Js('t-shirt'), Js('dress')]))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length')))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
    var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    var.put('rnd13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length')))))
    var.put('rnd16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    var.put('rnd17', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('name', ((((((Js('What was once a ')+var.get('nm2').get(var.get('rnd2')))+Js(' is now '))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm1').get(var.get('x')))+Js(' shoulders like a discarded old towel.')))
    def PyJs_LONG_0_(var=var):
        return ((((((((((((((var.get('nm1').get(var.get('w'))+Js("'s wearing "))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm6').get(var.get('rnd6')))+Js(' over '))+var.get('nm1').get(var.get('x')))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js('. '))+var.get('nm7').get(var.get('rnd7')))+Js(', but at least it helps '))+var.get('nm1').get(var.get('z')))+Js(' '))+var.get('nm8').get(var.get('rnd8')))
    var.put('name3', (PyJs_LONG_0_()+Js(', even if only for a little.')))
    def PyJs_LONG_1_(var=var):
        return ((((((((((((((var.get('nm1').get(var.get('v'))+Js(' pants '))+var.get('nm9').get(var.get('rnd9')))+Js('. '))+var.get('nm10').get(var.get('rnd10')))+Js('. But at least '))+var.get('nm1').get(var.get('y')))+Js(' has shoes to protect '))+var.get('nm1').get(var.get('x')))+Js(" feet. Although they're "))+var.get('nm11').get(var.get('rnd11')))+Js(', '))+var.get('nm12').get(var.get('rnd12')))+Js(' and '))+var.get('nm13').get(var.get('rnd13')))
    var.put('name4', (PyJs_LONG_1_()+Js('.')))
    var.put('name5', (((((((((((var.get('nm1').get(var.get('w'))+Js(' wears a  '))+var.get('nm14').get(var.get('rnd14')))+Js(' around '))+var.get('nm1').get(var.get('x')))+Js(' neck and has it wrapped around '))+var.get('nm1').get(var.get('x')))+Js(' '))+var.get('nm15').get(var.get('rnd15')))+Js(". It's "))+var.get('nm16').get(var.get('rnd16')))+Js('.')))
    var.put('name6', (((var.get('nm1').get(var.get('v'))+Js(' head is covered by a '))+var.get('nm17').get(var.get('rnd17')))+Js('.')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(8.0)):
        try:
            pass
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
ragClothes = var.to_python()