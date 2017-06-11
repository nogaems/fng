__all__ = ['sportTeams']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Amazing'), Js('Ancient'), Js('Angry'), Js('Awesome'), Js('Big'), Js('Big Bad'), Js('Bitter'), Js('Black'), Js('Blue'), Js('Bold'), Js('Brave'), Js('Bright'), Js('Brutal'), Js('Brute'), Js('Calm'), Js('Careless'), Js('Classic'), Js('Clever'), Js('Colossal'), Js('Courageous'), Js('Crazy'), Js('Creative'), Js('Dapper'), Js('Daring'), Js('Deadly'), Js('Defiant'), Js('Determined'), Js('Eager'), Js('Earnest'), Js('Enchanted'), Js('Exalted'), Js('Fabulous'), Js('Fantastic'), Js('Fast'), Js('Fearless'), Js('Fiery'), Js('Flawless'), Js('Flying'), Js('Free'), Js('Freedom'), Js('Giant'), Js('Glorious'), Js('Golden'), Js('Grand'), Js('Grave'), Js('Great'), Js('Grim'), Js('Grizzly'), Js('Gruesome'), Js('Handsome'), Js('Happy'), Js('Hard'), Js('Haunting'), Js('Heavenly'), Js('Hidden'), Js('Hot'), Js('Hungry'), Js('Incredible'), Js('Infamous'), Js('Iron'), Js('Loyal'), Js('Lucky'), Js('Mad'), Js('Magic'), Js('Majestic'), Js('Major'), Js('Marvelous'), Js('Mean'), Js('Merry'), Js('Monstrous'), Js('Mysterious'), Js('Mystery'), Js('Naughty'), Js('Nimble'), Js('Potent'), Js('Powerful'), Js('Prime'), Js('Proud'), Js('Pure'), Js('Quick'), Js('Quiet'), Js('Rapid'), Js('Red'), Js('Regal'), Js('Rough'), Js('Royal'), Js('Silent'), Js('Silver'), Js('Skeleton'), Js('Spectacular'), Js('Spirit'), Js('Stark'), Js('Steel'), Js('Storm'), Js('Strong'), Js('Swift'), Js('Terrific'), Js('Thunder'), Js('Tough'), Js('True'), Js('United'), Js('Valiant'), Js('White'), Js('Wicked'), Js('Wild'), Js('Wise'), Js('Young')]))
var.put('nm2', Js([Js('Aces'), Js('Admirals'), Js('Aliens'), Js('Alligators'), Js('Alphas'), Js('Anacondas'), Js('Androids'), Js('Angels'), Js('Ants'), Js('Apes'), Js('Arrows'), Js('Asteroids'), Js('Baboons'), Js('Badgers'), Js('Barracudas'), Js('Bats'), Js('Bears'), Js('Beasts'), Js('Beavers'), Js('Bees'), Js('Beluga Whales'), Js('Birds'), Js('Bison'), Js('Blades'), Js('Blazers'), Js('Blazes'), Js('Blitzes'), Js('Blizzards'), Js('Boars'), Js('Bolts'), Js('Boomers'), Js('Bottle Rockets'), Js('Boulders'), Js('Braves'), Js('Broncos'), Js('Bruisers'), Js('Buccanneers'), Js('Buffalo'), Js('Bulldogs'), Js('Bullets'), Js('Bulls'), Js('Busters'), Js('Camels'), Js('Cannons'), Js('Cardinals'), Js('Cats'), Js('Cavaliers'), Js('Champs'), Js('Chargers'), Js('Cheetahs'), Js('Chiefs'), Js('Chimpanzees'), Js('Chimps'), Js('Claws'), Js('Cobras'), Js('Comets'), Js('Cougars'), Js('Coyotes'), Js('Crabs'), Js('Cranes'), Js('Creatures'), Js('Crickets'), Js('Crocodiles'), Js('Crocs'), Js('Crows'), Js('Crunchers'), Js('Crusaders'), Js('Cubs'), Js('Deer'), Js('Demons'), Js('Devils'), Js('Dingos'), Js('Dinos'), Js('Dinosaurs'), Js('Dodgers'), Js('Dogs'), Js('Dolphins'), Js('Donkeys'), Js('Doves'), Js('Dragonflies'), Js('Dragons'), Js('Dreamers'), Js('Dreams'), Js('Droids'), Js('Ducks'), Js('Eagles'), Js('Earthquakes'), Js('Elephants'), Js('Enigmas'), Js('Explorers'), Js('Falcons'), Js('Ferrets'), Js('Foxes'), Js('Furies'), Js('Gargoyles'), Js('Gators'), Js('Ghosts'), Js('Giants'), Js('Gibbons'), Js('Giraffes'), Js('Gladiators'), Js('Gnomes'), Js('Goats'), Js('Goblins'), Js('Gophers'), Js('Gorillas'), Js('Grasshoppers'), Js('Griffins'), Js('Grizzlies'), Js('Gusts'), Js('Hammers'), Js('Hamsters'), Js('Hawks'), Js('Hedgehogs'), Js('Heroes'), Js('Hippos'), Js('Hogs'), Js('Honey Badgers'), Js('Hornets'), Js('Horses'), Js('Hounds'), Js('Howlers'), Js('Hurricanes'), Js('Hyenas'), Js('Imps'), Js('Infernos'), Js('Jackals'), Js('Jaguars'), Js('Jesters'), Js('Jokers'), Js('Kangaroos'), Js('Kingfishers'), Js('Kings'), Js('Knights'), Js('Koalas'), Js('Komodos'), Js('Krakens'), Js('Legends'), Js('Lemurs'), Js('Leopards'), Js('Lions'), Js('Lizards'), Js('Llamas'), Js('Lobsters'), Js('Magicians'), Js('Mallards'), Js('Mambas'), Js('Mammoths'), Js('Manatees'), Js('Manticores'), Js('Marines'), Js('Martians'), Js('Marvels'), Js('Mavericks'), Js('Menaces'), Js('Miracles'), Js('Monarchs'), Js('Monkeys'), Js('Monsters'), Js('Mountaineers'), Js('Mystics'), Js('Mythics'), Js('Nationals'), Js('Nightingales'), Js('Ninjas'), Js('Novas'), Js('Ocelots'), Js('Octopi'), Js('Ogres'), Js('Oracles'), Js('Orangutans'), Js('Orcas'), Js('Orcs'), Js('Ostriches'), Js('Pandas'), Js('Panthers'), Js('Parrots'), Js('Patriots'), Js('Peacocks'), Js('Pelicans'), Js('Penguins'), Js('Phantoms'), Js('Phoenixes'), Js('Pigeons'), Js('Pigs'), Js('Pirates'), Js('Pit Bulls'), Js('Porcupines'), Js('Predators'), Js('Prowlers'), Js('Pumas'), Js('Pythons'), Js('Raccoons'), Js('Raiders'), Js('Rams'), Js('Rangers'), Js('Raptors'), Js('Ravens'), Js('Rhinos'), Js('Riddles'), Js('Riders'), Js('Roaches'), Js('Roadrunners'), Js('Robins'), Js('Robots'), Js('Rockets'), Js('Rovers'), Js('Royals'), Js('Runners'), Js('Sabretooths'), Js('Sailors'), Js('Saints'), Js('Scorpions'), Js('Seagulls'), Js('Seals'), Js('Serpents'), Js('Shades'), Js('Shadows'), Js('Sharks'), Js('Sirens'), Js('Sliders'), Js('Snakes'), Js('Snowstorms'), Js('Soldiers'), Js('Sparks'), Js('Sparrows'), Js('Spartans'), Js('Spiders'), Js('Spikes'), Js('Squids'), Js('Squirrels'), Js('Stags'), Js('Stallions'), Js('Stars'), Js('Stingers'), Js('Storms'), Js('Striders'), Js('Suns'), Js('Swallows'), Js('Swans'), Js('Terrors'), Js('Tigers'), Js('Titans'), Js('Toads'), Js('Tornadoes'), Js('Toucans'), Js('Trojans'), Js('Trolls'), Js('Turkeys'), Js('Turtles'), Js('Vampires'), Js('Vikings'), Js('Vipers'), Js('Vultures'), Js('Warhawks'), Js('Warhogs'), Js('Warriors'), Js('Warthogs'), Js('Wasps'), Js('Weasels'), Js('Werewolves'), Js('Wildcats'), Js('Wildlings'), Js('Wings'), Js('Wizards'), Js('Wolverines'), Js('Wolves'), Js('Wombats'), Js('Wreckers'), Js('Yetis'), Js('Zebras'), Js('Zombies')]))
pass
pass


# Add lib to the module scope
sportTeams = var.to_python()