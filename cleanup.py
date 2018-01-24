# open the relevant files
f = open("haushalt1_clean.csv", "w+")
t = open("Haushalt1.csv", "r")

def textbau(l):
    l = l.strip("\"")
    l = l.split(",")
    s = l[-1].split(" ")
    l[-1] = s[0]
    l.append(s[-1])
    #print("Davor ", l)
    l = luckenschliesser(l) #EVTl hier etwas ändern - PARAMETER?
    #print("Fertig ", l)
    tmp = ""
    for item in l:
        tmp = tmp + "," + item
    #print(tmp)
    return tmp

##NACHARBEITEN!!!
    # Irgendein Fehler hier... weiß nicht was!
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
# write in the haushalt1_clean.csv file
f.write(text)

# close the original
t.close()
f.close()

