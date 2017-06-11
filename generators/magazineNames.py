__all__ = ['magazineNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('A Cappella'), Js('Academy'), Js('Acoustic'), Js('Advisor'), Js('Affairs'), Js('Alliance'), Js('Ambience'), Js('Analysis'), Js('Analyze'), Js('Angle'), Js('Animal'), Js('Apex'), Js('Applause'), Js('Appraisal'), Js('Architecture'), Js('Artist'), Js('Artistry'), Js('Assessment'), Js('Audio'), Js('Bargain'), Js('Beast'), Js('Bite Bits'), Js('Blueprint'), Js('Board'), Js('Boost'), Js('Boyfriend'), Js('Brain'), Js('Brainstorm'), Js('Breaking'), Js('Breakthrough'), Js('Business'), Js('Carnival'), Js('Case Study'), Js('Champion'), Js('Chance'), Js('Chic'), Js('Chief'), Js('Cinema'), Js('Coalition'), Js('Color'), Js('Comedian'), Js('Comedy'), Js('Comic'), Js('Communication'), Js('Connection'), Js('Constitution'), Js('Consumer'), Js('Context'), Js('Contract'), Js('Convention'), Js('Cookery'), Js('Cooking'), Js('Cosmos'), Js('Countdown'), Js('Craft'), Js('Craze'), Js('Crazy'), Js('Creation'), Js('Creative'), Js('Creativity'), Js('Critique'), Js('Cuddle'), Js('Cuisine'), Js('Culture'), Js('Custom'), Js('DIY'), Js('Darling'), Js('Data'), Js('Daydream'), Js('Dear'), Js('Debate'), Js('Design'), Js('Destiny'), Js('Destruction'), Js('Development'), Js('Diagnosis'), Js('Discovery'), Js('Divine'), Js('Doodle'), Js('Dragon'), Js('Dream'), Js('Earth'), Js('Eat'), Js('Edict'), Js('Egghead'), Js('Electronic'), Js('Electronics'), Js('Emotion'), Js('Engineering'), Js('Enterprise'), Js('Entertainment'), Js('Entrepreneur'), Js('Essence'), Js('Eternity'), Js('Etiquette'), Js('Euphoria'), Js('Evaluation'), Js('Examination'), Js('Executive'), Js('Expertise'), Js('Exposition'), Js('Fad'), Js('Fan'), Js('Fanatic'), Js('Fantasy'), Js('Fashion'), Js('Fate'), Js('Festival'), Js('Fiesta'), Js('Figure'), Js('Film'), Js('Finance'), Js('Fitness'), Js('Flick'), Js('Flux'), Js('Food'), Js('Foodstuff'), Js('Form'), Js('Fortune'), Js('Foundation'), Js('Fun'), Js('Fun Fest'), Js('Fun and Games'), Js('Fusion'), Js('Future'), Js('Gala'), Js('Game'), Js('Game On'), Js('Garden'), Js('Girlfriend'), Js('Globe'), Js('Grin'), Js('Growth'), Js('Harmony'), Js('Hazard'), Js('Health'), Js('Heart'), Js('Hero'), Js('Highbrow'), Js('Highlight'), Js('Holy'), Js('Home'), Js('Home Improvement'), Js('Illusion'), Js('Imagination'), Js('Imagine'), Js('Improv'), Js('Industry'), Js('Infinity'), Js('Innovation'), Js('Inquiry'), Js('Insight'), Js('Inspection'), Js('Inspiration'), Js('Inspire'), Js('Instrument'), Js('Intelligence'), Js('Invention'), Js('Investment'), Js('Jazz'), Js('Jester'), Js('Joker'), Js('Jubilee'), Js('Kiss'), Js('Landscape'), Js('Laugh'), Js('Life Style'), Js('Lime Light'), Js('Living'), Js('Love'), Js('Luck'), Js('Lumination'), Js('Lustrous'), Js('Magic'), Js('Make Up'), Js('Management'), Js('Manager'), Js('Mansion'), Js('Mastermind'), Js('Meal Time'), Js('Mech'), Js('Mecha'), Js('Mechanical'), Js('Meditation'), Js('Melody'), Js('Metal'), Js('Mind'), Js('Minor'), Js('Mode'), Js('Model'), Js('Modern'), Js('Monster'), Js('Motion'), Js('Muse'), Js('Music'), Js('Mystery'), Js('Myth'), Js('Mythic'), Js('Nature'), Js('Numbers'), Js('Nutrition'), Js('Observer'), Js('Opera'), Js('Oracle'), Js('Outlook'), Js('Ovation'), Js('Paint'), Js('Painting'), Js('Panorama'), Js('Parade'), Js('Paradox'), Js('Paramour'), Js('Partner'), Js('Partnership'), Js('Passion'), Js('Pastel'), Js('Pastry'), Js('Peace'), Js('Perspective'), Js('Pet'), Js('Photography'), Js('Physique'), Js('Picture'), Js('Pinnacle'), Js('Pleasure'), Js('Portrait'), Js('Power'), Js('Print'), Js('Prodigy'), Js('Progress'), Js('Prospect'), Js('Quiz'), Js('Ragtime'), Js('Reality'), Js('Realm'), Js('Reflection'), Js('Relax'), Js('Relaxation'), Js('Repair'), Js('Research'), Js('Resource'), Js('Revelation'), Js('Review'), Js('Riches'), Js('Rise'), Js('Satire'), Js('Scholar'), Js('Scope'), Js('Search'), Js('Sense'), Js('Sentience'), Js('Sketch'), Js('Smile'), Js('Snack'), Js('Snapshot'), Js('Solitude'), Js('Soul'), Js('Sound'), Js('Space'), Js('Sport'), Js('Spotlight'), Js('Stage'), Js('Stand-Up'), Js('Status'), Js('Strength'), Js('Study'), Js('Survey'), Js('Survival'), Js('Sweet'), Js('Sweetheart'), Js('Swing'), Js('Tattoo'), Js('Teen'), Js('Theater'), Js('Titans'), Js('Tone'), Js('Trance'), Js('Tranquility'), Js('Transfer'), Js('Treatment'), Js('Trend'), Js('Trending'), Js('Truelove'), Js('Turbine'), Js('Valuation'), Js('Value'), Js('Vertex'), Js('View'), Js('Viewpoint'), Js('Vision'), Js('Vista'), Js('Vitality'), Js('Vogue'), Js('Wealth'), Js('Web'), Js('Wheeler'), Js('Wheels'), Js('Wild'), Js('Wildlife'), Js('Word'), Js('World'), Js('Youth')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('Chronicle'), Js('Daily'), Js('Digest'), Js('Focus'), Js('Gazette'), Js('Guide'), Js('Illustrated'), Js('Journal'), Js('Life'), Js('Magazine'), Js('Monthly'), Js('Monthly Magazine'), Js('Report'), Js('Reports'), Js('Review'), Js('Times'), Js('Today'), Js('Week'), Js('Weekly'), Js('Weekly Magazine'), Js('Magazine'), Js('Magazine')]))
pass
pass


# Add lib to the module scope
magazineNames = var.to_python()