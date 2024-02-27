alpha = {
    " " : ["           ","           ","           ","           ","           ","           ","           "],
    "a" : ["   ###     ","  ## ##    "," ##   ##   ","##     ##  ","#########  ","##     ##  ","##     ##  "],
    "b" : ["########   ","##     ##  ","##     ##  ","########   ","##     ##  ","##     ##  ","########   "],
    "c" : [" ######    ","##    ##   ","##         ","##         ","##         ","##    ##   "," ######    "],
    "d" : ["########   ","##     ##  ","##     ##  ","##     ##  ","##     ##  ","##     ##  ","########   "],
    "e" : ["########   ","##         ","##         ","######     ","##         ","##         ","########   "],
    "f" : ["########   ","##         ","##         ","######     ","##         ","##         ","##         "],
    "g" : [" ######    ","##    ##   ","##         ","##   ####  ","##    ##   ","##    ##   "," ######    "],
    "h" : ["##     ##  ","##     ##  ","##     ##  ","#########  ","##     ##  ","##     ##  ","##     ##  "],
    "i" : ["####       "," ##        "," ##        "," ##        "," ##        "," ##        ","####       "],
    "j" : ["      ##   ","      ##   ","      ##   ","      ##   ","##    ##   ","##    ##   "," ######    "],
    "k" : ["##    ##   ","##   ##    ","##  ##     ","#####      ","##  ##     ","##   ##    ","##    ##   "],
    "l" : ["##         ","##         ","##         ","##         ","##         ","##         ","########   "],
    "m" : ["##     ##  ","###   ###  ","#### ####  ","## ### ##  ","##     ##  ","##     ##  ","##     ##  "],
    "n" : ["##    ##   ","###   ##   ","####  ##   ","## ## ##   ","##  ####   ","##   ###   ","##    ##   "],
    "o" : [" #######   ","##     ##  ","##     ##  ","##     ##  ","##     ##  ","##     ##  "," #######   "],
    "p" : ["########   ","##     ##  ","##     ##  ","########   ","##         ","##         ","##         "],
    "q" : [" #######   ","##     ##  ","##     ##  ","##     ##  ","##  ## ##  ","##    ##   "," ##### ##  "],
    "r" : ["########   ","##     ##  ","##     ##  ","########   ","##   ##    ","##    ##   ","##     ##  "],
    "s" : [" ######    ","##    ##   ","##         "," ######    ","      ##   ","##    ##   "," ######    "],
    "t" : ["########   ","   ##      ","   ##      ","   ##      ","   ##      ","   ##      ","   ##      "],
    "u" : ["##     ##  ","##     ##  ","##     ##  ","##     ##  ","##     ##  ","##     ##  "," #######   "],
    "v" : ["##     ##  ","##     ##  ","##     ##  ","##     ##  "," ##   ##   ","  ## ##    ","   ###     "],
    "w" : ["##      ## ","##  ##  ## ","##  ##  ## ","##  ##  ## ","##  ##  ## ","##  ##  ## "," ###  ###  "],
    "x" : ["##     ##  "," ##   ##   ","  ## ##    ","   ###     ","  ## ##    "," ##   ##   ","##     ##  "],
    "y" : ["##    ##   "," ##  ##    ","  ####     ","   ##      ","   ##      ","   ##      ","   ##      "],
    "z" : ["########   ","     ##    ","    ##     ","   ##      ","  ##       "," ##        ","########   "]
}
############ for char ############
# ch = input("Enter a char = ").lower()
# for i in range(7):
#     print(alpha[ch][i])

############ output ############
# enter a char = a
#    ###
#   ## ##
#  ##   ##
# ##     ##
# #########
# ##     ##
# ##     ##

############ For String ############
name = input("Enter a name = ").lower()

for i in range(7):
    for j in name:
        print(alpha[j][i].replace("#", f"{j}"),end="")
    print()

############ output ############
# enter your name = aadesh
   ###       ###    ########  ########  ######  ##     ##
  ## ##     ## ##   ##     ## ##       ##    ## ##     ##
 ##   ##   ##   ##  ##     ## ##       ##       ##     ##
##     ## ##     ## ##     ## ######    ######  #########
######### ######### ##     ## ##             ## ##     ##
##     ## ##     ## ##     ## ##       ##    ## ##     ##
##     ## ##     ## ########  ########  ######  ##     ##

