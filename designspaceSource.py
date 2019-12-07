from fontTools.designspaceLib import *

document = DesignSpaceDocument()

weightAxis = AxisDescriptor()
weightAxis.maximum = 170
weightAxis.minimum = 50
weightAxis.default = 50
weightAxis.name = 'weight'
weightAxis.tag = 'wght'
weightAxis.labelNames[u'fr'] = u'poids'
weightAxis.labelNames[u'en'] = u'weight'
weightAxis.labelNames[u'it'] = u'peso'
document.addAxis(weightAxis)

styles = {
    'light': [50, 'Jatoru-Light.ufo'],
    'black': [170, 'Jatoru-Bold.ufo']
    }


for i, (style, (pos, path)) in enumerate(styles.items()):
    source = SourceDescriptor()
    source.path = path
    source.name = style
    source.familyName = "Jatoru"
    source.styleName = style
    source.location = dict(weight=pos)
    if i == 0:
        source.copyLib = True
        source.copyInfo = True
        source.copyGroups = True
        source.copyFeatures = True
    document.addSource(source)

rule = RuleDescriptor()
rule.name = 'substitution.g'
rule.conditionSets.append([dict(name='weight', minimum=100, maximum=170)])
rule.subs.append(('g', 'g.alt'))
document.addRule(rule)

document.write('Jatoru.designspace')