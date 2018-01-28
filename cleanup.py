# open the relevant files
#------------------------------------------------------------------------
# !!!!! CHANGE FILE NAME !!!!!!
#------------------------------------------------------------------------
f = open("haushalt6_clean.csv", "w+")
t = open("haushalt6.csv", "r")

#------------------------------------------------------------------------
# Creates one line of text
#------------------------------------------------------------------------
def textbau(l):
    l = l.strip("\"")               # delete "-symbols
    l = l.split(",")                # create list l from ","
    s = l[-1].split(" ")            # create sublist s from last list l item
    if len(s) == 2:                 # if sublist s has 2 items
        pass
    else:
        more_spaces(s, l)               # start function more_spaces(s) if more items than 2
    l[-1] = s[0]
    l.append(s[-1])
    #print("Davor ", l)
    l = luckenschliesser(l)
    #print("Fertig ", l)
    if l[0] == "":
        del l[0]
    tmp = ""
    for item in l:
        tmp = tmp + "," + item
    #print(tmp)
    return tmp

#------------------------------------------------------------------------
# Deletes spaces in cells
#------------------------------------------------------------------------
def luckenschliesser(zellen):
    zellen = zellen
    ind = 0
    for zelle in zellen:
        if zelle[:3].isalpha():
            #print(zelle)
            pass
        else:
            z_new = ""
            for z in zelle:
                if z == " ":
                    pass
                else:
                    z_new = z_new + z
            zellen[ind] = z_new
        ind += 1
    l = zellen
    #print("Inzwischen ", l)
    return l
          
#------------------------------------------------------------------------
# In case there are more spaces in the last row
#------------------------------------------------------------------------      
def more_spaces(s, l):
    count = len(s)
    l[-1] = s[0]
    for index in range(1, count):       # ERROR! Cullumn gets copied twice for some reason
        l.append(s[index])              # or appended twice... In very rare cases though.
    return l
    
    
text = ""
for l in t:
    if l[:2] == "\"\"":
        if l[:8] == "\"\",Summe":
            text = text + textbau(l)
        else:
            pass
    elif l[:2] == "Nr":
        pass
    elif l[:3] == "1,2":
        pass
    else:
        text = text + textbau(l)
        
# write in "haushalt1_clean.csv"
f.write(text)

# close files
t.close()
f.close()

