__all__ = ['mgtTroll']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm4').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                if (var.get('i')<Js(3.0)):
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3'))))
                else:
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd3')),var.get('nm3').get(var.get('rnd4'))):
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd3'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm5').get(var.get('rnd')),var.get('nm6').get(var.get('rnd2'))):
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('names', (((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+Js(' '))+var.get('nm7').get(var.get('rnd3'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm8').get(var.get('rnd'))+Js(' '))+var.get('nm7').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('bh'), Js('br'), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gh'), Js('gr'), Js('kh'), Js('khr'), Js('r'), Js('th'), Js('tr'), Js('thr'), Js('v'), Js('z'), Js('zh')]))
var.put('nm2', Js([Js('u'), Js('u'), Js('u'), Js('u'), Js('u'), Js('o'), Js('a')]))
var.put('nm3', Js([Js('b'), Js('bv'), Js('bb'), Js('bl'), Js('d'), Js('dd'), Js('dr'), Js('dv'), Js('dz'), Js('g'), Js('gg'), Js('gl'), Js('gn'), Js('gv'), Js('gz'), Js('k'), Js('kk'), Js('kl'), Js('kv'), Js('lb'), Js('ld'), Js('lg'), Js('l'), Js('ll'), Js('ln'), Js('lr'), Js('lt'), Js('lz'), Js('lv'), Js('m'), Js('md'), Js('mg'), Js('ml'), Js('mr'), Js('mz'), Js('nd'), Js('nv'), Js('nz'), Js('nl'), Js('nd'), Js('ndr'), Js('ng'), Js('ngr'), Js('ngb'), Js('ngz'), Js('r'), Js('rr'), Js('rl'), Js('rv'), Js('rz'), Js('v'), Js('vl'), Js('vn'), Js('z'), Js('zd'), Js('zg'), Js('zl'), Js('zn')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('l'), Js('lg'), Js('ld'), Js('n'), Js('ng'), Js('nd'), Js('rd'), Js('rg')]))
var.put('nm5', Js([Js('amber'), Js('ash'), Js('bitter'), Js('blaze'), Js('blunt'), Js('bone'), Js('boulder'), Js('brick'), Js('bristle'), Js('broad'), Js('cave'), Js('cinder'), Js('claw'), Js('crag'), Js('dim'), Js('dirge'), Js('dust'), Js('far'), Js('fern'), Js('flask'), Js('flint'), Js('fog'), Js('fore'), Js('forge'), Js('gloom'), Js('grand'), Js('gravel'), Js('grim'), Js('heavy'), Js('hill'), Js('horn'), Js('keen'), Js('krag'), Js('lone'), Js('low'), Js('moss'), Js('mourn'), Js('mud'), Js('oat'), Js('orb'), Js('pale'), Js('pyre'), Js('rend'), Js('saur'), Js('shadow'), Js('skull'), Js('sky'), Js('slate'), Js('snake'), Js('spore'), Js('stone'), Js('tall'), Js('terra'), Js('tree'), Js('tusk'), Js('whit'), Js('wild')]))
var.put('nm6', Js([Js('back'), Js('bane'), Js('beam'), Js('belly'), Js('belt'), Js('bend'), Js('blade'), Js('blight'), Js('bough'), Js('braid'), Js('branch'), Js('brand'), Js('breath'), Js('brew'), Js('bridge'), Js('brow'), Js('claw'), Js('crag'), Js('crest'), Js('flare'), Js('flaw'), Js('force'), Js('fury'), Js('gaze'), Js('grip'), Js('grog'), Js('gut'), Js('hide'), Js('hood'), Js('horn'), Js('howl'), Js('husk'), Js('jaw'), Js('lance'), Js('lash'), Js('limb'), Js('lock'), Js('mane'), Js('mark'), Js('maw'), Js('scar'), Js('scrub'), Js('shard'), Js('shroud'), Js('snarl'), Js('spine'), Js('stride'), Js('strike'), Js('stub'), Js('surge'), Js('toe'), Js('trap')]))
var.put('nm7', Js([Js('Aggressor'), Js('Assailant'), Js('Barbarian'), Js('Battler'), Js('Brawler'), Js('Bruiser'), Js('Brute'), Js('Bully'), Js('Castaway'), Js('Degenerate'), Js('Derelict'), Js('Exile'), Js('Fiend'), Js('Hireling'), Js('Merc'), Js('Mercenary'), Js('Outcast'), Js('Sadist'), Js('Savage'), Js('Scrapper'), Js('Shaman'), Js('Slugger'), Js('Troll'), Js('Troll'), Js('Troll'), Js('Troll'), Js('Troll'), Js('Troll'), Js('Troll'), Js('Troll'), Js('Troll'), Js('Troll'), Js('Troll'), Js('Troll'), Js('Troll'), Js('Trow'), Js('Trow'), Js('Trow'), Js('Trow'), Js('Trow'), Js('Trow'), Js('Vagabond'), Js('Vagrant'), Js('Warrior'), Js('Wildcat'), Js('Wildling'), Js('Wretch')]))
var.put('nm8', Js([Js('Abandoned'), Js('Aching'), Js('Aged'), Js('Aggressive'), Js('Albino'), Js('Ancient'), Js('Angry'), Js('Anxious'), Js('Arctic'), Js('Bitter'), Js('Blind'), Js('Bony'), Js('Broken'), Js('Bruised'), Js('Bush'), Js('Careless'), Js('Cave'), Js('Cavern'), Js('Charging'), Js('Clever'), Js('Clueless'), Js('Clumsy'), Js('Colossal'), Js('Confused'), Js('Corrupt'), Js('Corrupted'), Js('Crafty'), Js('Crooked'), Js('Cruel'), Js('Defiant'), Js('Diligent'), Js('Dull'), Js('Eager'), Js('Elder'), Js('Enraged'), Js('Fearless'), Js('Feisty'), Js('Fickle'), Js('Forest'), Js('Forsaken'), Js('Fungus'), Js('Gloomy'), Js('Grave'), Js('Greedy'), Js('Grim'), Js('Grotesque'), Js('Harvester'), Js('Haunting'), Js('Hedge'), Js('Hidden'), Js('Horned'), Js('Hungry'), Js('Hunting'), Js('Jaded'), Js('Jungle'), Js('Juvenile'), Js('Lanky'), Js('Limping'), Js('Lone'), Js('Lost'), Js('Lumbering'), Js('Marsh'), Js('Meager'), Js('Mountain'), Js('Noxious'), Js('Numb'), Js('Oblivious'), Js('Ocean'), Js('Powerful'), Js('Primal'), Js('Prime'), Js('Pygmy'), Js('Rash'), Js('Reckless'), Js('River'), Js('Sea'), Js('Selfish'), Js('Shady'), Js('Shameless'), Js('Skinny'), Js('Sneaking'), Js('Sneaky'), Js('Sniveling'), Js('Swamp'), Js('Swift'), Js('Troubled'), Js('Twin'), Js('Vicious'), Js('Vile'), Js('Wicked'), Js('Wrathful'), Js('Wretched')]))
pass
pass


# Add lib to the module scope
mgtTroll = var.to_python()