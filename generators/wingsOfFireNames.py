__all__ = ['wingsOfFireNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(14.0)):
        try:
            if (var.get('i')<Js(2.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', var.get('nm2').get(var.get('rnd')))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        if (var.get('rnd')<Js(60.0)):
                            var.put('names', var.get('nm3').get(var.get('rnd')))
                        else:
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                            var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                            var.put('names', var.get('nm5').get(var.get('rnd')))
                        else:
                            if (var.get('i')<Js(10.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                                var.put('names', var.get('nm6').get(var.get('rnd')))
                            else:
                                if (var.get('i')<Js(12.0)):
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                                    var.put('names', var.get('nm7').get(var.get('rnd')))
                                else:
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                                    var.put('names', var.get('nm8').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Anorak'), Js('Avalanche'), Js('Beret'), Js('Bleak'), Js('Blizz'), Js('Blizzard'), Js('Borean'), Js('Brumal'), Js('Calve'), Js('Casaba'), Js('Chill'), Js('Chinook'), Js('Clinch'), Js('Crymodinia'), Js('Cryo'), Js('Crystal'), Js('Diamond'), Js('Draft'), Js('Eranthis'), Js('Ermine'), Js('Flake'), Js('Fleece'), Js('Floe'), Js('Flurry'), Js('Frappe'), Js('Frigid'), Js('Frigor'), Js('Frost'), Js('Glacial'), Js('Hailstone'), Js('Halcyon'), Js('Hiemal'), Js('Hiems'), Js('Hoar'), Js('Humboldt'), Js('Hummock'), Js('Hyemal'), Js('Hyemate'), Js('Icy'), Js('Igloo'), Js('Luge'), Js('Melt'), Js('Miniver'), Js('Mistral'), Js('Neige'), Js('Nippy'), Js('Nivial'), Js('Parka'), Js('Perhiemate'), Js('Polar'), Js('Quilt'), Js('Rime'), Js('Serac'), Js('Sherbet'), Js('Shiver'), Js('Skate'), Js('Ski'), Js('Sledge'), Js('Sleet'), Js('Slide'), Js('Slush'), Js('Snap'), Js('Solstice'), Js('Sorbet'), Js('Stale'), Js('Thaw'), Js('Thaws'), Js('Toboggan'), Js('Uncia'), Js('Woolens')]))
var.put('nm2', Js([Js('Amber'), Js('Aroid'), Js('Auburn'), Js('Belute'), Js('Bemire'), Js('Bitternut'), Js('Bog'), Js('Bogmat'), Js('Bonobo'), Js('Calamus'), Js('Cienaga'), Js('Daub'), Js('Deluge'), Js('Dirt'), Js('Draggle'), Js('Drench'), Js('Dun'), Js('Everglade'), Js('Fawn'), Js('Fen'), Js('Flood'), Js('Flow'), Js('Gumbo'), Js('Hazel'), Js('Iva'), Js('Jarble'), Js('Khaki'), Js('Lily'), Js('Lutose'), Js('Mangrove'), Js('Mareis'), Js('Maremma'), Js('Miasma'), Js('Mire'), Js('Morass'), Js('Muck'), Js('Muddle'), Js('Myrtle'), Js('Ooze'), Js('Paludicole'), Js('Paludine'), Js('Papyrus'), Js('Parnassia'), Js('Pocosin'), Js('Puddle'), Js('Puttock'), Js('Quag'), Js('Quaggy'), Js('Recurvine'), Js('Rush'), Js('Russet'), Js('Sabbatia'), Js('Sable'), Js('Salse'), Js('Saute'), Js('Sceliphron'), Js('Sedge'), Js('Sediment'), Js('Shale'), Js('Sienna'), Js('Sleech'), Js('Sleetch'), Js('Slime'), Js('Slit'), Js('Slog'), Js('Slop'), Js('Slosh'), Js('Slough'), Js('Sludge'), Js('Slurry'), Js('Swang'), Js('Tawny'), Js('Umber'), Js('Wallow')]))
var.put('nm3', Js([Js('Annihilation'), Js('Carnage'), Js('Massacre'), Js('Destruction'), Js('Extinction'), Js('Ruin'), Js('Elimination'), Js('Abolition'), Js('Bane'), Js('Havoc'), Js('Fury'), Js('Rage'), Js('Ravage'), Js('Wreckage'), Js('Crash'), Js('Undoing'), Js('Extermination'), Js('Demolition'), Js('Revenge'), Js('Retribution'), Js('Wrath'), Js('Ire'), Js('Storm'), Js('Temper'), Js('Frenzy'), Js('Furor'), Js('Mania'), Js('Madness'), Js('Violence'), Js('Bluster'), Js('Hysteria'), Js('Bold'), Js('Confidence'), Js('Aweless'), Js('Gritty'), Js('Sanguine'), Js('Valiant'), Js('Wit'), Js('Foresight'), Js('Savvy'), Js('Prudence'), Js('Poise'), Js('Sapience'), Js('Insight'), Js('Judgment'), Js('Intuition'), Js('Genius'), Js('Sanity'), Js('Insanity'), Js('Chaos'), Js('Mayhem'), Js('Plunder'), Js('Wreck'), Js('Waste'), Js('Calamity'), Js('Cataclysm'), Js('Catastrophe'), Js('Confusion'), Js('Devestation'), Js('Desolation'), Js('Alder'), Js('Arrow'), Js('Battle'), Js('Big'), Js('Blaze'), Js('Bone'), Js('Boulder'), Js('Bright'), Js('Bull'), Js('Burn'), Js('Burning'), Js('Cloud'), Js('Dark'), Js('Dawn'), Js('Death'), Js('Doom'), Js('Dread'), Js('Dream'), Js('Dull'), Js('Dusk'), Js('Elder'), Js('Far'), Js('Fate'), Js('Fear'), Js('Fierce'), Js('Fire'), Js('Flame'), Js('Fury'), Js('Ghost'), Js('Gloom'), Js('Glow'), Js('Great'), Js('Grim'), Js('Hallow'), Js('Hollow'), Js('Hypno'), Js('Iron'), Js('Light'), Js('Little'), Js('Marble'), Js('Master'), Js('Mighty'), Js('Mind'), Js('Moon'), Js('Night'), Js('Phantom'), Js('Power'), Js('Prey'), Js('Rage'), Js('Razor'), Js('Rumble'), Js('Shade'), Js('Shadow'), Js('Shiver'), Js('Silver'), Js('Steel'), Js('Stone'), Js('Storm'), Js('Stout'), Js('Strong'), Js('Sun'), Js('Swift'), Js('Terror'), Js('Thunder'), Js('Whirl'), Js('Wild')]))
var.put('nm4', Js([Js('back'), Js('beast'), Js('belly'), Js('brand'), Js('breaker'), Js('breath'), Js('bringer'), Js('brow'), Js('claw'), Js('claws'), Js('cutter'), Js('eye'), Js('eyes'), Js('fang'), Js('fangs'), Js('flayer'), Js('flight'), Js('fly'), Js('forge'), Js('forger'), Js('glide'), Js('grip'), Js('hunter'), Js('jaw'), Js('mind'), Js('mover'), Js('reader'), Js('ripper'), Js('roar'), Js('sight'), Js('speaker'), Js('striker'), Js('tail'), Js('teeth'), Js('tooth'), Js('watcher'), Js('wing'), Js('wings')]))
var.put('nm5', Js([Js('Acute'), Js('Alert'), Js('Amplitude'), Js('Argent'), Js('Astute'), Js('August'), Js('Beaming'), Js('Beautiful'), Js('Beauty'), Js('Blazing'), Js('Bold'), Js('Brilliant'), Js('Chic'), Js('Dainty'), Js('Dapper'), Js('Daring'), Js('Dazzle'), Js('Dazzling'), Js('Delicate'), Js('Dignity'), Js('Elegant'), Js('Elevation'), Js('Eminence'), Js('Ethereal'), Js('Exalted'), Js('Excellent'), Js('Flashing'), Js('Flawless'), Js('Fulgent'), Js('Gallant'), Js('Glaring'), Js('Glittering'), Js('Glorious'), Js('Glory'), Js('Gorgeous'), Js('Grand'), Js('Grandeur'), Js('Grandiose'), Js('Imposing'), Js('Jaunty'), Js('Jolly'), Js('Keen'), Js('Lambent'), Js('Lavish'), Js('Light'), Js('Lively'), Js('Luster'), Js('Lustrous'), Js('Luxurious'), Js('Magnefic'), Js('Magnificence'), Js('Majestic'), Js('Majesty'), Js('Merry'), Js('Might'), Js('Nobility'), Js('Noble'), Js('Opulence'), Js('Opulent'), Js('Plucky'), Js('Precious'), Js('Quick'), Js('Radiance'), Js('Radiant'), Js('Rare'), Js('Refined'), Js('Renown'), Js('Royal'), Js('Sanguine'), Js('Sharp'), Js('Smare'), Js('Smart'), Js('Smashing'), Js('Smooth'), Js('Sparkling'), Js('Spectacle'), Js('Splendid'), Js('Splendor'), Js('Striking'), Js('Suave'), Js('Sublime'), Js('Sublimity'), Js('Superb'), Js('Swank'), Js('Sway'), Js('Swish'), Js('Vivid'), Js('Whiz'), Js('Wonderful'), Js('Aerosol'), Js('Aqua'), Js('Basin'), Js('Berain'), Js('Bilge'), Js('Billow'), Js('Blirt'), Js('Cirrus'), Js('Cloudburst'), Js('Coma'), Js('Cumulus'), Js('Dew'), Js('Dowse'), Js('Drench'), Js('Drizzle'), Js('Droplet'), Js('Flush'), Js('Fume'), Js('Gale'), Js('Hail'), Js('Halo'), Js('Hula'), Js('Hydra'), Js('Hydro'), Js('Hyetal'), Js('Miasma'), Js('Misle'), Js('Mist'), Js('Mizzle'), Js('Mottle'), Js('Naga'), Js('Naiad'), Js('Nebula'), Js('Nimbus'), Js('Nubia'), Js('Nymph'), Js('Ombro'), Js('Parjanya'), Js('Patter'), Js('Pelter'), Js('Petrichor'), Js('Pluvial'), Js('Pour'), Js('Reyn'), Js('Saman'), Js('Selva'), Js('Serein'), Js('Sluice'), Js('Smither'), Js('Soak'), Js('Sprinkle'), Js('Storm'), Js('Stratus'), Js('Tempest'), Js('Torrent'), Js('Zamang')]))
var.put('nm6', Js([Js('Arenose'), Js('Arenulous'), Js('Atacama'), Js('Bulwark'), Js('Bunker'), Js('Burrow'), Js('Cabana'), Js('Caftan'), Js('Caracal'), Js('Cerastes'), Js('Chilopsis'), Js('Compo'), Js('Coville'), Js('Creosote'), Js('Dene'), Js('Ditch'), Js('Djanet'), Js('Draggle'), Js('Drifter'), Js('Dust'), Js('Eremic'), Js('Firma'), Js('Gerbil'), Js('Gila'), Js('Gobi'), Js('Gopher'), Js('Gravel'), Js('Grind'), Js('Grit'), Js('Gypsum'), Js('Hediondilla'), Js('Hemen'), Js('Hornel'), Js('Iguana'), Js('Jerboa'), Js('Kalahari'), Js('Larrea'), Js('Launce'), Js('Lichanura'), Js('Lido'), Js('Maravilla'), Js('Maroon'), Js('Marram'), Js('Mohave'), Js('Mojava'), Js('Mole'), Js('Moloch'), Js('Namib'), Js('Negev'), Js('Nubian'), Js('Patch'), Js('Pebble'), Js('Plage'), Js('Prime'), Js('Psammoma'), Js('Sahara'), Js('Shore'), Js('Simoom'), Js('Sinai'), Js('Sirocco'), Js('Soil'), Js('Strond'), Js('Tan'), Js('Tannest'), Js('Terra'), Js('Terrain'), Js('Tombolo'), Js('Xerophilous')]))
var.put('nm7', Js([Js('Abyss'), Js('Actinia'), Js('Actinian'), Js('Adriatic'), Js('Aegean'), Js('Agonus'), Js('Archipelago'), Js('Ascidian'), Js('Auk'), Js('Baltic'), Js('Bass'), Js('Bathypelagic'), Js('Batture'), Js('Bay'), Js('Beaufort'), Js('Benthos'), Js('Billow'), Js('Bismarck'), Js('Bream'), Js('Brine'), Js('Bromine'), Js('Bryozoan'), Js('Buccaneer'), Js('Caretta'), Js('Caribbean'), Js('Clangula'), Js('Coast'), Js('Conger'), Js('Corsair'), Js('Cove'), Js('Davy'), Js('Dive'), Js('Echinoidea'), Js('Echinus'), Js('Estuary'), Js('Expanse'), Js('Firth'), Js('Fugu'), Js('Fulmar'), Js('Grouper'), Js('Gulf'), Js('Holothurian'), Js('Hydro'), Js('Hydrophid'), Js('Inlet'), Js('Leviathan'), Js('Main'), Js('Manatee'), Js('Marine'), Js('Maritime'), Js('Marmara'), Js('Marmora'), Js('Mew'), Js('Naumachy'), Js('Nautical'), Js('Nereid'), Js('Nereus'), Js('Ocean'), Js('Pelagic'), Js('Peristedion'), Js('Petrel'), Js('Puffin'), Js('Recess'), Js('River'), Js('Rosmarine'), Js('Samphire'), Js('Scoter'), Js('Spindrift'), Js('Squid'), Js('Squill'), Js('Starfish'), Js('Submarine'), Js('Thatch'), Js('Thetis'), Js('Trepang'), Js('Triton'), Js('Ultramarine'), Js('Ulva'), Js('Urchin')]))
var.put('nm8', Js([Js('Above'), Js('Aestival'), Js('Aether'), Js('Air'), Js('Amber'), Js('Andromeda'), Js('Anu'), Js('Aquila'), Js('Ara'), Js('Aries'), Js('Atrium'), Js('Aurora'), Js('Azure'), Js('Azured'), Js('Borealis'), Js('Canicula'), Js('Canopus'), Js('Canopy'), Js('Cassiopeia'), Js('Celeste'), Js('Celestial'), Js('Cepheus'), Js('Cerulean'), Js('Cerulific'), Js('Cloud'), Js('Comet'), Js('Constellation'), Js('Cyaneous'), Js('Cyanite'), Js('Draco'), Js('Dyaus'), Js('Either'), Js('Empyreal'), Js('Empyrean'), Js('Ensky'), Js('Expanse'), Js('Gemini'), Js('Heaven'), Js('Hemisphere'), Js('Hypaethral'), Js('Iceblink'), Js('Ionosphere'), Js('Lepus'), Js('Lift'), Js('Lyra'), Js('Meridian'), Js('Meteor'), Js('Nebula'), Js('Nimbus'), Js('Orion'), Js('Pitch'), Js('Rainbow'), Js('Sapphire'), Js('Serein'), Js('Sirius'), Js('Skyey'), Js('Skyward'), Js('Sphere'), Js('Steward'), Js('Stratus'), Js('Supernal'), Js('Taurus'), Js('Toss'), Js('Twilight'), Js('Vault'), Js('Vesper'), Js('Violet'), Js('Welkin'), Js('Yonder'), Js('Zenith'), Js('Zodiac')]))
pass
pass


# Add lib to the module scope
wingsOfFireNames = var.to_python()