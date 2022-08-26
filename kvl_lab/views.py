from django.shortcuts import render


def index(requests):
    return render(requests, 'home.html', {})


def explain(requests):
    return render(requests, 'explain.html', {})


def code(requests):
    return render(requests, 'code.html', {})


def vlab(requests):
    circuit = requests.GET.get('type', 'default')
    resistor = requests.GET.get('resistor', 'default')
    voltage = requests.GET.get('voltage', 'default')
    f = open("circuit.txt", "a")
    if circuit != "default":
        f.write(circuit)

    if circuit != 'default':
        return render(requests, 'vlab.html', {'t': circuit})
    else:
        return render(requests, 'vlab.html', {'t': " ", 'r': " "})


# Create your views here.


def components(requests):
    circuit = requests.GET.get('type', 'default')
    resistor = requests.GET.get('resistor', 'default')
    voltage = requests.GET.get('voltage', 'default')
    print(circuit)
    if circuit == "parallel":
        return render(requests, 'components.html', {'t': circuit})
    elif circuit == "series":
        return render(requests, 'components.html', {'t': circuit})
    elif circuit == "simple":
        return render(requests, 'components.html', {'t': circuit})
    elif circuit == "sparallel":
        return render(requests, 'components.html', {'t': circuit})
    else:
        return render(requests, 'components.html')


def simple(requests):
    r = requests.GET.get('resistor', 'default')
    v = requests.GET.get('voltage', 'default')
    i = round(float(v) / float(r), 2)
    vd = round(-(float(i) * int(r)), 2)
    s = str(v) + "V" + " " + "+" + " " + "(" + str(vd) + ")" + "V"
    print(s)
    return render(requests, 'simpe.html', {"eq": s, 'r_value': r, 'c_value': v, 'i_value': i, 'v_drop': vd})


def series(requests):
    sr = requests.GET.get('sresistor', 'default')
    sv = requests.GET.get('svoltage', 'default')
    print(sr, sv)

    return render(requests, 'series.html', {'nr': sr, 'nv': sv})


def parallel(requests):
    pr = requests.GET.get('presistor', 'default')
    pv = requests.GET.get('pvoltage', 'default')
    return render(requests, 'parallel.html', {'nr': pr, 'nv': pv})


def seriescircuit(requests):
    tr = requests.GET.get('totalres', 'default')
    tv = requests.GET.get('totalvolt', 'default')
    ltr = []
    ltv = []
    for i in range(int(tr)):
        temp = 'r' + str(i)
        r = requests.GET.get(temp, 'default')
        ltr.append(int(r))

    for i in range(int(tv)):
        temp = 'v' + str(i)
        v = requests.GET.get(temp, 'default')
        ltv.append(int(v))

    length = len(ltr)
    vlength = len(ltv)
    resser = []
    vser = []
    respar = []
    vpar = []
    bat = []
    cpar = []

    Rsums = sum(ltr)
    Vsum = sum(ltv)
    cur = round((Vsum / Rsums), 2)
    print(ltr)
    print(ltv)
    print(Rsums)
    print(Vsum)
    for i in range(len(ltr)):
        vser.append(round((ltr[i] * cur), 2))

    loop0 = ""
    for i in range(len(ltv)):
        loop0 = loop0 + str(ltv[i]) + "V " + "+ "
    print((loop0))
    i = len(vser) - 1
    while i >= 0:
        loop0 = loop0 + "(" + str(round(-vser[i], 2)) + ")" + "V" + " " + "+" + " "
        i = i - 1
    s = loop0[0:len(loop0) - 2]
    print(s)

    print(vser)

    print(tr, tv)
    return render(requests, 'seriescircuit.html',
                  {"cal": s, "volts": ltv, "res": ltr, "lx": length, "lv" : vlength, "total_res": tr, "total_volt": tv,
                   "serisvolt": vser, "total_cur": cur})


def parallelcircuit(requests):
    tr = requests.GET.get('totalres', 'default')
    tv = requests.GET.get('totalvolt', 'default')
    h = int(tr)
    ltr = []
    ltv = []
    for i in range(int(tr)):
        temp = 'r' + str(i)
        r = requests.GET.get(temp, 'default')
        ltr.append(int(r))

    for i in range(int(tv)):
        temp = 'v' + str(i)
        v = requests.GET.get(temp, 'default')
        ltv.append(int(v))

    resser = []
    vser = []
    respar = []
    vpar = []
    bat = []
    cpar = []
    Rsump = 0
    for i in ltr:
        Rsump += 1 / i
    Rsump = round(1 / Rsump, 2)
    Vsum = sum(ltv)
    cur = round((Vsum / Rsump), 2)
    for i in range(len(ltr)):
        vpar.append(round(Vsum, 2))
    for i in range(len(ltr)):
        cpar.append(round((vpar[i] / ltr[i]), 2))
    vdrop = []
    for i in range(0, len(cpar)):
        vdrop.append(cpar[i] * ltr[i])
    print(vdrop)
    print(vpar)
    print(Rsump)
    print(cpar)
    print(cur)

    loop0 = ""
    loop1 = ""
    loop = ""
    t = ""
    for i in range(len(vdrop)):
        t = t + "loop" + str(i+1) + ","
        if i == 0:
            loop0 = loop0 + str(round(-vdrop[i], 2)) + " V" + " " + "+" + " "
        if i == 1:
            loop0 = loop0 + str(round(vdrop[i], 2)) + " V"
    print((loop0))
    j = t[0:len(t)-7]
    print(j)
    vt = h * 150 + 50
    theight = h * 150
    print(vt)

    print(tr, tv)

    return render(requests, 'parallelcircuit.html',
                  {"y":j,"loop0": loop0, "p": 60, "theight": theight, "calht": vt, "volts": vpar, "curpar": cpar, "res": ltr,
                   "vpar": Vsum, "total_res": h, "total_volt": tv, "total_cur": cur})

def sparallel(requests):
    spp_r = requests.GET.get('spp_resistor', 'default')
    sps_r = requests.GET.get('sps_resistor', 'default')
    sp_v = requests.GET.get('sp_voltage', 'default')
    return render(requests,"sparallel.html",{"spp_r":spp_r,"sps_r":sps_r,"sp_v":sp_v})

def sparallelcircuit(requests):
    p_totalres = requests.GET.get("p_totalres","default")
    s_totalres = requests.GET.get("s_totalres","default")
    totalvolt = requests.GET.get("totalvolt", "default")
    sps_r = []
    spp_r = []
    vt = []
    for i in range(int(p_totalres)):
        temp = 'sp' + str(i)
        r = requests.GET.get(temp, 'default')
        spp_r.append(int(r))
    for i in range(int(s_totalres)):
        temp = 'sr' + str(i)
        r = requests.GET.get(temp, 'default')
        sps_r.append(int(r))
    for i in range(int(totalvolt)):
        temp = 'v' + str(i)
        v = requests.GET.get(temp, 'default')
        vt.append(int(v))

    vser = []
    vpar = []
    cpar = []
    Rsums = sum(sps_r)
    Rsump = 0
    for i in spp_r:
        Rsump += 1 / i
    if Rsump:
        Rsump = 1 / Rsump
    Rsum = Rsump + Rsums
    Vsum = sum(vt)
    cur = round((Vsum / Rsum),2)
    for i in range(int(s_totalres)):
        vser.append(round((sps_r[i] * cur),2))
    Vsum -= sum(vser)
    Vsum = round(Vsum,2)
    for i in range(int(p_totalres)):
        vpar.append(round(Vsum,2))
    for i in range(int(p_totalres)):
        cpar.append(round((vpar[i] / spp_r[i]),2))
    print(vser,vpar,cpar)

    loop0 = ""
    for i in range(int(len(cpar))):
        if i ==0:
            loop0 = loop0 + "(" + "-"+(str(cpar[i])) + "*" +(str(spp_r[i])) + ")" +"V"+" + " + " "
        if i == 1:
            loop0 = loop0 + (str(cpar[i])) + "*" +(str(spp_r[i])) +"V"
        if i>1:
            break
    print(loop0)

    bigloop = ""
    for i in range(len(vt)):
        bigloop = bigloop + str(vt[i]) + "V" + " + "
    bigloop = bigloop + "(" + "-" +str(Vsum)+"V"+ ")" + " + "
    i = len(vser) - 1
    while i>=0:
        bigloop = bigloop + "(" + "-" +str(vser[i]) + "V"+ ")" +  " + "
        i = i - 1
    bigloop = bigloop[0:len(bigloop)-2]
    print(bigloop)

    bigloop1 = ""
    for i in range(len(vt)):
        bigloop1 = bigloop1 + str(vt[i]) + "V" + " + "
    bigloop1 = bigloop1 + "(" + "-"+(str(cpar[1])) + "*" +(str(spp_r[1])) + ")" +"V"+ " + "
    i = len(vser) - 1
    while i >= 0:
        bigloop1 = bigloop1 + "(" + "-" + str(vser[i]) + "V" + ")" + " + "
        i = i - 1
    bigloop1 = bigloop1[0:len(bigloop1) - 2]
    print(bigloop1)

    return render(requests,"sparallelcircuit.html",{"bigloop":bigloop,"bigloop1":bigloop1,"loop0":loop0,"vser":vser,"Vsum":Vsum,"vt":vt,"cpar" : cpar , "cur":cur, "sps_r":sps_r,"spp_r":spp_r,"s_totalres":s_totalres,"p_totalres":p_totalres,"totalvolt" : totalvolt})
