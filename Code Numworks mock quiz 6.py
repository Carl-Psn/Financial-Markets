# Fin Markets Fast Solver (Tout en decimal) - Mock 6


def q1():
    print("\n--- Q1 : Prix Annuite (Meme Rating) ---")
    c_ann = float(input("Coupon Annuite C (€) : "))
    n_b = float(input("Nominal Oblig/ZC (€) : "))
    c_rate = float(input("Taux coupon Oblig (ex: 0.05) : "))
    p_bond = float(input("Prix Oblig coupon (€) : "))
    p_zc = float(input("Prix ZC (0% coupon) (€) : "))

    # Annuite sur T=2 ans = (C_ann / C_bond) * (P_bond - P_zc)
    c_bond = n_b * c_rate
    ratio = c_ann / c_bond
    p_ann = ratio * (p_bond - p_zc)

    print("----------------------")
    print("Prix Annuite =", round(p_ann, 2), "€")


def q2():
    print("\n--- Q2 : Prix ZC (Mois) ---")
    n = float(input("N (€) : "))
    y = float(input("y (ex: 0.11) : "))
    mois = float(input("Maturite (mois) : "))

    t = mois / 12.0
    p0 = n / ((1 + y) ** t)

    print("----------------------")
    print("T =", round(t, 4), "ans")
    print("P0 =", round(p0, 2))


def q3():
    print("\n--- Q3 : Prix Oblig Coupon ---")
    n = float(input("N (€) : "))
    c_rate = float(input("Taux coupon (ex: 0.05) : "))
    y = float(input("YTM y (ex: 0.15) : "))
    t = float(input("T (annees) : "))

    c = n * c_rate
    pv_c = (c / y) * (1 - (1 / ((1 + y) ** t)))
    pv_n = n / ((1 + y) ** t)
    p0 = pv_c + pv_n

    print("----------------------")
    print("P0 =", round(p0, 2))


def q4():
    print("\n--- Q4 : Sensibilite (Duration) ---")
    n = float(input("N (€) : "))
    c_rate = float(input("Taux coupon (ex: 0.13) : "))
    y = float(input("YTM y (ex: 0.10) : "))
    ta = int(input("T Oblig A (ex: 2) : "))
    tb = int(input("T Oblig B (ex: 16) : "))

    def mod_dur(t_mat):
        c = n * c_rate
        pvs = [
            (c + n if i == t_mat else c) / ((1 + y) ** i)
            for i in range(1, t_mat + 1)
        ]
        p = sum(pvs)
        mac = sum([i * pv for i, pv in enumerate(pvs, 1)]) / p
        return mac / (1 + y)

    da = mod_dur(ta)
    db = mod_dur(tb)

    print("----------------------")
    print("D_Mod A =", round(da, 2), "| B =", round(db, 2))
    if db > da:
        print("Plus sensible : B (T =", tb, ")")
    else:
        print("Plus sensible : A (T =", ta, ")")


def q5():
    print("\n--- Q5 : Payoff Forward ---")
    sens = input("Position (L=Long / S=Short) : ").upper()
    nb = float(input("Nb contrats (ex: 88) : "))
    m = float(input("Taille contrat (ex: 100) : "))
    f0 = float(input("Prix Fwd F0 (ex: 151) : "))
    st = float(input("Prix Spot ST (ex: 139) : "))

    if sens == "L":
        payoff = nb * m * (st - f0)
    else:
        payoff = nb * m * (f0 - st)

    print("----------------------")
    print("Payoff =", int(round(payoff, 0)))


def main():
    while True:
        print("\n=== FIN SOLVER (MOCK 6) ===")
        print("1: Prix Annuite (No-Arb)")
        print("2: Prix ZC (en mois)")
        print("3: Prix Oblig Coupon")
        print("4: Sensibilite / Duration")
        print("5: Payoff Forward")
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