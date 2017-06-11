__all__ = ['cowNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Apple'), Js('Athene'), Js('Bambam'), Js('Barrage'), Js('Barry'), Js('Beefcake'), Js('Berry'), Js('Big B'), Js('Bigfoot'), Js('Biggy'), Js('Biscuit'), Js('Blitz'), Js('Bluster'), Js('Bolt'), Js('Bones'), Js('Boomboom'), Js('Boomer'), Js('Boot'), Js('Booth'), Js('Bosco'), Js('Boulder'), Js('Brownie'), Js('Brucie'), Js('Bud'), Js('Bubba'), Js('Buddy'), Js('Buffo'), Js('Bullet'), Js('Bullseye'), Js('Bullwinkle'), Js('Bumble'), Js('Buster'), Js('Butters'), Js('Button'), Js('Calvin'), Js('Chip'), Js('Chuck'), Js('Coal'), Js('Coloss'), Js('Comet'), Js('Conan'), Js('Cookie'), Js('Crazy'), Js('Cream'), Js('Dozer'), Js('Duke'), Js('Echo'), Js('Elmo'), Js('Ernie'), Js('Froghurt'), Js('Fury'), Js('Gale'), Js('George'), Js('Grand'), Js('Gus'), Js('Hank'), Js('Harry'), Js('Jackson'), Js('Jet'), Js('Kargo'), Js('Maddock'), Js('Madeye'), Js('Mambo'), Js('Mammoth'), Js('Maverick'), Js('Max'), Js('Midnight'), Js('Moe'), Js('Momoo'), Js('Moofasa'), Js('Mooffin'), Js('Moomoo'), Js('Moostache'), Js('Mustache'), Js('Nemoo'), Js('Onyx'), Js('Oreo'), Js('Otis'), Js('Paladin'), Js('Patch'), Js('Pepper'), Js('Pierce'), Js('Pounder'), Js('Rage'), Js('Rambo'), Js('Rant'), Js('Rock'), Js('Rocky'), Js('Rufus'), Js('Rumble'), Js('Sable'), Js('Shadow'), Js('Sir Loin'), Js('Slate'), Js('Smash'), Js('Sparky'), Js('Spartacus'), Js('Spice'), Js('Spot'), Js('Stomper'), Js('Storm'), Js('Sunny'), Js('Tank'), Js('Taurus'), Js('Thor'), Js('Thunder'), Js('Tiny'), Js('Toro'), Js('Ug'), Js('Vegas'), Js('Warpath'), Js('Wasabi'), Js('Wonder'), Js('Yoghi'), Js('Yoghurt'), Js('Zipper'), Js('Zug')]))
var.put('nm2', Js([Js('Abby'), Js('Amazone'), Js('Amber'), Js('Annabelle'), Js('Apple'), Js('April'), Js('Arizone'), Js('Autumn'), Js('Babette'), Js('Babs'), Js('Baby'), Js('Barbara'), Js('Bella'), Js('Belle'), Js('Bernice'), Js('Bertha'), Js('Bess'), Js('Bessy'), Js('Beth'), Js('Betsy'), Js('Booboo'), Js('Brooke'), Js('Brownie'), Js('Bubble'), Js('Bubbles'), Js('Bumble'), Js('Bumbles'), Js('Butter'), Js('Buttercup'), Js('Button'), Js('Buttons'), Js('Caramel'), Js('Caramelle'), Js('Chancey'), Js('Charme'), Js('Chloe'), Js('Cinnamon'), Js('Clarabell'), Js('Clover'), Js('Coco'), Js('Cookie'), Js('Corona'), Js('Creame'), Js('Creme'), Js('Cutie'), Js('Daffodil'), Js('Daisy'), Js('Dala'), Js('Darcy'), Js('Darla'), Js('Dear'), Js('Dew'), Js('Dolly'), Js('Dora'), Js('Doris'), Js('Dot'), Js('Dottie'), Js('Dream'), Js('Dutchess'), Js('Eleanor'), Js('Fancy'), Js('Flower'), Js('Fortuna'), Js('Fortune'), Js('Freckles'), Js('Gambles'), Js('Ginger'), Js('Grace'), Js('Gracie'), Js('Gwen'), Js('Hazel'), Js('Honey'), Js('Isabella'), Js('Jade'), Js('Jane'), Js('Jess'), Js('July'), Js('June'), Js('Lavender'), Js('Lilly'), Js('Lily'), Js('Lilypad'), Js('Lola'), Js('Lulu'), Js('Magnolia'), Js('Maple'), Js('Marge'), Js('Marigold'), Js('Martha'), Js('Maude'), Js('May'), Js('Midnight'), Js('Moode'), Js('Mooffin'), Js('Moogy'), Js('Moolissa'), Js('Moolly'), Js('Mooly'), Js('Moomee'), Js('Moomoo'), Js('Moomy'), Js('Moona'), Js('Moonbeam'), Js('Moonica'), Js('Muffin'), Js('Nemoo'), Js('Nighte'), Js('Nora'), Js('Olive'), Js('Oreo'), Js('Patches'), Js('Patience'), Js('Pearl'), Js('Penny'), Js('Pepper'), Js('Petunia'), Js('Pickle'), Js('Pickles'), Js('Precious'), Js('Princess'), Js('Prudence'), Js('Pumpkin'), Js('Queen'), Js('Queenie'), Js('Queste'), Js('Rose'), Js('Rosie'), Js('Ruby'), Js('Satin'), Js('Savanah'), Js('Shade'), Js('Shadow'), Js('Snow'), Js('Snowdrop'), Js('Snowflake'), Js('Sparkle'), Js('Spot'), Js('Spring'), Js('Sprinkles'), Js('Sugar'), Js('Summer'), Js('Sunbeam'), Js('Sweetie'), Js('Valentine'), Js('Viola'), Js('Violet'), Js('Wendy'), Js('Willow'), Js('Winter')]))
pass
pass


# Add lib to the module scope
cowNames = var.to_python()