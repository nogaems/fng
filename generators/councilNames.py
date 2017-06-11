__all__ = ['councilNames']

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
    var.registers(['nm1', 'nm2', 'nm3', 'result'])
    var.put('nm1', Js([Js('Abandoned'), Js('Adamant'), Js('Aegis'), Js('Ageless'), Js('All-Knowing'), Js('Ancient'), Js('Angelic'), Js('Arachnid'), Js('Arch'), Js('Austere'), Js('Balance'), Js('Blind'), Js('Brilliant'), Js('Bronze'), Js('Champion'), Js('Chief'), Js('Climate'), Js('Cloud'), Js('Clover'), Js('Creation'), Js('Crimson'), Js('Crown'), Js('Dark'), Js('Diamond'), Js('Dire'), Js('Dream'), Js('Dual'), Js('Earth'), Js('Earthen'), Js('Ebon'), Js('Elated'), Js('Elderly'), Js('Elite'), Js('Ember'), Js('Empath'), Js('Enchanted'), Js('Enlightened'), Js('Eternal'), Js('Ethereal'), Js('Exalted'), Js('Fearless'), Js('Flame'), Js('Forsaken'), Js('Garden'), Js('Ghost'), Js('Golden'), Js('Grand'), Js('Granite'), Js('Hallowed'), Js('Harmonious'), Js('Harmony'), Js('Heavenly'), Js('High'), Js('Ice'), Js('Infernal'), Js('Infinite'), Js('Infinity'), Js('Iris'), Js('Iron'), Js('Ivory'), Js('Jade'), Js('Judgment'), Js('Justice'), Js('Last'), Js('Legion'), Js('Liberty'), Js('Light'), Js('Living'), Js('Lone'), Js('Lunar'), Js('Mad'), Js('Marked'), Js('Masked'), Js('Memory'), Js('Mercy'), Js('Midnight'), Js('Moon'), Js('Mute'), Js('Mystery'), Js('Nightmare'), Js('Obsidian'), Js('Omen'), Js('Onyx'), Js('Oracle'), Js('Oval'), Js('Paradox'), Js('Parallel'), Js('Phantom'), Js('Portal'), Js('Primal'), Js('Prime'), Js('Private'), Js('Prism'), Js('Radiant'), Js('Round'), Js('Royal'), Js('Sanguine'), Js('Serpent'), Js('Shadow'), Js('Silent'), Js('Silver'), Js('Skeletal'), Js('Skeleton'), Js('Snow'), Js('Solar'), Js('Spirit'), Js('Storm'), Js('Sun'), Js('Supreme'), Js('Thunder'), Js('Tranquil'), Js('Tree'), Js('Twilight'), Js('Twin'), Js('Union'), Js('Unity'), Js('Velvet'), Js('Vessel'), Js('Voiceless'), Js('War'), Js('Wicked'), Js('Wisdom'), Js('Wise'), Js('Zephyr')]))
    var.put('nm2', Js([Js('Council'), Js('Board'), Js('Convocation'), Js('Congregation'), Js('Conclave'), Js('Council'), Js('Council'), Js('Council'), Js('Council'), Js('Council'), Js('Board')]))
    var.put('nm3', Js([Js('Advice'), Js('Ancients'), Js('Angels'), Js('Averages'), Js('Balance'), Js('Beginnings'), Js('Birth'), Js('Bliss'), Js('Blood'), Js('Borders'), Js('Brilliance'), Js('Candles'), Js('Chains'), Js('Champions'), Js('Chaos'), Js('Clarity'), Js('Corruption'), Js('Darkness'), Js('Death'), Js('Defiance'), Js('Dreams'), Js('Dust'), Js('Duty'), Js('Eternity'), Js('Evil'), Js('Experience'), Js('Faith'), Js('Fate'), Js('Fertility'), Js('Ghosts'), Js('Glass'), Js('Glory'), Js('God'), Js('Gods'), Js('Grace'), Js('Harmony'), Js('Heaven'), Js('Hell'), Js('Honor'), Js('Hope'), Js('Ice'), Js('Independence'), Js('Infinity'), Js('Iron'), Js('Justice'), Js('Knowledge'), Js('Life'), Js('Light'), Js('Lights'), Js('Memories'), Js('Mercy'), Js('Minds'), Js('Mithril'), Js('Nightmares'), Js('Omens'), Js('Opportunity'), Js('Peace'), Js('Phantoms'), Js('Protection'), Js('Reality'), Js('Rebels'), Js('Redemption'), Js('Reflection'), Js('Riddles'), Js('Shadows'), Js('Solitude'), Js('Spirits'), Js('Statues'), Js('Time'), Js('Tomorrow'), Js('Trade'), Js('Tranquility'), Js('Truth'), Js('Twilight'), Js('Unity'), Js('Victors'), Js('Voices'), Js('War'), Js('Whispers'), Js('Widows'), Js('Wisdom'), Js('the Abandoned'), Js('the Afterlife'), Js('the Ages'), Js('the Ancient'), Js('the Blind'), Js('the Brave'), Js('the Chosen'), Js('the Chosen One'), Js('the Clouds'), Js('the Colossus'), Js('the Corrupt'), Js('the Crown'), Js('the Dark'), Js('the Dead'), Js('the Defiant'), Js('the Enchanted'), Js('the End'), Js('the Enigma'), Js('the Enlightened'), Js('the Eternal'), Js('the Exalted'), Js('the Father'), Js('the Few'), Js('the Flawed'), Js('the Flawless'), Js('the Flock'), Js('the Forest'), Js('the Forgotten'), Js('the Forsaken'), Js('the Free'), Js('the Gifted'), Js('the God'), Js('the Gods'), Js('the Grim'), Js('the Hallowed'), Js('the Hive'), Js('the Hollow'), Js('the Honored'), Js('the Infinite'), Js('the Lake'), Js('the Light'), Js('the Living'), Js('the Many'), Js('the Mind'), Js('the Mother'), Js('the Mountain'), Js('the Next Realm'), Js('the Night'), Js('the Nocturnal'), Js('the Ocean'), Js('the Oracle'), Js('the Owl'), Js('the People'), Js('the Primal'), Js('the Prime'), Js('the Radiant'), Js('the Rebellion'), Js('the River'), Js('the Ruins'), Js('the Serene'), Js('the Storm'), Js('the Supreme'), Js('the Tempest'), Js('the Underworld'), Js('the Union'), Js('the Wolf')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm2').get(var.get('rnd2')))+Js(' of '))+var.get('nm3').get(var.get('rnd'))))
                var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
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
councilNames = var.to_python()