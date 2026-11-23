# Fin Markets Fast Solver (Tout en decimal) - Mock 7


def q1():
    print("\n--- Q1 : Payoff Forward (Commodites) ---")
    sens = input("Position (L=Long / S=Short) : ").upper()
    nb = float(input("Nb contrats (ex: 91) : "))
    taille = float(input("Taille contrat (ex: 127) : "))
    f0 = float(input("Prix Fwd F0 (ex: 56) : "))
    st = float(input("Prix Spot ST (ex: 46) : "))

    if sens == "L":
        payoff = nb * taille * (st - f0)
    else:
        payoff = nb * taille * (f0 - st)

    print("----------------------")
    print("Payoff =", int(round(payoff, 0)))


def q2():
    print("\n--- Q2 : Prix Livraison Forward ---")
    s0 = float(input("Prix action S0 (ex: 36.5) : "))
    b0 = float(input("Prix ZC B0 (ex: 87.1) : "))
    n = float(input("Nominal ZC N (ex: 100) : "))
    nb = float(input("Nb actions (ex: 100) : "))

    d_t = b0 / n
    f0 = s0 / d_t
    total_f = nb * f0

    print("----------------------")
    print("F0/action =", round(f0, 4))
    print("Total =", round(total_f, 2))


def q3():
    print("\n--- Q3 : Duration Obligation ---")
    t = int(input("Maturite T (annees) : "))
    c_rate = float(input("Taux coupon (0 si ZC) : "))

    if c_rate == 0:
        d = t
    else:
        y = float(input("YTM y (ex: 0.07) : "))
        n = 100.0
        c = n * c_rate
        pvs = [
            (c + n if i == t else c) / ((1 + y) ** i) for i in range(1, t + 1)
        ]
        d = sum([i * pv for i, pv in enumerate(pvs, 1)]) / sum(pvs)

    print("----------------------")
    print("Duration D =", round(d, 4))


def q4():
    print("\n--- Q4 : Payoff Forward (Actions) ---")
    sens = input("Position (L=Long / S=Short) : ").upper()
    nb = float(input("Nb contrats (ex: 97) : "))
    m = float(input("Actions/contrat (ex: 100) : "))
    f0 = float(input("Prix Fwd F0 (ex: 270) : "))
    st = float(input("Prix Spot ST (ex: 282) : "))

    if sens == "L":
        payoff = nb * m * (st - f0)
    else:
        payoff = nb * m * (f0 - st)

    print("----------------------")
    print("Payoff =", int(round(payoff, 0)))


def q5():
    print("\n--- Q5 : Variation Prix (% Delta P) ---")
    t = int(input("Maturite T (ex: 20) : "))
    c_rate = float(input("Taux coupon (0 si ZC) : "))
    y = float(input("Taux y (ex: 0.02) : "))
    bps = float(input("Variation bps (ex: 32) : "))

    if c_rate == 0:
        d = t
    else:
        n = 100.0
        c = n * c_rate
        pvs = [
            (c + n if i == t else c) / ((1 + y) ** i) for i in range(1, t + 1)
        ]
        d = sum([i * pv for i, pv in enumerate(pvs, 1)]) / sum(pvs)

    dy = bps / 10000.0
    dp_p = -d * (dy / (1 + y))

    print("----------------------")
    print("Delta P / P0 =", round(dp_p, 4))


def main():
    while True:
        print("\n=== FIN SOLVER (MOCK 7) ===")
        print("1: Payoff Fwd (Commodites)")
        print("2: Prix Livraison Forward")
        print("3: Duration (ZC ou Coupon)")
        print("4: Payoff Fwd (Actions)")
        print("5: Delta P / P0 (bps)")
        print("0: Quitter")

        choix = input("Q# (0-5) : ")
        if choix == "1":
            q1()
        elif choix == "2":
            q2()
        elif choix == "3":
            q3()
        elif choix == "4":
            q4()
        elif choix == "5":
            q5()
        elif choix == "0":
            break


main()