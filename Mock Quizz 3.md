### Formula Header (Aide-mémoire from Note)

\\\\\\\[P\_0 \= \\\\frac{C}{1+y} \+ \\\\frac{C}{(1+y)^2} \+ \\\\dots \+ \\\\frac{C+N}{(1+y)^T} \= \\\\frac{C}{y}\\\\left(1 \- \\\\frac{1}{(1+y)^T}\\\\right) \+ \\\\frac{N}{(1+y)^T}, \\\\quad \\\\text{where } y \= \\\\text{yield-to-maturity}\\\\\\\]  
\\\\\\\[P\_0 \= \\\\frac{C}{1+r\_1} \+ \\\\frac{C}{(1+r\_2)^2} \+ \\\\dots \+ \\\\frac{C+N}{(1+r\_T)^T}, \\\\quad \\\\text{where } r\_t \= \\\\text{t-year interest rate}\\\\\\\]

### Question 1

**Verbatim Question:**  
*"The government-issued zero-coupon bond Z has a par (face) value of 1000 € and a time-until maturity of exactly 23 years from today (t=0). If the yield-to-maturity on bond Z is equal to 7% per year, what must be the price of bond Z today?"*  
**Required Formula:** For a zero-coupon bond, there are no intermediate coupon payments (\\\\(C \= 0\\\\)). The price formula simplifies to discounting the face value \\\\(N\\\\) over \\\\(T\\\\) years at rate \\\\(y\\\\): \\\\\\\[P\_0 \= \\\\frac{N}{(1+y)^T}\\\\\\\]  
**Numerical Application:**

* Given: \\\\(N \= 1000\\\\ €\\\\), \\\\(T \= 23\\\\text{ years}\\\\), \\\\(y \= 7% \= 0.07\\\\)

\\\\\\\[P\_0 \= \\\\frac{1000}{(1 \+ 0.07)^{23}} \= \\\\frac{1000}{1.07^{23}} \= \\\\frac{1000}{4.74053} \\\\approx 210.9469\\\\ €\\\\\\\]  
**Final Answer:** **\\\\(P\_0 \= 210.95\\\\ €\\\\)**

### Question 2

**Verbatim Question:**  
*"As of today, the 1-year risk-free interest rate is r1 \= 2% and the two year risk-free interest rate is r2 \= 7%, respectively. What is the price of a default-risk-free bond B with a maturity of T \= 2-years, a face value of N \= 100 € and an annual coupon rate of 12% with one coupon payment per year? Please enter your answer with 2-digits after the decimal point: for ex., if your answer is 12345.6789 €, enter 12345.68"*  
**Required Formula:** Discount each cash flow using the spot interest rate \\\\(r\_t\\\\) corresponding to its payment date \\\\(t\\\\): \\\\\\\[P\_0 \= \\\\frac{C}{1+r\_1} \+ \\\\frac{C+N}{(1+r\_2)^2}\\\\\\\]  
**Numerical Application:**

* Given: \\\\(r\_1 \= 2% \= 0.02\\\\), \\\\(r\_2 \= 7% \= 0.07\\\\), \\\\(N \= 100\\\\ €\\\\), \\\\(\\\\text{Coupon rate} \= 12%\\\\)  
* Coupon amount \\\\(C \= 12% \\\\times 100\\\\ € \= 12\\\\ €\\\\)  
* Cash flow at \\\\(t=1\\\\): \\\\(C \= 12\\\\ €\\\\)  
* Cash flow at \\\\(t=2\\\\): \\\\(C \+ N \= 12 \+ 100 \= 112\\\\ €\\\\)

\\\\\\\[P\_0 \= \\\\frac{12}{1 \+ 0.02} \+ \\\\frac{112}{(1 \+ 0.07)^2} \= \\\\frac{12}{1.02} \+ \\\\frac{112}{1.07^2}\\\\\\\] \\\\\\\[P\_0 \= 11.764706 \+ \\\\frac{112}{1.1449} \= 11.764706 \+ 97.825138 \= 109.589844\\\\ €\\\\\\\]  
**Final Answer:** **\\\\(P\_0 \= 109.59\\\\ €\\\\)**

### Question 3

**Verbatim Question:**  
*"Consider the following bonds:* *Bond A: maturity one-year exactly, coupon rate 0%, face (par) value 100 €, current price 96 €* *Bond B: maturity two-years, coupon rate 0%, face (par) value 100 €, current price 92 €* *Bond C: maturity two years, coupon rate 10% per year, annual coupon payments, face (par) value 1000 €*  
*The no-arbitrage price of Bond C is:"*  
**Required Formula:** By the **Law of One Price**, the price of Bond C equals the cost of a replicating portfolio made of zero-coupon bonds A and B:

* Cash flow of Bond C at \\\\(t=1\\\\): \\\\(C \= 10% \\\\times 1000\\\\ € \= 100\\\\ €\\\\)  
* Cash flow of Bond C at \\\\(t=2\\\\): \\\\(C \+ N \= 100 \+ 1000 \= 1100\\\\ €\\\\)

Replication logic:

* To replicate the \\\\(100\\\\ €\\\\) payment at \\\\(t=1\\\\), buy \\\\(\\\\frac{100}{100} \= 1\\\\) unit of Bond A.  
* To replicate the \\\\(1100\\\\ €\\\\) payment at \\\\(t=2\\\\), buy \\\\(\\\\frac{1100}{100} \= 11\\\\) units of Bond B.

\\\\\\\[P\_C \= (\\\\text{Units of A} \\\\times P\_A) \+ (\\\\text{Units of B} \\\\times P\_B)\\\\\\\]  
*Alternatively using Discount Factors:* \\\\(d\_1 \= \\\\frac{96}{100} \= 0.96\\\\) and \\\\(d\_2 \= \\\\frac{92}{100} \= 0.92\\\\): \\\\\\\[P\_C \= CF\_1 \\\\times d\_1 \+ CF\_2 \\\\times d\_2\\\\\\\]  
**Numerical Application:**

* Given: \\\\(P\_A \= 96\\\\ €\\\\), \\\\(P\_B \= 92\\\\ €\\\\)

\\\\\\\[P\_C \= (1 \\\\times 96\\\\ €) \+ (11 \\\\times 92\\\\ €) \= 96 \+ 1012 \= 1108\\\\ €\\\\\\\]  
**Final Answer:** **\\\\(P\_C \= 1108\\\\ €\\\\)**

### Question 4

**Verbatim Question:**  
*"The government-issued zero-coupon bond with a 9-years of maturity and a face value of 1000 € has a price of 885 € today (at t=0). What is the yield-to-maturity of this bond?*  
*Enter your answer in decimals, for example, if you find 1.23% you should write 0.0123 in the answer box"*  
**Required Formula:** For a zero-coupon bond: \\\\\\\[P\_0 \= \\\\frac{N}{(1+y)^T} \\\\implies (1+y)^T \= \\\\frac{N}{P\_0} \\\\implies y \= \\\\left(\\\\frac{N}{P\_0}\\\\right)^{1/T} \- 1\\\\\\\]  
**Numerical Application:**

* Given: \\\\(N \= 1000\\\\ €\\\\), \\\\(P\_0 \= 885\\\\ €\\\\), \\\\(T \= 9\\\\text{ years}\\\\)

\\\\\\\[y \= \\\\left(\\\\frac{1000}{885}\\\\right)^{1/9} \- 1 \= (1.1299435)^{1/9} \- 1\\\\\\\] \\\\\\\[y \= 1.013667 \- 1 \= 0.013667\\\\\\\]  
**Final Answer:** **\\\\(y \= 0.0137\\\\)** *(or \\\\(1.37%\\\\))*

### Question 5

**Verbatim Question:**  
*"Bond A is a 2-year maturity bond with a face value of 1000 €, with coupon paid once annually. This bond's current price is 1000 € and its yield-to-maturity is 13% per year. What is its coupon payment in € ?"*  
**Required Formula:**

* **Exam Fast-Track Rule:** When a bond sells **at par** (\\\\(P\_0 \= N \= 1000\\\\ €\\\\)), its annual **coupon rate \\\\(c\\\\) equals its yield-to-maturity \\\\(y\\\\)**. \\\\\\\[c \= y \\\\implies C \= y \\\\times N\\\\\\\]  
* **Standard Valuation Proof:** \\\\\\\[P\_0 \= \\\\frac{C}{1+y} \+ \\\\frac{C+N}{(1+y)^2} \\\\implies C \= \\\\frac{P\_0 \- \\\\frac{N}{(1+y)^2}}{\\\\frac{1}{1+y} \+ \\\\frac{1}{(1+y)^2}}\\\\\\\]

**Numerical Application:**

* Given: \\\\(N \= 1000\\\\ €\\\\), \\\\(P\_0 \= 1000\\\\ €\\\\), \\\\(y \= 13% \= 0.13\\\\)

*Method 1 (Par bond property):* Since \\\\(P\_0 \= N\\\\), the bond is trading at par \\\\(\\\\implies \\\\text{Coupon rate } c \= y \= 13%\\\\). \\\\\\\[C \= 13% \\\\times 1000\\\\ € \= 130\\\\ €\\\\\\\]  
*Method 2 (Algebraic verification):* \\\\\\\[1000 \= \\\\frac{C}{1.13} \+ \\\\frac{C \+ 1000}{1.13^2}\\\\\\\] \\\\\\\[1000 \- \\\\frac{1000}{1.2769} \= C \\\\left(\\\\frac{1}{1.13} \+ \\\\frac{1}{1.13^2}\\\\right)\\\\\\\] \\\\\\\[216.85332 \= C \\\\times 1.668103 \\\\implies C \= \\\\frac{216.85332}{1.668103} \= 130\\\\ €\\\\\\\]  
**Final Answer:** **\\\\(C \= 130\\\\ €\\\\)**  
