__all__ = ['spiritNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7'])
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
            if (var.get('i')<Js(5.0)):
                if PyJsStrictEq(var.get('tp'),Js(1.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('names', var.get('names2').get(var.get('rnd')))
                else:
                    if PyJsStrictEq(var.get('tp'),Js(2.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                        var.put('names', var.get('names3').get(var.get('rnd')))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                        var.put('names', var.get('names1').get(var.get('rnd')))
            else:
                if PyJsStrictEq(var.get('tp'),Js(1.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('names', (((Js('The ')+var.get('names4').get(var.get('rnd')))+Js(' '))+var.get('names6').get(var.get('rnd2'))))
                else:
                    if PyJsStrictEq(var.get('tp'),Js(2.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                        var.put('names', (((Js('The ')+var.get('names4').get(var.get('rnd')))+Js(' '))+var.get('names7').get(var.get('rnd2'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                        var.put('names', (((Js('The ')+var.get('names4').get(var.get('rnd')))+Js(' '))+var.get('names5').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Aberran'), Js('Aeran'), Js('Aiden'), Js('Airian'), Js('Airon'), Js('Alaife'), Js('Alastor'), Js('Cloud'), Js('Malone'), Js('Alife'), Js('Angelo'), Js('Anim'), Js('Auran'), Js('Aurath'), Js('Aurin'), Js('Azur'), Js('Bane'), Js('Benedict'), Js('Blase'), Js('Brand'), Js('Brath'), Js('Cense'), Js('Chase'), Js('Curce'), Js('Daemn'), Js('Daimon'), Js('Damian'), Js('Damon'), Js('Delic'), Js('Desir'), Js('Dwell'), Js('Dyno'), Js('Eaden'), Js('Empyr'), Js('Ether'), Js('Ethern'), Js('Flaym'), Js('Ghose'), Js('Guarian'), Js('Guyde'), Js('Hall'), Js('Hallo'), Js('Harro'), Js('Haunn'), Js('Hawnt'), Js('Hyde'), Js('Illus'), Js('Immor'), Js('Karm'), Js('Kurse'), Js('Lloyl'), Js('Menos'), Js('Mort'), Js('Nate'), Js('Paradai'), Js('Pawer'), Js('Perm'), Js('Perry'), Js('Phanto'), Js('Phyntom'), Js('Rath'), Js('Rayth'), Js('Remane'), Js('Saul'), Js('Sentine'), Js('Shephard'), Js('Spiro'), Js('Torme'), Js('Torne'), Js('Vitali'), Js('Ward'), Js('Warde'), Js('Wayke'), Js('Wayte'), Js('Waythe'), Js('Will')]))
var.put('names2', Js([Js('Abby'), Js('Aeriel'), Js('Airiel'), Js('Airielle'), Js('Angelica'), Js('Angy'), Js('Anima'), Js('Anshee'), Js('Lucy'), Js('Apaera'), Js('Appara'), Js('Arriel'), Js('Aura'), Js('Aurabelle'), Js('Auralee'), Js('Aure'), Js('Auriana'), Js('Auriel'), Js('Aurora'), Js('Azure'), Js('Mallory'), Js('Evilyn'), Js('Belesse'), Js('Blesse'), Js('Branda'), Js('Breeth'), Js('Carisma'), Js('Celeste'), Js('Chasey'), Js('Chasity'), Js('Daeva'), Js('Damia'), Js('Damya'), Js('Delica'), Js('Delice'), Js('Desira'), Js('Dove'), Js('Dwelle'), Js('Ela'), Js('Elega'), Js('Elisum'), Js('Elle'), Js('Ellis'), Js('Elvira'), Js('Elvire'), Js('Elyse'), Js('Enya'), Js('Erie'), Js('Essence'), Js('Essy'), Js('Eterna'), Js('Exme'), Js('Fade'), Js('Faith'), Js('Fantasia'), Js('Fayde'), Js('Faythe'), Js('Felicity'), Js('Gloria'), Js('Guardia'), Js('Guida'), Js('Haeven'), Js('Illuse'), Js('Infi'), Js('Karisma'), Js('Karma'), Js('Karmay'), Js('Kendel'), Js('Loya'), Js('Mindy'), Js('Mira'), Js('Misrey'), Js('Missy'), Js('Misty'), Js('Mortia'), Js('Mortitia'), Js('Mystique'), Js('Natura'), Js('Ondine'), Js('Ora'), Js('Perma'), Js('Queste'), Js('Sentina'), Js('Shay'), Js('Spiri'), Js('Sprit'), Js('Temperance'), Js('Temperence'), Js('Temprence'), Js('Topia'), Js('Umber'), Js('Umbra'), Js('Vex'), Js('Vexa'), Js('Via'), Js('Vissi'), Js('Zoe')]))
var.put('names3', Js([Js('Aberra'), Js('Aener'), Js('Aerel'), Js('Aeren'), Js('Aerin'), Js('Angis'), Js('Kindel'), Js('Aethe'), Js('Aerie'), Js('Aide'), Js('Aidel'), Js('Aidis'), Js('Airin'), Js('Angel'), Js('Apara'), Js('Arie'), Js('Aurel'), Js('Auris'), Js('Blaise'), Js('Blisse'), Js('Blythe'), Js('Bone'), Js('Bones'), Js('Bowne'), Js('Celes'), Js('Charis'), Js('Daevi'), Js('Defi'), Js('Desi'), Js('Deth'), Js('Devi'), Js('Devo'), Js('Duff'), Js('Eaven'), Js('Ener'), Js('Ethae'), Js('Ethe'), Js('Fidel'), Js('Flo'), Js('Flowe'), Js('Folo'), Js('Fyre'), Js('Gallo'), Js('Gose'), Js('Guardi'), Js('Guya'), Js('Harth'), Js('Ligh'), Js('Lite'), Js('Lloial'), Js('Lyte'), Js('Mewse'), Js('Muse'), Js('Myst'), Js('Perris'), Js('Phan'), Js('Psyche'), Js('Remane'), Js('Shado'), Js('Shayde'), Js('Shaydo'), Js('Shayepe'), Js('Sparkle'), Js('Spec'), Js('Spooks'), Js('Spryte'), Js('Spryth'), Js('Stray'), Js('Strey'), Js('Tormey'), Js('Undine'), Js('Undy'), Js('Vysio'), Js('Yuto'), Js('Zion')]))
var.put('names4', Js([Js('Abandoned'), Js('Accepted'), Js('Amusing'), Js('Angry'), Js('Beach'), Js('Bitter'), Js('Black'), Js('Blind'), Js('Bloodied'), Js('Bloody'), Js('Blue'), Js('Brown'), Js('Burning'), Js('Cheerful'), Js('Cherished'), Js('Crying'), Js('Crypt'), Js('Dark'), Js('Defending'), Js('Drifting'), Js('Escaped'), Js('Fat'), Js('Fiery'), Js('Following'), Js('Forest'), Js('Friendly'), Js('Full Moon'), Js('Garden'), Js('Graveyard'), Js('Gray'), Js('Grim'), Js('Headless'), Js('Helpful'), Js('Hostile'), Js('Howling'), Js('Ignored'), Js('Invited'), Js('Ivory'), Js('Jolly'), Js('Killer'), Js('Laughing'), Js('Light'), Js('Lost'), Js('Malevolent'), Js('Mansion'), Js('Marching'), Js('Midnight'), Js('Mocking'), Js('Mourning'), Js('Mute'), Js('Noisy'), Js('Oblivious'), Js('Playful'), Js('Pleasant'), Js('Praying'), Js('Preaching'), Js('Protecting'), Js('Raging'), Js('Reading'), Js('Red'), Js('Roaming'), Js('Running'), Js('Sad'), Js('Saluting'), Js('Screaming'), Js('Searching'), Js('Seeking'), Js('Shrieking'), Js('Shy'), Js('Silent'), Js('Silver'), Js('Sinister'), Js('Sitting'), Js('Sleeping'), Js('Slender'), Js('Snoring'), Js('Sobbing'), Js('Spying'), Js('Stalking'), Js('Standing'), Js('Staring'), Js('Sweet'), Js('Talking'), Js('Thin'), Js('Tombstone'), Js('Twin'), Js('Unaware'), Js('Unwanted'), Js('Vengeful'), Js('Vicious'), Js('Violent'), Js('Wandering'), Js('Watching'), Js('Waving'), Js('Weeping'), Js('Welcome'), Js('Whispering'), Js('White'), Js('Wicked'), Js('Wild')]))
var.put('names5', Js([Js('Baron'), Js('Boy'), Js('Father'), Js('Gentleman'), Js('Grandfather'), Js('Groom'), Js('Groomsman'), Js('Incubus'), Js('Mailman'), Js('Man'), Js('Angel'), Js('Apparition'), Js('Appearance'), Js('Artist'), Js('Barber'), Js('Barkeeper'), Js('Blacksmith'), Js('Butcher'), Js('Camper'), Js('Child'), Js('Cleaner'), Js('Clown'), Js('Cook'), Js('Curator'), Js('Dancer'), Js('Defender'), Js('Demon'), Js('Devil'), Js('Doctor'), Js('Eyes'), Js('Force'), Js('Gatekeeper'), Js('Ghost'), Js('Guard'), Js('Guardian'), Js('Guest'), Js('Hunter'), Js('Jester'), Js('Judge'), Js('Keeper'), Js('Kid'), Js('Knight'), Js('Lover'), Js('Maniac'), Js('Mime'), Js('Monk'), Js('Musician'), Js('Necromancer'), Js('Nightmare'), Js('Nightwatch'), Js('Nurse'), Js('Orphan'), Js('Patrol'), Js('Phantom'), Js('Prisoner'), Js('Protector'), Js('Reaper'), Js('Revenant'), Js('Rider'), Js('Screamer'), Js('Sentinel'), Js('Sentry'), Js('Servant'), Js('Shade'), Js('Shadow'), Js('Shepherd'), Js('Shopkeeper'), Js('Soldier'), Js('Soul'), Js('Specter'), Js('Squire'), Js('Stalker'), Js('Student'), Js('Teacher'), Js('Teenager'), Js('Templar'), Js('Toddler'), Js('Torturer'), Js('Vision'), Js('Visitor'), Js('Warden'), Js('Widow'), Js('Wizard'), Js('Woman'), Js('Wraith'), Js('Writer')]))
var.put('names6', Js([Js('Banshee'), Js('Baroness'), Js('Bride'), Js('Bridesmaid'), Js('Girl'), Js('Grandmother'), Js('Lady'), Js('Maiden'), Js('Mother'), Js('Succubus'), Js('Temptress'), Js('Trickster'), Js('Witch'), Js('Angel'), Js('Apparition'), Js('Appearance'), Js('Artist'), Js('Barber'), Js('Barkeeper'), Js('Blacksmith'), Js('Butcher'), Js('Camper'), Js('Child'), Js('Cleaner'), Js('Clown'), Js('Cook'), Js('Curator'), Js('Dancer'), Js('Defender'), Js('Demon'), Js('Devil'), Js('Doctor'), Js('Eyes'), Js('Force'), Js('Gatekeeper'), Js('Ghost'), Js('Guard'), Js('Guardian'), Js('Guest'), Js('Hunter'), Js('Jester'), Js('Judge'), Js('Keeper'), Js('Kid'), Js('Knight'), Js('Lover'), Js('Maniac'), Js('Mime'), Js('Monk'), Js('Musician'), Js('Necromancer'), Js('Nightmare'), Js('Nightwatch'), Js('Nurse'), Js('Orphan'), Js('Patrol'), Js('Phantom'), Js('Prisoner'), Js('Protector'), Js('Reaper'), Js('Revenant'), Js('Rider'), Js('Screamer'), Js('Sentinel'), Js('Sentry'), Js('Servant'), Js('Shade'), Js('Shadow'), Js('Shepherd'), Js('Shopkeeper'), Js('Soldier'), Js('Soul'), Js('Specter'), Js('Squire'), Js('Stalker'), Js('Student'), Js('Teacher'), Js('Teenager'), Js('Templar'), Js('Toddler'), Js('Torturer'), Js('Vision'), Js('Visitor'), Js('Warden'), Js('Widow'), Js('Wizard'), Js('Woman'), Js('Wraith'), Js('Writer')]))
var.put('names7', Js([Js('Angel'), Js('Apparition'), Js('Appearance'), Js('Artist'), Js('Barber'), Js('Barkeeper'), Js('Blacksmith'), Js('Butcher'), Js('Camper'), Js('Child'), Js('Cleaner'), Js('Clown'), Js('Cook'), Js('Curator'), Js('Dancer'), Js('Defender'), Js('Demon'), Js('Devil'), Js('Doctor'), Js('Eyes'), Js('Force'), Js('Gatekeeper'), Js('Ghost'), Js('Guard'), Js('Guardian'), Js('Guest'), Js('Hunter'), Js('Jester'), Js('Judge'), Js('Keeper'), Js('Kid'), Js('Knight'), Js('Lover'), Js('Maniac'), Js('Mime'), Js('Monk'), Js('Musician'), Js('Necromancer'), Js('Nightmare'), Js('Nightwatch'), Js('Nurse'), Js('Orphan'), Js('Patrol'), Js('Phantom'), Js('Prisoner'), Js('Protector'), Js('Reaper'), Js('Revenant'), Js('Rider'), Js('Screamer'), Js('Sentinel'), Js('Sentry'), Js('Servant'), Js('Shade'), Js('Shadow'), Js('Shepherd'), Js('Shopkeeper'), Js('Soldier'), Js('Soul'), Js('Specter'), Js('Squire'), Js('Stalker'), Js('Student'), Js('Teacher'), Js('Teenager'), Js('Templar'), Js('Toddler'), Js('Torturer'), Js('Vision'), Js('Visitor'), Js('Warden'), Js('Widow'), Js('Wizard'), Js('Woman'), Js('Wraith'), Js('Writer')]))
pass
pass


# Add lib to the module scope
spiritNames = var.to_python()