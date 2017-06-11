__all__ = ['fungiNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
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
var.put('nm1', Js([Js('Aborted'), Js('Acute'), Js('Alder'), Js('Almond'), Js('Alpine'), Js('Amethyst'), Js('Amethyst'), Js('Amethyst'), Js('Amethyst'), Js('Anemone'), Js('Aniseed'), Js('Appressed'), Js('Apricot'), Js('Apricot'), Js('Apricot'), Js('Armored'), Js('Artillery'), Js('Artist’s'), Js('Artist'), Js("Artist's"), Js("Artist's"), Js('Artists'), Js('Ashy'), Js('Ashy'), Js('Ashy'), Js('Asian'), Js('Aspen'), Js('Baccharis'), Js('Banded'), Js('Bare-toothed'), Js('Barometer'), Js('Bay-brown'), Js('Bear'), Js("Bear's"), Js("Bear's"), Js('Bearded'), Js('Beautiful'), Js('Beech'), Js('Beech'), Js('Beefsteak'), Js('Bell'), Js('Belted'), Js("Berkeley's"), Js('Big'), Js('Birch'), Js('Birch'), Js('Birch'), Js("Bird's"), Js("Bird's"), Js("Bird's"), Js("Bird's-nest"), Js('Birds'), Js('Bitter'), Js('Bitter'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black'), Js('Black-eyed'), Js('Black-eyed'), Js('Black-foot'), Js('Black-leg'), Js('Blackcurly'), Js('Blackening'), Js('Bleeding'), Js('Bleeding'), Js('Bleeding'), Js('Blood-foot'), Js('Blood-spattered'), Js('Blotched'), Js('Blotched'), Js('Blue'), Js('Blue'), Js('Blue'), Js('Blue-black'), Js('Blue-green'), Js('Blue-staining'), Js('Bluish'), Js('Blushing'), Js('Blushing'), Js('Blushing'), Js('Blushing'), Js('Blushing'), Js('Bog'), Js('Bogus'), Js('Bonnet'), Js('Bootlace'), Js('Bootlace'), Js('Boring'), Js('Bouquet'), Js('Bouquet'), Js('Bracket'), Js('Bracket'), Js('Bracket'), Js('Bracket'), Js('Brain'), Js('Brain'), Js('Branched'), Js('Branched'), Js('Branched'), Js('British'), Js('British'), Js('Brittle'), Js('Brittle'), Js('Brown'), Js('Brown'), Js('Brown'), Js('Brown'), Js('Brown'), Js('Brown'), Js('Blushing'), Js('Blushing'), Js('Blushing'), Js('Bog'), Js('Bogus'), Js('Bonnet'), Js('Bootlace'), Js('Bootlace'), Js('Boring'), Js('Bouquet'), Js('Bouquet'), Js('Bracket'), Js('Bracket'), Js('Bracket'), Js('Bracket'), Js('Brain'), Js('Brain'), Js('Branched'), Js('Branched'), Js('Branched'), Js('Brittle'), Js('Brittle'), Js('Brown'), Js('Brown'), Js('Brown'), Js('Brown'), Js('Brown'), Js('Brown'), Js('Amethyst'), Js('Agaricus'), Js("Artist's"), Js('Beech'), Js('Beef-steak'), Js('Birch'), Js('Birch'), Js('Birch'), Js("Bird's"), Js('Black'), Js('Blood-Foot'), Js('Blue'), Js('Blue-Green'), Js('Butter'), Js('Bovine'), Js('Candlesnuff'), Js('Carbon'), Js('Clavulinopsis'), Js('Club'), Js('Clustered'), Js('Clustered'), Js('Collard'), Js('Common'), Js('Common'), Js('Common'), Js('Coral'), Js('Crab'), Js('Crystal'), Js('Dead'), Js('Deer'), Js('Dog'), Js("Dog's"), Js("Dryad's"), Js("Dyer's"), Js('Emetic'), Js('Eyelash'), Js('Fairy'), Js('False'), Js('Fly'), Js('Fringed'), Js('Giant'), Js('Giant'), Js('Grey'), Js('Horse'), Js('Hypoxylon'), Js('Hypoxylon'), Js('Jelly'), Js("Jew's"), Js('King'), Js('Lacquered'), Js('Lactarius'), Js('Larch'), Js('Leccinum'), Js("Lion's"), Js('Meadow'), Js('Oakbug'), Js('Orange'), Js('Orange'), Js('Ob'), Js('Panther'), Js('Peck'), Js('Pestle'), Js('Plums'), Js('Pluteus'), Js('Porcelain'), Js('Potato'), Js('Pterula'), Js('Purple'), Js('Red'), Js('Rooting'), Js('Rosy'), Js('Scarlet'), Js('Scurfy'), Js('Scurfy'), Js('Shaggy'), Js('Shaggy'), Js('Shaggy'), Js('Silverleaf'), Js('Small'), Js('Smoky'), Js('Spectacular'), Js('Straight-Branched'), Js('Sulphur'), Js('Sulphur'), Js('Tarzetta'), Js('Thelephora'), Js('Turkey'), Js('Weeping'), Js('White'), Js('White'), Js("Witch's"), Js("Wolf's"), Js('Wood'), Js('Wrinkled'), Js('Yellow'), Js('Yellow'), Js('Brown'), Js('Brown'), Js('Brown-eyed'), Js('Bruised'), Js('Bulbous'), Js('Bullseye'), Js('Bushing'), Js('Butter'), Js('Calcareous'), Js('California'), Js('Candleflame'), Js('Candleflame'), Js('Candlesnuff'), Js('Candy'), Js('Candy'), Js('Candy'), Js('Candy'), Js('Cannon'), Js('Carbon'), Js('Carbon'), Js('Carbon'), Js('Carnival Candy'), Js('Caterpillar'), Js('Cauliflower'), Js('Cauliflower'), Js('Chestnut'), Js('Chocolate'), Js('Chocolate'), Js('Chocolate'), Js('Cinnabar-red'), Js('Cinnamon'), Js('Clinker'), Js('Cloudy'), Js('Club'), Js('Club'), Js('Club'), Js('Club-footed'), Js('Club-like'), Js('Clublike'), Js('Clustered'), Js('Clustered'), Js('Clustered'), Js('Clustered'), Js('Coal'), Js('Cobalt'), Js('Coccoli'), Js('Coccoli'), Js('Coccoli'), Js('Collared'), Js('Comb'), Js('Comb'), Js('Comb'), Js('Comb'), Js('Common'), Js('Common'), Js('Common'), Js('Compressed'), Js('Conch'), Js('Conic'), Js('Conical'), Js('Conidial'), Js('Conifer'), Js('Conifer-base'), Js('Copper'), Js('Coral'), Js('Coral'), Js('Coral'), Js('Corn'), Js('Corn'), Js('Corral'), Js("Cowboy's"), Js('Cracked-cap'), Js('Craked-Cap'), Js('Cramp'), Js('Cramp'), Js('Crested'), Js('Crested'), Js('Crimped'), Js('Crimson'), Js('Crowded'), Js('Crown'), Js('Crown'), Js('Crumble'), Js('Cryptic'), Js('Cup'), Js('Cup'), Js("Darwin's"), Js('Dead'), Js('Dead'), Js('Deadly'), Js('Deadly'), Js('Death'), Js('Death'), Js('Deer'), Js('Delicious'), Js('Delicious'), Js('Desert'), Js('Desert'), Js('Destroying'), Js('Destroying'), Js("Devil's"), Js("Devil's"), Js("Devil's"), Js('Dimple'), Js('Dimple'), Js('Dog'), Js('Dog'), Js('Douglas'), Js('Douglas'), Js('Douglas-fir'), Js("Dryad's"), Js('Dung'), Js('Dung'), Js('Dung-loving'), Js('Dye'), Js('Dye'), Js("Dyemaker's"), Js("Dyer's"), Js('Early'), Js('Earpick'), Js('Earthy'), Js('Egg-yolk'), Js('Elegant'), Js('Elegant'), Js('Elegant'), Js('Elephant'), Js('Elfin'), Js("Elfin's"), Js('Emetic'), Js('Eyelash'), Js('Eyelash'), Js('Fabby'), Js('Fairy'), Js('Fairy'), Js('Fairy'), Js('False'), Js('False'), Js('Fan'), Js('Fan-shaped'), Js('Fawn'), Js('Felt'), Js('Felt-Ringed'), Js('Fetid'), Js('Field'), Js('Finger'), Js('Flabby'), Js('Flaky'), Js('Flaky'), Js('Flame'), Js('Flat'), Js('Flat'), Js('Flat-topped'), Js('Fleecy'), Js('Fluted'), Js('Fluted'), Js('Fly'), Js('Fly'), Js('Fly'), Js('Fly-agaric'), Js('Fog'), Js('Foliose'), Js('Foliose'), Js('Forked'), Js('Fragile'), Js('Fragile'), Js('Fringed'), Js('Fringed'), Js('Frosted'), Js('Fruiticose'), Js('Funnel'), Js('Funnel'), Js('Fuzzy'), Js('Gabled'), Js('Garlic'), Js('Garlic'), Js('Gastroid'), Js('Gem-studded'), Js('Gemmed'), Js('Giant'), Js('Giant'), Js('Gilled'), Js('Glistening'), Js('Glistening'), Js('Globe'), Js('Globe'), Js('Glutinous'), Js('Glutinous'), Js('Goblet'), Js('Gold'), Js('Gold'), Js('Golden'), Js('Golden'), Js('Gomphus'), Js('Gooseberry'), Js('Grassblade'), Js('Gray'), Js('Great'), Js('Green'), Js('Green-spored'), Js('Grey'), Js('Grey'), Js('Grooved'), Js("Hadrian's"), Js('Hairy'), Js('Hairy'), Js("Hare's"), Js('Harefoot'), Js("Haymaker's"), Js('Hazel'), Js('Head'), Js('Head'), Js('Heath'), Js('Hedgehod'), Js('Hedgehog'), Js('Hemlock'), Js('Hexagonal-pored'), Js('Hideous'), Js('Honey'), Js('Hongo'), Js('Hooded'), Js('Hoof'), Js('Horn'), Js('Horn'), Js('Horse'), Js('Hydrothyria'), Js('Hygrophorus'), Js('Hygroscopic'), Js('Indigo'), Js('Inky'), Js('Insect-egg'), Js('Insidious'), Js('Iodine'), Js('Ivory'), Js('Ivory'), Js('Jack-O-Lantern'), Js('Umbrella'), Js('Jelly'), Js('Jelly'), Js('Jersey'), Js('Kidney'), Js('Kidney'), Js('King'), Js('King'), Js('Lackluster'), Js('Lady'), Js('Larch'), Js('Late'), Js('Latticed'), Js("Lawyer's"), Js('Leafy'), Js('Leafy'), Js('Lemon'), Js('Lemon'), Js('Lilac'), Js('Ling'), Js("Lion's"), Js("Lion's"), Js("Lion's"), Js('Lipstick'), Js('Lipstick'), Js('Little'), Js('Llao'), Js('Lobster'), Js('Luminescent'), Js('Lumpy'), Js('Lung'), Js('Lung'), Js('Lurid'), Js('Man'), Js('Many-forked'), Js('Many-headed'), Js('Map'), Js('Maple'), Js('Marasmiellus'), Js('Maritime'), Js('Meadow'), Js('Meadowsweet'), Js('Mealy'), Js('Membranous'), Js('Mica'), Js('Mica'), Js('Midnight'), Js('Midnight'), Js('Miniature'), Js('Mock'), Js('Mossy'), Js('Mossy'), Js('Mottled'), Js('Multi-branched'), Js('Multicolor'), Js('Mushroom'), Js('Mustard'), Js('Mustard-yellow'), Js('Nail'), Js('Noble'), Js('Fuzzy'), Js('Oak'), Js('Oak-loving'), Js('Ochre'), Js('Ocre'), Js('Old'), Js('Orange'), Js('Orange'), Js('Orange-latex'), Js('Orange-peel'), Js('Orangeroter'), Js('Oregon'), Js('Oyster'), Js('Oyster-type'), Js('Pacific'), Js('Palamino'), Js('Pale'), Js('Paltry'), Js('Pan'), Js('Panther'), Js('Panther'), Js('Parasitic'), Js('Parasol'), Js('Parrot'), Js('Pea'), Js('Pear-shaped'), Js('Pear-shaped'), Js('Peeling'), Js('Pepper-spore'), Js('Peppermint'), Js('Pestle'), Js('Pestle'), Js('Petaled'), Js('Petite'), Js('Phaecollybia'), Js("Pheasant's"), Js("Pig's"), Js('Pin'), Js('Pin-cushion'), Js('Pine'), Js('Pine'), Js('Pinecone'), Js('Pink'), Js('Pink-Fleshed'), Js('Pink-Tipped'), Js('Pinkish'), Js('Pipecleaner'), Js('Pixie'), Js('Pixie-cup'), Js('Pleated'), Js('Pleated'), Js('Poached'), Js('Poison'), Js('Poison'), Js('Poor'), Js('Poplar'), Js('Porcelain'), Js('Powdered'), Js('Powdery'), Js('Pretzel'), Js('Prunes'), Js('Puffball'), Js('Puffball'), Js('Pulvinate'), Js('Purple'), Js('Purple-Spored'), Js('Pyxie'), Js('Queen'), Js('Questionable'), Js('Quilted'), Js('Ragged'), Js('Ramularia'), Js('Raspberry'), Js('Recurved'), Js('Red'), Js('Red-belted'), Js('Red-belted'), Js('Red-cracking'), Js('Red-juice'), Js('Redwood'), Js('Righteous'), Js('Rim'), Js('Ringed'), Js('Rock'), Js('Rockmoss'), Js('Rooting'), Js('Rosy'), Js('Rosy-Brown'), Js('Ruffle'), Js('Rufous'), Js('Russet'), Js('Rusty'), Js('Rusty'), Js('Sagebrush'), Js('Sagebrush'), Js('Salmon'), Js("Satan's"), Js("Satyr's"), Js('Saucered'), Js('Sauthern'), Js('Scaly'), Js('Scaly'), Js('Scarlet'), Js('Scarlet'), Js('Scrambled'), Js('Sculptured'), Js('Scum'), Js('Sessile'), Js('Sessile'), Js('Shaggy'), Js('Shaggy'), Js('Shaggy-mane'), Js('Shaggy-stalked'), Js('Shaggy-stalked'), Js('Shaly'), Js('Sheathed'), Js('Short-Stemmed'), Js('Shotgun'), Js('Shotgun'), Js('Shrimp'), Js('Sierran'), Js('Sierran'), Js('Silver-leaf'), Js('Silverleaf'), Js('Silvery-violet'), Js('Slime'), Js('Slimy'), Js('Slippery'), Js('Slippery'), Js('Small'), Js('Small'), Js("Smith's"), Js('Smoky'), Js('Smoky'), Js('Smooth'), Js('Snow'), Js('Snow-white'), Js('Snowbank'), Js('Snowy'), Js('Soft'), Js('Soil-living'), Js('Solid-stemmed'), Js('Sphere'), Js('Spiny'), Js('Splash'), Js('Splendid'), Js('Split'), Js('Split-pore'), Js('Spongy'), Js('Spotted'), Js('Spraypaint'), Js('Spring'), Js('Spring'), Js('Springtime'), Js('Spruce'), Js('Staghorn'), Js('Stag’s'), Js('Stalked'), Js('Stalked'), Js('Steel-blue'), Js('Stipplescale'), Js('Stonewall'), Js('Straight-branched'), Js('Strap'), Js('Strawberries'), Js('Strict'), Js('Strobilurus'), Js('Stump'), Js('Suburban'), Js('Sukver-Violet'), Js('Sulphur'), Js('Sulphur'), Js('Swamp'), Js('Sweet'), Js('Sweetbread'), Js('Tamarack'), Js('Tawny'), Js('Telephora'), Js('Thick'), Js('Thimble'), Js('Thin'), Js('Tigar'), Js('Tiger'), Js('Tile'), Js('Tinder'), Js('Tinder'), Js("Tippler's"), Js('Toothed'), Js('Toothpaste'), Js('Toy'), Js('Trametes'), Js('Trembling'), Js('Tripe'), Js('Triple'), Js('Trompeta'), Js('Truffle'), Js('Trumpet'), Js('Trumpet'), Js('Truncate'), Js('Tube'), Js("Tuckerman's"), Js("Tuckerman's"), Js('Tufted'), Js('Tumble'), Js('Tumbling'), Js('Turkey-tail'), Js('Turkey-tail'), Js('Two-colored'), Js('Umbrella'), Js('Unbranched'), Js('Unidentified'), Js('Urban'), Js('Varied'), Js('Variegated'), Js('Varnished'), Js('Varying'), Js('Veiled'), Js('Veiled'), Js('Veined'), Js('Velvet'), Js('Velvet'), Js('Velvet-cap'), Js('Velvet-cap'), Js('Velvety'), Js('Velvety'), Js('Verdigris'), Js('Vermicelli'), Js('Vinter'), Js('Violet'), Js('Violet'), Js('Viscid'), Js('Viscid'), Js('Walnut'), Js('Waxy'), Js('Weeping'), Js('Weeping'), Js('Western'), Js('Whiches'), Js('White'), Js('White'), Js('White-egg'), Js('White-footed'), Js('Whiteworm'), Js('Whitish'), Js('Wine'), Js('Winter'), Js('Winter'), Js('Winter'), Js("Witch's"), Js("Witch's"), Js('Wolf'), Js("Wolf's"), Js('Wolf’s'), Js('Wood'), Js('Wood'), Js('Woolly'), Js('Woolly'), Js('Wooly'), Js('Wooly'), Js('Wrinkled'), Js('Wrinkled'), Js('Wrinkled'), Js('Yellow'), Js('Yellow-Cracking'), Js('Yellow-Footed'), Js('Yellow-Fuzz'), Js('Yellow-Staining'), Js('Yellow-Stalked'), Js('Yellow-Stemmed'), Js('Yellow-Tipped'), Js('Yellow-Veiled'), Js('Yellowing'), Js('Yesquero'), Js("Zeller's"), Js('Ziza'), Js('Zoned')]))
var.put('nm2', Js([Js('Agareicus'), Js('Agaric'), Js('Agaric Mushroom'), Js('Agaricus'), Js('Agaricus'), Js('Agaricus'), Js('Agaricus '), Js("Alfred's Cake"), Js('Amanita'), Js('Amanita'), Js('Amanita'), Js('Amanita'), Js('Amethyst Laccaria'), Js('Amoeba Slime Mold'), Js('And Cream '), Js('And Custard'), Js('And Yellow Russula '), Js('Angel'), Js('Angel '), Js('Antlers'), Js('Azure'), Js('Babies'), Js('Baby'), Js('Back Mushroom '), Js('Ball Lichen'), Js('Banded Polypore '), Js('Bane'), Js('Barf'), Js('Bark Spot'), Js('Beacon'), Js('Beacon '), Js('Beacon '), Js('Beard'), Js('Beard'), Js('Beech Caps'), Js('Bellies '), Js('Belly'), Js('Birch Bolete'), Js("Bird's Nest"), Js("Bird's Nest Fungus"), Js("Bird's Nest Fungus"), Js('Black Earth Tongue'), Js('Black Earth Tongue'), Js('Black Elfin Saddle'), Js('Black Helvella'), Js('Blewit'), Js('Blewit'), Js('Blewitt'), Js('Blue Entoloma'), Js('Blue Entoloma'), Js('Blusher'), Js('Blusher'), Js('Bolbitius '), Js('Bolete'), Js('Bolete'), Js('Boletus'), Js('Bone Lichen'), Js('Bonnet'), Js('Bonnet'), Js('Bottle'), Js('Bracket'), Js('Bracket'), Js('Bradley '), Js('Brain'), Js('Brain'), Js('Brain Jelly '), Js('Brittlegill'), Js('Brittlegill'), Js('Brittlegill'), Js('Broadleaf Crust'), Js('Brown Elfin Saddle '), Js('Bulgar'), Js('Bushy Beard Lichen'), Js('Butter'), Js('Butter'), Js('Butter Fungus'), Js('Butter Fungus '), Js('Candy Cap'), Js('Canker Polypore'), Js('Cap'), Js('Cap'), Js('Cap'), Js('Cap Mushroom'), Js('Cap Mushroom'), Js('Caps '), Js('Cardoncello'), Js('Cardoon'), Js('Caterpillarclub'), Js('Cavlier'), Js('Cep '), Js('Cepe'), Js('Chalice Lichen'), Js('Champignon'), Js('Chanterelle'), Js('Chanterelle'), Js('Cheese Polypore'), Js('Chih'), Js('Chip Lichen'), Js('Cladonia'), Js('Cladonia '), Js('Clitocybe'), Js('Club'), Js('Club Coral'), Js('Club Coral '), Js('Clustered Ear Cup'), Js('Cobblestone Lichen'), Js('Coccora'), Js('Coccora'), Js('Collybia'), Js('Collybia'), Js('Colored Agaricus '), Js('Cone Amanita'), Js('Cone Head '), Js('Cone Slime'), Js('Conic Waxy Cap'), Js('Conifer Cortinarius'), Js('Conifer Cystoderma '), Js('Conk'), Js('Conk'), Js('Conk Fungus'), Js('Conk Mushroom '), Js('Conocybe'), Js('Conocybe'), Js('Coral'), Js('Coral'), Js('Coral'), Js('Coral Fungus'), Js('Coral Fungus'), Js('Coral Mushroom'), Js('Coral Mushroom'), Js('Cort'), Js('Cort'), Js('Cortinarius'), Js('Cortinarius'), Js('Cow Mushroom'), Js('Cracked Bolete'), Js('Crep'), Js('Crep'), Js('Crepidotus'), Js('Crepidotus'), Js('Crust'), Js('Crust'), Js('Cup'), Js('Cup'), Js('Cup'), Js('Cup Fungus'), Js('Cup Fungus'), Js('Cup Fungus'), Js('Cup Lichen'), Js('Cups'), Js('Curtain Crust'), Js('Curtain Crust'), Js('Cushion'), Js('Cushion Hypoxylon'), Js('Custard'), Js('De Indio'), Js('Death Cap'), Js('Deathcap'), Js('Deathcap'), Js('Deceiver'), Js('Deceiver'), Js('Destroyer Fungi '), Js('Destroyer Fungus'), Js('Disco'), Js('Discus Mushroom'), Js('Dog-lichen'), Js('Dog-lichen '), Js('Domecap'), Js('Drop Lichen'), Js('Dung Cup'), Js('Dyeball'), Js('Dyeball'), Js('Ear'), Js('Ear'), Js('Ear Fungus'), Js('Ears '), Js('Ears Mushroom'), Js('Ears Mushroom'), Js('Earth Tongue'), Js('Earth Tongue '), Js('Earthball'), Js('Earthball'), Js('Earthstar'), Js('Earthstar'), Js('Eater'), Js("Egg Bird's Nest Fungus "), Js('Egg Fungus'), Js('Egg Slime'), Js('Elf Cup'), Js('Elfcup'), Js('Elfin Cup'), Js('Elfin Saddle'), Js('Elfin Saddle'), Js('Enokitake'), Js('Entoloma'), Js('Entoloma'), Js('Eye Lichen'), Js('Fairy Club'), Js('Fairy Club Mushroom'), Js('Fairy Cups'), Js('Fairy Cups Lemon Disco'), Js('Fairy Helmet'), Js('Fall Oyster'), Js('False Coral Mushroom '), Js('False Morel'), Js('False Morel'), Js('Felt Lichen'), Js('Felt Lichen'), Js('Fern'), Js('Fingers'), Js('Fir Collybia'), Js('Fir Cone Mushroom'), Js('Firedot Lichen'), Js('Firedot Lichen '), Js('Fishscale Lichen'), Js('Fishscale Lichen'), Js('Fishscale Lichen '), Js('Flat-top Agaricus'), Js('Fog Lichen'), Js('Fog Lichen'), Js('Foot'), Js('Foot'), Js('Foot Coprinus'), Js('Fott'), Js('Freckle Pelt'), Js('Fungi'), Js('Fungi'), Js('Fungus'), Js('Fungus'), Js('Fungus'), Js('Honey Fungus  '), Js('Honey Fungus  '), Js('Funnel Cap'), Js('Funnel Cap'), Js('Funnel Cap '), Js('Galerina '), Js("Gel Bird's Nest"), Js('Giant Puffball'), Js('Gill'), Js('Gill '), Js('Gill Polypore'), Js('Gilled Polypore'), Js('Globe Fungus'), Js('Gold Fleece Mushroom'), Js('Goldspeck Lichen '), Js('Gomphidius'), Js('Gomphidius'), Js('Gomphus'), Js('Gray Disco'), Js('Gray Saddle '), Js('Green Russula'), Js('Green-algae Coral'), Js('Greenshied Lichen'), Js('Greenshield Lichen'), Js('Grisette'), Js('Grisette'), Js('Gymnopilus '), Js('Hair'), Js('Hair Lichen'), Js('Hair Lichen'), Js('Hairy Fairy Cup'), Js('Hallimasch '), Js('Handkerchief'), Js('Hat'), Js('Hat '), Js('Head'), Js('Head Fungus '), Js('Heart Mushroom'), Js('Hedgehog'), Js('Helmling'), Js('Hericium'), Js('Hericium'), Js('Hobnail Canker'), Js('Horn'), Js('Hydnellum'), Js('Inkcap'), Js('Inkcap'), Js('Inkcap '), Js('Inky Cap'), Js('Inky Cap'), Js('Jack'), Js('Jack'), Js('Jelly'), Js('Jelly'), Js('Jelly Club'), Js('Jelly Cone'), Js('Jelly Cone '), Js('Jelly Cones'), Js('Jelly Drop'), Js('Jelly Drops'), Js('Jelly Drops '), Js('Jelly Fungus'), Js('Jelly Fungus'), Js('Jelly Fungus'), Js('Jelly Lichen'), Js('Jelly Mushroom '), Js('Jelly Roll'), Js('Jelly Spot'), Js('Jelly Disc'), Js('Jelly Disc'), Js('Jelly Disc'), Js('Jewel Lichen '), Js('Knight'), Js('Knight Gas Agaric'), Js('Laccaria'), Js('Laccaria'), Js('Lactarius '), Js('Laughing Gym'), Js('Leaf '), Js('Leaf Spot'), Js('Lentinellus'), Js('Lepiota'), Js('Leptonia'), Js('Leptonia'), Js('Lichen'), Js('Lichen'), Js('Lichen'), Js('Lichen'), Js('Lichen'), Js('Licorice'), Js('Lilly Fungus'), Js('Lion '), Js('Lishen'), Js("Lizard's Claw"), Js('Lover'), Js('Lung Lichen'), Js('Lungwort'), Js('Lungwort '), Js("Man's Beard"), Js("Man's Fingers "), Js("Man's Foot"), Js("Man's Foot"), Js("Man's Licorice"), Js('Mane'), Js('Mane'), Js('Mane Hericium'), Js('Mane Mushroom'), Js('Mane Mushroom '), Js('Mans Fingers'), Js('Map Lichen'), Js('Marasmius'), Js('Marasmius'), Js('Maze Conk'), Js('Maze Flat Polypore'), Js('Maze Oak Polypore'), Js('Maze Polypore '), Js('Mazegill'), Js('Mazegill Bracket '), Js('Merulius'), Js('Mildew'), Js('Mildew '), Js('Milk'), Js('Milk'), Js('Milk Cap'), Js('Milk Cap '), Js('Milk Cup Mushroom'), Js('Milk Slime'), Js('Milk-cap'), Js('Milkcap'), Js('Milkcap '), Js('Milky'), Js('Milky '), Js('Mirasmius '), Js('Mlushroom '), Js('Mold'), Js('Mold '), Js('Morel'), Js('Morel'), Js('Morel'), Js('Mould'), Js('Mould'), Js('Mushroom '), Js('Mushroom '), Js('Mushrooms'), Js('Mushrooms'), Js('Mycena'), Js('Mycena'), Js('Mycena'), Js('Navel '), Js('Nest Fungi'), Js('Nest Fungus'), Js('Nest Fungus'), Js('Orange Elf-cup '), Js('Orange Lichen'), Js('Orange Peel Fungus'), Js('Orange Peel Fungus '), Js('Ori '), Js('Oyster'), Js('Oyster'), Js('Oyster Fungus'), Js('Oysterling '), Js('Oysterling '), Js('Painted Suillus'), Js('Panaeolus'), Js('Panellus'), Js('Panus'), Js('Panus'), Js('Parasol'), Js('Parasol'), Js('Parchment'), Js('Peel'), Js('Peel Fungus'), Js('Peel Fungus '), Js('Phellodon'), Js('Phlebia'), Js('Phlebia'), Js('Pholiota'), Js('Pholiota'), Js('Pine Spike'), Js('Pixie Cup'), Js('Pixie Cup'), Js('Pixie Cups'), Js('Pluteous'), Js('Pluteus'), Js('Poisonpie'), Js('Polvera Bejin '), Js('Polypore'), Js('Polypore'), Js('Polypore'), Js('Porcini'), Js('Pored Bolete'), Js('Poria'), Js('Powdercap '), Js('Powderhorn'), Js('Powderhorn Lichen'), Js('Prince'), Js('Prince '), Js('Psalthyrella '), Js('Psathyrella'), Js('Puff Ball'), Js('Puffball'), Js('Puffball'), Js('Puffball'), Js('Puffball Fungus '), Js('Puffballs'), Js('Purple Cortinarius'), Js('Rag Lichen'), Js('Rebozuelo'), Js('Red Waxy Cap'), Js('Red Waxy Cap'), Js('Redwood Collybia'), Js('Redwood Mushroom'), Js('Ribbed Elfin Cup'), Js('Ribbed Elfin Cup'), Js('Rim Lichen'), Js('Rim-lichen'), Js('Rimmed Lichen'), Js('Ring Mushroom '), Js('Rock Tripe'), Js('Rock Tripe'), Js('Rooter '), Js('Rooter '), Js('Rosette Lichen'), Js('Rosette Lichen '), Js('Rot Fungus'), Js('Roundhead'), Js('Russula'), Js('Russula'), Js('Rust'), Js('Rust Gall'), Js('Rust Gall Fungus'), Js('Saddle'), Js('Saddle'), Js('Salad'), Js('Sandozi'), Js('Saw-toothed'), Js('Sawgill'), Js('Sawgill '), Js('Scaber Stalk '), Js('Scale'), Js('Scale'), Js('Scalycap'), Js('Script Lichen '), Js('Seaver'), Js('Shank'), Js('Shanklet '), Js('Shanklet '), Js('Shanklet Branched Collybia'), Js('Shanklet Branched Collybia  '), Js('Shelf'), Js('Shelf'), Js('Shelf Mushroom'), Js('Shelf Mushroom'), Js('Shelf Mushroom'), Js('Shelf Mushrooms'), Js('Shield'), Js('Shield Lichen'), Js('Shingle Lichen'), Js('Sickener'), Js('Sickener '), Js('Silk Inocybe '), Js('Slime'), Js('Slime '), Js('Slime Milk '), Js('Slime Mold'), Js('Slime Mold'), Js('Slimy Cortinarius'), Js('Slipper'), Js('Smooth'), Js('Smooth Host'), Js('Snuff-box'), Js('Snuffbox '), Js('Soldier Lichen'), Js('Soldiers'), Js('Soldiers '), Js('Spike'), Js('Spike'), Js('Spindle Coral'), Js('Spindles'), Js('Spindles '), Js('Spot Fungus'), Js('Staghorn Fungus'), Js('Staghorn Jelly Fungus'), Js('Stagshorn'), Js('Stagshorn'), Js('Stagshorn Fungus'), Js('Stain'), Js('Stainer'), Js('Staining Mushroom'), Js('Steinpilz'), Js('Stem'), Js('Stereum'), Js('Stinkhorn'), Js('Stinkhorn'), Js('Stippleback Lichen'), Js('Strap'), Js('Stropharia'), Js('Stropharia'), Js('Sunburst Lichen'), Js('Sunburst Lichen'), Js('Sunshine Lichen'), Js('Sunshine Lichen'), Js('Swamp Russula '), Js('Tar Spot '), Js('Thimble-cap'), Js('Thrower '), Js('Tile Lichen'), Js('Tile Lichen '), Js('Toadskin Lichen'), Js('Toadstool'), Js('Toadstool '), Js('Tooth'), Js('Tooth'), Js('Tooth Mushroom'), Js('Tooth Mushroom'), Js('Tooth Mushroom'), Js('Toothed Polypore'), Js('Top'), Js('Tough-shank'), Js('Toughshank'), Js('Trotter'), Js('Trumpet '), Js('Tub'), Js('Tubaria'), Js('Tube Lichen'), Js('Tube Slime '), Js('Tube Slime Mold'), Js('Tuft'), Js('Tuft'), Js('Tuft Mushroom'), Js('Tuft Mushrooms'), Js('Tuning Fork Mushroom'), Js('Tuning Fork Mushroom'), Js('Tuning Fork Mushrooms'), Js('Turkey Tail'), Js('Turkey Tail'), Js('Turkey Tails'), Js('Twiglet'), Js('Urn'), Js('Varnish Shelf'), Js('Vase Chanterelle'), Js('Vermilion Slender Caesar'), Js('Versicolor '), Js('Vomit Slime '), Js('Vomit Slime Mold'), Js('Vomit Slime Mold'), Js('Warted Mountain Puffball'), Js('Water Lichen'), Js('Waxcap'), Js('Waxcap'), Js('Waxy Cap'), Js('Waxy Cap'), Js('Waxycap '), Js('Webcap'), Js('Webcap'), Js('Webcap '), Js('White Coral Mushroom'), Js('White Elfin Saddle'), Js('White Russula'), Js('White Russula'), Js('Widow'), Js('Wig '), Js('Wood Cup'), Js('Wood Stain '), Js('Woodland Grisette '), Js('Woodlove'), Js('Woodtuft'), Js('Woodwart'), Js('Woodwart'), Js('Woodwax'), Js('Woodwax'), Js('Worm Coral'), Js('Wrinkle-Lichen '), Js('Yellow Jelly'), Js('Yellow Morel'), Js('Yellow Polypore'), Js('Yellow Slime'), Js('Yellow Slime Mold '), Js('Yellow-veiled Amanita'), Js('de los Muertos '), Js('False Truffel'), Js('Fungus'), Js('Helveola'), Js('Hortensis'), Js('Hydnum'), Js('Leoninus'), Js('Mane'), Js('Multifida'), Js('Oyster'), Js('Penicillata'), Js('Powderpuff'), Js('Ringless Amanita'), Js('Rustgill '), Js('Rutilum'), Js('Serpens'), Js('Slime '), Js('Spot Fungus'), Js('Tails'), Js('Trumpets'), Js('Veil Amanita')]))
pass
pass


# Add lib to the module scope
fungiNames = var.to_python()