__all__ = ['militaryRanks']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names4', 'names2', 'nameGen', 'names3'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(4.0)):
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('names', ((var.get('names3').get(var.get('rnd0'))+Js(' of '))+var.get('names4').get(var.get('rnd1'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                    var.put('names', var.get('names1').get(var.get('rnd0')))
                else:
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('names', var.get('names2').get(var.get('rnd0')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Adjunct'), Js('Adjutant'), Js('Admiral'), Js('Air Marshal'), Js('Airman'), Js('Army General'), Js('Aspirant'), Js('Brigade General'), Js('Brigadier'), Js('Brigadier General'), Js('Cadet'), Js('Captain'), Js('Captain-Commandant'), Js('Chief'), Js('Chief Engineer'), Js('Chief Marshal'), Js('Chief Technician'), Js('Colonel'), Js('Commander'), Js('Commander General'), Js('Commodore'), Js('Corporal'), Js('Corps General'), Js('Divisional General'), Js('Doctor'), Js('Engineer'), Js('Ensign'), Js('Field Marshal'), Js('Flag Officer'), Js('Fleet Captain'), Js('Fleet Commander'), Js('Fleet General'), Js('Fleet Officer'), Js('Flight Captain'), Js('Flight Corporal'), Js('Flight Lieutenant'), Js('Flight Officer'), Js('Flight Sergeant'), Js('General'), Js('Grand Admiral'), Js('Gunnery Sergeant'), Js('High Colonel'), Js('Lance Corporal'), Js('Lieutenant'), Js('Lieutenant Junior '), Js('Lieutenant Senior '), Js('Lieutenant-Colonel'), Js('Lieutenant-Commander'), Js('Lieutenant-General'), Js('Major'), Js('Major-General'), Js('Marshal'), Js('Master'), Js('Master Chief'), Js('Master Corporal'), Js('Master Sergeant'), Js('Medic'), Js('Midshipman'), Js('Naval Captain'), Js('Naval Commander'), Js('Naval General'), Js('Naval Officer'), Js('Officer'), Js('Petty Officer'), Js('Pilot'), Js('Pilot Officer'), Js('Principal Master'), Js('Private'), Js('Quartermaster'), Js('Rear Admiral'), Js('Recruit'), Js('Seaman'), Js('Senior Officer'), Js('Sergeant'), Js('Sergeant-Major'), Js('Specialist'), Js('Spy'), Js('Squadron Leader'), Js('Staff Sergeant'), Js('Sub-Lieutenant'), Js('Subcommander'), Js('Supply Officer'), Js('Supreme Admiral'), Js('Supreme Commander'), Js('Supreme General'), Js('Supreme Master'), Js('Technical Sergeant'), Js('Technician'), Js('Vice Admiral'), Js('Vice Captain'), Js('Vice Commander'), Js('Vice General'), Js('Warrant Officer'), Js('Wing Commander'), Js('Wing Commodore')]))
var.put('names2', Js([Js('Adjunct'), Js('Aerial Cavalry'), Js('Apprentice'), Js('Archer'), Js('Archmage'), Js('Berzerker'), Js('Besieger'), Js('Buckaneer'), Js('Captain'), Js('City Guard'), Js('Cleaver'), Js('Cloud Rider'), Js('Corporal'), Js('Covert Infantry'), Js('Crusher'), Js('Defender'), Js('Duke'), Js('Earl'), Js('Emperor'), Js('Executor'), Js('Fist'), Js('Footsoldier'), Js('General'), Js('Ground Cavalry'), Js('Ground Infantry'), Js('High Mage'), Js('High Priest'), Js('Justicar'), Js('King'), Js('Knight'), Js('Lawbringer'), Js('Lord'), Js('Lord General'), Js('Major'), Js('Man-at-arms'), Js('Marine'), Js('Marshal'), Js('Mounteneer'), Js('Naval Cavalry'), Js('Naval Infantry'), Js('Paladin'), Js('Patrol'), Js('Peon'), Js('Priest'), Js('Private'), Js('Reaper'), Js('Rescuer'), Js('Rocketeer'), Js('Rusher'), Js('Sage'), Js('Scout'), Js('Seeker'), Js('Seer'), Js('Serpent Rider'), Js('Sniper'), Js('Spec-Ops Captain'), Js('Spec-Ops Cavalry'), Js('Spec-Ops Infantry'), Js('Spelunker'), Js('Spy'), Js('Squad Mage'), Js('Squire'), Js('Stalker'), Js('Supreme Warlock'), Js('Supreme Warlord'), Js('Thunder Trooper'), Js('Tresher'), Js('Tunneler'), Js('Warden'), Js('Warlock'), Js('Warlord'), Js('Warrior')]))
var.put('names3', Js([Js('Officer'), Js('General'), Js('Commander'), Js('Lieutenant'), Js('Chief'), Js('Captain'), Js('Colonel'), Js('Sergeant'), Js('Commandant'), Js('Master')]))
var.put('names4', Js([Js('Aid'), Js('Air'), Js('Armor'), Js('Armored Vehicles'), Js('Beasts'), Js('Cavalry'), Js('Covert Operations'), Js('Deception'), Js('Defence'), Js('Demolition'), Js('Destruction'), Js('Explosives'), Js('Fear'), Js('Fire'), Js('Flight'), Js('Hostages'), Js('Illusions'), Js('Infantry'), Js('Information'), Js('Justice'), Js('Mages'), Js('Misinformation'), Js('Morale'), Js('Navigation'), Js('Paladins'), Js('Penalties'), Js('Planes'), Js('Planning'), Js('Preparation'), Js('Prisoners'), Js('Propaganda'), Js('Protection'), Js('Public Relations'), Js('Recruits'), Js('Rescues'), Js('Resources'), Js('Sanctions'), Js('Ships'), Js('Siege Weapons'), Js('Spec-Ops'), Js('Supplies'), Js('Support'), Js('Tanks'), Js('Terror'), Js('Traps'), Js('Warlocks'), Js('Warlords'), Js('Water'), Js('Weapons'), Js('Witness Protection'), Js('the Air'), Js('the Army'), Js('the Bezerkers'), Js('the City'), Js('the Code'), Js('the Company'), Js('the Court'), Js('the Covert'), Js('the Deck'), Js('the Fleet'), Js('the Guard'), Js('the Guardians'), Js('the Hounds'), Js('the Law'), Js('the Line'), Js('the Mob'), Js('the Navy'), Js('the Order'), Js('the Reavers'), Js('the Riders'), Js('the Siege'), Js('the Underground'), Js('the Wall'), Js('the Watch')]))
pass
pass


# Add lib to the module scope
militaryRanks = var.to_python()