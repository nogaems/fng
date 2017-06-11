__all__ = ['haloHuragokNames']

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
    var.put('nm1', Js([Js('A Little Too Heavy'), Js('A Little Too Light'), Js('Absurd Drifter'), Js('Absurd Floater'), Js('Absurd Plunger'), Js('Absurd Sinker'), Js('Adapted With Ease'), Js('Adeqautely Buoyant'), Js('Adjusted With Ease'), Js('Airier Than Most'), Js('Altered With Ease'), Js('Ascents Quickly'), Js('Awfully Airy'), Js('Awfully Light'), Js('Balanced With Ease'), Js('Barely Floats'), Js('Barely Hangs'), Js('Barely Hovers'), Js('Barely Off The Ground'), Js('Bothersome Balance'), Js('Bothersome Floater'), Js('Bounces Around'), Js('Bulkier Than Most'), Js('Bumpy Drifter'), Js('Bumpy Floater'), Js('Calmly Drifts'), Js('Calmly Floats'), Js('Common Sinker'), Js('Commonly Crashes'), Js('Constantly Ascends'), Js('Constantly Sinks'), Js('Crashes Continuously'), Js('Crashes Often'), Js('Dainty Floater'), Js('Dainty Lift'), Js('Delicately Adapted'), Js('Delicately Balanced'), Js('Delicately Floats'), Js('Delicately Sinks'), Js('Demanding Adjustments'), Js('Demanding To Alter'), Js('Descends Over Time'), Js('Descends Quickly'), Js('Difficult Balance'), Js('Difficult Equalization'), Js('Difficult To Adapt'), Js('Difficult To Balance'), Js('Difficult To Lift'), Js('Difficulties Rising'), Js('Dives Quickly'), Js("Doesn'T Lift"), Js("Doesn'T Rise"), Js('Doubtful Floater'), Js('Doubtful Riser'), Js('Drift Around'), Js('Drifts Around'), Js('Drifts Away Over Time'), Js('Drifts Backwards'), Js('Drifts With The Wind'), Js('Drops A Lot'), Js('Drops Like A Brick'), Js('Drops Like A Star'), Js('Drops Quickly'), Js('Dwindles Over Time'), Js('Easily Adjusted'), Js('Easily Altered'), Js('Easily Equalized'), Js('Easily In The Air'), Js('Easily Inflated'), Js('Easily Regulated'), Js('Easy To Adapt'), Js('Easy To Balance'), Js('Easy To Descent'), Js('Easy To Sink'), Js('Effortless Glide'), Js('Effortlessly Drifts'), Js('Effortlessly Floats'), Js('Effortlessly Rises'), Js('Eternal Floater'), Js('Eternal Sinker'), Js('Evened With Ease'), Js('Excessively Bulky'), Js('Excessively Heavy'), Js('Exorbitantly Airy'), Js('Exorbitantly Bulky'), Js('Exorbitantly Heavy'), Js('Exorbitantly Light'), Js('Extremely Feathery'), Js('Extremely Light'), Js('Falls Like A Star'), Js('Far Too Airy'), Js('Far Too Dense'), Js('Far Too Heavy'), Js('Far Too Light'), Js('Feathery Than Some'), Js('Finely Attuned'), Js('Finely Balanced'), Js('Floated With Ease'), Js('Floats Freely'), Js('Floats Steadily'), Js('Floats Too Quickly'), Js('Floats With Ease'), Js('Gently Adapted'), Js('Gently Adjusted'), Js('Gently Floats'), Js('Gently Lifts'), Js('Gently Rises'), Js('Gently Sinks'), Js('Glides Around'), Js('Glides Freely'), Js('Glides Sideways'), Js('Glides To One Side'), Js('Glides With Ease'), Js('Gone With The Wind'), Js('Gradually Lifts'), Js('Gradually Sinks'), Js('Hangs To The Front'), Js('Hard To Adjust'), Js('Hard To Balance'), Js('Heavier Than Average'), Js('Heavier Than Most'), Js('Heavier Than Some'), Js('Hovers With Ease'), Js('Idle Drifter'), Js('Idle Floater'), Js('Immensely Bulky'), Js('Immensely Heavy'), Js('Inclined To Decline'), Js('Inclined To Sink'), Js('Inconceivable Drifter'), Js('Inconceivable Sinker'), Js('Increasingly Ascends'), Js('Increasingly Wanders'), Js('Incredible Floater'), Js('Incredible Glider'), Js('Incredible Rises'), Js('Incredible Sinker'), Js('Intricate Adjustments'), Js('Intricate Alterations'), Js('Intricate Balance'), Js('Intricate Measurements'), Js('Just Keeps Sinking'), Js('Just Meanders'), Js('Keeps Drifting'), Js('Keeps Rising'), Js('Labored Alterations'), Js('Labored Lift'), Js('Laborious Adjustments'), Js('Laborious Alterations'), Js('Lead-Footed'), Js('Lifts Gradually'), Js('Lifts In Small Doses'), Js('Lifts With Difficulties'), Js('Lifts With Ease'), Js('Lighter Than Average'), Js('Lighter Than Most'), Js('Lightly Adjusted'), Js('Lightly Altered'), Js('Likely To Glide'), Js('Likely To Sink'), Js('Lingers Above'), Js('Lingers Below'), Js('May Crash'), Js('May Plummet'), Js('Moderately Ascends'), Js('Moderately Descends'), Js('Moderately Floats'), Js('Moderately Sinks'), Js('Never Floats Right'), Js('Never Glides Well'), Js('Never Sinks'), Js('Never Stops Sinking'), Js('Often Crashes'), Js('Often Drifts Off'), Js('Often Plummets'), Js('Often Sinks'), Js('Overly Airy'), Js('Overly Dense'), Js('Overly Heavy'), Js('Overly Light'), Js('Plummets A Lot'), Js('Plunges Fast'), Js('Predisposed To Float'), Js('Predisposed To Glide'), Js('Predisposed To Plummet'), Js('Predisposed To Sink'), Js('Prone To Plummet'), Js('Prone To Sink'), Js('Quickly Balanced'), Js('Quickly Tailored'), Js('Quite Airy'), Js('Quite Hefty'), Js('Regular Crasher'), Js('Regular Drifter'), Js('Regular Riser'), Js('Regular Sinker'), Js('Remarkably Floaty'), Js('Remarkably Light'), Js('Rough Adjustment'), Js('Rough Alterations'), Js('Sensitive To Winds'), Js('Severely Dense'), Js('Severely Light'), Js('Sinks A Lot'), Js('Sinks Continuously'), Js('Sinks Fast'), Js('Sinks Gradually'), Js('Sinks In Small Doses'), Js('Sinks Like A Brick'), Js('Sinks Often'), Js('Sinks Over Time'), Js('Sinks Steadily'), Js('Sinks To The Back'), Js('Sinks To The Front'), Js('Sinks Too Quickly'), Js('Slight Drifter'), Js('Slight Sinker'), Js('Slowly Descends'), Js('Slowly Rises'), Js('Smooth Sailing'), Js('Smoothly Altered'), Js('Smoothly Fine-Tuned'), Js('Strangely Plummets'), Js('Strangely Sinks'), Js('Strenuous Adjustments'), Js('Strenuous Alterations'), Js('Struggles To Float'), Js('Struggles To Rise'), Js('Subject To Sinking'), Js('Sufficiently Buoyant'), Js('Tendencies To Plummet'), Js('Tendencies To Plunge'), Js('Terrible Balance'), Js('Terrible Lift'), Js('Tilts Sidewards'), Js('Tilts To One Side'), Js('Tiring Adjustment'), Js('Tiring Alterations'), Js('Troublesome Balance'), Js('Troublesome Floater'), Js('Troublesome Plummet'), Js('Troublesome Sinker'), Js('Tumbles A Lot'), Js('Unhurriedly Floats'), Js('Unhurriedly Sinks'), Js('Unlikely To Balance'), Js('Unlikely To Crash'), Js('Unlikely To Float'), Js('Unlikely To Sink'), Js('Very Dense'), Js('Very Heavy')]))
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
haloHuragokNames = var.to_python()