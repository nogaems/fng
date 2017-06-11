__all__ = ['witchCovens']

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
    var.registers(['nm1', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Aether'), Js('Ancient'), Js('Ancient Oak'), Js('Aurora'), Js('Azure'), Js('Balance'), Js('Beating Heart'), Js('Blue Moon'), Js('Boulder'), Js('Bramble Root'), Js('Brilliant Light'), Js('Cascade'), Js('Cedar Grove'), Js('Chalice'), Js('Charity'), Js('Clarity'), Js('Community'), Js('Compassion'), Js('Convert'), Js('Crescent'), Js('Crescent Moon'), Js('Crystal Flower'), Js('Crystal Garden'), Js('Crystal Lake'), Js('Crystal Rose'), Js('Discovery'), Js('Divine'), Js('Divine Dream'), Js('Divine Energy'), Js('Divine Journey'), Js('Divine Spirit'), Js('Divine Teachings'), Js('Divine Touch'), Js('Dream'), Js('Earth Spirit'), Js('Earth Temple'), Js('Earthen'), Js('Eclipse'), Js('Elder Flame'), Js('Elder Grove'), Js('Elemental'), Js('Elemental Grove'), Js('Elysium'), Js('Ember'), Js('Enchanted'), Js('Enchanted Moon'), Js('Enchanted Tree'), Js('Enlightened'), Js('Equinox'), Js('Eternal Flame'), Js('Eternal Garden'), Js('Eternal Light'), Js('Eternal Teachings'), Js('Eternity'), Js('Fae Woods'), Js('Faery Tree'), Js('Forest Grove'), Js('Forest Path'), Js('Fortuna'), Js('Freedom'), Js('Full Moon'), Js('Goddess'), Js('Grass Roots'), Js('Grove'), Js('Guiding Hand'), Js('Hallowed'), Js('Hallowed Guide'), Js('Harmony'), Js('Harvest'), Js('Healing'), Js('Hyacinth'), Js('Ice Garden'), Js('Illuminated'), Js('Illumination'), Js('Independence'), Js('Infinity'), Js('Knowledge'), Js('Lady Fortune'), Js('Liberty'), Js('Light'), Js('Lode Star'), Js('Lone Star'), Js('Lunar'), Js('Lunar Owl'), Js('Medicine'), Js('Midnight'), Js('Mirror'), Js('Mirror Lake'), Js('Moon'), Js('Moon Oasis'), Js('Moon Siren'), Js('Moon Temple'), Js('Moon Thicket'), Js('Moon Thread'), Js('Moonlight'), Js('Moonlit'), Js('Moonlit Cloud'), Js('Moonrise'), Js('Morning Dew'), Js('Morning Star'), Js('Mountain Rose'), Js('Mystic'), Js('Mystic Grove'), Js('Night Garden'), Js('Night Grove'), Js('Nightshade'), Js('Nightshadow'), Js('Nightsky'), Js('Oak Spirit'), Js('Oasis'), Js('Observation'), Js('Patience'), Js('Pentacle'), Js('Phoenix Fire'), Js('Presence'), Js('Quiet Meadows'), Js('Radiant Heart'), Js('Raven'), Js("Raven's Nest"), Js('Requiem'), Js('Revolution'), Js('Rising Sun'), Js('River'), Js('Rowan Tree'), Js('Sacred'), Js('Sacred Flame'), Js('Sacred Journey'), Js('Sacred Meadows'), Js('Sacred Voyage'), Js('Sacred Well'), Js('Serenity'), Js('Setting Sun'), Js('Shadowmoon'), Js('Silver'), Js('Silver Branch'), Js('Silver Cloud'), Js('Silver Flame'), Js('Silver Flock'), Js('Silver Grace'), Js('Silver Grass'), Js('Silver Lake'), Js('Silver Moon'), Js('Silver Reserve'), Js('Silver Sliver'), Js('Silver Star'), Js('Silver Thread'), Js('Silverbark'), Js('Solar'), Js('Spiral Tree'), Js('Spirit Drum'), Js('Spirit Energy'), Js('Spirit Lake'), Js('Stardust'), Js('Starfall'), Js('Starlight'), Js('Sunset'), Js('Tree Roots'), Js('Trillium Moon'), Js('Trinity'), Js('Twilight'), Js('Twilight Flame'), Js('Twilight Goddess'), Js('Twilight Grove'), Js('Unseen Moon'), Js('Voyage'), Js('White Lotus'), Js('White Tree'), Js('Willow'), Js('Wisdom'), Js('World Tree')]))
    var.put('nm2', Js([Js('Azure'), Js('Balance'), Js('Charity'), Js('Clarity'), Js('Community'), Js('Compassion'), Js('Discovery'), Js('Divine Energy'), Js('Divine Teachings'), Js('Elysium'), Js('Ember'), Js('Eternal Teachings'), Js('Eternity'), Js('Fortuna'), Js('Freedom'), Js('Harmony'), Js('Healing'), Js('Illumination'), Js('Independence'), Js('Infinity'), Js('Knowledge'), Js('Lady Fortune'), Js('Liberty'), Js('Medicine'), Js('Midnight'), Js('Moonlight'), Js('Morning Dew'), Js('Nightshade'), Js('Nightshadow'), Js('Observation'), Js('Patience'), Js('Phoenix Fire'), Js('Presence'), Js('Requiem'), Js('Sacred Meadows'), Js('Serenity'), Js('Shadowmoon'), Js('Silver'), Js('Silver Grace'), Js('Silver Grass'), Js('Spirit Energy'), Js('Stardust'), Js('Starfall'), Js('Starlight'), Js('Tree Roots'), Js('Twilight'), Js('Wisdom'), Js('the Aether'), Js('the Ancient'), Js('the Ancient Oak'), Js('the Aurora'), Js('the Beating Heart'), Js('the Blue Moon'), Js('the Boulder'), Js('the Bramble Root'), Js('the Brilliant Light'), Js('the Cascade'), Js('the Cedar Grove'), Js('the Chalice'), Js('the Convert'), Js('the Crescent'), Js('the Crescent Moon'), Js('the Crystal Flower'), Js('the Crystal Garden'), Js('the Crystal Lake'), Js('the Crystal Rose'), Js('the Divine'), Js('the Divine Dream'), Js('the Divine Journey'), Js('the Divine Spirit'), Js('the Divine Touch'), Js('the Dream'), Js('the Earth Spirit'), Js('the Earth Temple'), Js('the Earthen'), Js('the Eclipse'), Js('the Elder Flame'), Js('the Elder Grove'), Js('the Elemental'), Js('the Elemental Grove'), Js('the Enchanted'), Js('the Enchanted Moon'), Js('the Enchanted Tree'), Js('the Enlightened'), Js('the Equinox'), Js('the Eternal Flame'), Js('the Eternal Garden'), Js('the Eternal Light'), Js('the Fae Woods'), Js('the Faery Tree'), Js('the Forest Grove'), Js('the Forest Path'), Js('the Full Moon'), Js('the Goddess'), Js('the Grass Roots'), Js('the Grove'), Js('the Guiding Hand'), Js('the Hallowed'), Js('the Hallowed Guide'), Js('the Harvest'), Js('the Hyacinth'), Js('the Ice Garden'), Js('the Illuminated'), Js('the Light'), Js('the Lode Star'), Js('the Lone Star'), Js('the Lunar Owl'), Js('the Mirror'), Js('the Mirror Lake'), Js('the Moon'), Js('the Moon Oasis'), Js('the Moon Siren'), Js('the Moon Temple'), Js('the Moon Thicket'), Js('the Moon Thread'), Js('the Moonlit'), Js('the Moonlit Cloud'), Js('the Moonrise'), Js('the Morning Star'), Js('the Mountain Rose'), Js('the Mystic'), Js('the Mystic Grove'), Js('the Night Garden'), Js('the Night Grove'), Js('the Night Sky'), Js('the Oak Spirit'), Js('the Oasis'), Js('the Pentacle'), Js('the Quiet Meadows'), Js('the Radiant Heart'), Js('the Raven'), Js("the Raven's Nest"), Js('the Revolution'), Js('the Rising Sun'), Js('the River'), Js('the Rowan Tree'), Js('the Sacred Flame'), Js('the Sacred Journey'), Js('the Sacred One'), Js('the Sacred Voyage'), Js('the Sacred Well'), Js('the Setting Sun'), Js('the Silver Branch'), Js('the Silver Cloud'), Js('the Silver Flame'), Js('the Silver Flock'), Js('the Silver Lake'), Js('the Silver Moon'), Js('the Silver Reserve'), Js('the Silver Sliver'), Js('the Silver Star'), Js('the Silver Thread'), Js('the Silverbark'), Js('the Spiral Tree'), Js('the Spirit Drum'), Js('the Spirit Lake'), Js('the Sun'), Js('the Sunset'), Js('the Trillium Moon'), Js('the Trinity'), Js('the Twilight Flame'), Js('the Twilight Goddess'), Js('the Twilight Grove'), Js('the Unseen Moon'), Js('the Voyage'), Js('the White Lotus'), Js('the White Tree'), Js('the Willow'), Js('the World Tree')]))
    var.put('nm3', Js([Js('Coven'), Js('Circle'), Js('Sisters'), Js('Wives'), Js('Witches'), Js('Coven'), Js('Coven'), Js('Circle'), Js('Circle'), Js('Coven')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm3').get(var.get('rnd2'))+Js(' of '))+var.get('nm2').get(var.get('rnd'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
witchCovens = var.to_python()