__all__ = ['tribalNames']

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
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Agile one'), Js('Always running'), Js('Animal companion'), Js('Beautiful voice'), Js('Best friend'), Js('Big heart'), Js('Bitter as a berry'), Js('Blazing fire'), Js('Blossoms like a flower'), Js('Born of magic'), Js('Born of rain'), Js('Born of the solstice'), Js('Born of thunder'), Js('Born of violence'), Js('Brave one'), Js('Bright as a full moon'), Js('Bright like fire'), Js('Bright smile'), Js('Brings messages'), Js('Builder of boats'), Js('Builder of homes'), Js('Burning fire'), Js('Catches birds'), Js('Chases bugs'), Js('Climbs trees'), Js('Cooks delicious food'), Js('Crashing waves'), Js('Cries like a wolf'), Js('Curly haired'), Js('Dances like a sprite'), Js('Dancing bear'), Js('Dark as a forest'), Js('Dark as the night'), Js('Deep waters'), Js('Defends us all'), Js('Dressed in furs'), Js('Ears of a fox'), Js('Eternal blossom'), Js('Eternal one'), Js('Eyes big as the moon'), Js('Eyes bright as the sun'), Js('Eyes like the moon'), Js('Eyes of a snake'), Js('Eyes of an eagle'), Js('Falcon that soars in the sky'), Js('Fallen eagle'), Js('Falls a lot'), Js('Fast runner'), Js('Fell from tree'), Js('Field of flowers'), Js('First to dance'), Js('First to walk'), Js('Flies like a bird'), Js('Flower blooming at night'), Js('Flower of pure gold'), Js('Flower of pure snow'), Js('Flower of the river'), Js('Flows like a river'), Js('Friend among foes'), Js('Friend of foe'), Js('Friend of snakes'), Js('Gentle walk'), Js('Gives kisses'), Js('Gliding snowflake'), Js('Glow of rising sun'), Js('Goes to war'), Js('Good one'), Js('Granted wish'), Js('Grazing bull'), Js('Great protector'), Js('Guide of the spirits'), Js('Hair like ash'), Js('Hair like straw'), Js('Hair of feathers'), Js('Hair of the earth'), Js('Hair of the sun'), Js('Handsome one'), Js('Hard as a rock'), Js('Has a pure aura'), Js('Has big feet'), Js('Has good fortune'), Js('Has many secrets'), Js('Healer of pain'), Js('Healer of wounds'), Js('Helps all'), Js('Hidden treasure'), Js('Horned one'), Js('Hot as fire'), Js('Jumps like a frog'), Js('Kind and generous'), Js('Knows medicines'), Js('Laughing child'), Js('Laughs like an owl'), Js('Leaping fish'), Js('Light as a feather'), Js('Like a beast'), Js('Like a bird'), Js('Like a blue sky'), Js('Like a butterfly'), Js('Like a fawn'), Js('Like a mermaid'), Js('Like a mountain'), Js('Like a snake'), Js('Like a spider'), Js('Like a star at night'), Js('Like a vine'), Js('Like an owl'), Js('Like clear water of a lake'), Js('Like rumbling earth'), Js('Like snow'), Js('Like the thunder'), Js('Like the wind'), Js('Liked by all'), Js('Likes to chase'), Js('Likes to speak'), Js('Little bumblebee'), Js('Little companion'), Js('Little flower'), Js('Little fox'), Js('Little leaf in the wind'), Js('Little miracle'), Js('Little one'), Js('Little pebble'), Js('Littlest one'), Js('Lives with a monster'), Js('Lone wolf'), Js('Lost and found again'), Js('Loud voice'), Js('Lover of animals'), Js('Loves little bells'), Js('Loves shiny things'), Js('Loves snow'), Js('Loves storms'), Js('Loves the night'), Js('Loves the rain'), Js('Loves to bathe'), Js('Loves to dance'), Js('Loves war'), Js('Loves water'), Js('Lucky charm'), Js('Makes a lot of noise'), Js('Makes beautiful crafts'), Js('Makes music'), Js('Marked by war'), Js('Marked like a leopard'), Js('Meets the enemy'), Js('Mountain river'), Js('My heart'), Js('Nimble feet'), Js('Oak tree'), Js('Of the earth'), Js('Old leader'), Js('Overflowing spring'), Js('Part monster'), Js('Patient one'), Js('Picks flowers'), Js('Playful like a cub'), Js('Possesses magic'), Js('Precious one'), Js('Pretty flower'), Js('Proud as a lion'), Js('Red as the earth'), Js('Red like blood'), Js('Remembers all'), Js('Returned from death'), Js('Returned from war'), Js('Rippling water'), Js('Roars as a bear'), Js('Runs like the wind'), Js('Runs with horses'), Js('Searched for and found'), Js('Shooting star'), Js('Sigh of the sun in the sky'), Js('Sings like a bird'), Js('Skin as stone'), Js('Skin like ash'), Js('Skin like night sky'), Js('Skin of stars'), Js('Sleeps during the day'), Js('Speaks wisely'), Js('Speaks with dogs'), Js('Special like a white lion'), Js('Spins around'), Js('Spirit among us'), Js('Spirit dancer'), Js('Stalking panther'), Js('Strange one'), Js('Strikes true'), Js('Strong as a bear'), Js('Strong as a boulder'), Js('Strong as an ox'), Js('Strong guardian'), Js('Stronger one'), Js('Sun rising above the horizon'), Js('Sweet as fruit'), Js('Swims like a fish'), Js('Tallest tree'), Js('Teeth like a wolf'), Js('Thunder that rolls over clouds'), Js('Touched by magic'), Js('Travels a lot'), Js('Tree blossom'), Js('Tree swaying in the wind'), Js('Tumbling rock'), Js('Turtle dove'), Js('Turtle laying eggs'), Js('Twinkling star'), Js('Unique being'), Js('Valley of blossoms'), Js('Voice of a bird'), Js('Walks like a fairy'), Js('Walks on four claws'), Js('Warrior spirit'), Js('Waves crashing against rock'), Js('Wild as a river'), Js('Wild horse'), Js('Wild rose'), Js('Willow tree'), Js('Wise leader'), Js('Wise like an elder'), Js('Wise one')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
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
tribalNames = var.to_python()