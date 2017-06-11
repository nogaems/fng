__all__ = ['spellDescriptions']

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
    var.registers(['nm1', 'rnd15', 'rnd11', 'rnd8', 'name', 'name7', 'nm3', 'rnd14', 'name3', 'name6', 'nm2', 'rnd2', 'name9', 'br', 'name2', 'nm7', 'name4', 'rnd5', 'rnd4', 'rnd10b', 'rnd7', 'name8', 'result', 'nm6', 'rnd6', 'rnd2b', 'rnd13', 'nm4', 'rnd3', 'nm8', 'name5', 'rnd16', 'rnd10', 'rnd9', 'rnd12', 'rnd1'])
    var.put('nm1', Js([Js('Aug'), Js('Corrupt'), Js('Deflect'), Js('Dupl'), Js('Ech'), Js('Ejec'), Js('Erec'), Js('Evic'), Js('Evict'), Js('Exp'), Js('Exting'), Js('Ignit'), Js('Ill'), Js('Imb'), Js('Imm'), Js('Incant'), Js('Incent'), Js('Incept'), Js('Invoc'), Js('Lag'), Js('Magn'), Js('Mend'), Js('Morph'), Js('Muffl'), Js('Oblit'), Js('Obsc'), Js('Pest'), Js('Petrif'), Js('Port'), Js('Purif'), Js('Rect'), Js('Refl'), Js('Reflect'), Js('Sanc'), Js('Sanct'), Js('Scorch'), Js('Slug'), Js('Supr'), Js('Tranq'), Js('Trans'), Js('Alte'), Js('Alter'), Js('Apear'), Js('Aper'), Js('Ara'), Js('Augmen'), Js('Clar'), Js('Clari'), Js('Confus'), Js('Conju'), Js('Conjur'), Js('Cor'), Js('Corrup'), Js('Cur'), Js('Decim'), Js('Defen'), Js('Deler'), Js('Depres'), Js('Depri'), Js('Descen'), Js('Divi'), Js('Ethe'), Js('Ether'), Js('Evi'), Js('Expel'), Js('Expul'), Js('Exte'), Js('Extermi'), Js('Extermin'), Js('Exti'), Js('Fier'), Js('Fir'), Js('Flar'), Js('Fluo'), Js('Igni'), Js('Illumi'), Js('Immol'), Js('Immun'), Js('Imped'), Js('Impedim'), Js('Imper'), Js('Incen'), Js('Incre'), Js('Increm'), Js('Incren'), Js('Inter'), Js('Iso'), Js('Isol'), Js('Lev'), Js('Levi'), Js('Levita'), Js('Libe'), Js('Liber'), Js('Loco'), Js('Locomo'), Js('Lum'), Js('Lumi'), Js('Magni'), Js('Mobi'), Js('Mobil'), Js('Mor'), Js('Muf'), Js('Mystif'), Js('Neur'), Js('Neural'), Js('Ob'), Js('Obli'), Js('Obliter'), Js('Pes'), Js('Pesti'), Js('Pet'), Js('Petri'), Js('Por'), Js('Porta'), Js('Pro'), Js('Prot'), Js('Puri'), Js('Quen'), Js('Re'), Js('Red'), Js('Redu'), Js('Rege'), Js('Regen'), Js('Rejuvi'), Js('Rel'), Js('Releas'), Js('Reno'), Js('Rep'), Js('Repa'), Js('Repe'), Js('Repel'), Js('Restor'), Js('Revi'), Js('Sco'), Js('Scor'), Js('Ser'), Js('Sever'), Js('Shri'), Js('Sil'), Js('Silen'), Js('Slu'), Js('Stu'), Js('Stup'), Js('Supres'), Js('Tra'), Js('Tranqi'), Js('Venge')]))
    var.put('nm2', Js([Js('a'), Js('actum'), Js('actus'), Js('arbus'), Js('armus'), Js('aro'), Js('ashio'), Js('asi'), Js('asis'), Js('aris'), Js('ate'), Js('ecto'), Js('ectum'), Js('ectus'), Js('ego'), Js('egra'), Js('egris'), Js('elio'), Js('ello'), Js('em'), Js('empra'), Js('endio'), Js('endius'), Js('endo'), Js('enim'), Js('enis'), Js('enta'), Js('entus'), Js('enum'), Js('enus'), Js('eo'), Js('eom'), Js('eos'), Js('eous'), Js('erbus'), Js('ergio'), Js('erio'), Js('eris'), Js('erous'), Js('es'), Js('esco'), Js('eseo'), Js('etus'), Js('eum'), Js('eus'), Js('i'), Js('iate'), Js('iatis'), Js('iato'), Js('ictum'), Js('ictus'), Js('icum'), Js('icus'), Js('id'), Js('igeo'), Js('im'), Js('indo'), Js('inio'), Js('inius'), Js('io'), Js('ior'), Js('is'), Js('iseo'), Js('ite'), Js('iteus'), Js('itus'), Js('ium'), Js('ius'), Js('orgio'), Js('ori'), Js('orpus'), Js('ortia'), Js('ortis'), Js('ortus'), Js('orus'), Js('otis'), Js('otum'), Js('ucio'), Js('ucto'), Js('ula'), Js('ulsi'), Js('ulsis'), Js('ulso'), Js('ulus'), Js('um'), Js('undis'), Js('undo'), Js('uno'), Js('uro'), Js('us')]))
    var.put('nm3', Js([Js('Anim'), Js('Anno'), Js('Arach'), Js('Arachn'), Js('Arachni'), Js('Av'), Js('Avi'), Js('Ban'), Js('Bull'), Js('Can'), Js('Cand'), Js('Candel'), Js('Cani'), Js('Canin'), Js('Consi'), Js('Consil'), Js('Contag'), Js('Dem'), Js('Demo'), Js('Demon'), Js('Drac'), Js('Drag'), Js('Elem'), Js('Elemen'), Js('Element'), Js('Fel'), Js('Feli'), Js('Felin'), Js('Foc'), Js('Focu'), Js('Infec'), Js('Infect'), Js('Intim'), Js('Intimi'), Js('Intimid'), Js('Ligh'), Js('Light'), Js('Noct'), Js('Oppon'), Js('Oppres'), Js('Padl'), Js('Padloc'), Js('Perso'), Js('Person'), Js('Pest'), Js('Rasc'), Js('Rat'), Js('Serp'), Js('Serpen'), Js('Stri'), Js('Strix'), Js('Torch'), Js('Torm'), Js('Tormen'), Js('Tyr'), Js('Tyran'), Js('Vesper'), Js('Vex'), Js('Vexat'), Js('Vir'), Js('Viral'), Js('Ache'), Js('Ago'), Js('Agon'), Js('Miser')]))
    var.put('nm4', Js([Js('Alatar'), Js('Ariane'), Js('Babidi'), Js('Balthazar'), Js('Circe'), Js('Crispin'), Js('Dumbledore'), Js('Else'), Js('Gandalf'), Js('Howell J.'), Js('Jadis'), Js('Jafar'), Js('Joseph C.'), Js('Maediv'), Js('Manannan'), Js('Merlin'), Js('Mordack'), Js('Morgan Le Fay'), Js('Morrigan'), Js('Neloth'), Js('P. Halliwell'), Js('Pallando'), Js('Radagast'), Js('Saruman'), Js('Shazam'), Js('Solcius'), Js('Tim the Enchanter'), Js('W. Witch'), Js('Willow'), Js('Zatanna')]))
    var.put('nm6', Js([Js('A bright'), Js('A clear'), Js('A cluttered'), Js('A complex'), Js('A constant'), Js('A dark'), Js('A dim'), Js('A flat'), Js('A fluid'), Js('A gentle'), Js('A jagged'), Js('A jumbled'), Js('A light'), Js('A mellow'), Js('A mixed'), Js('A modest'), Js('A plain'), Js('A pure'), Js('A rough'), Js('A rounded'), Js('A simple'), Js('A smooth'), Js('A spiky'), Js('A stable'), Js('A straight'), Js('A strong'), Js('A tangled'), Js('A thick'), Js('A thin'), Js('A transparent'), Js('A uniform'), Js('A vibrant'), Js('A violent'), Js('A wild'), Js('A wobbly'), Js('An impure'), Js('An interwoven'), Js('An intricate'), Js('An irregular'), Js('An unstable')]))
    var.put('nm7', Js([Js('amber'), Js('azure'), Js('blue'), Js('blue-green'), Js('bronze'), Js('brown'), Js('burgundy'), Js('cerulean'), Js('cobalt'), Js('copper'), Js('crimson'), Js('emerald'), Js('golden'), Js('green'), Js('indigo'), Js('ivory'), Js('jade'), Js('lilac'), Js('magenta'), Js('maroon'), Js('multi-colored'), Js('orange'), Js('pink'), Js('purple'), Js('red'), Js('rose'), Js('ruby'), Js('sanguine'), Js('scarlet'), Js('silver'), Js('teal'), Js('vermilion'), Js('violet'), Js('white'), Js('yellow')]))
    var.put('nm8', Js([Js('beam'), Js('blast of particles'), Js('blast of small waves'), Js('blast of waves'), Js('blaze of fragments'), Js('blaze of particles'), Js('blaze of sparks'), Js('coil'), Js('coil of particles'), Js('coil of waves'), Js('corkscrew of particles'), Js('flash'), Js('flash of particles'), Js('flash of sparks'), Js('glowing beam'), Js('glowing corkscrew'), Js('glowing fragment cluster'), Js('glowing particle cluster'), Js('glowing ray'), Js('glowing shaft'), Js('glowing sparks'), Js('glowing spike'), Js('glowing wave'), Js('intertwining duo of coils'), Js('intertwining duo of rays'), Js('intertwining duo of ripples'), Js('intertwining duo of streams'), Js('intertwining duo of twirls'), Js('intertwining duo of waves'), Js('line'), Js('line of particles'), Js('particle wave'), Js('ray'), Js('ray of particles'), Js('ray of sparks'), Js('rush of ripples'), Js('rush of small spikes'), Js('rush of small waves'), Js('rush of spikes'), Js('shaft'), Js('spike of particles'), Js('stream'), Js('stream of fragments'), Js('stream of particles'), Js('stream of sparks'), Js('surge'), Js('surge of fragments'), Js('surge of particles'), Js('surge of ripples'), Js('surge of sparks'), Js('surge of waves'), Js('twirl'), Js('twisting coil'), Js('twisting stream'), Js('twisting wave'), Js('wave of fragments'), Js('wave of particles'), Js('wave of tiny particles')]))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd2b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd10b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    var.put('rnd16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    var.put('name', (((((Js('Spell name: ')+var.get('nm1').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd10')))+Js(' '))+var.get('nm3').get(var.get('rnd11')))+var.get('nm2').get(var.get('rnd10b'))))
    var.put('name2', (Js('Inventor: ')+var.get('nm4').get(var.get('rnd12'))))
    var.put('name3', ((Js('Effect: ')+var.get('nm5').get(var.get('rnd13')))+Js('.')))
    var.put('name4', ((((((Js('Appearance: ')+var.get('nm6').get(var.get('rnd14')))+Js(', '))+var.get('nm7').get(var.get('rnd15')))+Js(' '))+var.get('nm8').get(var.get('rnd16')))+Js('.')))
    var.put('name5', Js('----------------------------'))
    var.put('name6', (((((Js('Spell name: ')+var.get('nm1').get(var.get('rnd1')))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd2b'))))
    var.put('name7', (Js('Inventor: ')+var.get('nm4').get(var.get('rnd4'))))
    var.put('name8', ((Js('Effect: ')+var.get('nm5').get(var.get('rnd5')))+Js('.')))
    var.put('name9', ((((((Js('Appearance: ')+var.get('nm6').get(var.get('rnd6')))+Js(', '))+var.get('nm7').get(var.get('rnd7')))+Js(' '))+var.get('nm8').get(var.get('rnd8')))+Js('.')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            pass
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
spellDescriptions = var.to_python()