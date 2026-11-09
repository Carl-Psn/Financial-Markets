### Formula Header (Aide-mémoire)

\\\\\\\[P\_0 \= \\\\frac{C}{1+y} \+ \\\\frac{C}{(1+y)^2} \+ \\\\dots \+ \\\\frac{C+N}{(1+y)^T} \= \\\\frac{C}{y}\\\\left(1 \- \\\\frac{1}{(1+y)^T}\\\\right) \+ \\\\frac{N}{(1+y)^T}, \\\\quad \\\\text{where } y \= \\\\text{yield-to-maturity}\\\\\\\]  
\\\\\\\[P\_0 \= \\\\frac{C}{1+r\_1} \+ \\\\frac{C}{(1+r\_2)^2} \+ \\\\dots \+ \\\\frac{C+N}{(1+r\_T)^T}, \\\\quad \\\\text{where } r\_t \= t\\\\text{-year interest rate}\\\\\\\]  
\\\\\\\[(1+r\_T)^T \= (1+r\_t)^t \\\\times (1+f\\\_{t \\\\to T})^{(T-t)} \\\\quad \\\\text{where } T \\\> t, \\\\text{ and } f\\\_{t \\\\to T} \= \\\\text{forward rate from year } t \\\\text{ to year } T\\\\\\\]

### Question 1

**Verbatim Question:**  
*"A government zero-coupon bond Z has a par (face) value of N \= 1000 euros and it is exactly 24-years away from maturity. What is the yield-to-maturity (y) of this zero-coupon bond if its market price today (at t=0) is equal to Z0 \= 832 euros ? If your answer is, for ex., 0.0500, then enter your answer with four-digits after the decimal point as 0.0500 (but do not enter 5.00%, or 5% or 5,00% or 0,0500, or "five percent", etc.)"*

#### 1\. Required Formula:

For a zero-coupon bond (\\\\(C \= 0\\\\)), the pricing formula simplifies to discounting the face value \\\\(N\\\\) over \\\\(T\\\\) years: \\\\\\\[Z\_0 \= \\\\frac{N}{(1+y)^T}\\\\\\\]  
Solving for the yield-to-maturity \\\\(y\\\\): \\\\\\\[(1+y)^T \= \\\\frac{N}{Z\_0} \\\\implies \\\\mathbf{y \= \\\\left(\\\\frac{N}{Z\_0}\\\\right)^{1/T} \- 1}\\\\\\\]

#### 2\. Numerical Application:

* **Given data:** \\\\(N \= 1000\\\\text{ €}\\\\), \\\\(T \= 24\\\\text{ years}\\\\), \\\\(Z\_0 \= 832\\\\text{ €}\\\\)

\\\\\\\[y \= \\\\left(\\\\frac{1000}{832}\\\\right)^{1/24} \- 1\\\\\\\]  
\\\\\\\[y \= (1.2019230769)^{0.0416666667} \- 1\\\\\\\]  
\\\\\\\[y \= 1.0076930059 \- 1 \= \\\\mathbf{0.0076930059}\\\\\\\]

#### Final Answer:

**0.0077**

### Question 2

**Verbatim Question:**  
*"Find the price at t=0 of a government coupon-paying bond that matures in exactly 18-years from today (t=0), with a coupon rate of 6 percent per year, annual coupon payments, and a yield-to-maturity of 9 percent per year. Par (face) value is 1000 euros. If your answer is 1234.56789, enter it as 1234.57 with two digits after the decimal point."*

#### 1\. Required Formula:

Using the annuity formula for a coupon-paying bond: \\\\\\\[\\\\mathbf{P\_0 \= \\\\frac{C}{y}\\\\left(1 \- \\\\frac{1}{(1+y)^T}\\\\right) \+ \\\\frac{N}{(1+y)^T}}\\\\\\\]

#### 2\. Numerical Application:

* **Given data:** \\\\(N \= 1000\\\\text{ €}\\\\), \\\\(T \= 18\\\\text{ years}\\\\), \\\\(\\\\text{Coupon rate } c \= 6% \\\\implies C \= 0.06 \\\\times 1000 \= \\\\mathbf{60\\\\text{ €}}\\\\), \\\\(y \= 9% \= \\\\mathbf{0.09}\\\\)  
1. **Present Value of Coupons:** \\\\\\\[\\\\text{PV}(\\\\text{Coupons}) \= \\\\frac{60}{0.09}\\\\left(1 \- \\\\frac{1}{(1.09)^{18}}\\\\right) \= 666.666667 \\\\times (1 \- 0.2119937) \= \\\\mathbf{525.337546\\\\text{ €}}\\\\\\\]  
2. **Present Value of Principal:** \\\\\\\[\\\\text{PV}(\\\\text{Face Value}) \= \\\\frac{1000}{(1.09)^{18}} \= \\\\frac{1000}{4.7171204} \= \\\\mathbf{211.993701\\\\text{ €}}\\\\\\\]  
3. **Total Bond Price:** \\\\\\\[P\_0 \= 525.337546 \+ 211.993701 \= \\\\mathbf{737.331247\\\\text{ €}}\\\\\\\]

#### Final Answer:

**737.33**

### Question 3

**Verbatim Question:**  
*"Consider a government coupon-paying bond with a maturity of exactly T=3 years from now, annual coupon payments of 60 euros once a year, a par (face) value of 1000 euros. The relevant term-structure of interest rates is such that r1 \=1 percent (per annum) for year 1, r2=5 percent (per annum) for year 2, and r3=8 percent (per annum) for year 3\. The bond has face value N \= 1000 euros. Determine the price of this bond today (i.e., at date t=0). If your answer is 1234.56789, enter it as 1234.57 with two digits after the decimal point."*

#### 1\. Required Formula:

Discounting each annual cash flow using its corresponding spot rate \\\\(r\_t\\\\) from the term structure: \\\\\\\[\\\\mathbf{P\_0 \= \\\\frac{C}{1+r\_1} \+ \\\\frac{C}{(1+r\_2)^2} \+ \\\\frac{C+N}{(1+r\_3)^3}}\\\\\\\]

#### 2\. Numerical Application:

* **Given data:** \\\\(C \= 60\\\\text{ €}\\\\), \\\\(N \= 1000\\\\text{ €}\\\\), \\\\(r\_1 \= 1% \= \\\\mathbf{0.01}\\\\), \\\\(r\_2 \= 5% \= \\\\mathbf{0.05}\\\\), \\\\(r\_3 \= 8% \= \\\\mathbf{0.08}\\\\)  
1. **Year 1 Cash Flow (\\\\(t=1\\\\)):** \\\\\\\[\\\\text{PV}\\\_1 \= \\\\frac{60}{1 \+ 0.01} \= \\\\frac{60}{1.01} \= \\\\mathbf{59.405941\\\\text{ €}}\\\\\\\]  
2. **Year 2 Cash Flow (\\\\(t=2\\\\)):** \\\\\\\[\\\\text{PV}\\\_2 \= \\\\frac{60}{(1 \+ 0.05)^2} \= \\\\frac{60}{1.1025} \= \\\\mathbf{54.421769\\\\text{ €}}\\\\\\\]  
3. **Year 3 Cash Flow (\\\\(t=3\\\\)):** \\\\\\\[\\\\text{PV}\\\_3 \= \\\\frac{60 \+ 1000}{(1 \+ 0.08)^3} \= \\\\frac{1060}{1.259712} \= \\\\mathbf{841.462176\\\\text{ €}}\\\\\\\]  
4. **Total Bond Price:** \\\\\\\[P\_0 \= 59.405941 \+ 54.421769 \+ 841.462176 \= \\\\mathbf{955.289885\\\\text{ €}}\\\\\\\]

#### Final Answer:

**955.29**

### Question 4

**Verbatim Question:**  
*"Today (at t=0) the 5-year spot rate is 5 percent (per annum), while the 7-year spot rate is 9 percent (per annum). What is, as of date t=0, on a per-annum basis, the forward interest rate f that is expected to prevail between dates 5 and 7 ? If your answer is 12.34 percent, enter it as 0.1234 using four digits after the decimal point."*

#### 1\. Required Formula:

Relating spot rates to forward rates over multi-year horizons: \\\\\\\[(1+r\_T)^T \= (1+r\_t)^t \\\\times (1+f\\\_{t \\\\to T})^{(T-t)}\\\\\\\]  
For \\\\(t \= 5\\\\) and \\\\(T \= 7\\\\) (\\\\(T \- t \= 2\\\\text{ years}\\\\)): \\\\\\\[(1+r\_7)^7 \= (1+r\_5)^5 \\\\times (1+f\\\_{5 \\\\to 7})^2 \\\\implies \\\\mathbf{f\\\_{5 \\\\to 7} \= \\\\sqrt{\\\\frac{(1+r\_7)^7}{(1+r\_5)^5}} \- 1}\\\\\\\]

#### 2\. Numerical Application:

* **Given data:** \\\\(r\_5 \= 5% \= \\\\mathbf{0.05}\\\\), \\\\(r\_7 \= 9% \= \\\\mathbf{0.09}\\\\)  
1. **Calculate compound factors:** \\\\\\\[(1+r\_7)^7 \= (1.09)^7 \= \\\\mathbf{1.828039121}\\\\\\\] \\\\\\\[(1+r\_5)^5 \= (1.05)^5 \= \\\\mathbf{1.276281563}\\\\\\\]  
2. **Calculate 2-year forward compounding factor:** \\\\\\\[(1+f\\\_{5 \\\\to 7})^2 \= \\\\frac{1.828039121}{1.276281563} \= \\\\mathbf{1.432316499}\\\\\\\]  
3. **Extract annual forward rate:** \\\\\\\[1+f\\\_{5 \\\\to 7} \= \\\\sqrt{1.432316499} \= \\\\mathbf{1.196794259}\\\\\\\] \\\\\\\[f\\\_{5 \\\\to 7} \= 1.196794259 \- 1 \= \\\\mathbf{0.196794259}\\\\\\\]

#### Final Answer:

**0.1968**

### Question 5

**Verbatim Question:**  
*"The yield curve based on government zero-coupon bonds is completely flat. The price of a government coupon-paying bond B with a face (par) value of 1000 euros, coupon-payment frequency of one per year, and with exactly 50 years until maturity, is equal to 1000 euros today. If this bond B has an annual coupon with a rate of 14 percent per annum, what must be the 39-year government zero-coupon bond rate on a per annum basis? If your answer is 1 percent per year, enter your answer as 0.0100 with four digits after the decimal point."*

#### 1\. Required Formula:

When the yield curve is completely flat, all spot rates across all maturities are identical (\\\\(r\_1 \= r\_2 \= \\\\dots \= r\_T \= r\\\\)). Under a flat yield curve, a bond's price formula is: \\\\\\\[P\_0 \= \\\\frac{C}{r}\\\\left(1 \- \\\\frac{1}{(1+r)^T}\\\\right) \+ \\\\frac{N}{(1+r)^T}\\\\\\\]  
Key financial property: **When a bond trades at par (\\\\(P\_0 \= N\\\\)), its coupon rate \\\\(c\\\\) equals its yield-to-maturity \\\\(y\\\\) (\\\\(c \= y\\\\))**. Since the yield curve is flat, **\\\\(\\\\mathbf{r\_t \= r \= y \= c}\\\\) for any maturity \\\\(t\\\\)**.

#### 2\. Numerical Application:

* **Given data:** \\\\(N \= 1000\\\\text{ €}\\\\), \\\\(P\_0 \= 1000\\\\text{ €}\\\\) (bond trades at par), \\\\(T \= 50\\\\text{ years}\\\\), \\\\(\\\\text{Coupon rate } c \= 14% \= \\\\mathbf{0.1400}\\\\)  
1. **Par bond condition:** \\\\\\\[P\_0 \= N \\\\implies y \= c \= 14% \= \\\\mathbf{0.1400}\\\\\\\]  
2. **Flat yield curve property:** Since the yield curve is completely flat, the zero-coupon spot rate for **any** maturity \\\\(t\\\\) (including \\\\(t \= 39\\\\text{ years}\\\\)) equals the flat rate: \\\\\\\[r\\\_{39} \= r\\\_{50} \= y \= \\\\mathbf{0.1400}\\\\\\\]

#### Final Answer:

**0.1400**  
