__all__ = ['werePacks']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd3')))+Js(' Pack')))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', (((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd3')))+Js(' Pack')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm5').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ambersky'), Js('Arctic'), Js('Ash'), Js('Bane'), Js('Barbaric'), Js('Black'), Js('Bloodlust'), Js('Bloodrose'), Js('Bloodvenom'), Js('Blue'), Js('Broken'), Js('Brown'), Js('Brutal'), Js('Calm'), Js('Crescent'), Js('Crimson'), Js('Cruel'), Js('Dark'), Js('Dawn'), Js('Dawnfall'), Js('Dawnguard'), Js('Dessert'), Js('Dusk'), Js('Duskfall'), Js('Evening'), Js('Feral'), Js('Ferocious'), Js('Fierce'), Js('Golden'), Js('Grey'), Js('Hollow'), Js('Imperial'), Js('Kind'), Js('Lichen'), Js('Lightning'), Js('Lost'), Js('Lunar'), Js('Lupine'), Js('Lycan'), Js('Midnight'), Js('Morning'), Js('Mountain'), Js('Mystic'), Js('Native'), Js('Night'), Js('Nightfall'), Js('Nightshade'), Js('Nightstar'), Js('Primal'), Js('Prime'), Js('Raging'), Js('Red'), Js('Sanguis'), Js('Savage'), Js('Scarlet'), Js('Scarred'), Js('Sentinel'), Js('Shadowed'), Js('Silent'), Js('Silver'), Js('Silverback'), Js('Solar'), Js('Spirit'), Js('Starry'), Js('Sundown'), Js('Sunset'), Js('Thunder'), Js('Tranquil'), Js('Vanished'), Js('Vengeful'), Js('Vicious'), Js('Whisper'), Js('White'), Js('Wild'), Js('Moonlit'), Js('Darkmoon'), Js('Blue Moon'), Js('Moonstone'), Js('Bloodmoon'), Js('Crescent Moon'), Js('Moonvalley'), Js('Full Moon'), Js('Moon')]))
var.put('nm2', Js([Js('Ambersky'), Js('Arctic'), Js('Ash'), Js('Bane'), Js('Barbaric'), Js('Black'), Js('Bloodlust'), Js('Bloodrose'), Js('Bloodvenom'), Js('Blue'), Js('Broken'), Js('Brown'), Js('Brutal'), Js('Calm'), Js('Crescent'), Js('Crimson'), Js('Cruel'), Js('Dark'), Js('Dawn'), Js('Dawnfall'), Js('Dawnguard'), Js('Dessert'), Js('Dusk'), Js('Duskfall'), Js('Evening'), Js('Feral'), Js('Ferocious'), Js('Fierce'), Js('Golden'), Js('Grey'), Js('Hollow'), Js('Imperial'), Js('Kind'), Js('Lichen'), Js('Lightning'), Js('Lost'), Js('Lunar'), Js('Lupine'), Js('Lycan'), Js('Midnight'), Js('Morning'), Js('Mountain'), Js('Mystic'), Js('Native'), Js('Night'), Js('Nightfall'), Js('Nightshade'), Js('Nightstar'), Js('Primal'), Js('Prime'), Js('Raging'), Js('Red'), Js('Sanguis'), Js('Savage'), Js('Scarlet'), Js('Scarred'), Js('Sentinel'), Js('Shadowed'), Js('Silent'), Js('Silver'), Js('Silverback'), Js('Solar'), Js('Spirit'), Js('Starry'), Js('Sundown'), Js('Sunset'), Js('Thunder'), Js('Tranquil'), Js('Vanished'), Js('Vengeful'), Js('Vicious'), Js('Whisper'), Js('White'), Js('Wild')]))
var.put('nm3', Js([Js('Alpha'), Js('Angel'), Js('Ash'), Js('Beta'), Js('Blood'), Js('Burst'), Js('Canine'), Js('Canis'), Js('Cave'), Js('Creek'), Js('Crows'), Js('Darkness'), Js('Delta'), Js('Depths'), Js('Dream'), Js('Eclipse'), Js('Edge'), Js('Eye'), Js('Eyed'), Js('Eyes'), Js('Feather'), Js('Fire'), Js('Forest'), Js('Gloom'), Js('Grin'), Js('Heart'), Js('Hill'), Js('Ice'), Js('Lake'), Js('Light'), Js('Lupis'), Js('Oak'), Js('Oasis'), Js('Omega'), Js('Peak'), Js('Pride'), Js('Raven'), Js('River'), Js('Rock'), Js('Rufus'), Js('Shadow'), Js('Silence'), Js('Sky'), Js('Snow'), Js('Star'), Js('Stars'), Js('Stealth'), Js('Summit'), Js('Tail'), Js('Thunder'), Js('Timber'), Js('Tooth'), Js('Valley'), Js('Venture'), Js('Water'), Js('Woodland')]))
var.put('nm4', Js([Js('Alpha'), Js('Angel'), Js('Ash'), Js('Beta'), Js('Blood'), Js('Burst'), Js('Canine'), Js('Canis'), Js('Cave'), Js('Creek'), Js('Crows'), Js('Darkness'), Js('Delta'), Js('Depths'), Js('Dream'), Js('Eclipse'), Js('Edge'), Js('Eye'), Js('Eyed'), Js('Eyes'), Js('Feather'), Js('Fire'), Js('Forest'), Js('Gloom'), Js('Grin'), Js('Heart'), Js('Hill'), Js('Ice'), Js('Lake'), Js('Light'), Js('Lupis'), Js('Moon'), Js('Oak'), Js('Oasis'), Js('Omega'), Js('Peak'), Js('Pride'), Js('Raven'), Js('River'), Js('Rock'), Js('Rufus'), Js('Shadow'), Js('Silence'), Js('Sky'), Js('Snow'), Js('Star'), Js('Stars'), Js('Stealth'), Js('Summit'), Js('Tail'), Js('Thunder'), Js('Timber'), Js('Tooth'), Js('Valley'), Js('Venture'), Js('Water'), Js('Woodland')]))
var.put('nm5', Js([Js('Banes'), Js('Canines'), Js('Claws'), Js('Furs'), Js('Growlers'), Js('Guardians'), Js('Hounds'), Js('Howlers'), Js('Hunters'), Js('Keepers'), Js('Manes'), Js('Nightstalkers'), Js('Nightwalkers'), Js('Prowlers'), Js('Shadows'), Js('Stalkers'), Js('Walkers'), Js('Warriors')]))
pass
pass


# Add lib to the module scope
werePacks = var.to_python()