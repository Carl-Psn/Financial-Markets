# Mock Quiz 7 — Concise Solution Manual

##### **Formula Header (Reference Formulas)**

$$P_0 = \frac{C}{(1+y)} + \frac{C}{(1+y)^2} + \dots + \frac{C+N}{(1+y)^T} = \frac{C}{y}\left(1 - \frac{1}{(1+y)^T}\right) + \frac{N}{(1+y)^T} \quad \text{, where } y = \text{yield-to-maturity}$$

$$P_0 = \frac{C}{(1+r_1)} + \frac{C}{(1+r_2)^2} + \dots + \frac{C+N}{(1+r_T)^T} \quad \text{, where } r_t = t\text{-year interest rate}$$

$$\frac{\Delta P_0}{P_0} = -D \times \frac{\Delta y}{1+y}$$

$$D = w_1 \times 1 + w_2 \times 2 + \dots + w_T \times T \quad \text{where for } w_t = \frac{C/(1+r)^t}{P_0} \text{ for } t < T\text{, and } w_T = \frac{(C+N)/(1+r)^T}{P_0} \text{ for } t = T$$

---

##### **Question 1**

**Énoncé :**
You just entered into 91 short positions for a forward contract with the following features:
* **Underlying asset:** gold
* **Size per contract:** 127 grams
* **Maturity:** 21 months
* **Forward price:** $F_{0, 21\text{ months}} = 56\text{ euros/gram}$
* **Settlement type:** cash
If after 21 months the price of gold is $S_{21\text{ months}} = 46\text{ €/gram}$ in the spot market, what is your payoff?

###### **1. Formula:**
$$\text{Payoff}_{\text{short}} = \text{Number of contracts} \times \text{Size per contract} \times (F_{0,T} - S_T)$$

###### **2. Step-by-Step Resolution:**
* **Given data:** $\text{Contracts} = 91$, $\text{Size} = 127\text{ g}$, $F_0 = 56\text{ €/g}$, $S_T = 46\text{ €/g}$.
1. **Total quantity:** $91 \times 127 = 11,557\text{ grams}$
2. **Gain per gram:** $F_0 - S_T = 56 - 46 = 10\text{ €/gram}$
3. **Total payoff:** $11,557 \times 10 = +115,570\text{ €}$

###### **Final Answer:**
**115570** *(enter full integer without commas, symbols, or decimals)*

---

##### **Question 2**

**Énoncé :**
Company A will pay no dividends for the next 10 years. One common share of company A currently trades for $S_0 = 36.5\text{ euros}$ per share. A 2.1-year maturity government zero-coupon bond with face value 100 currently trades for $B_0 = 87.1\text{ euros}$ per bond. What is the no-arbitrage delivery price of a 2.1-year forward for 100 shares of company A?

###### **1. Formula:**
For an asset paying no dividends over maturity $T$:
$$F_{0,T} = \frac{S_0}{d_T} = \frac{S_0}{B_0 / N}$$
$$\text{Total Forward Delivery Price} = \text{Number of shares} \times F_{0,T}$$

###### **2. Step-by-Step Resolution:**
* **Given data:** $S_0 = 36.5\text{ €}$, $B_0 = 87.1\text{ €}$, $N = 100\text{ €}$, $\text{Shares} = 100$.
1. **Discount factor:** $d_{2.1} = \frac{B_0}{N} = \frac{87.1}{100} = 0.871$
2. **Forward price per share:** $F_{0, 2.1} = \frac{36.5}{0.871} \approx 41.905855\text{ €}$
3. **Total delivery price for 100 shares:** $100 \times 41.905855 = 4,190.5855\text{ €}$

###### **Final Answer:**
**4190.59** *(rounded to 2 decimal places)*

---

##### **Question 3**

**Énoncé :**
Calculate the duration of a government zero-coupon bond with a maturity of 9 years, a face value (par value) of 1000 euros. The relevant government yield curve is flat for all maturities at 7 percent per year.

###### **1. Formula:**
For any zero-coupon bond ($C = 0$), cash flow occurs only at maturity $T$:
$$w_T = \frac{N / (1+r)^T}{P_0} = 1 \implies D = T$$

###### **2. Step-by-Step Resolution:**
* **Given data:** $T = 9\text{ years}$, $N = 1000\text{ €}$, $r = 7\%$.
1. Since all cash flow weight is concentrated entirely at maturity $T = 9$:
   $$D = 1.0 \times 9 = 9\text{ years}$$

###### **Final Answer:**
**9**

---

##### **Question 4**

**Énoncé :**
One week ago, you sold 97 forward contracts (i.e., you entered 97 short positions) with the following characteristics:
* Underlying asset is Apple Inc. shares;
* Each forward contract is on 100 shares;
* Contract maturity is 28/11/2025;
* One week ago, the price of the forward was $F_{28/11/25} = 270\text{ USD/share}$.
What is your payoff on 28/11/2025 if, at that date, the spot price of one Apple Inc. share is 282 USD?

###### **1. Formula:**
$$\text{Payoff}_{\text{short}} = \text{Number of contracts} \times \text{Multiplier} \times (F_0 - S_T)$$

###### **2. Step-by-Step Resolution:**
* **Given data:** $\text{Contracts} = 97$, $\text{Multiplier} = 100\text{ shares/contract}$, $F_0 = 270\text{ USD}$, $S_T = 282\text{ USD}$.
1. **Total shares:** $97 \times 100 = 9,700\text{ shares}$
2. **Payoff per share:** $270 - 282 = -12\text{ USD}$
3. **Total payoff:** $9,700 \times (-12) = -116,400\text{ USD}$

###### **Final Answer:**
**-116400** *(enter minus sign without commas or currency symbols)*

---

##### **Question 5**

**Énoncé :**
As of today, the government zero-coupon bond-based yield curve is flat at 2 percent per year for all maturities. Using the duration formula, what is the percentage change in the price of a zero-coupon bond of exactly 20-years of maturity, if the entire yield curve moves up by 32 basis points? Recall that 1 basis point = 0.01 percent. If your answer is -3 percent (that is a three percent decrease in bond's price), enter -0.0300.

###### **1. Formula:**
$$\frac{\Delta P_0}{P_0} = -D \times \frac{\Delta y}{1+y}$$

###### **2. Step-by-Step Resolution:**
* **Given data:** $T = 20\text{ years} \implies D = 20\text{ years}$, $y = 2\% = 0.02$, $\Delta y = +32\text{ bps} = +0.0032$.
1. **Apply modified duration formula:**
   $$\frac{\Delta P_0}{P_0} = -20 \times \frac{0.0032}{1 + 0.02} = -20 \times \frac{0.0032}{1.02} = -\frac{0.064}{1.02} \approx -0.0627451$$
2. **Format to 4 decimal places:** $-0.0627$

###### **Final Answer:**
**-0.0627**
