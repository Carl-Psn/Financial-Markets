### Mock Quiz 8 — Concise Solution Manual

###### **Formula Header (Reference Formulas)**
$${F}_{0,T} = \left({S}_{0} - rac{{I}_{t}}{(1+{r}_{t})^{t}}ight) 	imes (1+{r}_{T})^{T} \quad 	ext{where } I_t = 	ext{interim cash flow at date } t < T$$
$$	ext{For a zero-coupon bond/asset with no interim cash flows } (I_t = 0): \quad F_{0,T} = S_0 	imes (1 + r_T)^T$$
$$	ext{For commodities with storage cost } U_t 	ext{ paid at } t: \quad F_{0,T} = \left(S_0 + rac{U_t}{(1+r_t)^t}ight) 	imes (1+r_T)^T$$

--------------------------------------------------------------------------------

###### **Question 1**
**Énoncé:** A coupon-paying government bond B with a face (par) value of 855 euros makes annual coupon payments at the end of each year and has a coupon rate of 5.9 percent per year. The price today of this bond is 855 euros. The risk-free yield curve is flat. The first coupon of this bond will be paid in exactly 1 year from now and in the morning. You consider a forward contract that delivers one bond B in exactly 1 year from now in the afternoon, i.e. right after the first coupon has been paid out to bondholders. **What must be the no-arbitrage delivery (forward) price in this forward contract initiated today?**

###### **1. Formula:**
$$F_{0,T} = \left(S_0 - rac{I_t}{(1+r_t)^t}ight) 	imes (1+r_T)^T$$

###### **2. Step-by-Step Resolution:**
* **Given data:** $S_0 = 855	ext{ €}$, Face Value $N = 855	ext{ €}$, Coupon Rate $= 5.9\%$, Maturity $T = 1	ext{ year}$, Coupon Payment Date $t = 1	ext{ year}$ (morning).
1. **Bond Yield & Spot Rate:** Since the bond sells at par ($S_0 = N = 855	ext{ €}$), its yield-to-maturity equals its coupon rate ($y = 5.9\%$). The flat yield curve implies $r_1 = 5.9\% = 0.059$.
2. **Interim Coupon Payment:** Paid at $t = 1$ year in the morning: $I_1 = 5.9\% 	imes 855 = 50.445	ext{ €}$.
3. **Forward Price Calculation:**
   $$F_{0,1} = \left(855 - rac{50.445}{1 + 0.059}ight) 	imes (1 + 0.059) = 855 	imes (1.059) - 50.445 = 905.445 - 50.445 = 855	ext{ €}$$

###### **Final Answer:**
**855** *(or **855.00**)*

--------------------------------------------------------------------------------

###### **Question 2**
**Énoncé:** Consider a corporate zero-coupon bond ZC with a price of 160 euros today (at t=0) and a maturity of 17 years. If the yield-curve for government bonds is flat for all maturities at 3 percent per year, **what is the no-arbitrage delivery (forward) price in a forward contract initiated today (t=0) that delivers one corporate zero-coupon bond ZC in 3-years from now?**

###### **1. Formula:**
For a zero-coupon bond, no interim cash flows occur prior to forward maturity ($I_t = 0$):
$$F_{0,T} = S_0 	imes (1+r_T)^T$$

###### **2. Step-by-Step Resolution:**
* **Given data:** $S_0 = 160	ext{ €}$, Forward Maturity $T = 3	ext{ years}$, Risk-Free Rate $r_3 = 3\% = 0.03$.
1. **Apply Spot-Forward Parity:**
   $$F_{0,3} = 160 	imes (1 + 0.03)^3 = 160 	imes (1.03)^3 = 160 	imes 1.092727 = 174.83632	ext{ €}$$
2. **Format to 2 decimal places:** $174.84	ext{ €}$

###### **Final Answer:**
**174.84**

--------------------------------------------------------------------------------

###### **Question 3**
**Énoncé:** Consider a government-issued default-risk-free coupon bond B with a face (par) value of 1000 euros, a coupon rate of 6 percent per year, exactly 14-years until maturity, and a frequency of coupon payment of one per year. The associated yield curve is flat at 6 percent per year. **What is the no-arbitrage delivery (forward) price in a forward contract on B initiated today (at t=0) and that will mature in exactly 6-months from now?**

###### **1. Formula:**
Since coupons are paid annually, no coupon is paid during the 6-month forward contract horizon ($I_t = 0$):
$$F_{0,T} = S_0 	imes (1+r_T)^T$$

###### **2. Step-by-Step Resolution:**
* **Given data:** $N = 1000	ext{ €}$, Coupon Rate $= 6\%$, Flat Yield Curve $r = 6\% = 0.06$, Forward Maturity $T = 6	ext{ months} = 0.5	ext{ years}$.
1. **Bond Spot Price ($S_0$):** Because coupon rate equals the YTM ($c = y = 6\%$), the bond sells at par: $S_0 = 1000	ext{ €}$.
2. **Apply Forward Formula ($T = 0.5$):**
   $$F_{0, 0.5} = 1000 	imes (1 + 0.06)^{0.5} = 1000 	imes \sqrt{1.06} pprox 1000 	imes 1.029563 = 1029.5630	ext{ €}$$
3. **Format to 2 decimal places:** $1029.56	ext{ €}$

###### **Final Answer:**
**1029.56**

--------------------------------------------------------------------------------

###### **Question 4**
**Énoncé:** Stock A will pay its next dividend in exactly 3 years from now. The stock's current price (at t=0) is 100 euros/share. Today's no-arbitrage forward price for delivery of one share of stock A in 2 years is 113 euros/share. **What is the 2-year interest rate r2?**

###### **1. Formula:**
Since the next dividend occurs at $t = 3$ years (after forward maturity $T = 2$ years), there is no interim dividend ($I_t = 0$):
$$F_{0,T} = S_0 	imes (1+r_2)^2 \implies (1+r_2)^2 = rac{F_{0,2}}{S_0}$$

###### **2. Step-by-Step Resolution:**
* **Given data:** $S_0 = 100	ext{ €}$, $F_{0,2} = 113	ext{ €}$, Maturity $T = 2	ext{ years}$.
1. **Solve for Compounding Factor:**
   $$(1+r_2)^2 = rac{113}{100} = 1.13$$
2. **Extract Annual Spot Rate $r_2$:**
   $$1+r_2 = \sqrt{1.13} pprox 1.06301458 \implies r_2 = 0.06301458 	ext{ (or } 6.3015\%)$$
3. **Format as Decimal (4 decimal places):** $0.0630$

###### **Final Answer:**
**0.0630**

--------------------------------------------------------------------------------

###### **Question 5**
**Énoncé:** Today's (t=0) spot price of gold is 3,124 GBP per troy ounce. To store 1 troy ounce you must pay 4 GBP per troy ounce per year. Suppose you pay the whole storage cost at t=1 for 2 years of storage (so from time 0 to time 2). The yield curve is the following: r1=3.78% and r2=4.16%. **What is the forward price for delivery at t=2 of 1 troy ounce of gold?**

###### **1. Formula:**
Storage cost is a cost of carry that increases the synthetic forward price. Discounting the storage cost $U_1$ paid at $t=1$:
$$F_{0,2} = \left(S_0 + rac{U_1}{1+r_1}ight) 	imes (1+r_2)^2$$

###### **2. Step-by-Step Resolution:**
* **Given data:** $S_0 = 3124	ext{ GBP}$, Storage Cost $= 4	ext{ GBP/year}$, paid at $t=1$ for 2 years ($U_1 = 2 	imes 4 = 8	ext{ GBP}$), $r_1 = 3.78\% = 0.0378$, $r_2 = 4.16\% = 0.0416$.
1. **Present Value of Storage Cost:**
   $$	ext{PV}(	ext{Storage}) = rac{8}{1 + 0.0378} = rac{8}{1.0378} pprox 7.708614	ext{ GBP}$$
2. **Adjusted Spot Price:**
   $$S_0 + 	ext{PV}(	ext{Storage}) = 3124 + 7.708614 = 3131.708614	ext{ GBP}$$
3. **Calculate 2-Year Forward Price:**
   $$F_{0,2} = 3131.708614 	imes (1 + 0.0416)^2 = 3131.708614 	imes 1.08493056 pprox 3397.6864	ext{ GBP}$$
4. **Format to 2 decimal places:** $3397.69	ext{ GBP}$

###### **Final Answer:**
**3397.69**
