__all__ = ['wildWestTowns']

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
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abandon'), Js('Angel'), Js("Angel's "), Js('Anger'), Js('Aurora '), Js('Bad'), Js('Bare'), Js('Barren'), Js('Barren '), Js('Big'), Js('Bitter'), Js('Black'), Js('Blank'), Js('Bleak'), Js('Blind'), Js('Bliss'), Js('Bold'), Js('Bone'), Js('Boulder'), Js('Brave'), Js('Break'), Js('Broken'), Js('Bronze'), Js('Bruise'), Js('Bull'), Js("Bull's "), Js("Buzzard's "), Js('Cattle'), Js('Clear'), Js('Clear '), Js('Coal'), Js('Copper'), Js('Copper '), Js('Court'), Js("Coyote's "), Js('Craze'), Js('Crazy'), Js('Crime'), Js('Crimson'), Js('Cripple '), Js('Crook'), Js('Crooked'), Js("Crow's "), Js('Cruel'), Js('Cruelty '), Js('Dark'), Js('Dead'), Js("Dead Man's "), Js("Death's "), Js('Defiant '), Js('Demon'), Js("Demon's "), Js('Desert'), Js('Desert '), Js('Desolation '), Js('Devil'), Js("Devil's "), Js('Dodge'), Js('Dread'), Js('Dry'), Js('Dry '), Js('Dull'), Js('Dust'), Js('Dusty '), Js('Elder'), Js('Evil '), Js("Evil's "), Js('Fair'), Js('False '), Js('Far'), Js('Farm'), Js('Filth'), Js('Flat'), Js('Forsaken '), Js('Frail'), Js('Free'), Js('Freedom '), Js('Ghost'), Js("Ghost's "), Js("Giant's "), Js('Glum'), Js('Gold'), Js('Golden'), Js('Grand'), Js('Grand '), Js('Grave'), Js('Grave '), Js('Gray'), Js('Greed'), Js('Grim'), Js('Grime'), Js('Grind'), Js('Grub'), Js('Gun'), Js('Harmony '), Js('High'), Js('Hell'), Js("Hope's "), Js('Idle'), Js('Imp'), Js('Infernal '), Js('Iron'), Js('Jagged'), Js('Last '), Js('Lawless '), Js('Lead'), Js('Light'), Js('Limbo '), Js('Limp'), Js('Little'), Js('Little '), Js('Living'), Js('Lone '), Js('Lonely '), Js('Long'), Js('Lords'), Js('Lost'), Js('Lost '), Js("Lost Hope's "), Js('Low'), Js('Marrow'), Js('Meek'), Js('Mellow '), Js('Mud'), Js('Narrow '), Js('New '), Js('Numb'), Js('Oat'), Js('Obsidian '), Js('Old '), Js('Onyx'), Js('Over'), Js('Ox'), Js('Pale'), Js('Phantom'), Js('Pistol'), Js('Plain'), Js('Plain '), Js('Pride '), Js('Prospector '), Js("Prospector's "), Js('Proud'), Js('Pure'), Js('Purgatory '), Js('Purity '), Js('Quick'), Js('Rag'), Js('Ragged'), Js('Ragged '), Js('Rapid'), Js('Rattle'), Js('Red'), Js('Rich'), Js('Rich '), Js('Rot'), Js('Ruby '), Js('Rust'), Js('Rusty '), Js('Sand'), Js('Sandy '), Js('Scorn'), Js('Scorpion'), Js("Scorpion's "), Js('Serenity '), Js('Serpent'), Js("Serpent's "), Js('Shade '), Js('Shadow'), Js('Shady '), Js('Shallow '), Js('Short'), Js('Silent '), Js('Silver'), Js('Sin'), Js('Skeleton '), Js('Skinny '), Js('Skull'), Js('Slim'), Js('Slow'), Js('Smooth '), Js('Snake'), Js('Sneak'), Js('Soft'), Js('Sore'), Js('Sour'), Js('Stag'), Js('Stale'), Js('Stark'), Js('Stark '), Js('Steel'), Js('Steep'), Js('Stiff'), Js("Stiff's "), Js('Storm'), Js('Strong'), Js('Sunny'), Js('Swift'), Js('Swift '), Js('Talon'), Js("Talon's "), Js('Tame'), Js('Tan'), Js('Thin'), Js('Thorn'), Js('Thunder'), Js('Tight'), Js('Tomb'), Js('Torn'), Js('Tucker'), Js('Twin '), Js('Vain'), Js('Vapid'), Js('Vast'), Js('Venom'), Js('Vicious '), Js('Violence '), Js('Violent '), Js('Warm'), Js('Warp'), Js('Whisper'), Js('White'), Js('Wide'), Js('Wild'), Js('Wild '), Js('Willow'), Js('Windy '), Js('Wolf'), Js("Wolf's "), Js('Wrath'), Js('Wrath '), Js('Wry'), Js('Yellow')]))
var.put('nm2', Js([Js('alley'), Js('bank'), Js('banks'), Js('bend'), Js('brook'), Js('burg'), Js('butte'), Js('canyon'), Js('chapel'), Js('city'), Js('creak'), Js('creek'), Js('cross'), Js('edge'), Js('field'), Js('flats'), Js('ford'), Js('fort'), Js('gate'), Js('gulch'), Js('hallow'), Js('hill'), Js('hollow'), Js('lake'), Js('landing'), Js('mesa'), Js('mountain'), Js('pass'), Js('peak'), Js('stream'), Js('branch'), Js('ridge'), Js('bluff'), Js('dune'), Js('downs'), Js('range'), Js('summit'), Js('rise'), Js('cliff'), Js('crag'), Js('scar'), Js('stand'), Js('gorge'), Js('vale'), Js('gorge'), Js('glen'), Js('dale'), Js('snag'), Js('tusk'), Js('howl'), Js('bellow'), Js('peaks'), Js('plains'), Js('point'), Js('port'), Js('post'), Js('reach'), Js('ridge'), Js('river'), Js('rock'), Js('roost'), Js('run'), Js('spring'), Js('springs'), Js('stead'), Js('stone'), Js('tooth'), Js('town'), Js('trail'), Js('trails'), Js('ville'), Js('water'), Js('wood'), Js('worth')]))
pass
pass


# Add lib to the module scope
wildWestTowns = var.to_python()