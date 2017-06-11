__all__ = ['bats']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aidec'), Js('Alucard'), Js('Aluminum'), Js('Anca'), Js('Athugz'), Js('Awin'), Js('Azurisz'), Js('Azurys'), Js('Azuryz'), Js('Balgzr'), Js('Balloon'), Js('Baloo'), Js('Bartok'), Js('Bast'), Js('BatPitt'), Js('Batholomew'), Js('Batista'), Js('Batita'), Js('Batley'), Js('BatleyCooper'), Js('Batty'), Js('Bax'), Js('Baxter'), Js('Belfry'), Js('Belphegor'), Js('Beniam'), Js('Bephelgor'), Js('Bibacr'), Js('Bloodmaw'), Js('Bloodscent'), Js('Bloodwing'), Js('BloodyMary'), Js('Bloodymuzzle'), Js('Blurp'), Js('Boannan'), Js('Brandusa'), Js('Brokenfang'), Js('Bruce'), Js('Bubbles'), Js('Bunted'), Js('Camazotz'), Js('Caped'), Js('Cecirh'), Js('Cezar'), Js('Chausiku'), Js('Chocula'), Js('Cipanr'), Js('Ciprian'), Js('Corneliu'), Js('Count'), Js('CountChocula'), Js('CountDracula'), Js('Danut'), Js('Darkness'), Js('Dawn'), Js('Deathmaw'), Js('Delano'), Js('Demetrie'), Js('Dimitri'), Js('Ding'), Js('Dingbat'), Js('Dinu'), Js('Drac'), Js('Dracula'), Js('Draculon'), Js('Dradis'), Js('Drakul'), Js('Dreuc'), Js('Dung'), Js('Eclipse'), Js('Ecture'), Js('Edimmu'), Js('Eseit'), Js('Fang'), Js('Fangs'), Js('Fanteriso'), Js('Fizzle'), Js('Flapper'), Js('Flappy'), Js('Fledermaus'), Js('Floater'), Js('Flotsam'), Js('Flygon'), Js('Fontenay'), Js('Fuzzy'), Js('Gargles'), Js('Gavril'), Js('Glider'), Js('Golbat'), Js('Grigore'), Js('Guano'), Js('Gullet'), Js('HairTangler'), Js('Haze'), Js('Helldiver'), Js('Horatiu'), Js('Hynraic'), Js('Hynryac'), Js('Iach'), Js('Iarsere'), Js('Iatosr'), Js('Ioan'), Js('Irritant'), Js('Irubleu'), Js('Jet'), Js('Kite'), Js('Knuckle'), Js('Lacip'), Js('Laicch'), Js('Laimhynr'), Js('Laitpaurh'), Js('Lamsor'), Js('Lasis'), Js('Liwa'), Js('Lockjaw'), Js('Lollipop'), Js('Longfang'), Js('Lorenna'), Js('Loryss'), Js('Lucifer'), Js('Lucirr'), Js('Luna'), Js('Man'), Js('Maya'), Js('Mihail'), Js('Mihaiti'), Js('Mist'), Js('Mothball'), Js('Mozzie'), Js('Nerf'), Js('Nibbles'), Js('Nightwing'), Js('Nosferatu'), Js('Nyx'), Js('Outtahell'), Js('Ozzy'), Js('Petru'), Js('Pickle'), Js('Quentynn'), Js('Quickfang'), Js('Quillestra'), Js('Quilstream'), Js('Rabbies'), Js('Rabies'), Js('Radar'), Js('Raich'), Js('Rajnish'), Js('Remus'), Js('Render'), Js('Reucec'), Js('Ripmaw'), Js('Ruqualash'), Js('Ryacoer'), Js('Sade'), Js('Screech'), Js('Screechy'), Js('Secr'), Js('Serenity'), Js('Sharptooth'), Js('Skona'), Js('Slideshow'), Js('Slithe'), Js('SlowMo'), Js('Snape'), Js('Sonar'), Js('Sorin'), Js('Sparkle'), Js('Spaulding'), Js('Spawnie'), Js('Spike'), Js('Sport'), Js('Spudnik'), Js('Spuds'), Js('Spyestra'), Js('Squeekers'), Js('Ssynec'), Js('Stinky'), Js('Sturmovic'), Js('Sucka'), Js('Suckah'), Js('Summanus'), Js('Sunshine'), Js('Sunshynne'), Js('Sushi'), Js('Swoops'), Js('Tampax'), Js('Tiberius'), Js('Tlaitparh'), Js('Tloiciac'), Js('Twilight'), Js('Twinkle'), Js('Twinkles'), Js('Umpire'), Js('Vampire'), Js('Vlad'), Js('Vladimir'), Js('Wayne'), Js('Wiggles'), Js('Willy'), Js('Wingnut'), Js('Wooden'), Js('Ybhugr'), Js('Ynremr'), Js('Yugnos'), Js('Zubat')]))
var.put('nm2', Js([Js('Aasterinian'), Js('Adarna'), Js('Aine'), Js('Aiolus'), Js('Ajax'), Js('Alaricus'), Js('Amani'), Js('Amber'), Js('Ametarasu'), Js('Anor'), Js('Apep'), Js('Apollo'), Js('Apophis'), Js('Archangel'), Js('Astilabor'), Js('Aurora'), Js('Azar'), Js('Azrael'), Js('Bahamut'), Js('Belinda'), Js('BlackHawkUp'), Js('Blaze'), Js('Blaziken'), Js('Bridget'), Js('Brimstone'), Js('CaptainMagestic'), Js('Char'), Js('Charizard'), Js('Chronepsis'), Js('Cinaed'), Js('Cinderella'), Js('Cindur'), Js('Combusken'), Js('Cupcake'), Js('Cyra'), Js('Dart'), Js('Dawn'), Js('DawningStar'), Js('Dragonair'), Js('Dragonite'), Js('Eclipse'), Js('Ember'), Js('Emberella'), Js('Emilius'), Js('Equiknocks'), Js('Equinox'), Js('Equintess'), Js('Esabon'), Js('Exona'), Js('Faluzure'), Js('Fefnir'), Js('Fiammetta'), Js('Fiera'), Js('Fierna'), Js('Fintan'), Js('Fiona'), Js('Firedancer'), Js('Flamebreath'), Js('Flamebringer'), Js('Flappy'), Js('Flare'), Js('Flareon'), Js('Flicker'), Js('Flutterby'), Js('Flygon'), Js('Fuego'), Js('Furrion'), Js('Gabija'), Js('Garyx'), Js('Gizmo'), Js('Glaurung'), Js('Griffin'), Js('Heatran'), Js('Heatwave'), Js('Helios'), Js('Hlal'), Js('Hyperion'), Js('ILikemCrispy'), Js('Ignacio'), Js('Ignescent'), Js('Illumina'), Js('Imatazeubro'), Js('Incandessa'), Js('Inti'), Js('Io'), Js('Kestrel'), Js('Kindle'), Js('Kiyo'), Js('Lendys'), Js('Leryda'), Js('LilMsCrispy'), Js('Lina'), Js('Loogie'), Js('Lucifer'), Js('Magmar'), Js('Magmortar'), Js('Matthew'), Js('Moltres'), Js('Morningstar'), Js('Mushu'), Js('Naur'), Js('Phoenix'), Js('PhoenixDown'), Js('Plume'), Js('Pyrrhus'), Js('Quilafyre'), Js('Quilla'), Js('Ra'), Js('Rainbow'), Js('Rhonin'), Js('Rouge'), Js('Ryuu'), Js('Salamence'), Js('Sardior'), Js('Seraphim'), Js('Serenity'), Js('Shina'), Js('Shrike'), Js('SimpleSensations'), Js('Smaug'), Js('Solar'), Js('Sora'), Js('Spectre'), Js('Spitfire'), Js('StarScream'), Js('Starburst'), Js('Sun Queen'), Js('Sunburn'), Js('Sunburst'), Js('Sunflare'), Js('Sunrise'), Js('Sunshine'), Js('Tamara'), Js('Tawhaki'), Js('Tequila'), Js('TequilaSundown'), Js('Tiamat'), Js('Timeus'), Js('Tinder'), Js('Tobias'), Js('Torchic'), Js('Uruloki'), Js('Vallenari'), Js('Vanity'), Js('Vulkan'), Js('Xolotl')]))
pass
pass


# Add lib to the module scope
bats = var.to_python()