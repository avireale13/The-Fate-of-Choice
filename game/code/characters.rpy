# Declaring characters

define d = Character("Derek", color="CB2626")
define j = Character("Josh", color="009A25")
define o = Character  ("Olivia", color="A55DF2")
define pm = Character ("Mr.Murphy",  color="00499A")

define joshSize = 0.35
define oliviaSize = 0.22
define derekSize = 0.69
define derekSize2 = 1.35

define oliviaWidth = 2766
define oliviaHeight = 3500
define derekWidth = 486
define derekHeight = 600
# Character Images

image derek casual neutral = im.FactorScale(im.Crop("derek_casual_open.png", (0, 0, derekWidth, derekHeight)), derekSize2)
image derek eyebrow up = im.FactorScale(im.Crop("derek_eyebrows_up.png", (0, 0, derekWidth, derekHeight)), derekSize2)
image derek smile = im.FactorScale(im.Crop("derek_smile.png", (0, 0, derekWidth, derekHeight)), derekSize2)
image derek smile no teeth = im.FactorScale(im.Crop("derek_smile_eyebrows_up.png", (0, 0, derekWidth, derekHeight)), derekSize2)
image derek sad = im.FactorScale(im.Crop("derek_sad.png", (0, 0, derekWidth, derekHeight)), derekSize2)
image derek concerned = im.FactorScale(im.Crop("derek_concerned.png", (0, 0, derekWidth, derekHeight)), derekSize2)
image derek surprised = im.FactorScale(im.Crop(im.FactorScale("derek_surprised.png", derekSize), (0, 0, derekWidth, derekHeight)), derekSize2)
image derek surprised blush = im.FactorScale(im.Crop(im.FactorScale("derek_surprised_blush.png", derekSize), (0, 0, derekWidth, derekHeight)), derekSize2)

image olivia casual frown = im.FactorScale(im.Crop("olivia_casual_frown.png", (0, 0, oliviaWidth, oliviaHeight)), oliviaSize)
image olivia casual smile = im.FactorScale(im.Crop("olivia_casual_smile.png", (0, 0, oliviaWidth, oliviaHeight)), oliviaSize)
image olivia casual smile blush = im.FactorScale(im.Crop("olivia_casual_smile_blush.png", (0, 0, oliviaWidth, oliviaHeight)), oliviaSize)
image olivia casual open blush = im.FactorScale(im.Crop("olivia_casual_open_blush.png", (0, 0, oliviaWidth, oliviaHeight)), oliviaSize)


image josh casual neutral = im.FactorScale("josh_casual_open.png", joshSize)
image josh mad = im.FactorScale("josh_mad.png", joshSize)
image josh sad = im.FactorScale("josh_sad.png", joshSize)
image josh think = im.FactorScale("josh_think.png", joshSize)
