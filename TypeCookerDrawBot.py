from collections import OrderedDict
import datetime

construction = ("Construction", [
    "roman",
    "italic",
    "caps and small caps",
    "capitals with roman",
    "capitals with italic",
    "continuous script",
    "casual brush script",
    "nothing",
])

ascender = ("Ascender", [
    "longer than normal",
    "shorter than normal",
    "much shorter than normal",
    "none at all",
    "doesn't matter",
])

descender = ("Descender", [
    "longer than normal",
    "shorter than normal",
    "much shorter than normal",
    "none at all",
    "doesn't matter",
])

width = ("Width", [
    "compressed",
    "condensed",
    "narrow",
    "normal",
    "extended",
    "wide",
    "very wide",
    "extremely wide",
])

contrastType = ("Contrast type", [
    "broad nib",
    "pointed nib",
    "transitional",
    "speedball nib",
    "brush",
    "can't be determined",
])

contrastAmount = ("Contrast amount", [    
    "inverted contrast",
    "slightly inverted contrast",
    "no contrast at all (thick = thin)",
    "no visible contrast",
    "very low contrast",
    "low contrast",
    "some contrast",
    "visible contrast",
    "quite some contrast",
    "a lot of contrast",
    "high contrast",
    "very high contrast",
    "extreme contrast",
])

stems = ("Stems", [
    "straight",
    "some ductus",
    "not a single straight line",
    "not a single straight angle",
    "flared",
])

strokeEndings = ("Stroke endings", [    
    "straight, no serif",
    "rounded, no serif",
    "wedge shaped serifs",
    "slab shaped serifs",
    "some serifs here and there",
    "only serifs at the top end",
    "only serifs at the bottom end",
])

strokeWeight = ("Stroke weight", [    
    "hairline",
    "very thin",
    "thin",
    "extra light",
    "light",
    "book",
    "plain",
    "medium",
    "semi bold",
    "bold",
    "extra bold",
    "black",
    "heavy",
])

intendedApplication = ("Intended application", [
    "unknown",
    "multi-purpose",
    "newsprint",
    "smooth offset printing",
    "engraving",
    "signage",
    "packaging",
    "subtitles on television",
    "anti-aliased bitmaps",
    "rubber stamping",
])

intendedSize = ("Intended size", [
    "use very small",
    "reading sizes",
    "display sizes",
    "very large sizes",
])

special = ("Special", [
    "only straight lines",
    "octagonal construction",
    "rough contours",
    "casual",
    "sketchy appearance",
    "cut as stencil without drop-out counters",
    "must contain at least 1 ligature",
    "must contain at least 2 ligatures",
    "initial and terminal swash variations",
])

recipe = OrderedDict([
    construction,
    ascender,
    descender,
    width,
    contrastType,
    contrastAmount,
    stems,
    strokeEndings,
    strokeWeight,
    intendedApplication,
    intendedSize,
    special
])


w, h = 842, 595
size(w, h)

m = 30
f = 8
fs = 7

font("Menlo-Regular")
fontSize(fs)

length = len(recipe.items())
col = 4
row = round((length/col))

today = datetime.datetime.now().strftime("%Y-%m-%d")

translate(m, f+row*f*3)

typeCookerDate = "TypeCooker "+today

text(typeCookerDate, (0, f*3))

print typeCookerDate
i = 1
for key, value in recipe.items():
    val = choice(value)
    print i, key, '—', val
    text(key.upper(), (0, 0))
    translate(0, -f)
    text(val, (0, 0))
    translate(0, -f*2)
    if i % row == 0:
        translate(w/col-m, row*f*3)
    i+=1

# save to desktop
#saveImage(["~/Desktop/"+typeCookerDate+".pdf"])