__all__ = ['battleCries']

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
    var.registers(['nm1', 'result'])
    var.put('nm1', Js([Js('At last'), Js('Awake, warriors'), Js('Bathe in their blood'), Js('Behold our power'), Js('Blood for the blood god'), Js('Blood for the emperor'), Js('Bow before us'), Js('Bring it on'), Js('Bring me their guts'), Js('Bring me their heads'), Js('Bring me their teeth'), Js('Bring on the pain'), Js('Bring them to their knees'), Js('Burn'), Js('By our blade'), Js('By our blades you shall perish'), Js('By the power bestowed upon us'), Js('Chaos and anarchy'), Js('Charge'), Js('Charge forward'), Js('Come and get us'), Js('Cower before us'), Js('Cut them down'), Js('Death and glory'), Js('Death can wait no longer'), Js('Death comes tomorrow'), Js('Death to the enemy'), Js('Death to the weak'), Js('Destroy everything'), Js('Destroy everything in your path'), Js('Destroy them all'), Js('Die'), Js("Don't run, you're already dead"), Js('Eternally great'), Js('Feed them to the maggots'), Js('Feel our might'), Js('Fertilize these lands with their corpses'), Js('Fill them with regret'), Js('Fire at will'), Js('Follow me to glory'), Js('For blood and glory'), Js('For chaos'), Js('For gold and glory'), Js('For honor'), Js('For justice'), Js('For king and country'), Js('For our people'), Js('For the light'), Js('Forever as one'), Js('Forever unbroken'), Js('Freedom'), Js('Glory to us all'), Js('God watches over us'), Js("God's on our side"), Js('Here we come'), Js("In god's name"), Js("It's feeding time"), Js('Kill every last one of them'), Js('Kill them all, leave no-one standing'), Js('Kneel before our lord'), Js('Leave none alive'), Js('Leave nothing standing'), Js('Leave only ashes'), Js('Leave them with nothing'), Js('Let the crows feast tonight'), Js('Let them feel true pain'), Js('Let them meet our best'), Js('Let them meet their maker'), Js('Let them taste our blades'), Js('Let there be blood'), Js("Let's get to know who they are on the inside"), Js("Let's go"), Js("Let's taste their flesh"), Js("Let's teach them how it's done"), Js('Make them fear our name'), Js('Make them suffer'), Js('None shall remember them'), Js('Obliterate them from history'), Js('Once more'), Js('Our blades hunger'), Js('Our life for god'), Js('Our time has come'), Js('Our time is now'), Js('Paint the fields in their blood'), Js('Praise the people'), Js('Prepare for destruction'), Js('Prepare to die'), Js('Remove them from this Earth'), Js('Send them to their maker'), Js('Shine in the light'), Js('Spit on their corpses'), Js('Stand united'), Js('Strike true'), Js('Swift and savage'), Js('Take everything'), Js('Take no prisoners'), Js('Take them down'), Js('Take what is ours'), Js('Tear them down'), Js('Tear them to pieces'), Js('Thank you for your sacrifice'), Js('That one is mine'), Js('The end is here'), Js('The god of death demands its pay'), Js('They will remember'), Js('Time for a warm up'), Js('Time to have fun'), Js('Time to pay'), Js('To glory'), Js('To victory'), Js('Trample them beneath your feet'), Js('Turn them to ash'), Js('United under god'), Js('Until eternity'), Js('Victory or death'), Js('We are eternal'), Js('We are immortal'), Js('We are the apocalypse'), Js('We are the dead'), Js('We are the greatest'), Js('We are the reapers'), Js('We fight as one'), Js('We have arrived'), Js('We have awoken'), Js('We have risen'), Js('We never tire'), Js('We reign forever'), Js('We ride forever'), Js('We shall be remembered'), Js('We shall be victorious'), Js('We shall conquer all'), Js('We shall feast tonight'), Js('We stand together'), Js('We stand united'), Js('We will be victorious'), Js('We will never stop'), Js("We're not afraid"), Js('Wipe them from history'), Js('With me, as one'), Js('Witness our might'), Js('You belong to us now'), Js("You're already dead"), Js('Your souls are ours')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(11.0)):
        try:
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('names', Js('--------'))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+Js('!')))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
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
battleCries = var.to_python()