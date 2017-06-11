__all__ = ['antiqueStoreNames']

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
    var.put('nm1', Js([Js('A New View'), Js('About Time'), Js('Age of Vintage'), Js('Aged Goodness'), Js('Anecdotes'), Js("Another Man's Treasures"), Js("Another's Treasures"), Js('Antique Appeal'), Js('Antique Cache'), Js('Antique Cuties'), Js('Antique Hut'), Js('Antique Trove'), Js('Antiques and Artifacts'), Js('Antiquities'), Js('Authentic Antiquities'), Js('Beautiful Salvage'), Js('Blasts from the Past'), Js('Bought Again'), Js('Bygones'), Js('Checkered Pasts'), Js('Cozy Collectibles'), Js('Dinky and Dainty'), Js('Discoveries'), Js('Drab to Fab'), Js('Echoes of the Past'), Js('Established Goods'), Js('Focus of the Past'), Js('Focus on the Past'), Js('Forget Me Nots'), Js('Forgotten Furnishings'), Js('Fortunes in Time'), Js('Found in Time'), Js('From Oblivion'), Js('From Time Immemorial'), Js('Frozen in Time'), Js('General Goods'), Js('Good As New'), Js('Good Goods'), Js("Good Ol' Days"), Js('Hodge Podge Lodge'), Js('Honest Heirlooms'), Js('In-Of-Date'), Js('Joys For Forever'), Js('Junk Deluxe'), Js('Just in Time'), Js('Knick-knack Paddywhack Shack'), Js('Legends of Their Time'), Js('Little Collectibles'), Js('Little House of Trinkets'), Js('Live in the Past'), Js('Living Memories'), Js('Long Time No See'), Js('Lost and Found in Time'), Js('Matters of Time'), Js('Memory Lane'), Js('Miracles of the Past'), Js('Mod Life'), Js('Modern Memories'), Js('Modern Vintage'), Js('Needful Things'), Js('Odd Types'), Js('Old Gold'), Js('Old Roots'), Js('Old Stuff'), Js('Old and Bold'), Js('Oldies and Goldies'), Js('Once upon a time'), Js('One Time or Another'), Js('Out of the Attic'), Js("Pandora's Box"), Js('Paragon Prizes'), Js('Pass On the Past'), Js('Pass The Time'), Js('Past Caring'), Js('Past Meets Present'), Js('Past On'), Js('Past Over'), Js('Past Passed On'), Js('Past Repast'), Js('Pockets of Time'), Js('Precious Past'), Js('Precious Things'), Js('Presents for the Present'), Js('Presents of the Past'), Js('Preserved'), Js('Primes of the Past'), Js('Rags and Riches'), Js('Recent Memories'), Js('Recollect Them All'), Js('Recollectibles'), Js('Relics and Rarities'), Js('Relics and Riches'), Js('Relics of Time'), Js('Reliquary'), Js('Remains to be Seen'), Js('Remember'), Js('Remember This'), Js('Remember, Remember'), Js('Renewed Life'), Js('Renewed Memories'), Js('Retro Relics'), Js('Revered Relics'), Js('Revival'), Js('Salvage Garden'), Js('Secrets of the Past'), Js('Shared Memories'), Js('Stuff and Things'), Js('Sweet Memories'), Js('Taken for Granted'), Js('Tales Resold'), Js('Tales of the Past'), Js('Tales Retold'), Js('Tales Untold'), Js('Tests of Time'), Js('The Antiki-Wiki'), Js('The Antique Market'), Js('The Salvage Beast'), Js('The Shuffle of Things'), Js('The Time is Ripe'), Js('The Treasure Chest'), Js('The Treasure Trove'), Js('Things Past'), Js('Things of the Past'), Js('Thingymabobs'), Js('Time Honored'), Js('Time Not Forgotten'), Js('Time Recovered'), Js("Time of One's Life"), Js('Timeless Treasures'), Js('Timeless Trinkets'), Js('Times Remembered'), Js('Top Drawer Antiques'), Js('Treasures and Trinkets'), Js('Treasures of Time'), Js('Trinkets and Traditions'), Js('Trinkets of Time'), Js('Twosided'), Js('Utter Clutter'), Js('Vagabond Vendor'), Js('Vestiges of the Past'), Js('Vintage'), Js('Vintage Baby'), Js('Vintage Treasures'), Js('Vintage Vogue'), Js('Vintage Wares'), Js('Warm Wares'), Js('Wayward Wealths'), Js('Wealth of Time'), Js('Well of a Time'), Js('Whispers of the Past'), Js('Wonders of the Past')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
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
antiqueStoreNames = var.to_python()