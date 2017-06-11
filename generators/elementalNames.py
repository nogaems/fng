__all__ = ['elementalNames']

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
    var.put('nm1', Js([Js('Flash (Lightning)'), Js('Spark (Lightning)'), Js('Bolt (Lightning)'), Js('Ramman (Lightning)'), Js('Baraq (Lightning)'), Js('Storm (Lightning)'), Js('Elec (Lightning)'), Js('Lec (Lightning)'), Js('Lectric (Lightning)'), Js('Volt (Lightning)'), Js('Tes (Lightning)'), Js('Tesla (Lightning)'), Js('Thun (Lightning)'), Js('Fulg (Lightning)'), Js('Fulgu (Lightning)'), Js('Gurate (Lightning)'), Js('Astra (Lightning)'), Js('Bron (Lightning)'), Js('Bronto (Lightning)'), Js('Cerau (Lightning)'), Js('Ceraun (Lightning)'), Js('Cerauno (Lightning)'), Js('Amp (Lightning)'), Js('Fara (Lightning)'), Js('Farad (Lightning)'), Js('Watt (Lightning)'), Js('Galv (Lightning)'), Js('Galva (Lightning)'), Js('Galvan (Lightning)'), Js('Ohm (Lightning)'), Js('Ohme (Lightning)'), Js('Volta (Lightning)'), Js('Sanguine (Blood)'), Js('Sanguinus (Blood)'), Js('Sange (Blood)'), Js('Sanguin (Blood)'), Js('Clot (Blood)'), Js('Cruor (Blood)'), Js('Plasma (Blood)'), Js('Gore (Blood)'), Js('Serum (Blood)'), Js('Vein (Blood)'), Js('Aorta (Blood)'), Js('Aort (Blood)'), Js('Plasm (Blood)'), Js('Arte (Blood)'), Js('Arter (Blood)'), Js('Anemis (Blood)'), Js('Anemia (Blood)'), Js('Anaemia (Blood)'), Js('Anae (Blood)'), Js('Anaemis (Blood)'), Js('Leuko (Blood)'), Js('Kocyte (Blood)'), Js('Leukos (Blood)'), Js('Hema (Blood)'), Js('Hemal (Blood)'), Js('Hemall (Blood)'), Js('Purpu (Blood)'), Js('Purpura (Blood)'), Js('Purpur (Blood)'), Js('Throm (Blood)'), Js('Thrombus (Blood)'), Js('Thromb (Blood)'), Js('Acidosis (Blood)'), Js('Acidos (Blood)'), Js('Abrus (Magic)'), Js('Adum (Shadow)'), Js('Aeon (Time)'), Js('Aeos (Time)'), Js('Aeranas (Air)'), Js('Aere (Air)'), Js('Aeria (Air)'), Js('Aeris (Air)'), Js('Aeros (Air)'), Js('Aetas (Time)'), Js('Aevum (Time)'), Js('Aevus (Time)'), Js('Afa (Earth)'), Js('Alchos (Magic)'), Js('Allure (Magic)'), Js('Amaranthinos (Time)'), Js('Animax (Life)'), Js('Animos (Life)'), Js('Animus (Life)'), Js('Anomalis (Magic)'), Js('Anomus (Magic)'), Js('Aqualis (Water)'), Js('Aqualon (Water)'), Js('Aquanis (Water)'), Js('Aquara (Water)'), Js('Aquifis (Water)'), Js('Aquira (Water)'), Js('Aquiris (Water)'), Js('Aquis (Water)'), Js('Arcanimus (Magic)'), Js('Arcanis (Magic)'), Js('Arcano (Magic)'), Js('Aros (Air)'), Js('Ash (Fire)'), Js('Ashe (Fire)'), Js('Atax (Shadow)'), Js('Atmos (Air)'), Js('Augur (Magic)'), Js('Augus (Magic)'), Js('Aura (Light)'), Js('Auris (Light)'), Js('Aurora (Light)'), Js('Avala (Ice/Snow)'), Js('Avalan (Earth)'), Js('Avalan (Ice/Snow)'), Js('Avian (Air)'), Js('Avis (Air)'), Js('Azura (Air)'), Js('Azure (Water)'), Js('Azuris (Water)'), Js('Baecos (Light)'), Js('Bane (Shadow)'), Js('Basalt (Earth)'), Js('Basselt (Earth)'), Js('Bayle (Fire)'), Js('Blaize (Fire)'), Js('Blaze (Fire)'), Js('Blizz (Ice/Snow)'), Js('Blyze (Fire)'), Js('Boulder (Earth)'), Js('Boyle (Fire)'), Js('Boyle (Water)'), Js('Breyze (Air)'), Js('Brine (Water)'), Js('Brun (Fire)'), Js('Bulder (Earth)'), Js('Caedos (Death)'), Js('Caenum (Water)'), Js('Calamis (Shadow)'), Js('Calas (Shadow)'), Js('Carbonne (Earth)'), Js('Cartos (Magic)'), Js('Celes (Air)'), Js('Cendis (Fire)'), Js('Centuris (Time)'), Js('Centuros (Time)'), Js('Cerulea (Air)'), Js('Cerulis (Air)'), Js('Cerulle (Air)'), Js('Chemos (Magic)'), Js('Chillis (Ice/Snow)'), Js('Chinook (Air)'), Js('Chrono (Time)'), Js('Chronos (Time)'), Js('Cimmeris (Shadow)'), Js('Circos (Air)'), Js('Claire (Fire)'), Js('Clarity (Water)'), Js('Claye (Earth)'), Js('Clipse (Shadow)'), Js('Clode (Air)'), Js('Cloud (Air)'), Js('Coale (Fire)'), Js('Cobble (Earth)'), Js('Cobbles (Earth)'), Js('Cole (Fire)'), Js('Conjis (Magic)'), Js('Conjus (Magic)'), Js('Conquitus (Death)'), Js('Continos (Time)'), Js('Core (Earth)'), Js('Corrus (Shadow)'), Js('Crayg (Earth)'), Js('Cryo (Ice/Snow)'), Js('Cryogen (Ice/Snow)'), Js('Crystal (Ice/Snow)'), Js('Cyclonis (Air)'), Js('Cyclonius (Air)'), Js('Cyclos (Air)'), Js('Cyclos (Life)'), Js('Dabrus (Magic)'), Js('Decess (Death)'), Js('Decessus (Death)'), Js('Demis (Death)'), Js('Dew (Water)'), Js('Diables (Shadow)'), Js('Diablos (Magic)'), Js('Diabolos (Magic)'), Js('Disaris (Shadow)'), Js('Disas (Shadow)'), Js('Divinos (Magic)'), Js('Divis (Magic)'), Js('Divos (Magic)'), Js('Drift (Ice/Snow)'), Js('Dune (Earth)'), Js('Dusk (Shadow)'), Js('Duster (Earth)'), Js('Eclipe (Shadow)'), Js('Elan (Life)'), Js('Ember (Fire)'), Js('Empearal (Air)'), Js('Enigmus (Magic)'), Js('Entros (Shadow)'), Js('Epoch (Time)'), Js('Epos (Time)'), Js('Eras (Time)'), Js('Eros (Life)'), Js('Essos (Life)'), Js('Eternos (Time)'), Js('Exalos (Air)'), Js('Exanimus (Death)'), Js('Exos (Death)'), Js('Exos (Magic)'), Js('Exto (Life)'), Js('Extos (Life)'), Js('Fax (Light)'), Js('Fenix (Fire)'), Js('Fernis (Death)'), Js('Fernis (Fire)'), Js('Ferno (Fire)'), Js('Fervis (Fire)'), Js('Finis (Death)'), Js('Firmis (Earth)'), Js('Firn (Ice/Snow)'), Js('Flaik (Ice/Snow)'), Js('Flair (Fire)'), Js('Flarion (Fire)'), Js('Flaris (Fire)'), Js('Flashfire (Fire)'), Js('Flayke (Ice/Snow)'), Js('Flo (Ice/Snow)'), Js('Flo (Water)'), Js('Flurris (Air)'), Js('Flurris (Ice/Snow)'), Js('Fluvis (Water)'), Js('Flux (Magic)'), Js('Frose (Ice/Snow)'), Js('Fross (Ice/Snow)'), Js('Fuegis (Fire)'), Js('Fuego (Fire)'), Js('Fumus (Fire)'), Js('Funis (Death)'), Js('Funus (Death)'), Js('Fusilis (Fire)'), Js('Fye (Fire)'), Js('Gale (Air)'), Js('Gayle (Air)'), Js('Genis (Magic)'), Js('Genos (Magic)'), Js('Geo (Earth)'), Js('Geod (Earth)'), Js('Geysis (Water)'), Js('Glace (Ice/Snow)'), Js('Glacia (Water)'), Js('Glacis (Ice/Snow)'), Js('Glacis (Water)'), Js('Glacius (Water)'), Js('Glamos (Magic)'), Js('Glayze (Ice/Snow)'), Js('Glimmes (Light)'), Js('Gliss (Ice/Snow)'), Js('Glo (Fire)'), Js('Gloom (Shadow)'), Js('Glum (Shadow)'), Js('Granit (Earth)'), Js('Granius (Earth)'), Js('Grant (Earth)'), Js('Graund (Earth)'), Js('Grav (Earth)'), Js('Grime (Earth)'), Js('Grimes (Earth)'), Js('Grine (Earth)'), Js('Gritt (Earth)'), Js('Halitus (Air)'), Js('Halo (Air)'), Js('Halos (Air)'), Js('Hayle (Ice/Snow)'), Js('Hayze (Shadow)'), Js('Heinios (Shadow)'), Js('Hex (Magic)'), Js('Hocus (Magic)'), Js('Hora (Time)'), Js('Horas (Time)'), Js('Horos (Magic)'), Js('Hurican (Air)'), Js('Huricus (Air)'), Js('Hydran (Water)'), Js('Hydris (Water)'), Js('Hydrius (Water)'), Js('Hydrox (Water)'), Js('Iciclis (Ice/Snow)'), Js('Iglis (Ice/Snow)'), Js('Igneos (Fire)'), Js('Igneous (Fire)'), Js('Ignis (Fire)'), Js('Ignit (Fire)'), Js('Illume (Light)'), Js('Illumine (Light)'), Js('Illus (Magic)'), Js('Imperos (Air)'), Js('Imum (Death)'), Js('Inanis (Death)'), Js('Inanos (Death)'), Js('Incantus (Magic)'), Js('Incedis (Fire)'), Js('Incendius (Fire)'), Js('Infernus (Fire)'), Js('Infinis (Time)'), Js('Iniq (Shadow)'), Js('Interis (Time)'), Js('Jinx (Magic)'), Js('Juju (Magic)'), Js('Kindle (Fire)'), Js('Kindra (Fire)'), Js('Lambence (Light)'), Js('Lanche (Ice/Snow)'), Js('Lavar (Fire)'), Js('Lavis (Fire)'), Js('Letos (Death)'), Js('Libitus (Death)'), Js('Limu (Water)'), Js('Limus (Water)'), Js('Lios (Earth)'), Js('Liquaxis (Water)'), Js('Liquire (Water)'), Js('Liquis (Water)'), Js('Locus (Time)'), Js('Luceras (Light)'), Js('Lucernas (Light)'), Js('Lucis (Light)'), Js('Lucus (Light)'), Js('Lumen (Light)'), Js('Lumes (Life)'), Js('Lumina (Light)'), Js('Luminus (Light)'), Js('Luminus (Magic)'), Js('Lumis (Light)'), Js('Lumus (Light)'), Js('Lumus (Magic)'), Js('Lunos (Magic)'), Js('Lussios (Magic)'), Js('Lustris (Light)'), Js('Lustrous (Light)'), Js('Lutu (Earth)'), Js('Lutum (Earth)'), Js('Lux (Light)'), Js('Lychnus (Light)'), Js('Magmis (Fire)'), Js('Magnos (Magic)'), Js('Malefis (Shadow)'), Js('Malignus (Shadow)'), Js('Malis (Shadow)'), Js('Malos (Shadow)'), Js('Malov (Shadow)'), Js('Manes (Death)'), Js('Manos (Magic)'), Js('Marble (Earth)'), Js('Melte (Ice/Snow)'), Js('Mementos (Time)'), Js('Mentos (Time)'), Js('Millenis (Time)'), Js('Miseris (Shadow)'), Js('Mistral (Air)'), Js('Mojo (Magic)'), Js('Monse (Water)'), Js('Monsoo (Water)'), Js('Mora (Time)'), Js('Mors (Death)'), Js('Mortis (Death)'), Js('Mortos (Life)'), Js('Mortus (Death)'), Js('Murmus (Air)'), Js('Myalis (Magic)'), Js('Myrios (Time)'), Js('Narchis (Shadow)'), Js('Narcos (Magic)'), Js('Neco (Death)'), Js('Necos (Death)'), Js('Necron (Magic)'), Js('Necros (Death)'), Js('Necros (Magic)'), Js('Nefaris (Shadow)'), Js('Neige (Ice/Snow)'), Js('Neptis (Water)'), Js('Neptulus (Water)'), Js('Neptune (Water)'), Js('Nex (Death)'), Js('Nexus (Death)'), Js('Nighe (Shadow)'), Js('Nite (Shadow)'), Js('Nova (Fire)'), Js('Novis (Fire)'), Js('Nox (Death)'), Js('Noxis (Death)'), Js('Obcasus (Death)'), Js('Obitus (Death)'), Js('Oblis (Death)'), Js('Obscuras (Shadow)'), Js('Ocea (Water)'), Js('Ocus (Magic)'), Js('Orcus (Death)'), Js('Oria (Earth)'), Js('Oris (Earth)'), Js('Oxyn (Air)'), Js('Ozone (Air)'), Js('Parados (Magic)'), Js('Pebble (Earth)'), Js('Penum (Shadow)'), Js('Peros (Death)'), Js('Perpetos (Time)'), Js('Pitch (Shadow)'), Js('Pocus (Magic)'), Js('Poole (Water)'), Js('Precipe (Water)'), Js('Precipise (Water)'), Js('Prophis (Magic)'), Js('Puddles (Water)'), Js('Puds (Water)'), Js('Pulvi (Earth)'), Js('Pulvis (Earth)'), Js('Purity (Water)'), Js('Pyre (Fire)'), Js('Pyro (Fire)'), Js('Pyroc (Fire)'), Js('Quarris (Earth)'), Js('Quary (Earth)'), Js('Ragnis (Fire)'), Js('Rane (Water)'), Js('Rayne (Water)'), Js('Retaw (Water)'), Js('River (Water)'), Js('Rivule (Water)'), Js('Roc (Earth)'), Js('Rune (Magic)'), Js('Saeclum (Time)'), Js('Saeclus (Time)'), Js('Saline (Water)'), Js('Salis (Water)'), Js('Salvus (Life)'), Js('Scald (Fire)'), Js('Scaldor (Fire)'), Js('Scaldris (Fire)'), Js('Scorch (Fire)'), Js('Scorchis (Fire)'), Js('Scuris (Shadow)'), Js('Sear (Fire)'), Js('Secos (Time)'), Js('Senso (Life)'), Js('Sensos (Life)'), Js('Sentos (Life)'), Js('Septos (Magic)'), Js('Shayde (Shadow)'), Js('Shaye (Shadow)'), Js('Sigmis (Fire)'), Js('Siles (Death)'), Js('Sizzle (Fire)'), Js('Skye (Air)'), Js('Slab (Earth)'), Js('Slait (Earth)'), Js('Slate (Earth)'), Js('Sleat (Ice/Snow)'), Js('Sleigh (Magic)'), Js('Smo (Fire)'), Js('Smog (Shadow)'), Js('Smoldris (Fire)'), Js('Smulder (Fire)'), Js('Snift (Ice/Snow)'), Js('Sod (Earth)'), Js('Soile (Earth)'), Js('Sol (Light)'), Js('Solaris (Light)'), Js('Solas (Light)'), Js('Soleis (Light)'), Js('Sonas (Air)'), Js('Sonis (Air)'), Js('Sono (Air)'), Js('Sonus (Air)'), Js('Soots (Fire)'), Js('Soros (Shadow)'), Js('Spark (Fire)'), Js('Spirans (Life)'), Js('Spiras (Life)'), Js('Spiris (Life)'), Js('Spiritus (Life)'), Js('Spirus (Life)'), Js('Spyte (Shadow)'), Js('Squalos (Water)'), Js('Stamen (Life)'), Js('Stamos (Life)'), Js('Stowne (Earth)'), Js('Stratos (Air)'), Js('Sum (Life)'), Js('Sumus (Life)'), Js('Talis (Magic)'), Js('Tempes (Time)'), Js('Tempest (Water)'), Js('Tempeste (Air)'), Js('Tempestus (Water)'), Js('Tempos (Time)'), Js('Tempris (Fire)'), Js('Tempus (Time)'), Js('Tera (Earth)'), Js('Terberis (Earth)'), Js('Terbis (Earth)'), Js('Terbius (Earth)'), Js('Terminos (Time)'), Js('Terminus (Time)'), Js('Terra (Earth)'), Js('Terrane (Earth)'), Js('Terros (Earth)'), Js('Thaumus (Magic)'), Js('Thawe (Ice/Snow)'), Js('Thera (Earth)'), Js('Theran (Earth)'), Js('Therris (Earth)'), Js('Theuros (Magic)'), Js('Tinder (Fire)'), Js('Tropos (Air)'), Js('Tsuna (Water)'), Js('Tsunis (Water)'), Js('Tumul (Air)'), Js('Tumulus (Air)'), Js('Turf (Earth)'), Js('Turve (Earth)'), Js('Twileigh (Shadow)'), Js('Typhis (Water)'), Js('Typhos (Water)'), Js('Umber (Earth)'), Js('Umbris (Shadow)'), Js('Umbrus (Shadow)'), Js('Valanche (Earth)'), Js('Vape (Water)'), Js('Vapora (Water)'), Js('Vapore (Water)'), Js('Vapos (Water)'), Js('Veilios (Shadow)'), Js('Ventis (Air)'), Js('Vexus (Magic)'), Js('Vigor (Life)'), Js('Vigos (Life)'), Js('Vilis (Shadow)'), Js('Vitae (Life)'), Js('Vitalis (Life)'), Js('Vitalos (Life)'), Js('Vitalus (Life)'), Js('Vitos (Life)'), Js('Vividus (Life)'), Js('Vivus (Life)'), Js('Volance (Air)'), Js('Volaris (Air)'), Js('Volcanis (Fire)'), Js('Vox (Air)'), Js('Voxis (Air)'), Js('Vudos (Magic)'), Js('Whiff (Air)'), Js('Xygen (Air)'), Js('Yce (Ice/Snow)'), Js('Zephyr (Air)'), Js('Zephys (Air)')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
elementalNames = var.to_python()