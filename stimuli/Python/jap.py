# math_seq 1
ei = 3
suu1 = int(ei)
suu2 = int(ei*ei)
suu3 = int(ei*ei*ei)

print(suu1 + suu2 + suu3)

# math_seq 2
import math

ei, be = 4, 8
heikin = (ei + be) / 2
bunsan = (ei - heikin)**2 + (be - heikin)**2
hensa = math.sqrt(bunsan / 2)

print(hensa)

# math_seq 3
tenn1 = [3, 0]
tenn2 = [6, 4]
kyori = (tenn1[0] - tenn2[0])**2 + (tenn1[1] - tenn2[1])**2

print(kyori**0.5)

# math_seq 4
sincho = 5
taiju = 100
keisu = taiju / (sincho*sincho)

print(keisu)

# math_seq 5
suu = 3432
shin_suu1 = suu // 1000
shin_suu2 = (suu - shin_suu1*1000)

print(shin_suu2)

# math_seq 6
(ex1, wi1) = (5, 3)
(ex2, wi2) = (7, 9)

chu_ex = (ex1 + ex2) / 2
chu_wi = (wi1 + wi2) / 2

print((chu_ex, chu_wi))

# math_seq 7
iremono = [11, 23, 35]
kekka = iremono[0] + iremono[-1]

print(kekka)

# math_seq 8
suu_risto = [5, 3, 8, 4, 9]

daiichi_kotae = max(suu_risto)
daini_kotae = min(suu_risto)

print(daiichi_kotae - daini_kotae)

# math_seq 9
rinpen = 12
shahen = 13
taihen = (shahen**2 - rinpen**2)**0.5

print(taihen)

# math_seq 10
suu = 4
bunbo = 8

pacento = suu*100 / bunbo

print(str(pacento) + '%')

# math_seq 11
otonas = 15
hiritu_oto_ko = 2.5
kodomo = otonas / hiritu_oto_ko

print(kodomo)

# math_seq 12
cho_inchi = 3
haba_inchi = 5
inchi_he_fiito = 3
kekka = cho_inchi*inchi_he_fiito*haba_inchi*inchi_he_fiito

print(kekka)

# math_seq 13
ech_genshis = 2
ou_genshis = 2
suu_bunshis = 12
zenn_genshis = suu_bunshis*(ech_genshis + ou_genshis)

print(zenn_genshis)

# math_seq 14
ringos, nashis, orenjis = 5, 4, 2
suu_kakeras = ringos*4 + nashis*4 + orenjis*8

print(suu_kakeras)

# math_seq 15
import math

suuji1, suuji2 = 4, 3
suuji1_chisa = math.sqrt(suuji1)
suuji2_ooki = suuji2**2

print(suuji1_chisa + suuji2_ooki)

# math_seq 16
he_waru = 3
he_tasu = 5
he_hiku = 10
suu1 = 4
suu2 = suu1 + (he_tasu*5)
suu2 -= he_hiku
suu1 = 1
suu2 = (suu2 - suu1) / he_waru

print(suu2)

# math_seq 17
ex, wi = 2, 4
kekka1 = ex**2 + wi**2
kekka2 = (ex + wi)**2
zenn = kekka1 + kekka2

print(zenn)

# math_seq 18
ei, be, se = 1, 3.5, 10
nameraka = (ei + se) // 2
chig = abs(nameraka - be)

print(chig)

# math_for 1
gunn_deeta = [1, 5, 3]
suu = 3

for atai in gunn_deeta:
    seki = suu*atai

print(seki)

# math_for 2
suujis = [5, 7, 4, 8]
kotaes = []

for atai in suujis:
    kotaes.append(atai - 1)

print(kotaes)

# math_for 3
kazu = 5
kei_kazu = 0

for enu in range(kazu + 1):
    kei_kazu += enu

print(kei_kazu)

# math_for 4
kazus = [10, 2, 30]
sek = 1

for enu in kazus:
    sek = sek*enu

print(sek)

# math_for 5
kazu_risto = [45, 60, 37]
kago = []

for kazu in kazu_risto:
    kago.append(kazu % 15)

print(kago)

# math_for 6
kazu = [3, 7, 0, 1, 2, 2]
shin_kazu = 1

for ex in range(1, len(kazu), 2):
    shin_kazu *= kazu[ex]

print(shin_kazu)

# math_for 7
kazus = [3, 5, 8]
chigai = 0

for kazu in kazus:
    chigai = kazu - chigai

print(chigai)

# math_for 8
enu = 3
zenn = 0

for ai in range(enu, -1, -1):
    zenn += ai*ai*ai

print(zenn)

# math_for 9
hitobito = 12
kazokus = hitobito / 4
amedama = 0

for kazoku in range(int(kazokus)):
    amedama += 2

print(amedama)

# math_for 10
teisuu = 1
suuji_kous = 3
aru = 2
zenn = 0

for ai in range(suuji_kous):
    zenn += teisuu*aru**ai

print(zenn)

# math_for 11
risto1 = [4, 4, 6]
risto2 = [1, 2, 4]
risto3 = [3, 2, 1]

for ai in range(len(risto1)):
    risto3[ai] += risto1[ai] + risto2[ai]

print(risto3)

# math_for 12
tapuru_risto = [(1, 2), (3, 4), (-1, 9)]
ittei_kei = 0

for kazu_kumi in tapuru_risto:
    ittei_kei += kazu_kumi[1]

print(ittei_kei)

# math_for 13
kazu_risto = [3, 1, 0, -2, 5]
zenn = 0

for shisu, kazu in enumerate(kazu_risto):
    zenn += shisu*kazu

print(zenn)

# math_for 14
el = list()

for ai in range(1, 4):
    el.append(ai**2)

print(el[-2:])

# math_for 15
shisu_risto = [1, 0, 2]
kazu_risto = [1, 4, 6]
tou_risto = []

for ai in range(len(shisu_risto)):
    tou_risto.append(kazu_risto[shisu_risto[ai]])

print(tou_risto)

# math_for 16
suujis = [1, 2, -2, -8, 0]
hohaba = 2
kekka = []

for shs in range(0, len(suujis), hohaba):
    kekka.append(suujis[shs] - 1)

print(kekka)

# math_for 17
suujis = [4, 5, 3, 8, 3, 2, 5]
nagasa = len(suujis)
kazu = 0

for ai in range(nagasa // 2 + 1):
    kazu += suujis[ai]

print(kazu)

# math_for 18
kaishi = 3
zenn = 0

for ai in range(kaishi, -1, -1):
    zenn -= ai*ai

print(zenn)

# math_if 1
enu = 1800

if abs(1000 - enu) <= 100:
    print(1)
elif abs(2000 - enu) <= 100:
    print(1)
else:
    print(0)

# math_if 2
ex, wi, ze = 3, 3, 3
tasu = ex + wi + ze

if ex == wi == ze:
    tasu = tasu*3

print(tasu)

# math_if 3
kazu1, kazu2, kazu3 = 3, 2, 2

if kazu1 == kazu2 or kazu2 == kazu3 or kazu1 == kazu3:
    tasu = 0
else:
    tasu = kazu1 + kazu2 + kazu3

print(tasu)

# math_if 4
dorus1, dorus2 = 10, 6
dorus_kei = dorus1 + dorus2

if dorus_kei in range(15, 20):
    print(20)
else:
    print(dorus_kei)

# math_if 5
yosoku = 13
jissai = 11
gosa = 2

if (yosoku - jissai < gosa) or (yosoku - jissai > -1*gosa):
    print(yosoku - jissai + gosa)
else:
    print(yosoku - jissai - gosa)

# math_if 6
ooki_kazu, chisa_kazu = 64, 16

if ooki_kazu % chisa_kazu == 0:
    print(1)
else:
    print(0)

# math_if 7
jibun, kimi, kanojyo = 5, 3, 2

if (kimi < jibun and jibun < kanojyo):
    print(jibun)

elif (kanojyo < jibun and jibun < kimi):
    print(jibun)

elif (kanojyo < kimi and kimi < jibun):
    print(kimi)

elif (jibun < kimi and kimi < kanojyo):
    print(kimi)

else:
    print(kanjyo)

# math_if 8
nen = 2018
if (nen % 400 == 0):
    print("A")
elif (nen % 100 == 0):
    print("B")
elif (nen % 4 == 0):
    print("C")
else:
    print("D")

# math_if 9
inu_toshi = 12

if inu_toshi <= 2:
    hito_toshi = inu_toshi*10.5
else:
    hito_toshi = 21 + (inu_toshi - 2)*4

print(hito_toshi)

# math_if 10
import math

kazu1, kazu2, kazu3 = 10, 12, 14

if math.sqrt(kazu1 + kazu2 + kazu3).is_integer():
    print(kazu1 + kazu2 + kazu3)
else:
    print(kazu2 + kazu3)

# math_if 11
nyuryoku = [123, 32, 43, 10, 0, -2, -59, 12, 0]

if nyuryoku[0] // 100 in nyuryoku:
    print(nyuryoku[0] // 100)
elif nyuryoku[0] % 100 in nyuryoku:
    print(nyuryoku[0] % 100)
elif nyuryoku[0] // 10 in nyuryoku:
    print(nyuryoku[0] // 10)

# math_if 12
kyara1, kyara2 = 10, 10

if kyara1 < 10:
    print("b")
elif kyara2 == 10:
    print("b")
elif kyara2 < 10:
    print("a")
elif kyara1 == 10 and kyara2 == 10:
    print("tie")

# math_if 13
risto1 = [12, 34, 36, 71, 3, 42]
risto2 = [53, 23, 16, 24, 5, 15]
risto3 = [1, 34, 10, 91, 43, 26]
suuji = 34

if suuji in risto1 or (suuji in risto2 and suuji in risto3):
    print(risto1[0])
elif suuji in risto2 or (suuji in risto3 and suuji in risto1):
    print(risto2[0])
elif suuji in risto3 or (suuji in risto1 and suuji in risto2):
    print(risto3[0])

# math_if 14
yosoku = 8
jissai = 10
gosa = 3

if (yosoku - jissai < gosa) and (yosoku - jissai > -1*gosa):
    print(yosoku - jissai)
else:
    print(gosa)

# math_if 15
ringos, orenjis = 3, 8

if ringos == orenjis:
    print(ringos + orenjis)
elif abs(ringos - orenjis) == 5 or (ringos + orenjis) == 5:
    print(ringos*orenjis)
else:
    print(ringos - orenjis)

# math_if 16
kuukiondo = 70
shitsudo = 100

if kuukiondo >= 100:
    print("A")
elif kuukiondo >= 92 and shitsudo > 75:
    print("B")
elif kuukiondo > 88 and shitsudo >= 85:
    print("C")
elif kuukiondo == 75 and shitsudo <= 65:
    print("D")
else:
    print("E")

# math_if 17
henn1 = 12
henn2 = 14
henn3 = 124

if henn1 == henn2 and henn2 == henn3:
    print(1)
elif henn1 == henn2 or henn2 == henn3 or henn1 == henn3:
    print(2)
else:
    print(3)

# math_if 18
kumas, inus, ookamis = 10, 4, 16

if (kumas > inus) and (kumas > ookamis):
    print(ookamis)
elif (inus > kumas) and (inus > ookamis):
    print(kumas)
elif (ookamis > kumas) and (ookamis > inus):
    print(inus)

# str_seq 1
daiichi_namae = "Fernando"
saigo_namae = "Federiko"

print(saigo_namae + " " + daiichi_namae)

# str_seq 2
fairumei = "alphabet.java"
henkou = fairumei.split(".")

print(henkou[-1])

# str_seq 3
iro_retsu = ["Red", "Green", "White", "Black"]

print((iro_retsu[0], iro_retsu[-1]))

# str_seq 4
jibunno = "red"
kimino = "green"

kari = jibunno
jibunno = kimino
kimino = kari

print(jibunno, kimino)

# str_seq 5
kudamono = "banana"
kekka = kudamono[-1:] + kudamono[1:-1] + kudamono[:1]

print(kekka)

# str_seq 6
tagu = "i"
kotoba = "MIT"
shin_kotoba = "<" + tagu + ">" + kotoba

print(shin_kotoba)

# str_seq 7
mojiretu1 = "onion"
shin_mojiretu = mojiretu1[-2:]
zoufukugo = shin_mojiretu*4

print(zoufukugo)

# str_seq 8
mojiretu1 = "WEEKEND"

print(mojiretu1[:4].lower() + mojiretu1[4:])

# str_seq 9
koto = "python"
shin_koto = koto[0].upper() + koto[1:-1] + koto[-2].upper()

print(shin_koto)

# str_seq 10
shoku_retsu = ["crab", "lettuce", "carrot"]
shoku_retsu[1] = shoku_retsu[2] + shoku_retsu[1]

print(len(shoku_retsu[1]))

# str_seq 11
kotoba_ichi = "rap"
kotoba_ni = "hat"

kotoba_san = len(kotoba_ni)*kotoba_ichi + kotoba_ni

print(kotoba_san)

# str_seq 12
basuke = "groceries"
shin_basuke = basuke[1:3]

print(shin_basuke[0])

# str_seq 13
nomimono_ichi = "wine"
nomimono_ni = "beer"

maze = nomimono_ichi[:2] + nomimono_ni + nomimono_ichi[:2]

print(maze)

# str_seq 14
nezumi_ichi = "rat"
nezumi_ni = "mouse"

haiburi = nezumi_ichi[1:] + nezumi_ni[3]*2

print(haiburi)

# str_seq 15
iroha = "star"
nihohe = iroha + iroha

print(nihohe[2:5])

# str_seq 16
henshin = "wow"
henshin = henshin*2

print(henshin[2:4])

# str_seq 17
angou = "he.elk.set.to"
kaidoku = angou.split("e")

print(kaidoku[-1])

# str_seq 18
kotoba1 = "apple"
kotoba2 = "orange"

kotoba_souzou = kotoba1 + kotoba2
kotoba_souzou += kotoba1

print(kotoba_souzou)

# str_for 1
petto = "cat"
enu = len(petto)
kekka = ""

for ai in range(enu):
    kekka = kekka + petto

print(kekka)

# str_for 2
bunsyo = "red fox"
karappo = ""

for kana in bunsyo:
    karappo = karappo + kana + "s"

print(karappo)

# str_for 3
kotobas_retsu = ["PHP", "Code", "Hack"]
kotoba_cho = ""

for enu in kotobas_retsu:
    kotoba_cho += str(len(enu))

print(kotoba_cho)

# str_for 4
kotoba_retsu = ["apple", "carrot", "orange"]

for kotoba in kotoba_retsu:
    arata_kotoba = ">" + kotoba

print(arata_kotoba)

# str_for 5
pazuru = "crow"
kotoba_ginko = []

for ai in range(len(pazuru) - 1):
    kotoba_ginko.append(pazuru[ai] + pazuru[ai + 1])

print(kotoba_ginko)

# str_for 6
kotoba = "outer"
tegamis = "the"
bunsuirei = []

for tegami in tegamis:
    bunsuirei.append(tegami in kotoba)

print(bunsuirei)

# str_for 7
mojiretu1 = "humdrum"
mojiretu2 = ""

for shisu in range(2):
    kana = mojiretu1[shisu]
    mojiretu2 += kana*shisu

print(mojiretu2)

# str_for 8
angou = "set"
kotae = ""

for shisu in range(1, 3):
    kotae = kotae + angou[shisu] + "ab"

print(kotae)

# str_for 9
doubutu = "pigs"
shin_kotoba = ""

for kana in range(len(doubutu) - 1, -1, -2):
    shin_kotoba += doubutu[kana]

print(shin_kotoba)

# str_for 10
kudamonos = ["apple", "plum", "fig"]
kazoe = 0

for kudamono in kudamonos:
    kazoe += len(kudamono)

print(kazoe)

# str_for 11
shoku = "cop"
chochiku = ""

for sih in range(len(shoku)):
    chochiku += shoku[sih]*sih

print(chochiku)

# str_for 12
shokubutu = "clover"
tane = "seed"
shin_tane = ""

for shisu in range(len(tane)):
    shin_tane += shokubutu[shisu]

print(shin_tane)

# str_for 13
gengo = "hello"
kara_mojiretu = ""

for kana in gengo:
    kara_mojiretu += kana*2

print(kara_mojiretu)

# str_for 14
tegami = "q"
daimeisis = ["I", "you"]

for sihyo in range(len(daimeisis)):
    daimeisis[sihyo] = daimeisis[sihyo] + tegami

print(daimeisis)

# str_for 15
gengo = "babyface"
seika = ""

for kosu in range(2):
    seika += gengo[-(kosu + 2)]

print(seika)

# str_for 16
yogo = "sausage"
usiro = ""

for keta in range(3):
    usiro += yogo[2*keta]

print(usiro)

# str_for 17
kakera1 = "gab"
kakera2 = "cab"
kotae = []

for sih in range(len(kakera1)):
    kotae.append(kakera1[sih] == kakera2[sih])

print(kotae)

# str_for 18
kyoushitu = ["An", "May", "John"]
kurasu_retsu = ""

for namae in kyoushitu:
    kurasu_retsu += namae[1]

print(kurasu_retsu)

# str_if 1
mojiretu = "Array"

if mojiretu[:2] == "ra":
    print(mojiretu)
else:
    print("ra" + mojiretu)

# str_if 2
furui = "stuff"
ikichi = 2

if len(furui) < 2:
    ikichi = len(furui)

shin = furui[:ikichi]

print(shin)

# str_if 3
gengo = "characteristic"

if len(gengo) <= 6:
    print(gengo)
else:
    print(gengo[0:3])

# str_if 4
mojiretu = "resource"

if len(mojiretu) < 2:
    print("--")
else:
    print(mojiretu[0:2] + mojiretu[-2:])

# str_if 5
hyougen = "interesting"

if hyougen[-3:] == "ing":
    hyougen += "ly"
else:
    hyougen += "ing"

print(hyougen)

# str_if 6
mokuhyo = "program"

if len(mokuhyo) <= 3:
    print(mokuhyo)
else:
    print(mokuhyo[:3])

# str_if 7
adoresu = "https://www.mit.edu/bcs"

if adoresu[0] == "h" and adoresu[-1] == "/":
    print(adoresu[1])
elif adoresu[0] == "h":
    print(adoresu[-1])
else:
    print(adoresu)

# str_if 8
shoku = "popcorn"

if len(shoku) % 4 == 0:
    print(shoku)
else:
    print(shoku[-1::-1])

# str_if 9
gengo = "crybaby"
sihyo = "crx"

if gengo[:len(sihyo)] == sihyo:
    print(1)
else:
    print("Nothing")

# str_if 10
ippan = "aardvark"
tokuhitu = ippan[:2]

if tokuhitu[0] == tokuhitu[1]:
    print(ippan)
else:
    print(tokuhitu)

# str_if 11
hento = ["hey", "me", "too"]

if len(hento[2]) < 2:
    hento = "ab"

print(hento)

# str_if 12
tegamis = ["a", "e", "t", "o", "u"]
gengo = "CreepyNuts"

if (gengo[1] in tegamis) and (gengo[6] in tegamis):
    print(0)
elif (gengo[1] in tegamis) or (gengo[6] in tegamis):
    print(1)
else:
    print(2)

# str_if 13
karada_ichi = "eat"
karada_ni = "ear"

if karada_ichi[0] == karada_ni[0] and karada_ichi[2] == karada_ni[2]:
    print(0)
elif karada_ichi[0] == karada_ni[0] and karada_ichi[1] == karada_ni[1]:
    print(1)
else:
    print(2)

# str_if 14
bunsyou = "I am a"
gengo = "cat"

if len(gengo) > 3:
    print(gengo)
elif bunsyou[-1] == gengo[1]:
    print(bunsyou)
else:
    print(bunsyou + " " + gengo)

# str_if 15
namae = "Gauss"
setto1 = "art"
setto2 = "science"

if namae[1:3] in setto1:
    print(1)
elif namae[-1] in setto2:
    print(2)
else:
    print(0)

# str_if 16
gakko = "middle"
undou = "football"

if gakko in undou:
    print(1)
elif len(gakko) > len(undou):
    print(2)
else:
    print(3)

# str_if 17
genpon = "coyote"
mosya = genpon[3:6]

if len(mosya)*2 > len(genpon):
    print(mosya)
else:
    print(genpon)

# str_if 18
honn = "anemone"

if (honn[2] == honn[-1]) and (honn[1] == honn[-3]):
    print(1)
elif honn[2] == honn[-1]:
    print(2)
else:
    print(3)
