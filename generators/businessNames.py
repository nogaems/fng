__all__ = ['businessNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names5', 'names2', 'names3', 'names1'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', ((var.get('names1').get(var.get('rnd0'))+Js(' '))+var.get('names2').get(var.get('rnd1'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('names', var.get('names3').get(var.get('rnd0')))
                else:
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('names', (var.get('names4').get(var.get('rnd0'))+var.get('names5').get(var.get('rnd1'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Accent'), Js('Ace'), Js('Alligator'), Js('Alp'), Js('Alpha'), Js('Alpine'), Js('Amazon'), Js('Angel'), Js('Answer'), Js('Ant'), Js('Antler'), Js('Apache'), Js('Apex'), Js('Apple'), Js('Apricot'), Js('Arcane'), Js('Ask'), Js('Aura'), Js('Banshee'), Js('Bear Paw'), Js('Beedle'), Js('Berry'), Js('Beta'), Js('Blizzard'), Js('Blossom'), Js('Blue'), Js('Bluff'), Js('Boar'), Js('Bridge'), Js('Brisk'), Js('Buck'), Js('Bull'), Js('Bumblebee'), Js('Butterfly'), Js('Buzzy Bee'), Js('Canine'), Js('Cannon'), Js('Cave'), Js('Cavern'), Js('Ceasar'), Js('Champion'), Js('Chief'), Js('Cliff'), Js('Cloud'), Js('Clover'), Js('Core'), Js('Crow'), Js('Cruise'), Js('Crux'), Js('Cryptic'), Js('Crystal'), Js('Cube'), Js('Cyclone'), Js('Cyclops'), Js('Daydream'), Js('Deluge'), Js('Desert'), Js('Diamond'), Js('Dinosaur'), Js('Dragon'), Js('Dream'), Js('Drift'), Js('Dwarf'), Js('Dynamic'), Js('Eclipse'), Js('Ecstatic'), Js('Electra'), Js('Electron'), Js('Elite'), Js('Elvish'), Js('Energy'), Js('Enigma'), Js('Equinox'), Js('Essence'), Js('Explorer'), Js('Fairy'), Js('Feline'), Js('Fire'), Js('Fjord'), Js('Flower'), Js('Fluke'), Js('Flux'), Js('Forest'), Js('Fortune'), Js('Freak'), Js('Frostfire'), Js('Gale'), Js('Gem'), Js('Ghost'), Js('Glacier'), Js('Global'), Js('Globe'), Js('Gnome'), Js('Goblin'), Js('Gold'), Js('Golden Road'), Js('Gorilla'), Js('Granite'), Js('Grasshopper'), Js('Great White'), Js('Green'), Js('Griffin'), Js('Grizzly'), Js('Grotto'), Js('Hammer'), Js('Happy'), Js('Hatch'), Js('Heart'), Js('Herb'), Js('Hercules'), Js('Hero'), Js('High Tide'), Js('Hog'), Js('Honey'), Js('Honeydew'), Js('Hook'), Js('Hound'), Js('Hummingbird'), Js('Hurricane'), Js('Ice'), Js('Iceberg'), Js('Icecap'), Js('Imagination'), Js('Imagine'), Js('Iron'), Js('Jet'), Js('Jewel'), Js('Joy'), Js('Jungle'), Js('Jupiter'), Js('Karma'), Js('Labyrinth'), Js('Lagoon'), Js('Lemon'), Js('Leopard'), Js('Life'), Js('Lion'), Js('Lioness'), Js('Loki'), Js('Low Tide'), Js('Lucent'), Js('Lucky'), Js('Maple'), Js('Marble'), Js('Mars'), Js('Marsh'), Js('Maze'), Js('Melon'), Js('Mercury'), Js('Mermaid'), Js('Micro'), Js('Midnight'), Js('Monarch'), Js('Moon'), Js('Moondust'), Js('Moonlight'), Js('Moonlit'), Js('Moth'), Js('Motion'), Js('Mount'), Js('Mountain'), Js('Mystic'), Js('Nemo'), Js('Neptune'), Js('Nero'), Js('Night'), Js('Nimble'), Js('North Star'), Js('Nymph'), Js('Oak'), Js('Ocean'), Js('Odin'), Js('Ogre'), Js('Omega'), Js('Oracle'), Js('Orange'), Js('Orc'), Js('Owl'), Js('Oyster'), Js('Padlock'), Js('Parable'), Js('Paragon'), Js('Peach'), Js('Pearl'), Js('Petal'), Js('Phantasm'), Js('Phantom'), Js('Phenomenon'), Js('Phoenix'), Js('Pink'), Js('Pinnacle'), Js('Pixel'), Js('Pixy'), Js('Pluto'), Js('Pride'), Js('Primal'), Js('Prime'), Js('Prodigy'), Js('Prophecy'), Js('Proton'), Js('Pumpkin'), Js('Purple'), Js('Pyramid'), Js('Quad'), Js('Question'), Js('Rabbit'), Js('Radiant'), Js('Raptor'), Js('Raven'), Js('Red'), Js('Revelation'), Js('Rhino'), Js('Riddle'), Js('Ridge'), Js('River'), Js('Robin'), Js('Root'), Js('Rose'), Js('Rush'), Js('Sail'), Js('Sapling'), Js('Saturn'), Js('Saw'), Js('Seaway'), Js('Seed'), Js('Shade'), Js('Shadow'), Js('Sharkfin'), Js('Shrub'), Js('Sign'), Js('Signal'), Js('Silver'), Js('Silver Lining'), Js('Slick'), Js('Smart'), Js('Smile'), Js('Solstice'), Js('Soul'), Js('Specter'), Js('Sphere'), Js('Sphinx'), Js('Spider'), Js('Spike'), Js('Spirit'), Js('Sprite'), Js('Squid'), Js('Star'), Js('Stardust'), Js('Starlight'), Js('Storm'), Js('Summit'), Js('Sun'), Js('Sunlight'), Js('Sunshine'), Js('Surge'), Js('Surprise'), Js('Tempest'), Js('Thor'), Js('Thunder'), Js('Tide'), Js('Tiger'), Js('Tigress'), Js('Timber'), Js('Titanium'), Js('Topiary'), Js('Tortoise'), Js('Trek'), Js('Triumph'), Js('Tucan'), Js('Tulip'), Js('Tundra'), Js('Turtle'), Js('Twilight'), Js('Twister'), Js('Typhoon'), Js('Valkyrie'), Js('Venus'), Js('Vertex'), Js('Vine'), Js('Vision'), Js('Void'), Js('Vortex'), Js('Voyage'), Js('Wave'), Js('Web'), Js('Whirlpool'), Js('Whirlwind'), Js('White Wolf'), Js('Whiteout'), Js('Whiz'), Js('Willow'), Js('Witch'), Js('Wizard'), Js('Wolf'), Js('Wonder'), Js('Wood'), Js('World'), Js('Yellow'), Js('Yew'), Js('Zeus')]))
var.put('names2', Js([Js(''), Js(''), Js('Acoustics'), Js('Arts'), Js('Aviation'), Js('Brews'), Js('Co.'), Js('Coms'), Js('Corp'), Js('Corporation'), Js('Electronics'), Js('Enterprises'), Js('Entertainment'), Js('Foods'), Js('Industries'), Js('Intelligence'), Js('Lighting'), Js('Limited'), Js('Media'), Js('Microsystems'), Js('Motors'), Js('Navigations'), Js('Networks'), Js('Productions'), Js('Records'), Js('Security'), Js('Softwares'), Js('Solutions'), Js('Sports'), Js('Systems'), Js('Technologies')]))
var.put('names3', Js([Js('Accenco'), Js('Aces'), Js('Allico'), Js('Alphacom'), Js('Alpire'), Js('Alpite'), Js('Amazystems'), Js('Angelico'), Js('Ansoft'), Js('Antarts'), Js('Antelligence'), Js('Apachicorp'), Js('Apexi'), Js('Appiation'), Js('Aprico'), Js('Arcanetworks'), Js('Asco'), Js('Aurarts'), Js('Bansheelectronis'), Js('Bearings'), Js('Beedlectrics'), Js('Berrycords'), Js('Betarts'), Js('Blizzart'), Js('Blossomotors'), Js('Bluetronics'), Js('Bluffoods'), Js('Boarco'), Js('Bridgelectrics'), Js('Brisco'), Js('Buckoustics'), Js('Bullimited'), Js('Bumblebeelectrics'), Js('Butterflyght'), Js('Buzzylectrics'), Js('Canics'), Js('Cannonics'), Js('Cavernetworks'), Js('Cavologies'), Js('Ceasarts'), Js('Champroductions'), Js('Chiefoods'), Js('Cliffoods'), Js('Cloudustries'), Js('Cloverprises'), Js('Corecords'), Js('Crowares'), Js('Cruisertainment'), Js('Cruxolutions'), Js('Crypticorps'), Js('Crystalightning'), Js('Cubrews'), Js('Cyclolutions'), Js('Cycloration'), Js('Daydreamotors'), Js('Delugation'), Js('Deserprises'), Js('Diamontronics'), Js('Dinosecurity'), Js('Dragonetworks'), Js('Dreamedia'), Js('Driftonics'), Js('Dwarfoods'), Js('Dynamico'), Js('Ecliprises'), Js('Ecstaticorps'), Js('Elecoms'), Js('Electrorks'), Js('Elitelligence'), Js('Elviations'), Js('Energence'), Js('Enigmotors'), Js('Equinetworks'), Js('Essensecurity'), Js('Explority'), Js('Fairiprises'), Js('Felinetworks'), Js('Firetronics'), Js('Fjordustries'), Js('Flowertainment'), Js('Flukords'), Js('Fluxystems'), Js('Forestics'), Js('Fortunetworks'), Js('Freacrosystems'), Js('Frostfiretronics'), Js('Galerprises'), Js('Gemedia'), Js('Ghostronics'), Js('Glaciarts'), Js('Globaviations'), Js('Globeworks'), Js('Gnomelectrics'), Js('Goblintelligence'), Js('Golbrews'), Js('Goldustries'), Js('Gorillacoustics'), Js('Granitelligence'), Js('Grasshoproductions'), Js('Greatechnologies'), Js('Greenetworks'), Js('Griffindustries'), Js('Grizzlimited'), Js('Grottolutions'), Js('Hammertronics'), Js('Happindustries'), Js('Hatchworks'), Js('Heartelligence'), Js('Herbrews'), Js('Herculentertainment'), Js('Herolutions'), Js('High Tidustries'), Js('Hogurity'), Js('Honeydustries'), Js('Honeytelligence'), Js('Hookurity'), Js('Houndnavigations'), Js('Hummingbirdustries'), Js('Hurricanetworks'), Js('Icebergarts'), Js('Icecaproductions'), Js('Icecorps'), Js('Imaginavigations'), Js('Imaginetworks'), Js('Ironavigation'), Js('Jetechnologies'), Js('Jewelectrics'), Js('Joytechs'), Js('Junglectics'), Js('Jupitelligence'), Js('Karmarts'), Js('Labyrintelligence'), Js('Lagoonavigations'), Js('Lemonetworks'), Js('Leopardworks'), Js('Lifoods'), Js('Lionessolutions'), Js('Lionetworks'), Js('Lokilutions'), Js('Low Tidustries'), Js('Lucentertainment'), Js('Luckytronics'), Js('Mapletainment'), Js('Marblightning'), Js('Marsecuriy'), Js('Marsoftwares'), Js('Mazecurity'), Js('Melonetworks'), Js('Mercurtainment'), Js('Mermedia'), Js('Microlutions'), Js('Midnightelligence'), Js('Monarctronics'), Js('Moondustries'), Js('Moonlightings'), Js('Moonlimited'), Js('Moonnetworks'), Js('Mothechnologies'), Js('Motionavigations'), Js('Mountainetworks'), Js('Mountelligence'), Js('Mysticorps'), Js('Nemotors'), Js('Neptunetworks'), Js('Neroductions'), Js('Nightelligence'), Js('Nimbletainment'), Js('North Starporation'), Js('Nymphoods'), Js('Oakoms'), Js('Oceanavigations'), Js('Odinetworks'), Js('Ogreprises'), Js('Omegacoustics'), Js('Oracleutions'), Js('Orangations'), Js('Orco'), Js('Owlimited'), Js('Oystertainment'), Js('Padlockurity'), Js('Parableutions'), Js('Paragonetworks'), Js('Peachco'), Js('Pearlightning'), Js('Petalimited'), Js('Phantasmedia'), Js('Phantomedia'), Js('Phenomenologies'), Js('Phoenixolutions'), Js('Pinkorps'), Js('Pinnaclelectrics'), Js('Pixelimited'), Js('Pixystems'), Js('Plutronics'), Js('Priductions'), Js('Primacoustics'), Js('Primedia'), Js('Prodintelligence'), Js('Prophecycurity'), Js('Protonetworks'), Js('Pumpkinavigation'), Js('Purplelimited'), Js('Pyramidustries'), Js('Quaductions'), Js('Questindustries'), Js('Rabbitechnologies'), Js('Radiantelligence'), Js('Raptolutions'), Js('Ravenetworks'), Js('Redustries'), Js('Revelationetworks'), Js('Rhinotainment'), Js('Riddlectronics'), Js('Ridgeco'), Js('Riverecords'), Js('Robinetworks'), Js('Rootechnologies'), Js('Rosecurity'), Js('Rushcorp'), Js('Sailightning'), Js('Saplimited'), Js('Saturnetworks'), Js('Sawwares'), Js('Seawares'), Js('Seedtronics'), Js('Shadearts'), Js('Shadoworks'), Js('Sharkfinetworks'), Js('Shrubrews'), Js('Signalimited'), Js('Signetworks'), Js('Silver Linetworks'), Js('Silverecords'), Js('Slickorps'), Js('Smartechnologies'), Js('Smilectronics'), Js('Solsticetems'), Js('Soulightning'), Js('Spectertainment'), Js('Spherecords'), Js('Sphinxecurity'), Js('Spicurity'), Js('Spideradio'), Js('Spiritechnologies'), Js('Spritechnologies'), Js('Squidustries'), Js('Stardustechnologies'), Js('Starecords'), Js('Starlightning'), Js('Stormedia'), Js('Summitechnologies'), Js('Sunavigations'), Js('Sunlightning'), Js('Sunshinetworks'), Js('Surgesystems'), Js('Surprisystems'), Js('Tempestechnologies'), Js('Thorecords'), Js('Thunderecords'), Js('Tidustries'), Js('Tigertainment'), Js('Tigressystems'), Js('Timberecords'), Js('Titaniumotors'), Js('Topiarytelligence'), Js('Tortoisecurity'), Js('Trekords'), Js('Triumphoods'), Js('Tucanterprises'), Js('Tuliproductions'), Js('Tundracoustics'), Js('Turtletainment'), Js('Twilightechnologies'), Js('Twisterecords'), Js('Typhoonavigations'), Js('Valkyrecords'), Js('Venusystems'), Js('Vertexoftwards'), Js('Vinedustries'), Js('Visionetworks'), Js('Voidustries'), Js('Vortexecurity'), Js('Voyagetronics'), Js('Wavigations'), Js('Webrews'), Js('Whirlpoolutions'), Js('Whirlwindustries'), Js('White Wolfoods'), Js('Whiteoutwares'), Js('Whizystems'), Js('Willowares'), Js('Witchystems'), Js('Wizardustries'), Js('Wolfoods'), Js('Wonderprises'), Js('Wooductions'), Js('Worldwares'), Js('Yelloworks'), Js('Yeworks'), Js('Zeusolutions')]))
var.put('names4', Js([Js('Accent'), Js('Ace'), Js('Alligator'), Js('Alpha'), Js('Alpine'), Js('Amazon'), Js('Angel'), Js('Apache'), Js('Apex'), Js('Arcane'), Js('Aura'), Js('Banshee'), Js('Beedle'), Js('Berry'), Js('Beta'), Js('Blossom'), Js('Blue'), Js('Boar'), Js('Bridge'), Js('Bull'), Js('Bee'), Js('Cannon'), Js('Cave'), Js('Cavern'), Js('Chief'), Js('Cliff'), Js('Cloud'), Js('Core'), Js('Crow'), Js('Crystal'), Js('Cube'), Js('Desert'), Js('Diamond'), Js('Dino'), Js('Dragon'), Js('Dream'), Js('Drift'), Js('Dwarf'), Js('Dynamic'), Js('Fairy'), Js('Fire'), Js('Flower'), Js('Forest'), Js('Freak'), Js('Gem'), Js('Ghost'), Js('Global'), Js('Globe'), Js('Gnome'), Js('Gold'), Js('Gorilla'), Js('Granite'), Js('Green'), Js('Griffin'), Js('Grizzly'), Js('Grotto'), Js('Hammer'), Js('Happy'), Js('Hatch'), Js('Heart'), Js('Herb'), Js('Hero'), Js('Hog'), Js('Honey'), Js('Hook'), Js('Hound'), Js('Humming'), Js('Ice'), Js('Iron'), Js('Jet'), Js('Joy'), Js('Karma'), Js('Lagoon'), Js('Lemon'), Js('Leopard'), Js('Life'), Js('Lion'), Js('Lioness'), Js('Lucent'), Js('Lucky'), Js('Maple'), Js('Marble'), Js('Mars'), Js('Marsh'), Js('Maze'), Js('Mermaid'), Js('Micro'), Js('Moon'), Js('Motion'), Js('Mountain'), Js('Nemo'), Js('Night'), Js('Nimble'), Js('Nymph'), Js('Oak'), Js('Ocean'), Js('Omega'), Js('Owl'), Js('Oyster'), Js('Peach'), Js('Pearl'), Js('Petal'), Js('Phantomn'), Js('Phoenix'), Js('Pink'), Js('Pinnacle'), Js('Pixel'), Js('Pixy'), Js('Prime'), Js('Purple'), Js('Quad'), Js('Raven'), Js('Red'), Js('Rhino'), Js('Riddle'), Js('Ridge'), Js('River'), Js('Robin'), Js('Root'), Js('Rose'), Js('Sail'), Js('Shade'), Js('Shadow'), Js('Sign'), Js('Signal'), Js('Silver'), Js('Smart'), Js('Smile'), Js('Soul'), Js('Sphere'), Js('Spider'), Js('Spike'), Js('Spirit'), Js('Sprite'), Js('Squid'), Js('Star'), Js('Storm'), Js('Sun'), Js('Thunder'), Js('Tiger'), Js('Timber'), Js('Tulip'), Js('Twilight'), Js('Typhoon'), Js('Vine'), Js('Void'), Js('Vortex'), Js('Wave'), Js('Web'), Js('Wizard'), Js('Wolf'), Js('Wonder'), Js('Wood'), Js('World'), Js('Yellow'), Js('Yew'), Js('Zeus')]))
var.put('names5', Js([Js('aid'), Js('air'), Js('bank'), Js('bar'), Js('beat'), Js('bit'), Js('bite'), Js('books'), Js('bridge'), Js('cast'), Js('cloud'), Js('coms'), Js('dale'), Js('dew'), Js('dream'), Js('ex'), Js('fly'), Js('force'), Js('fruit'), Js('gate'), Js('gold'), Js('head'), Js('hive'), Js('house'), Js('hut'), Js('king'), Js('land'), Js('life'), Js('light'), Js('man'), Js('mart'), Js('master'), Js('media'), Js('mobile'), Js('nite'), Js('paw'), Js('phone'), Js('point'), Js('poly'), Js('rover'), Js('scape'), Js('search'), Js('shack'), Js('shade'), Js('shadow'), Js('shine'), Js('show'), Js('space'), Js('star'), Js('stone'), Js('stones'), Js('sun'), Js('sys'), Js('tales'), Js('techs'), Js('time'), Js('tronics'), Js('tube'), Js('walk'), Js('ware'), Js('wares'), Js('water'), Js('way'), Js('ways'), Js('well'), Js('wheels'), Js('wood'), Js('works'), Js('world'), Js('worth')]))
pass
pass


# Add lib to the module scope
businessNames = var.to_python()