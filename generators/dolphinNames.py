__all__ = ['dolphinNames']

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
var.put('nm1', Js([Js('Abalone'), Js('Acro'), Js('Aenon'), Js('Artic'), Js('Avalon'), Js('Bay'), Js('Bayou'), Js('Beaker'), Js('Beck'), Js('Bered'), Js('Blue'), Js('Bo'), Js('Boomer'), Js('Bourne'), Js('Brook'), Js('Bubbles'), Js('Bullet'), Js('Captain'), Js('Caspian'), Js('Comet'), Js('Cruise'), Js('Dash'), Js('Crunch'), Js('Dew'), Js('Dips'), Js('Diver'), Js('Dover'), Js('Dune'), Js('Dyve'), Js('Echo'), Js('Finn'), Js('Flipper'), Js('Flips'), Js('Frost'), Js('Gal'), Js('Gar'), Js('Harbor'), Js('Harbour'), Js('Haven'), Js('Hurley'), Js('Ice'), Js('Jetty'), Js('Jive'), Js('Kai'), Js('Kane'), Js('Krill'), Js('Kyle'), Js('Lach'), Js('Lagoon'), Js('Laike'), Js('Lake'), Js('Mako'), Js('Marlin'), Js('Marlow'), Js('Marsh'), Js('Moor'), Js('Moore'), Js('Muir'), Js('Neptune'), Js('Nerio'), Js('Nero'), Js('Nile'), Js('Niles'), Js('Pisces'), Js('Plunge'), Js('Poseidon'), Js('Rain'), Js('Ray'), Js('Reef'), Js('Ren'), Js('Rio'), Js('Rip'), Js('Ripley'), Js('Sailor'), Js('Salty'), Js('Saul'), Js('Screech'), Js('Shade'), Js('Shadow'), Js('Shimmy'), Js('Shore'), Js('Sid'), Js('Sidney'), Js('Snorkel'), Js('Snowball'), Js('Snowflake'), Js('Soakes'), Js('Speedy'), Js('Splash'), Js('Spray'), Js('Sprinkle'), Js('Storm'), Js('Strom'), Js('Tad'), Js('Tails'), Js('Tango'), Js('Tide'), Js('Tracker'), Js('Triton'), Js('Troy'), Js('Tumble'), Js('Twister'), Js('Tyde'), Js('Wayde')]))
var.put('nm2', Js([Js('Abalone'), Js('Aeria'), Js('Aerial'), Js('Aqua'), Js('Aquina'), Js('Ara'), Js('Arial'), Js('Ariel'), Js('Artica'), Js('Baye'), Js('Bayou'), Js('Belle'), Js('Blue'), Js('Briny'), Js('Brooke'), Js('Bubbles'), Js('Bullette'), Js('Cari'), Js('Cascade'), Js('Cerulea'), Js('Comette'), Js('Cora'), Js('Coral'), Js('Coralia'), Js('Crystal'), Js('Dandy'), Js('Delta'), Js('Dew'), Js('Dips'), Js('Dorea'), Js('Doria'), Js('Dot'), Js('Echo'), Js('Fen'), Js('Finne'), Js('Flip'), Js('Gemma'), Js('Gloria'), Js('Grace'), Js('Hydris'), Js('Icee'), Js('Isla'), Js('Kai'), Js('Kaia'), Js('Kelby'), Js('Kelpe'), Js('Kura'), Js('Kyla'), Js('Laguna'), Js('Lagune'), Js('Lana'), Js('Llyn'), Js('Lumina'), Js('Luna'), Js('Mahi'), Js('Mai'), Js('Malibu'), Js('Mareen'), Js('Marine'), Js('Marinelle'), Js('Marinna'), Js('Marsha'), Js('Maryn'), Js('Maya'), Js('Melanie'), Js('Melody'), Js('Meri'), Js('Meris'), Js('Mime'), Js('Misty'), Js('Molly'), Js('Muriel'), Js('Nahla'), Js('Nami'), Js('Nebula'), Js('Neptuna'), Js('Nerina'), Js('Nile'), Js('Nixie'), Js('Oceana'), Js('Oceane'), Js('Opal'), Js('Pace'), Js('Pearl'), Js('Peirene'), Js('Pisces'), Js('Pitch'), Js('Pure'), Js('Raine'), Js('Razzle'), Js('Rhode'), Js('Ria'), Js('Riva'), Js('River'), Js('Sandy'), Js('Sapphire'), Js('Sealea'), Js('Shade'), Js('Shadow'), Js('Shelby'), Js('Shelly'), Js('Siera'), Js('Sierra'), Js('Siren'), Js('Sirena'), Js('Sirene'), Js('Snowball'), Js('Snowflake'), Js('Snowwhite'), Js('Sona'), Js('Sparkle'), Js('Splash'), Js('Splashy'), Js('Sprinkle'), Js('Sprinkles'), Js('Squeal'), Js('Squeek'), Js('Squiggle'), Js('Squiggles'), Js('Star'), Js('Sundance'), Js('Tide'), Js('Tumble'), Js('Tyde'), Js('Ula'), Js('Una'), Js('Yoka'), Js('Zippy')]))
pass
pass


# Add lib to the module scope
dolphinNames = var.to_python()