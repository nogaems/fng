__all__ = ['knightOrderNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm2', 'nm3', 'result', 'nm4'])
    var.put('nm1', Js([Js('Ash'), Js('Autumn'), Js('Balance'), Js('Battle'), Js('Blood'), Js('Brass'), Js('Carnage'), Js('Chains'), Js('Change'), Js('Courage'), Js('Darkness'), Js('Dawn'), Js('Death'), Js('Defiance'), Js('Desire'), Js('Devotion'), Js('Direction'), Js('Dusk'), Js('Exaltation'), Js('Existence'), Js('Faith'), Js('Fate'), Js('Fear'), Js('Fire'), Js('Fortitude'), Js('Fury'), Js('Gallantry'), Js('Giants'), Js('Glory'), Js('Gold'), Js('Grit'), Js('Guidance'), Js('Harmony'), Js('Heroism'), Js('History'), Js('Honor'), Js('Ice'), Js('Infinity'), Js('Iron'), Js('Judgment'), Js('Justice'), Js('Knowledge'), Js('Leather'), Js('Light'), Js('Limbo'), Js('Nightfall'), Js('Oaths'), Js('Peace'), Js('Pestilence'), Js('Prayer'), Js('Riddles'), Js('Serenity'), Js('Servitude'), Js('Shadows'), Js('Silver'), Js('Smoke and Ash'), Js('Solitude'), Js('Spirit'), Js('Spirits'), Js('Spring'), Js('Summer'), Js('Sunrise'), Js('Tenacity'), Js('Thunder'), Js('Time'), Js('Tranquility'), Js('Valiance'), Js('Valor'), Js('Wealth'), Js('Winter'), Js('Worship')]))
    var.put('nm2', Js([Js('Abyss'), Js('Angel'), Js('Arachnid'), Js('Arch'), Js('Archangel'), Js('Ash'), Js('Banner'), Js('Bat'), Js('Bear'), Js('Beast'), Js('Birth'), Js('Blade'), Js('Blessed'), Js('Book'), Js('Brave'), Js('Bridge'), Js('Broken Sword'), Js('Brother'), Js('Bull'), Js('Carriage'), Js('Chain'), Js('Chalice'), Js('Cherub'), Js('Circle'), Js('Cleansing Flame'), Js('Coast'), Js('Crescent'), Js('Crest'), Js('Crib'), Js('Cross'), Js('Crow'), Js('Crown'), Js('Desire'), Js('Divine'), Js('Divine Hand'), Js('Dragon'), Js('Dust'), Js('Eagle'), Js('Earth'), Js('Edge'), Js('Eye'), Js('Faith'), Js('Falcon'), Js('Fang'), Js('Fate'), Js('Father'), Js('Feather'), Js('Fist'), Js('Flame'), Js('Flower'), Js('Fruit'), Js('Garden'), Js('Gate'), Js('Golden Thread'), Js('Griffin'), Js('Guardian'), Js('Hammer'), Js('Heart'), Js('Hook'), Js('Horn'), Js('Hydra'), Js('Ice'), Js('Isle'), Js('Knot'), Js('Lake'), Js('Land'), Js('Leaf'), Js('Light'), Js('Lion'), Js('Maple'), Js('Mask'), Js('Mire'), Js('Moon'), Js('Mother'), Js('Mountain'), Js('Nest'), Js('Night'), Js('Oak'), Js('Ocean'), Js('Oracle'), Js('Orb'), Js('Owl'), Js('Parchment'), Js('Phoenix'), Js('Prophet'), Js('Pyre'), Js('Quill'), Js('Quiver'), Js('Rain'), Js('Raven'), Js('Rose'), Js('Saint'), Js('Salt'), Js('Sand'), Js('Sanguine'), Js('Scarf'), Js('Scythe'), Js('Seraph'), Js('Seraphim'), Js('Serpent'), Js('Shadow'), Js('Shield'), Js('Silver'), Js('Sister'), Js('Sky'), Js('Snake'), Js('Spirit'), Js('Spur'), Js('Star'), Js('Stars'), Js('Stone'), Js('Sun'), Js('Sword'), Js('Temple'), Js('Truth'), Js('Voyage'), Js('Water'), Js('Wave')]))
    var.put('nm3', Js([Js('Abyss'), Js('Angel'), Js('Ashen'), Js('Autumn'), Js('Banner'), Js('Birth'), Js('Blessed'), Js('Blood'), Js('Brass'), Js('Brave'), Js('Chain'), Js('Chalice'), Js('Cherub'), Js('Circle'), Js('Cleansing'), Js('Crescent'), Js('Crest'), Js('Cross'), Js('Crow'), Js('Crown'), Js('Darkness'), Js('Dawn'), Js('Death'), Js('Divine'), Js('Dragon'), Js('Dusk'), Js('Dust'), Js('Eagle'), Js('Exaltation'), Js('Faith'), Js('Falcon'), Js('Fang'), Js('Fate'), Js('Father'), Js('Fear'), Js('Feather'), Js('Fire'), Js('Flame'), Js('Flower'), Js('Fury'), Js('Garden'), Js('Gate'), Js('Glory'), Js('Golden'), Js('Griffin'), Js('Guardian'), Js('Guiding'), Js('Honor'), Js('Hydra'), Js('Infinity'), Js('Iron'), Js('Judgment'), Js('Justice'), Js('Knowledge'), Js('Lake'), Js('Land'), Js('Leather'), Js('Light'), Js('Limbo'), Js('Lion'), Js('Maple'), Js('Masked'), Js('Mire'), Js('Moon'), Js('Mother'), Js('Mountain'), Js('Nest'), Js('Night'), Js('Nightfall'), Js('Oak'), Js('Ocean'), Js('Oracle'), Js('Owl'), Js('Parchment'), Js('Phoenix'), Js('Prayer'), Js('Prophet'), Js('Pyre'), Js('Raven'), Js('Rose'), Js('Salt'), Js('Sand'), Js('Sanguine'), Js('Scythe'), Js('Seraph'), Js('Seraphim'), Js('Serenity'), Js('Serpent'), Js('Shadow'), Js('Silver'), Js('Sister'), Js('Sky'), Js('Solitude'), Js('Spirit'), Js('Spring'), Js('Star'), Js('Stone'), Js('Summer'), Js('Sun'), Js('Sunrise'), Js('Temple'), Js('Thunder'), Js('Timeless'), Js('Tranquil'), Js('Valiant'), Js('Valor'), Js('Voyage'), Js('Water'), Js('Winter'), Js('Worship')]))
    var.put('nm4', Js([Js('Knights'), Js('Order'), Js('Soldiers'), Js('Squires'), Js('Preservers'), Js('Guardians'), Js('Custodians'), Js('Legion'), Js('League'), Js('Circle'), Js('Lancers'), Js('Shields'), Js('Helmets'), Js('Templars'), Js('Knights'), Js('Order'), Js('Knights'), Js('Order')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm4').get(var.get('rnd2')))+Js(' of the '))+var.get('nm2').get(var.get('rnd'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', (((Js('The ')+var.get('nm3').get(var.get('rnd')))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
                    var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', (((Js('The ')+var.get('nm4').get(var.get('rnd2')))+Js(' of '))+var.get('nm1').get(var.get('rnd'))))
                    var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
knightOrderNames = var.to_python()