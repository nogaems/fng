__all__ = ['apocalypseTowns']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('names', var.get('names1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Canyon Brook'), Js('Lakeside Ruins'), Js('Broken Metro'), Js('Acropolis Wreck'), Js('Banesteppe'), Js('Ash Valley'), Js('Sanctum Mesa'), Js('Crashpoint'), Js('Withermarsh'), Js('Murkshore'), Js('Concrete Jungle'), Js('Atrophy Wharf'), Js('Abandale'), Js('Ailmoor'), Js('Ailton'), Js('Anguith'), Js('Armagetown'), Js('Ashbourne'), Js('Ashshore'), Js('Ashtown'), Js('Atrophy'), Js('Baneville'), Js('Bareton'), Js('Bartertown'), Js("Beggar's End"), Js('Bilgewaters'), Js('Blackridge'), Js('Blightown'), Js('Blightville'), Js('Blissville'), Js('Boomtown'), Js('Borderville'), Js('Boundington'), Js('Breaktown'), Js('Burnington'), Js('Burnsley'), Js('Carnage'), Js('Carthage'), Js('Catatonia'), Js('Cavity'), Js('Ceaseton'), Js('Charcity'), Js('Charington'), Js('Cinders'), Js('City of Darwin'), Js('Closure'), Js('Cloudville'), Js('Corruptown'), Js('Crashmere'), Js('Crishire'), Js('Cruelfeld'), Js('Cruelfield'), Js('Crumbleton'), Js('Crumblewall'), Js('Curtain Falls'), Js('Cussington'), Js('Darkington'), Js('Dawnbury'), Js('Dawnford'), Js('Deadline'), Js('Deciville'), Js('Defacity'), Js('Defectown'), Js('Demonarm'), Js('Demonia'), Js('Desolation City'), Js('Destinus'), Js('Devils Fork'), Js('Diaborough'), Js('Direfall'), Js('Direfield'), Js('Ditchford'), Js('Doomcaster'), Js('Doomsbury'), Js('Doomville'), Js('Dreadville'), Js('Ecstacity'), Js('Eden'), Js('Edgetown'), Js('Elysium'), Js('Emberville'), Js('Emitton'), Js('Endcliff'), Js('Endsby'), Js('Eternity'), Js('Evermore'), Js('Everwinter'), Js('Expocity'), Js('Extinctown'), Js('Extremire'), Js('Felicity'), Js('Festerchapel'), Js('Festerfield'), Js('Festerville'), Js('Final Falls'), Js('Firebend'), Js('Foolshope'), Js('Forsaken Falls'), Js('Gloomville'), Js('Grieford'), Js('Grieftown'), Js('Grimburg'), Js('Gutterville'), Js('Guttown'), Js('Harmony'), Js('Havoc'), Js('Hazardine'), Js('Hells Gate'), Js('Hells Point'), Js('Hope Falls'), Js('Hope Rises'), Js('Horriford'), Js('Illmoor'), Js('Isolon'), Js('Isolone'), Js('Jericho'), Js('Karma'), Js('Kilead'), Js('Killmoor'), Js('Killville'), Js('Leaveside'), Js('Lightsville'), Js('Lost Angeles'), Js('Malady'), Js('Malaise'), Js('Malicity'), Js('Malimoor'), Js('Maraud'), Js('Mauseleum'), Js("Men's Rest"), Js('Mensfield'), Js('Miraclesfield'), Js('Misery'), Js('Moonblight'), Js('Murkville'), Js('Necroshire'), Js('Nefaria'), Js('Nemesis'), Js('Netherville'), Js('Nirvana'), Js('Paradise Falls'), Js('Pearly Gates'), Js('Perile'), Js('Perishton'), Js('Phantown'), Js('Pleasureville'), Js('Postville'), Js('Precipire'), Js('Privacity'), Js('Project Hope'), Js('Promise'), Js('Purgatory'), Js('Quellton'), Js('Quietus'), Js('Remorse'), Js('Repocity'), Js('Revoltown'), Js('Rottingham'), Js('Safari'), Js('Scramton'), Js('Scythe'), Js('Seclusion'), Js('Serenity'), Js('Slumberville'), Js('Snowmelt'), Js('Solaris'), Js('Solitude'), Js('Spoilford'), Js('Surmise'), Js('Taintborne'), Js('Taintchapel'), Js('Taintside'), Js('Termina'), Js('Terminus'), Js('The Barrens'), Js('The Blanks'), Js('The Boons'), Js('The Bounds'), Js('The Confines'), Js('The Curtains'), Js('The Dumps'), Js('The Falls'), Js('The Hub'), Js('The Mopes'), Js('The Nether'), Js('The Projects'), Js('The Prospects'), Js('The Shadows'), Js('The Skids'), Js('The Verdicts'), Js('The Void'), Js('The Wickeds'), Js('Tradesburg'), Js('Transfere'), Js('Turnville'), Js('Utopia'), Js('Vacancy'), Js('Victorville'), Js('Vileville'), Js('Vilewaters'), Js('Voidville'), Js('Wakefield'), Js('Wickhills'), Js('Windgrip'), Js('Witherbury'), Js('Withergate'), Js('Withervale'), Js('Woeford'), Js('Wolfwater'), Js('Wrathford'), Js('Wreckville'), Js('Zion')]))
pass
pass


# Add lib to the module scope
apocalypseTowns = var.to_python()