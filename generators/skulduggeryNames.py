__all__ = ['skulduggeryNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            if PyJsStrictEq(var.get('tp'),Js(2.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('names', ((((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(1.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    while PyJsStrictEq(var.get('nm2').get(var.get('rnd')),var.get('nm3').get(var.get('rnd2'))):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd2'))):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aberrant'), Js('Arbor'), Js('Arch'), Js('Archer'), Js('Argent'), Js('Art'), Js('Ash'), Js('Bane'), Js('Barb'), Js('Barbarous'), Js('Barren'), Js('Behemoth'), Js('Bellow'), Js('Berserk'), Js('Birch'), Js('Blade'), Js('Blaze'), Js('Booth'), Js('Brawl'), Js('Brawn'), Js('Brick'), Js('Brook'), Js('Brutus'), Js('Buster'), Js('Cane'), Js('Carnage'), Js('Carter'), Js('Chance'), Js('Chaos'), Js('Chase'), Js('Chuck'), Js('Cipher'), Js('Cliff'), Js('Clout'), Js('Coal'), Js('Copper'), Js('Cosmo'), Js('Coy'), Js('Crimson'), Js('Curse'), Js('Daemon'), Js('Dale'), Js('Darth'), Js('Dirk'), Js('Dolor'), Js('Drake'), Js('Duke'), Js('Dune'), Js('Dusty'), Js('Echo'), Js('Edge'), Js('Fiend'), Js('Fink'), Js('Flare'), Js('Flint'), Js('Forest'), Js('Frank'), Js('Furor'), Js('Gale'), Js('Gall'), Js('Gallant'), Js('Garotte'), Js('Ghoul'), Js('Giddy'), Js('Glint'), Js('Gloom'), Js('Glum'), Js('Grant'), Js('Grim'), Js('Grisly'), Js('Grit'), Js('Grog'), Js('Grub'), Js('Guillotine'), Js('Haggard'), Js('Hallow'), Js('Harm'), Js('Havoc'), Js('Hazard'), Js('Hog'), Js('Honor'), Js('Hunter'), Js('Insidious'), Js('Ire'), Js('Jack'), Js('Jasper'), Js('Jet'), Js('Jimmy'), Js('Jinx'), Js('Junior'), Js('Justice'), Js('Kindle'), Js('Kirk'), Js('Knave'), Js('Kris'), Js('Lament'), Js('Lance'), Js('Lore'), Js('Lynx'), Js('Lyric'), Js('Magnum'), Js('Mane'), Js('Mark'), Js('Mars'), Js('Maverick'), Js('Max'), Js('Maze'), Js('Meddle'), Js('Menace'), Js('Miles'), Js('Morrow'), Js('Mortar'), Js('Morte'), Js('Nick'), Js('Norm'), Js('Obsidian'), Js('Ocean'), Js('Omen'), Js('Onyx'), Js('Page'), Js('Pale'), Js('Paragon'), Js('Parker'), Js('Parrish'), Js('Pester'), Js('Phoenix'), Js('Picket'), Js('Proffer'), Js('Putrid'), Js('Pyre'), Js('Quell'), Js('Quill'), Js('Rage'), Js('Ray'), Js('Raze'), Js('Rebel'), Js('Red'), Js('Requiem'), Js('Riot'), Js('River'), Js('Rob'), Js('Rock'), Js('Rod'), Js('Rogue'), Js('Ruckus'), Js('Ruffian'), Js('Rum'), Js('Rusty'), Js('Saber'), Js('Sable'), Js('Sage'), Js('Sane'), Js('Savage'), Js('Scalawag'), Js('Scourge'), Js('Severus'), Js('Shade'), Js('Sinew'), Js('Slate'), Js('Slick'), Js('Slug'), Js('Sly'), Js('Snarl'), Js('Snitch'), Js('Spark'), Js('Spectre'), Js('Stain'), Js('Sterling'), Js('Storm'), Js('Stout'), Js('Strife'), Js('Sullen'), Js('Sully'), Js('Talon'), Js('Tax'), Js('Taylor'), Js('Teal'), Js('Tenor'), Js('Thorn'), Js('Torpid'), Js('Trinket'), Js('Tuck'), Js('Tucker'), Js('Vain'), Js('Venom'), Js('Venture'), Js('Verve'), Js('Vex'), Js('Victor'), Js('Vigor'), Js('Wicked'), Js('Will'), Js('Wily'), Js('Woe'), Js('Wolf'), Js('Wrath'), Js('Wright'), Js('Zeal'), Js('Zero'), Js('Zilch')]))
var.put('nm2', Js([Js('Affinity'), Js('Agate'), Js('Agony'), Js('Alma'), Js('Amber'), Js('Angel'), Js('Anima'), Js('Answer'), Js('Apathy'), Js('Apple'), Js('Aria'), Js('Ash'), Js('Atrophy'), Js('August'), Js('Aura'), Js('Aurora'), Js('Autumn'), Js('Banshee'), Js('Blaze'), Js('Blemish'), Js('Blight'), Js('Bliss'), Js('Blithe'), Js('Blitz'), Js('Bonnie'), Js('Breeze'), Js('Brook'), Js('Cadence'), Js('Caprice'), Js('Carmine'), Js('Carol'), Js('Cat'), Js('Cerise'), Js('Chance'), Js('Charity'), Js('Chastity'), Js('Chimera'), Js('Cicatrix'), Js('Cinnamon'), Js('Claret'), Js('Clover'), Js('Coral'), Js('Cosmo'), Js('Crystal'), Js('Cynthia'), Js('Dahlia'), Js('Daphne'), Js('Darling'), Js('Dawn'), Js('Desire'), Js('Destiny'), Js('Dew'), Js('Diamond'), Js('Distress'), Js('Dolorous'), Js('Drew'), Js('Ebony'), Js('Echo'), Js('Ember'), Js('Empathy'), Js('Enigma'), Js('Ennui'), Js('Erica'), Js('Erin'), Js('Euphoria'), Js('Eve'), Js('Faith'), Js('Fatality'), Js('Fawn'), Js('Feather'), Js('Felicity'), Js('Fern'), Js('Fever'), Js('Flare'), Js('Flora'), Js('Gem'), Js('Ginger'), Js('Goldie'), Js('Grace'), Js('Grief'), Js('Hail'), Js('Harmony'), Js('Hazel'), Js('Heirloom'), Js('Holly'), Js('Hope'), Js('Indigo'), Js('Iris'), Js('Isle'), Js('Ivory'), Js('Ivy'), Js('Jade'), Js('Jasmine'), Js('Jeopardy'), Js('Jewel'), Js('Joy'), Js('June'), Js('Juniper'), Js('Karma'), Js('Kat'), Js('Kelpie'), Js('Kitty'), Js('Laurel'), Js('Legacy'), Js('Liberty'), Js('Lily'), Js('Lullaby'), Js('Luna'), Js('Lyric'), Js('Mae'), Js('Magnolia'), Js('Magpie'), Js('Malady'), Js('Malaise'), Js('Melody'), Js('Merry'), Js('Mettle'), Js('Mirage'), Js('Mirth'), Js('Misery'), Js('Misty'), Js('Morgana'), Js('Muse'), Js('Mystery'), Js('Novelty'), Js('Oceane'), Js('Olive'), Js('Onyx'), Js('Opal'), Js('Oracle'), Js('Page'), Js('Paige'), Js('Paradox'), Js('Parody'), Js('Patience'), Js('Pearl'), Js('Penny'), Js('Penury'), Js('Pepper'), Js('Peril'), Js('Phoenix'), Js('Pixie'), Js('Psyche'), Js('Pyre'), Js('Raine'), Js('Rarity'), Js('Raven'), Js('Ravish'), Js('Riddle'), Js('River'), Js('Rose'), Js('Rosemary'), Js('Ruby'), Js('Rune'), Js('Ruth'), Js('Sable'), Js('Saffron'), Js('Sage'), Js('Sapphire'), Js('Saturninity'), Js('Scarlet'), Js('Scout'), Js('Serenity'), Js('Serpente'), Js('Shade'), Js('Shenanigan'), Js('Sierra'), Js('Sky'), Js('Skye'), Js('Soots'), Js('Sorrow'), Js('Spectacle'), Js('Sphinx'), Js('Spirit'), Js('Stigma'), Js('Storm'), Js('Summer'), Js('Sybil'), Js('Tawny'), Js('Teal'), Js('Tempest'), Js('Thorne'), Js('Thriller'), Js('Tinder'), Js('Tragedy'), Js('Trinity'), Js('Trinket'), Js('Twilight'), Js('Velleity'), Js('Velvet'), Js('Venus'), Js('Vex'), Js('Vice'), Js('Violet'), Js('Viper'), Js('Volley'), Js('Willow'), Js('Winter'), Js('Woe'), Js('Wraith')]))
var.put('nm3', Js([Js('Ache'), Js('Adroit'), Js('Alabaster'), Js('Alias'), Js('Amity'), Js('Anchor'), Js('Angel'), Js('Anguish'), Js('Anomaly'), Js('Arete'), Js('Argent'), Js('Armor'), Js('Arrow'), Js('Ash'), Js('Askew'), Js('Asset'), Js('Awry'), Js('Ballad'), Js('Ballaster'), Js('Bard'), Js('Bargain'), Js('Baron'), Js('Barrow'), Js('Battle'), Js('Beacon'), Js('Beggar'), Js('Belch'), Js('Belcher'), Js('Bellow'), Js('Binder'), Js('Black'), Js('Blade'), Js('Blank'), Js('Blood'), Js('Bloodworth'), Js('Bolt'), Js('Bond'), Js('Bones'), Js('Boon'), Js('Boor'), Js('Boulder'), Js('Bounty'), Js('Bovine'), Js('Brand'), Js('Brawn'), Js('Broke'), Js('Bruiser'), Js('Bullet'), Js('Burden'), Js('Burn'), Js('Burrow'), Js('Butler'), Js('Buzzard'), Js('Cairn'), Js('Caliber'), Js('Calibre'), Js('Candor'), Js('Cane'), Js('Carver'), Js('Cash'), Js('Castle'), Js('Chalice'), Js('Champion'), Js('Chance'), Js('Chase'), Js('Chosen'), Js('Cite'), Js('Clay'), Js('Cloud'), Js('Cole'), Js('Conceit'), Js('Couture'), Js('Cove'), Js('Craft'), Js('Crass'), Js('Crimson'), Js('Cross'), Js('Crumb'), Js('Crypt'), Js('Demise'), Js('Destiny'), Js('Diablo'), Js('Dolor'), Js('Doom'), Js('Drake'), Js('Dread'), Js('Eliminate'), Js('Epitome'), Js('Fable'), Js('Fade'), Js('Fang'), Js('Fatality'), Js('Festoon'), Js('Fletcher'), Js('Fortune'), Js('Foster'), Js('Frost'), Js('Gamble'), Js('Garland'), Js('Glass'), Js('Gold'), Js('Grave'), Js('Graves'), Js('Gripe'), Js('Grove'), Js('Grumble'), Js('Halo'), Js('Harsh'), Js('Heart'), Js('Heaven'), Js('Heirloom'), Js('Hook'), Js('Horn'), Js('Howler'), Js('Humble'), Js('Hunt'), Js('Incognito'), Js('Jinx'), Js('Lament'), Js('Largesse'), Js('Legacy'), Js('Lexicon'), Js('Luck'), Js('Memento'), Js('Mercy'), Js('Merit'), Js('Mock'), Js('Mondo'), Js('Mourn'), Js('Mute'), Js('Mystery'), Js('Myth'), Js('Nemesis'), Js('Nemo'), Js('Nova'), Js('Noxious'), Js('Oblivion'), Js('Obscure'), Js('Occult'), Js('Omnibus'), Js('Pain'), Js('Paradox'), Js('Patience'), Js('Pierce'), Js('Price'), Js('Quest'), Js('Rapture'), Js('Razor'), Js('Remedy'), Js('Remorse'), Js('Repose'), Js('Reserve'), Js('Reverse'), Js('Riddle'), Js('Rube'), Js('Rue'), Js('Ruth'), Js('Sanguine'), Js('Scope'), Js('Secret'), Js('Serpent'), Js('Shade'), Js('Shields'), Js('Silence'), Js('Silver'), Js('Sin'), Js('Skinner'), Js('Snow'), Js('Stitch'), Js('Stone'), Js('Storm'), Js('Strait'), Js('Sulk'), Js('Swagger'), Js('Swift'), Js('Sythe'), Js('Terminal'), Js('Token'), Js('Tomb'), Js('Torment'), Js('Trace'), Js('Trinket'), Js('Triumph'), Js('Truth'), Js('Twist'), Js('Unity'), Js('Vaunt'), Js('Veil'), Js('Vermin'), Js('Vigil'), Js('Vile'), Js('Virtue'), Js('Vista'), Js('Ward'), Js('Whisper'), Js('White'), Js('Woods'), Js('Worth'), Js('Wretch'), Js('Zephyr')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('d'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('z')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ue'), Js('au'), Js('io'), Js('ia'), Js('ie'), Js('ei'), Js('ai')]))
var.put('nm6', Js([Js('d'), Js('dd'), Js('dr'), Js('ff'), Js('fr'), Js('g'), Js('gr'), Js('gn'), Js('gm'), Js('k'), Js('kk'), Js('kn'), Js('l'), Js('ll'), Js('ln'), Js('lm'), Js('m'), Js('mm'), Js('mr'), Js('n'), Js('nn'), Js('nr'), Js('nd'), Js('nv'), Js('nt'), Js('ph'), Js('rk'), Js('rg'), Js('rq'), Js('rv'), Js('rf'), Js('rb'), Js('rd'), Js('rl'), Js('rm'), Js('s'), Js('ss'), Js('sh'), Js('sl'), Js('sr'), Js('sn'), Js('st'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('vr'), Js('d'), Js('d'), Js('g'), Js('g'), Js('k'), Js('k'), Js('l'), Js('l'), Js('l'), Js('m'), Js('m'), Js('n'), Js('n'), Js('s'), Js('s'), Js('t'), Js('t'), Js('v'), Js('v')]))
var.put('nm7', Js([Js(''), Js(''), Js('l'), Js('n'), Js('s'), Js('th')]))
pass
pass


# Add lib to the module scope
skulduggeryNames = var.to_python()