__all__ = ['planeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Agile'), Js('Ancient'), Js('Angry'), Js('Arid'), Js('Able'), Js('Bad'), Js('Big'), Js('Bitter'), Js('Black'), Js('Blaring'), Js('Blind'), Js('Blue'), Js('Bold'), Js('Bronze'), Js('Brown'), Js('Buzzing'), Js('Calm'), Js('Classic'), Js('Cold'), Js('Cool'), Js('Crazy'), Js('Cruel'), Js('Dapper'), Js('Dark'), Js('Defiant'), Js('Diligent'), Js('Double'), Js('Eager'), Js('Evil'), Js('False'), Js('Fast'), Js('Fatal'), Js('Feline'), Js('Forsaken'), Js('Free'), Js('Frozen'), Js('Gentle'), Js('Gold'), Js('Golden'), Js('Grand'), Js('Grave'), Js('Gray'), Js('Greedy'), Js('Grim'), Js('Happy'), Js('Harsh'), Js('High'), Js('Hollow'), Js('Hot'), Js('Huge'), Js('Humming'), Js('Hungry'), Js('Idle'), Js('Infamous'), Js('Infinite'), Js('Ironclad'), Js('Jagged'), Js('Keen'), Js('Last'), Js('Lazy'), Js('Light'), Js('Little'), Js('Livid'), Js('Lone'), Js('Long'), Js('Loud'), Js('Low'), Js('Loyal'), Js('Mad'), Js('Major'), Js('Mellow'), Js('Nervous'), Js('Numb'), Js('Old'), Js('Pale'), Js('Parallel'), Js('Prime'), Js('Proud'), Js('Quick'), Js('Quiet'), Js('Ragged'), Js('Rapid'), Js('Rare'), Js('Reckless'), Js('Red'), Js('Regal'), Js('Rough'), Js('Round'), Js('Royal'), Js('Rude'), Js('Sharp'), Js('Shy'), Js('Silent'), Js('Silver'), Js('Slim'), Js('Small'), Js('Smooth'), Js('Subtle'), Js('Sweet'), Js('Swift'), Js('Tiny'), Js('Tough'), Js('Vain'), Js('Vengeful'), Js('Vicious'), Js('Vivid'), Js('Warped'), Js('White'), Js('Wicked'), Js('Wild'), Js('Wise')]))
var.put('nm2', Js([Js('Albatross'), Js('Freak'), Js('Banshee'), Js('Voodoo'), Js('Arrow'), Js('Beast'), Js('Bee'), Js('Beetle'), Js('Bird'), Js('Blimp'), Js('Bolt'), Js('Bomb'), Js('Bomber'), Js('Boomerang'), Js('Boy'), Js('Bullet'), Js('Buzzard'), Js('Centurion'), Js('Chick'), Js('Cobra'), Js('Condor'), Js('Crane'), Js('Crow'), Js('Daddy'), Js('Dart'), Js('Darter'), Js('Diver'), Js('Dragon'), Js('Dragonfly'), Js('Ducchess'), Js('Duck'), Js('Duke'), Js('Eagle'), Js('Falcon'), Js('Fly'), Js('Ghost'), Js('Goose'), Js('Gryphon'), Js('Gull'), Js('Harrier'), Js('Hawk'), Js('Hornet'), Js('Ibis'), Js('Jet'), Js('King'), Js('Legionnaire'), Js('Lightning'), Js('Mamba'), Js('Mommy'), Js('Mosquito'), Js('Moth'), Js('Overcast'), Js('Owl'), Js('Pelican'), Js('Phantom'), Js('Queen'), Js('Raven'), Js('Robin'), Js('Rocket'), Js('Serpent'), Js('Shooter'), Js('Sparrow'), Js('Spirit'), Js('Stork'), Js('Thunder'), Js('Torpedo'), Js('Viper'), Js('Vulture'), Js('Widow'), Js('Woodpecker')]))
var.put('nm3', Js([Js('Aerial'), Js('Agile'), Js('Air'), Js('Avian'), Js('Azure'), Js('Banshee'), Js('Brass'), Js('Bright'), Js('Chaos'), Js('Cloud'), Js('Dark'), Js('Demon'), Js('Devil'), Js('Dragon'), Js('Dream'), Js('Drift'), Js('Ebon'), Js('Feral'), Js('Flight'), Js('Flying'), Js('Free'), Js('Frost'), Js('Ghost'), Js('Grey'), Js('Heaven'), Js('Hell'), Js('Iron'), Js('Little'), Js('Mad'), Js('Monster'), Js('Night'), Js('Nimble'), Js('Phantom'), Js('Prime'), Js('Quick'), Js('Rapid'), Js('Rogue'), Js('Shadow'), Js('Sky'), Js('Star'), Js('Swift'), Js('Thunder'), Js('Twin'), Js('Wild'), Js('Wrath')]))
var.put('nm4', Js([Js('beast'), Js('blast'), Js('blaze'), Js('blitz'), Js('bolt'), Js('bomb'), Js('brute'), Js('bullet'), Js('burst'), Js('charge'), Js('charm'), Js('comet'), Js('core'), Js('cry'), Js('eater'), Js('edge'), Js('fire'), Js('flare'), Js('flight'), Js('flow'), Js('flux'), Js('force'), Js('freak'), Js('fury'), Js('glider'), Js('hail'), Js('heat'), Js('lance'), Js('light'), Js('master'), Js('nova'), Js('pulse'), Js('punch'), Js('pyre'), Js('rage'), Js('raid'), Js('rise'), Js('roar'), Js('rush'), Js('scream'), Js('shade'), Js('spark'), Js('storm'), Js('strike'), Js('thunder'), Js('tooth'), Js('urge'), Js('ward'), Js('wing'), Js('wrath')]))
pass
pass


# Add lib to the module scope
planeNames = var.to_python()