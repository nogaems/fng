__all__ = ['motorClubNames']

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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(2.0)):
                var.put('names', (Js('The ')+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Alpha'), Js('Anarchy'), Js('Angry'), Js('Argent'), Js('Arrowhead'), Js('Asphalt'), Js('Barbaric'), Js('Barking'), Js('Barrel'), Js('Bearded'), Js('Big'), Js('Bitter'), Js('Black'), Js('Blackhawk'), Js('Blazing'), Js('Blue'), Js('Booze'), Js('Border'), Js('Born'), Js('Broken'), Js('Burning'), Js('Burnt'), Js('Capital'), Js('Casual'), Js('Celtic'), Js('Chained'), Js('Chaos'), Js('Chasing'), Js('Chosen'), Js('Cold'), Js('Comet'), Js('Country'), Js('Crazy'), Js('Cunning'), Js('Dark'), Js('Dawn'), Js('Daylight'), Js('Dead'), Js('Derby'), Js("Devil's"), Js('Devoted'), Js('Die-Hard'), Js('Dirt'), Js('Dirty'), Js('Double'), Js('Dragon'), Js('Drunken'), Js('Dusk'), Js('Eastern'), Js('Endless'), Js('Fallen'), Js('Famous'), Js('Feral'), Js('Flying'), Js('Forward'), Js('Free'), Js('Freestyle'), Js('Freezone'), Js('Frosty'), Js('Frozen'), Js('Full Moon'), Js('Galloping'), Js('Gliding'), Js('Grave'), Js('Gravel'), Js('Grim'), Js('Hairy'), Js('Hardcore'), Js('Havoc'), Js('Horizon'), Js('Ignited'), Js('Independent'), Js('Infamous'), Js('Inferno'), Js('Inland'), Js('Insane'), Js('Iron'), Js('Jagged'), Js('Legendary'), Js('Liberty'), Js('Lightning'), Js('Little'), Js('Living'), Js('Lone'), Js('Long'), Js('Lost'), Js('Loud'), Js('Missing'), Js('Monster'), Js('Moonlight'), Js('Nameless'), Js('New'), Js('Night'), Js('Northern'), Js('Old'), Js('Phantom'), Js('Primal'), Js('Prime'), Js('Raging'), Js('Rebel'), Js('Reckless'), Js('Red'), Js('Restless'), Js('Rising'), Js('Road'), Js('Roaring'), Js('Rolling'), Js('Rough'), Js('Rugged'), Js('Rusty'), Js('Salvation'), Js('Savage'), Js('Shadow'), Js('Silent'), Js('Sleepless'), Js('Smokey'), Js('Smoking'), Js('Solo'), Js('Southern'), Js('Spartan'), Js('Spectral'), Js('Spiked'), Js('Steel'), Js('Storm'), Js('Thunder'), Js('Tribal'), Js('Triple'), Js('True'), Js('Twisted'), Js('Valley'), Js('Warped'), Js('Western'), Js('Wild')]))
var.put('nm2', Js([Js('Aces'), Js('Alloys'), Js('Ancestors'), Js('Angels'), Js('Armada'), Js('Badgers'), Js('Bandidos'), Js('Bandits'), Js('Barbarians'), Js('Beanies'), Js('Beards'), Js('Bears'), Js('Bikers'), Js('Boars'), Js('Bones'), Js('Boots'), Js('Boys'), Js('Brotherhood'), Js('Brothers'), Js('Buzzards'), Js('Cannibals'), Js('Cats'), Js('Chariots'), Js('Chiefs'), Js('Clan'), Js('Cobras'), Js('Comets'), Js('Corps'), Js('Coyotes'), Js('Crew'), Js('Crows'), Js('Cruisers'), Js('Crusaders'), Js('Demons'), Js('Destroyers'), Js('Devils'), Js('Diablos'), Js('Disciples'), Js('Dogs'), Js('Dragons'), Js('Drakes'), Js('Drifters'), Js('Eagles'), Js('Emblems'), Js('Falcons'), Js('Fallen'), Js('Fathers'), Js('Fiends'), Js('Foxes'), Js('Freaks'), Js('Gargoyles'), Js('Ghosts'), Js('Girls'), Js('Griffins'), Js('Guardians'), Js('Heads'), Js('Hearts'), Js('Henchmen'), Js('Heretics'), Js('Highwaymen'), Js('Hogs'), Js('Horsemen'), Js('Horses'), Js('Hounds'), Js('Howlers'), Js('Hunters'), Js('Jackals'), Js('Jesters'), Js('Jokers'), Js('Keepers'), Js('Kings'), Js('Kingsmen'), Js('Knights'), Js('Legion'), Js('Legionnaires'), Js('Lions'), Js('Lords'), Js('Lovers'), Js('Machines'), Js('Marauders'), Js('Mavericks'), Js('Misfits'), Js('Mohawks'), Js('Mutants'), Js('Mutineers'), Js('Order'), Js('Outlaws'), Js('Owls'), Js('Panthers'), Js('Pirates'), Js('Pixies'), Js('Predators'), Js('Prowlers'), Js('Pythons'), Js('Raiders'), Js('Raptors'), Js('Rats'), Js('Reapers'), Js('Rebels'), Js('Renegades'), Js('Roadsters'), Js('Rockers'), Js('Rodents'), Js('Sabers'), Js('Saddles'), Js('Saints'), Js('Samurai'), Js('Scavengers'), Js('Scorpions'), Js('Sentinels'), Js('Shadows'), Js('Sidekicks'), Js('Sisterhood'), Js('Skulls'), Js('Slayers'), Js('Smugglers'), Js('Soldiers'), Js('Souls'), Js('Spades'), Js('Spiders'), Js('Spirits'), Js('Syndicate'), Js('Tigers'), Js('Travelers'), Js('Troopers'), Js('Vagabonds'), Js('Veterans'), Js('Vultures'), Js('Wanderers'), Js('Warriors'), Js('Weasels'), Js('Werewolves'), Js('Wheelers'), Js('Widows'), Js('Wings'), Js('Wolves')]))
pass
pass


# Add lib to the module scope
motorClubNames = var.to_python()