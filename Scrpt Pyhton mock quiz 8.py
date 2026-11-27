# Fin Markets Fast Solver (Tout en decimal) - Mock 8


def q1():
    print("\n--- Q1 : Fwd Oblig (Apres Coupon) ---")
    s0 = float(input("Prix S0 (€) : "))
    n = float(input("Nominal N (€) : "))
    c_rate = float(input("Taux coupon (ex: 0.059) : "))
    r = float(input("Taux r (ex: 0.059) : "))
    t_fwd = float(input("Mat Fwd T (ex: 1) : "))
    t_cpn = float(input("Date cpn t (ex: 1) : "))

    i_t = n * c_rate
    pv_i = i_t / ((1 + r) ** t_cpn)
    f0 = (s0 - pv_i) * ((1 + r) ** t_fwd)

    print("----------------------")
    print("F0 =", round(f0, 2))


def q2():
    print("\n--- Q2 : Fwd Zero-Coupon ---")
    s0 = float(input("Prix S0 (€) : "))
    r = float(input("Taux r (ex: 0.03) : "))
    t = float(input("Mat Fwd T (ans) : "))

    f0 = s0 * ((1 + r) ** t)

    print("----------------------")
    print("F0 =", round(f0, 2))


def q3():
    print("\n--- Q3 : Fwd Oblig (Avant Coupon) ---")
    n = float(input("Nominal N (€) : "))
    c_rate = float(input("Taux coupon (ex: 0.06) : "))
    r = float(input("Taux plat r (ex: 0.06) : "))
    t_bond = int(input("Mat Oblig (ans, ex: 14) : "))
    mois = float(input("Mat Fwd (mois, ex: 6) : "))

    if c_rate == r:
        s0 = n
    else:
        c = n * c_rate
        s0 = (c / r) * (1 - (1 / ((1 + r) ** t_bond))) + (
            n / ((1 + r) ** t_bond)
        )

    t_fwd = mois / 12.0
    f0 = s0 * ((1 + r) ** t_fwd)

    print("----------------------")
    print("S0 =", round(s0, 2))
    print("F0 =", round(f0, 2))


def q4():
    print("\n--- Q4 : Taux Spot Implicite r_T ---")
    s0 = float(input("Prix S0 (€) : "))
    f0 = float(input("Prix Fwd F0 (€) : "))
    t = float(input("Mat Fwd T (ex: 2) : "))

    r_t = (f0 / s0) ** (1 / t) - 1

    print("----------------------")
    print("r_" + str(int(t)) + " =", round(r_t, 4))


def q5():
    print("\n--- Q5 : Fwd Or + Stockage ---")
    s0 = float(input("Spot S0 (ex: 3124) : "))
    cout_an = float(input("Cout/an (ex: 4) : "))
    nb_ans = float(input("Nb ans payes (ex: 2) : "))
    t_pay = float(input("Date paiement t (ex: 1) : "))
    r_pay = float(input("Taux r_t (ex: 0.0378) : "))
    t_fwd = float(input("Mat Fwd T (ex: 2) : "))
    r_fwd = float(input("Taux r_T (ex: 0.0416) : "))

    u_t = cout_an * nb_ans
    pv_u = u_t / ((1 + r_pay) ** t_pay)
    f0 = (s0 + pv_u) * ((1 + r_fwd) ** t_fwd)

    print("----------------------")
    print("F0 =", round(f0, 2))


def main():
    while True:
        print("\n=== FIN SOLVER (MOCK 8) ===")
        print("1: Fwd Oblig (Apres Cpn)")
        print("2: Fwd Zero-Coupon")
        print("3: Fwd Oblig (Sans Cpn)")
        print("4: Taux Spot via Fwd")
        print("5: Fwd Or + Stockage")
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