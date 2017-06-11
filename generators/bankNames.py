__all__ = ['bankNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm2', 'result'])
    var.put('nm2', Js([Js('Absolute'), Js('Ace'), Js('Aegis'), Js('Agnate'), Js('Allied'), Js('Alpha'), Js('Apex'), Js('Apogee'), Js('Arcadia'), Js('Archetype'), Js('Armament'), Js('Ascension'), Js('Aspire'), Js('Associated'), Js('Assurance'), Js('Aurora'), Js('Azure'), Js('Bastion'), Js('Better Life'), Js('Big Heart'), Js('Bolt'), Js('Boon'), Js('Bright Horizon'), Js('Bulwark'), Js('Caliber'), Js('Capital'), Js('Celestial'), Js('Central'), Js('Champion'), Js('Citadel'), Js('Citizen Service'), Js('Citizen Union'), Js('Citizens First'), Js('City Ward'), Js('Cloud Nine'), Js('Clover'), Js('Cognate'), Js('Commonwealth'), Js('Community'), Js('Concorde'), Js('Connection'), Js('Core'), Js('Credence'), Js('Credit'), Js('Crest'), Js('Crown'), Js('Dawn'), Js('Diamond'), Js('Diligence'), Js('Domestic'), Js('Dominion'), Js('Duty'), Js('Edge'), Js('Elite'), Js('Elysium'), Js('Emblem'), Js('Eminence'), Js('Epitome'), Js('Essence'), Js('Esteem'), Js('Evolution'), Js('Excellence'), Js('Faith'), Js('Federal'), Js('Felicity'), Js('Fidelity'), Js('First'), Js('First Choice'), Js('First Guaranty'), Js('Flow'), Js('Focus'), Js('Foundation'), Js('Fountain'), Js('Free Citizen'), Js('Fundament'), Js('Gemstone'), Js('General'), Js('Generation'), Js('Genesis'), Js('Global Network'), Js('Globe'), Js('Gold Alliance'), Js('Gold Credit'), Js('Goldcorp'), Js('Golden Gates'), Js('Goldguard'), Js('Goldleaf'), Js('Goldward'), Js('Goodlife'), Js('Grade'), Js('Grand Credit'), Js('Grand Fortune'), Js('Grand Market'), Js('Grand Mutual'), Js('Grand Spire'), Js('Grand Summit'), Js('Green Market'), Js('Green Valley'), Js('Groundwork'), Js('Her Majesty'), Js('High Rise'), Js('His Majesty'), Js('Joint'), Js('Jones'), Js('Kindred'), Js('Life Essence'), Js('Life Tree'), Js('Lifespark'), Js('Lightning'), Js('Marshall'), Js('Meridian'), Js('Midland'), Js('Miracle'), Js('Monolith'), Js('Nation'), Js('National'), Js('New Alliance'), Js('New Blossom'), Js('New Civil'), Js('New Connection'), Js('New Corporate'), Js('New Edge'), Js('New Generation'), Js('New Heights'), Js('New Horizon'), Js('New Leaf'), Js('New Life'), Js('New National'), Js('New Sense'), Js('New Wave'), Js('New Wealth'), Js('Obelisk'), Js('Obsidian'), Js('Ocean'), Js('Oculus'), Js('Omega'), Js('One Capital'), Js('One Duty'), Js('One Nation'), Js('Origin'), Js('Padlock'), Js('Paradise'), Js('Paragon'), Js('Paramount'), Js('Phoenix'), Js('Pillar'), Js('Pinnacle'), Js('Polestar'), Js('Premium'), Js('Prime'), Js('Primo'), Js('Principal'), Js('Principle'), Js('Private'), Js('Private Citizen'), Js('Prominence'), Js('Prosperity'), Js('Provenance'), Js('Pulse'), Js('Purity'), Js('Pursuit'), Js('Reliance'), Js('Repose'), Js('Republic Citizens'), Js('Resolution'), Js('Rose'), Js('Royal Crown'), Js('Sky High'), Js('Skyward'), Js('Snowflake'), Js('Soar'), Js('Solace'), Js('Soul'), Js('South Trust'), Js('Sparkle'), Js('Spotlight'), Js('Spring'), Js('Springwell'), Js('Sprout'), Js('State'), Js('Sublime'), Js('Summit'), Js('Sunray'), Js('Surge'), Js('Syndicate'), Js('Trust'), Js('Trustcorp'), Js('United'), Js('Value'), Js('Velvet'), Js('Vertex'), Js('Victory'), Js('Vigor'), Js('Virtue'), Js('Vitality'), Js('Voyage'), Js('Ward'), Js('Wellness'), Js('Wellspring'), Js('Zenith'), Js('Zion')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', ((var.get('nm2').get(var.get('rnd2'))+Js(' '))+var.get('nm1').get(var.get('rnd'))))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Bancorp'), Js('Bancshares'), Js('Bank'), Js('Bank Corp.'), Js('Bank Group'), Js('Bank Inc.'), Js('Bank System'), Js('Banks'), Js('Banks Inc.'), Js('Corporation'), Js('Credit Union'), Js('Financial'), Js('Financial Corp.'), Js('Financial Group'), Js('Financial Holdings'), Js('Financial Inc.'), Js('Financial Services'), Js('Holding Company'), Js('Holdings'), Js('Holdings Inc.'), Js('Trust'), Js('Trust Corp.')]))
pass
pass


# Add lib to the module scope
bankNames = var.to_python()