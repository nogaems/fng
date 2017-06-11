__all__ = ['townDescriptions']

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
    var.registers(['names4', 'random15', 'names38', 'names5', 'names2', 'name', 'name7', 'names41', 'names21', 'random5', 'name3', 'name6', 'random40', 'random11', 'names20', 'random21', 'name2', 'random10', 'names14', 'names11', 'names18', 'random20', 'random8', 'names17', 'name4', 'random3', 'random17', 'random6', 'names9', 'random38', 'random39', 'names8', 'names3', 'names1', 'random9', 'random18', 'random4', 'random7', 'result', 'random2', 'random12', 'names6', 'names10', 'random6b', 'random19', 'random14', 'random1', 'random16', 'name5', 'names19', 'random13', 'random41', 'names7'])
    var.put('names1', Js([Js('Based'), Js('Built'), Js('Cast'), Js('Constructed'), Js('Designed'), Js('Engineered'), Js('Erected'), Js('Established'), Js('Fabricated'), Js('Forged'), Js('Formed'), Js('Found'), Js('Located'), Js('Positioned'), Js('Raised'), Js('Rooted'), Js('Set'), Js('Settled'), Js('Situated'), Js('Stationed')]))
    var.put('names2', Js([Js('on the Northern side of'), Js('on the Southern side of'), Js('on the Western side of'), Js('on the Eastern side of'), Js('on the top of'), Js('on top of'), Js('on the peak of'), Js('on the base of'), Js('on the bottom of'), Js('on the right side of'), Js('on the left side of'), Js('on the light side of'), Js('on the dark side of'), Js('on the highest point of'), Js('on the lowest point of'), Js('above'), Js('behind'), Js('under'), Js('inside'), Js('around'), Js('beside'), Js('next to'), Js('in'), Js('on the end of')]))
    var.put('names3', Js([Js(' bluff'), Js(' canal'), Js(' canyon'), Js(' cave'), Js(' cavern'), Js(' cliff'), Js(' covert'), Js(' desert'), Js(' field'), Js(' forest'), Js(' geyser field'), Js(' glacier'), Js(' grotto'), Js(' grove'), Js(' hill'), Js('n island'), Js(' jungle'), Js(' lake'), Js(' lava stream'), Js(' mound'), Js(' mountain'), Js('n ocean'), Js(' peninsula'), Js(' river'), Js(' sea'), Js(' stream'), Js(' thicket'), Js(' tundra'), Js(' valley'), Js(' vulcano'), Js(' waterfall'), Js(' wetlands'), Js(' woodlands')]))
    var.put('names4', Js([Js('village'), Js('town'), Js('city'), Js('metropolis'), Js('hamlet'), Js('megalopolis'), Js('outpost'), Js('port'), Js('township'), Js('settlement'), Js('crossroad'), Js('burg')]))
    var.put('names5', Js([Js('Barnemouth'), Js('Paethsmouth'), Js('Pernrith'), Js('Perthlochry'), Js('Pitmerden'), Js('Coalfell'), Js('Cullfield'), Js('Darkwell'), Js('Deathfall'), Js('Doonatel'), Js('Dry Gulch'), Js('Easthaven'), Js('Ecrin'), Js('Erast'), Js('Far Water'), Js('Firebend'), Js("Fool's March"), Js('Frostford'), Js('Goldcrest'), Js('Goldenleaf'), Js('Greenflower'), Js("Garen's Well"), Js('Haran'), Js('Hillfar'), Js('Hogsfeet'), Js('Hollyhead'), Js('Hull'), Js('Hwen')]))
    var.put('names6', Js([Js('humans'), Js('elves'), Js('orcs'), Js('dwarves'), Js('fairies'), Js('trolls'), Js('vampires'), Js('werewolves'), Js('humans'), Js('humans'), Js('humans'), Js('night elves'), Js('blood elves'), Js('gnomes'), Js('goblins'), Js('high elves'), Js('wood elves'), Js('dark elves'), Js('halflings'), Js('giants'), Js('pirates'), Js('barbarians'), Js('vikings')]))
    var.put('names7', Js([Js('Agent'), Js('Baron'), Js('Captain'), Js('Chief'), Js('Colonel'), Js('Commander'), Js('Director'), Js('Duchess'), Js('Duke'), Js('Earl'), Js('General'), Js('Governor'), Js('Judge'), Js('Knight'), Js('Lady'), Js('Lord'), Js('Major'), Js('Marshal'), Js('Master'), Js('Mayor'), Js('Minister'), Js('Mr.'), Js('Mrs.'), Js('Ms.'), Js('Officer'), Js('Ruler'), Js('Sergeant'), Js('Supervisor'), Js('Warlord')]))
    var.put('names8', Js([Js('Adwell'), Js('Ady'), Js('Afton'), Js('Barnett'), Js('Barney'), Js('Barnfield'), Js('Chilson'), Js('Chilton'), Js('Cawthorn'), Js('Davenport'), Js('Davey'), Js('Dallin'), Js('Eustice'), Js('Eustis'), Js('Evatt'), Js('Falcon'), Js('Faley'), Js('Falkner'), Js('Geary'), Js('Gedman'), Js('Gedney'), Js('Hanshaw'), Js('Hansley'), Js('Hanson'), Js('Lamkin'), Js('Lamkins'), Js('Lamm'), Js('Lockridge'), Js('Locks'), Js('Lockwood'), Js('Masser'), Js('Massey'), Js('Massingale'), Js('Rosemond'), Js('Shepherd'), Js('Shepley'), Js('Wakeley'), Js('Wakelin')]))
    var.put('names9', Js([Js('magical properties'), Js('fertile soils'), Js('ancient histories'), Js('a cultural history'), Js('hidden secrets'), Js('healing properties'), Js('an abundance of minerals'), Js('a dark history'), Js('rare resources'), Js('precious gems'), Js('ancient burial grounds'), Js('old tombs'), Js('a broken, hidden library'), Js('an ancient water source'), Js('dark ruins'), Js('rare plants'), Js('medicinal plants'), Js('strong metal ores'), Js('natural defences'), Js('hidden tunnels'), Js('ambush positions'), Js('escape routes'), Js('an abundance of wildlife'), Js('ancient, lost technologies'), Js('a comfortable weather system'), Js('unique wildlife'), Js('spiritual significance'), Js('ancestral grounds'), Js('ancient, unexplained statues'), Js('body enhancing properties')]))
    var.put('names10', Js([Js('n advancing'), Js(' booming'), Js(' breaking'), Js(' damaged'), Js(' declining'), Js(' developing'), Js(' failing'), Js(' feeble'), Js(' flourishing'), Js(' growing'), Js(' healthy'), Js(' hurting'), Js('n improving'), Js(' mending'), Js(' poor'), Js(' progressing'), Js(' prospering'), Js(' prosperous'), Js(' thriving'), Js(' tormented'), Js(' troubled'), Js('n unhealthy'), Js(' wounded')]))
    var.put('names11', Js([Js('alchemy'), Js('animal breeding'), Js('animal training'), Js('armorsmithing'), Js('baking'), Js('beer brewing'), Js('blacksmithing'), Js('carpenting'), Js('cooking'), Js('crafting'), Js('engineering'), Js('farming'), Js('fishing'), Js('fletching'), Js('herbalism'), Js('hunting'), Js('jewelcrafting'), Js('leatherworking'), Js('medicine'), Js('mining'), Js('tailoring'), Js('thieving'), Js('trade'), Js('war'), Js('weaponsmithing'), Js('wine brewing'), Js('wood production'), Js('woodcrafting')]))
    var.put('names14', Js([Js('alchemy'), Js('rare animal breeding'), Js('rare animal training'), Js('advanced armorsmithing'), Js('refined baking'), Js('elaborate beer brewing techniques'), Js('elaborate blacksmithing'), Js('refined carpenting'), Js('sophisticated cooking'), Js('complex crafting'), Js('master engineering'), Js('rare crop farming'), Js('ocean fishing'), Js('intricate fletching techniques'), Js('rare herbalism'), Js('sustainable hunting'), Js('intricate jewelcrafting'), Js('gorgeous leatherworking'), Js('advanced medicine'), Js('prosperous mining'), Js('delicate tailoring'), Js('highly skilled thieving'), Js('prosperous trade'), Js('skilled in the art of war'), Js('weaponsmithing'), Js('ancient wine brewing techniques'), Js('rare wood production'), Js('delicate woodcrafting'), Js('a strong defence'), Js('skilled fighters'), Js('strong magicians'), Js('deadly archers')]))
    var.put('names17', Js([Js('gorgeous'), Js('beautiful'), Js('majestic'), Js('elegant'), Js('glorious'), Js('impressive'), Js('flamboyant'), Js('luxuriant'), Js('stunning'), Js('impressive'), Js('delightful'), Js('graceful'), Js('magnificent'), Js('imposing'), Js('sublime'), Js('grandiose'), Js('humble'), Js('crude'), Js('rough'), Js('mediocre'), Js('dull'), Js('plain'), Js('ordinary'), Js('hideous'), Js('gruesome'), Js('dreadful'), Js('macabre'), Js('ghastly'), Js('unattractive'), Js('unexciting'), Js('worn'), Js('mundane')]))
    var.put('names18', Js([Js('oak wood'), Js('maple wood'), Js('yew wood'), Js('cypress wood'), Js('pine wood'), Js('spruce  wood'), Js('redwood'), Js('ash wood'), Js('birch wood'), Js('blackwood'), Js('ebony wood'), Js('elm wood'), Js('ironwood'), Js('mahogany wood'), Js('silky oak wood'), Js('willow wood'), Js('bamboo'), Js('tatchet'), Js('shingle'), Js('slate tile'), Js('wheat straw'), Js('seagrass'), Js('ceramic tile'), Js('copper')]))
    var.put('names19', Js([Js('golden brick'), Js('red brick'), Js('redstone'), Js('granite'), Js('marble'), Js('limestone'), Js('sandstone'), Js('stone veneer'), Js('chiseled stone'), Js('oak wood'), Js('maple wood'), Js('yew wood'), Js('cypress wood'), Js('pine wood'), Js('spruce  wood'), Js('redwood'), Js('ash wood'), Js('birch wood'), Js('blackwood'), Js('ebony wood'), Js('elm wood'), Js('ironwood'), Js('mahogany wood'), Js('silky oak wood'), Js('willow wood'), Js('bamboo'), Js('tatchet'), Js('shingle'), Js('slate tile'), Js('wheat straw'), Js('seagrass'), Js('ceramic tile'), Js('copper'), Js('lavastone')]))
    var.put('names20', Js([Js('lucious gardens'), Js('enchanting wildlife'), Js('swarms of fireflies'), Js('babbling creeks'), Js('vibrant, rare trees'), Js('breathtaking waterfall'), Js('calm and quiet collection of ponds'), Js('frozen lakes'), Js('frozen waterfall'), Js('imposing glacier'), Js('ambient light of nearby lava streams'), Js('the native bird species'), Js('rainbow of different flowers'), Js('everclear night sky'), Js('huge, majestic geyser'), Js('silent mountain range'), Js('foggy fields'), Js('a gorgeous mirror lake'), Js('rows upon rows of lucious trees'), Js('staircase of waterfalls'), Js('frozen ponds'), Js('aromatic flowers'), Js('calming ocean front'), Js('fields of farmland'), Js('bamboo forest'), Js('huge oak tree'), Js('stunning canyon'), Js('majestic fjords'), Js('white, sandy beaches'), Js('amazing sunsets')]))
    var.put('names21', Js([Js('amusing'), Js('captivating'), Js('charming'), Js('delightful'), Js('enchanting'), Js('enthralling'), Js('entrancing'), Js('fascinating'), Js('glamorous'), Js('heavenly'), Js('intriguing'), Js('inviting'), Js('magical'), Js('mystical'), Js('mythical'), Js('otherworldly'), Js('pleasant'), Js('pleasing'), Js('seductive'), Js('whimsical')]))
    var.put('names38', Js([Js('town hall'), Js('cathedral'), Js('farm'), Js('large park'), Js('bank'), Js('jail'), Js('wishing well'), Js('old bar'), Js('armory'), Js('training grounds'), Js('graveyard'), Js('mausoleum'), Js('watchtower'), Js('blacksmith'), Js('hotel'), Js('lighthouse'), Js('market'), Js('museum'), Js('hospital'), Js('barracks'), Js('power plant'), Js('watermill'), Js('windmill'), Js('library'), Js('school'), Js('temple'), Js('castle'), Js('dueling arena'), Js('fountain'), Js('greenhouse'), Js('guard tower'), Js('lumber mill'), Js('quarry'), Js('stables'), Js('statue'), Js('tombs'), Js('monument'), Js('ancient forge'), Js('inn'), Js('cemetery'), Js('theatre'), Js('stadium'), Js('wizard tower')]))
    var.put('names41', Js([Js('affluent'), Js('beautiful'), Js('bleak'), Js('booming'), Js('cheerful'), Js('comfortable'), Js('delightful'), Js('enjoyable'), Js('flourishing'), Js('frightful'), Js('gloomy'), Js('gracious'), Js('grim'), Js('grisly'), Js('growing'), Js('gruesome'), Js('harsh'), Js('horrendous'), Js('horrible'), Js('horrific'), Js('luxuriant'), Js('macabre'), Js('pleasant'), Js('pleasurable'), Js('prosperous'), Js('sinister'), Js('somber'), Js('terrible'), Js('terrifying'), Js('thriving')]))
    var.put('random1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length')))))
    var.put('random2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length')))))
    var.put('random3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length')))))
    var.put('random4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length')))))
    var.put('random6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length')))))
    var.put('random6b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length')))))
    var.put('random9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names9').get('length')))))
    var.put('random10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names10').get('length')))))
    var.put('random11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names11').get('length')))))
    var.put('random12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names11').get('length')))))
    while (var.get('random12')==var.get('random11')):
        var.put('random12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names11').get('length')))))
    var.put('random13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names11').get('length')))))
    while ((var.get('random13')==var.get('random12')) or (var.get('random13')==var.get('random11'))):
        var.put('random13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names11').get('length')))))
    var.put('random14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names14').get('length')))))
    var.put('random15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names14').get('length')))))
    while (var.get('random15')==var.get('random14')):
        var.put('random15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names14').get('length')))))
    var.put('random16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names11').get('length')))))
    while (((var.get('random16')==var.get('random11')) or (var.get('random16')==var.get('random12'))) or (var.get('random16')==var.get('random13'))):
        var.put('random16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names11').get('length')))))
    var.put('random17', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names17').get('length')))))
    if (var.get('random17')>Js(16.0)):
        var.put('names18', Js([Js('metal shingle'), Js('galvanised steel'), Js('rusted'), Js('decaying'), Js('blackened'), Js('gray'), Js('black wooden'), Js('dark wooden'), Js('murky wooden'), Js('gloomy wooden'), Js('half rotten')]))
        var.put('names19', Js([Js('mossy wooden'), Js('mossy stone'), Js('faded granite'), Js('faded marble'), Js('worn limestone'), Js('worn sandstone'), Js('stone veneer'), Js('chiseled stone'), Js('galvanised steel'), Js('rusted'), Js('decaying'), Js('blackened'), Js('gray'), Js('black wooden'), Js('dark wooden'), Js('murky wooden'), Js('gloomy wooden'), Js('half rotten'), Js('lavastone')]))
        def PyJs_LONG_0_(var=var):
            return var.put('names20', Js([Js('decaying trees'), Js('rotten fields'), Js('broken roads'), Js('overgrown gardens'), Js('vines overgrowing everything'), Js('unmaintained gardens'), Js('foggy surroundings'), Js('murky woods'), Js('musky swamps'), Js('menacing mountain tops'), Js('barren grounds'), Js('absolute silence'), Js('a large graveyard'), Js('large cobwebs'), Js('dusty windows'), Js('dirty roads'), Js('thick smoke'), Js('creaking wood'), Js('whistling wind'), Js('scary animals'), Js('a lot of insects'), Js('scavenger birds'), Js('ominous scarecrows')]))
        PyJs_LONG_0_()
        def PyJs_LONG_1_(var=var):
            return var.put('names21', Js([Js('bizarre'), Js('bleak'), Js('chilling'), Js('creepy'), Js('dark'), Js('desolate'), Js('dreary'), Js('dull'), Js('eerie'), Js('foreboding'), Js('frightening'), Js('ghostly'), Js('ghoulish'), Js('gloomy'), Js('grim'), Js('grisly'), Js('gruesome'), Js('macabre'), Js('morbid'), Js('mysterious'), Js('ominous'), Js('peculiar'), Js('repulsive'), Js('revolting'), Js('sinister'), Js('somber'), Js('spine-chilling'), Js('supernatural'), Js('uncanny'), Js('unearthly')]))
        PyJs_LONG_1_()
    var.put('random18', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names18').get('length')))))
    var.put('random20', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names20').get('length')))))
    var.put('random21', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names21').get('length')))))
    var.put('random38', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names38').get('length')))))
    var.put('random39', var.get('parseInt')(var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(50.0))+Js(20.0)))))
    var.put('random40', var.get('random39').callprop('toString'))
    var.put('random41', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names41').get('length')))))
    if (var.get('random6')==Js(2.0)):
        var.put('names5', Js([Js('Gorash'), Js('Ogrinar'), Js('Tohrall'), Js('Dranorg'), Js('Hammerfall'), Js('Orsanum'), Js('Wrothguard'), Js('Garlund'), Js('Kharn'), Js('Xarluk')]))
        var.put('names8', Js([Js('Gnarg'), Js('Gnarlug'), Js('Gnorl'), Js('Gnorth'), Js('Gnoth'), Js('Gnurl'), Js('Golag'), Js('Golub'), Js('Gomatug'), Js('Gomoku'), Js('Gorgu'), Js('Gorlag'), Js('Grikug'), Js('Grug'), Js('Grukag'), Js('Grukk'), Js('Grung'), Js('Gruul')]))
        var.put('random5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length')))))
        var.put('random8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length')))))
    else:
        if (var.get('random6')==Js(3.0)):
            var.put('names5', Js([Js('Balagost'), Js('Moriath'), Js('Nogrand'), Js('Frosthold'), Js('Hammerhold'), Js('Thar Modan'), Js('Kaz Modor'), Js('Uldama'), Js('Hammerforge'), Js('Stormforge')]))
            var.put('names8', Js([Js('Bengahdar'), Js('Banbrek'), Js('Drumdus'), Js('Dulgarn'), Js('Galirg'), Js('Kharnur'), Js('Iromuador'), Js('Ragorhdrom'), Js('Urmbrek'), Js('Theledon')]))
            var.put('random5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length')))))
            var.put('random8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length')))))
        else:
            if (var.get('random6')==Js(4.0)):
                var.put('names5', Js([Js('Eviana'), Js('Malica'), Js('Mystohr'), Js('Arconia'), Js('Aeria'), Js('Mithyria'), Js('Calairith'), Js('Myracal'), Js('Fentalia'), Js('Curacius')]))
                var.put('names7', Js([Js('Queen'), Js('King'), Js('Prince'), Js('Princess')]))
                def PyJs_LONG_2_(var=var):
                    return var.put('names8', Js([Js('Azore'), Js('Coral'), Js('Cowrie'), Js('Ebbie'), Js('Gullie'), Js('Ionia'), Js('Ivory'), Js('Marin'), Js('Meer'), Js('Meri'), Js('Mora'), Js('Nautila'), Js('Oceana'), Js('Pearl'), Js('Percula'), Js('Sandy'), Js('Shelly'), Js('Starfish'), Js('Tidal'), Js('Urchin'), Js('Wave'), Js('Whirl'), Js('Wrassey'), Js('Aed'), Js('Aodh'), Js('Aeden'), Js('Ash'), Js('Ashley'), Js('Blaze'), Js('Candala'), Js('Coala'), Js('Firo'), Js('Flare')]))
                PyJs_LONG_2_()
                var.put('random5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length')))))
                var.put('random7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length')))))
                var.put('random8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length')))))
            else:
                if (var.get('random6')==Js(5.0)):
                    var.put('names5', Js([Js('Zuldazin'), Js('Zalzabin'), Js('Jintalman'), Js('Zulamor'), Js('Julguroob'), Js('Atalakar'), Js('Zandalur'), Js('Farakazul'), Js('Guruubash'), Js('Amano')]))
                    var.put('names8', Js([Js('Ekon'), Js('Erasto'), Js('Haijen'), Js('Hamedi'), Js('Hokima'), Js('Jaafan'), Js('Jabir'), Js('Jalai'), Js('Javyn'), Js('Jijel'), Js('Juma'), Js('Jumoke'), Js('Kaijin'), Js('Kazko'), Js('Maalik'), Js('Makas'), Js('Malak'), Js('Nyabingi'), Js('Rahjin'), Js('Rakash'), Js('Rashi'), Js('Razi')]))
                else:
                    if ((((((var.get('random6')==Js(1.0)) or (var.get('random6')==Js(11.0))) or (var.get('random6')==Js(12.0))) or (var.get('random6')==Js(15.0))) or (var.get('random6')==Js(16.0))) or (var.get('random6')==Js(17.0))):
                        var.put('names5', Js([Js('Gandoline'), Js('Galadoneh'), Js('Tirianae'), Js('Darnassea'), Js('Sinashari'), Js('Kaladorei'), Js('Hiborane'), Js('Fandralore'), Js('Cenorias'), Js('Ishnuala')]))
                        var.put('names8', Js([Js('Wyninn'), Js('Ninleyn'), Js('Tinlef'), Js('Elluin'), Js('Elduin'), Js('Elmon'), Js('Almar'), Js('Alas'), Js('Alwin'), Js('Almer'), Js('Alre'), Js('Alred'), Js('Alen'), Js('Alluin'), Js('Alduin'), Js('Almon'), Js('Hagmar'), Js('Hagas'), Js('Hagwin'), Js('Hagmer'), Js('Hagre')]))
                    else:
                        if (var.get('random6')==Js(13.0)):
                            var.put('names5', Js([Js('Nomeregone'), Js('Meckotarq'), Js('Kasmord'), Js('Trokkus'), Js('Hitonkar'), Js('Serian'), Js('Gloufry'), Js('Hazelmyre'), Js('Erposanra'), Js('Ardnode')]))
                            var.put('names8', Js([Js('Glinoflonk'), Js('Bonlebick'), Js('Bimbik'), Js('Gnobflink'), Js('Binflonk'), Js('Nittlewizz'), Js('Gimkink'), Js('Merbibus'), Js('Totonk'), Js('Dinnus')]))
                        else:
                            if (var.get('random6')==Js(14.0)):
                                var.put('names5', Js([Js('Bolgewotar'), Js('Galowax'), Js('Kozan'), Js('Stimwedle'), Js('Bootabai'), Js('Midsprocket'), Js('Rotchet'), Js('Grozlik'), Js('Andormyn'), Js('Ventarco')]))
                                var.put('names8', Js([Js('Karax'), Js('Baxeek'), Js('Soxart'), Js('Rezikmez'), Js('Fizink'), Js('Wimax'), Js('Jexmelyx'), Js('Grexmex'), Js('Tinkbelex'), Js('Greekeels')]))
                            else:
                                if (var.get('random6')==Js(20.0)):
                                    var.put('names7', Js([Js('Captain')]))
                                else:
                                    var.get(u"null")
    if (var.get('random17')>Js(16.0)):
        var.put('names18', Js([Js('metal shingle'), Js('galvanised steel'), Js('rusted'), Js('decaying'), Js('blackened'), Js('gray'), Js('black wooden'), Js('dark wooden'), Js('murky wooden'), Js('gloomy wooden'), Js('half rotten')]))
        var.put('names19', Js([Js('faded granite'), Js('faded marble'), Js('worn limestone'), Js('worn sandstone'), Js('stone veneer'), Js('chiseled stone'), Js('galvanised steel'), Js('rusted'), Js('decaying'), Js('blackened'), Js('gray'), Js('black wooden'), Js('dark wooden'), Js('murky wooden'), Js('gloomy wooden'), Js('half rotten'), Js('lavastone')]))
        def PyJs_LONG_3_(var=var):
            return var.put('names20', Js([Js('decaying trees'), Js('rotten fields'), Js('broken roads'), Js('overgrown gardens'), Js('vines overgrowing everything'), Js('unmaintained gardens'), Js('foggy surroundings'), Js('murky woods'), Js('musky swamps'), Js('menacing mountain tops'), Js('barren grounds'), Js('absolute silence'), Js('a large graveyard'), Js('large cobwebs'), Js('dusty windows'), Js('dirty roads'), Js('thick smoke'), Js('creaking wood'), Js('whistling wind'), Js('scary animals'), Js('a lot of insects'), Js('scavenger birds'), Js('ominous scarecrows')]))
        PyJs_LONG_3_()
        def PyJs_LONG_4_(var=var):
            return var.put('names21', Js([Js('bizarre'), Js('bleak'), Js('chilling'), Js('creepy'), Js('dark'), Js('desolate'), Js('dreary'), Js('dull'), Js('eerie'), Js('foreboding'), Js('frightening'), Js('ghostly'), Js('ghoulish'), Js('gloomy'), Js('grim'), Js('grisly'), Js('gruesome'), Js('macabre'), Js('morbid'), Js('mysterious'), Js('ominous'), Js('peculiar'), Js('repulsive'), Js('revolting'), Js('sinister'), Js('somber'), Js('spine-chilling'), Js('supernatural'), Js('uncanny'), Js('unearthly')]))
        PyJs_LONG_4_()
    var.put('random5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length')))))
    var.put('random7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length')))))
    var.put('random8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length')))))
    var.put('random19', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names19').get('length')))))
    def PyJs_LONG_5_(var=var):
        return (((((((((((((var.get('names1').get(var.get('random1'))+Js(' '))+var.get('names2').get(var.get('random2')))+Js(' a '))+var.get('names3').get(var.get('random3')))+Js(', the '))+var.get('names4').get(var.get('random4')))+Js(' of '))+var.get('names5').get(var.get('random5')))+Js(' is home to '))+var.get('names6').get(var.get('random6')))+Js(' lead by '))+var.get('names7').get(var.get('random7')))+Js(' '))
    var.put('name', ((PyJs_LONG_5_()+var.get('names8').get(var.get('random8')))+Js('.')))
    var.put('name2', ((((((((Js('This ')+var.get('names4').get(var.get('random4')))+Js(" wasn't built by a"))+var.get('names3').get(var.get('random3')))+Js(' by accident, as it has '))+var.get('names9').get(var.get('random9')))+Js(', which is of great importance to the people of '))+var.get('names5').get(var.get('random5')))+Js(' and its success.')))
    def PyJs_LONG_6_(var=var):
        return (((((((((((((Js('The ')+var.get('names4').get(var.get('random4')))+Js(' itself looks '))+var.get('names17').get(var.get('random17')))+Js('. With its '))+var.get('names18').get(var.get('random18')))+Js(' rooftops, '))+var.get('names19').get(var.get('random19')))+Js(' walls and '))+var.get('names20').get(var.get('random20')))+Js(', '))+var.get('names5').get(var.get('random5')))+Js(' has a '))+var.get('names21').get(var.get('random21')))
    var.put('name3', (PyJs_LONG_6_()+Js(' atmosphere.')))
    var.put('name4', ((((((Js('The main attraction is the ')+var.get('names38').get(var.get('random38')))+Js(', which was built '))+var.get('random40'))+Js(' years ago and designed by '))+var.get('names6').get(var.get('random6b')))+Js('.')))
    def PyJs_LONG_7_(var=var):
        return ((((((((((var.get('names5').get(var.get('random5'))+Js(' has a'))+var.get('names10').get(var.get('random10')))+Js(' economy, which is mainly supported by '))+var.get('names11').get(var.get('random11')))+Js(', '))+var.get('names11').get(var.get('random12')))+Js(' and '))+var.get('names11').get(var.get('random13')))+Js('. But their biggest strengths are '))+var.get('names14').get(var.get('random14')))
    var.put('name5', (((PyJs_LONG_7_()+Js(' and '))+var.get('names14').get(var.get('random15')))+Js('.')))
    var.put('name6', ((((Js('However, ')+var.get('names5').get(var.get('random5')))+Js(' lacks people skilled in '))+var.get('names11').get(var.get('random16')))+Js('.')))
    var.put('name7', ((((((((Js('Despite its strengths and weaknesses, ')+var.get('names5').get(var.get('random5')))+Js(' is most likely headed towards a '))+var.get('names41').get(var.get('random41')))+Js(' future under the leadership of '))+var.get('names7').get(var.get('random7')))+Js(' '))+var.get('names8').get(var.get('random8')))+Js('. But this remains to be seen.')))
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
townDescriptions = var.to_python()