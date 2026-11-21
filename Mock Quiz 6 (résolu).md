### Question 1

#### Original Question & Cheat Sheet

**Bonds** Consider the following bonds with frequency of coupon payment of 1 year.  
,Rating,Coupon rate,Maturity,Face value,Current price  
Bond 1,AAA,5%,2 years,1000,1080  
Bond 2,AAA,0%,2 years,1000,995  
Bond 3,BB,5%,2 years,1000,"1,019"  
Bond 4,BB,0%,2 years,1000,969  
Annuity A is BB-rated and only pays an annual coupon of \\\\(C \= 50\\\\text{ euros/year}\\\\) at the end of each year (i.e., there is no final par (face) payment but there is only the coupon payment). Annuity A has a maturity of \\\\(T \= 2\\\\text{ years}\\\\). **What is the no-arbitrage price of annuity A?**

#### Required Formula

By the **Law of One Price (No-Arbitrage)**, if a portfolio of existing securities replicates the cash flows of a financial instrument, the price of the instrument must equal the price of the replicating portfolio: \\\\\\\[\\\\text{Price}(\\\\text{Annuity A}) \= \\\\text{Price}(\\\\text{Replicating Portfolio})\\\\\\\]  
Alternatively, using spot discount factors \\\\(d\_t\\\\) for BB-rated risk: \\\\\\\[\\\\text{Price}(\\\\text{Annuity A}) \= C\_1 \\\\cdot d\_1 \+ C\_2 \\\\cdot d\_2\\\\\\\]

#### Numerical Application

* **Identify the cash flows of Annuity A (BB-rated):**  
* Year 1 (\\\\(t=1\\\\)): **50 euros**  
* Year 2 (\\\\(t=2\\\\)): **50 euros**  
* **Identify the cash flows of the relevant BB-rated bonds:**  
* **Bond 3** (BB, 5% coupon, 2-year maturity, Price \= €1,019):  
* Coupon \= \\\\(5% \\\\times 1000 \= 50\\\\text{ euros}\\\\)  
* Year 1 CF \= **50 euros**  
* Year 2 CF \= \\\\(50 \+ 1000 \=\\\\) **1,050 euros**  
* **Bond 4** (BB, 0% coupon, 2-year maturity, Price \= €969):  
* Year 1 CF \= **0 euros**  
* Year 2 CF \= **1,000 euros**  
* **Construct the Replicating Portfolio:**  
* Buy **1 unit of Bond 3** and short **1 unit of Bond 4**:  
* Year 1 Cash Flow: \\\\(50 \- 0 \= \\\\mathbf{50\\\\text{ euros}}\\\\)  
* Year 2 Cash Flow: \\\\(1,050 \- 1,000 \= \\\\mathbf{50\\\\text{ euros}}\\\\)  
* This exact cash flow sequence matches **Annuity A**.  
* **Calculate No-Arbitrage Price:** \\\\\\\[\\\\text{Price}(\\\\text{Annuity A}) \= \\\\text{Price}(\\\\text{Bond 3}) \- \\\\text{Price}(\\\\text{Bond 4})\\\\\\\] \\\\\\\[\\\\text{Price}(\\\\text{Annuity A}) \= 1,019 \- 969 \= \\\\mathbf{50\\\\text{ euros}}\\\\\\\]

### Question 2

#### Original Question & Cheat Sheet

**Bonds** \\\\\\\[P\_0 \= \\\\frac{C}{(1+y)} \+ \\\\frac{C}{(1+y)^2} \+ \\\\dots \+ \\\\frac{C+N}{(1+y)^T} \= \\\\frac{C}{y} \\\\left( 1 \- \\\\frac{1}{(1+y)^T} \\\\right) \+ \\\\frac{N}{(1+y)^T} \\\\quad \\\\text{, where } y \= \\\\text{yield-to-maturity}\\\\\\\] \\\\\\\[P\_0 \= \\\\frac{C}{(1+r\_1)} \+ \\\\frac{C}{(1+r\_2)^2} \+ \\\\dots \+ \\\\frac{C+N}{(1+r\_T)^T} \\\\quad \\\\text{, where } r\_t \= t\\\\text{-year interest rate}\\\\\\\]  
The yield curve based on government zero-coupon bonds is flat at 11 percent per year for all maturities. What is the price of a government zero-coupon bond with a face value (par value) of 1000 euros and with exactly 260-months until maturity?

#### Required Formula

For a zero-coupon bond (\\\\(C \= 0\\\\)), the general bond pricing formula simplifies to: \\\\\\\[P\_0 \= \\\\frac{N}{(1 \+ y)^T}\\\\\\\] where:

* \\\\(N\\\\) \= Face value (Par value)  
* \\\\(y\\\\) \= Annual interest rate / yield  
* \\\\(T\\\\) \= Time to maturity in years \= \\\\(\\\\frac{\\\\text{Months}}{12}\\\\)

#### Numerical Application

* **Convert maturity to years:** \\\\\\\[T \= \\\\frac{260}{12} \= \\\\frac{65}{3} \\\\approx 21.6667\\\\text{ years}\\\\\\\]  
* **Substitute variables into the formula:**  
* \\\\(N \= 1,000\\\\text{ euros}\\\\)  
* \\\\(y \= 11% \= 0.11\\\\)  
* **Calculate price \\\\(P\_0\\\\):** \\\\\\\[P\_0 \= \\\\frac{1,000}{(1 \+ 0.11)^{260/12}} \= \\\\frac{1,000}{(1.11)^{21.6667}}\\\\\\\] \\\\\\\[P\_0 \= \\\\frac{1,000}{9.593962} \= \\\\mathbf{104.23\\\\text{ euros}}\\\\\\\]

### Question 3

#### Original Question & Cheat Sheet

**Bonds** \\\\\\\[P\_0 \= \\\\frac{C}{(1+y)} \+ \\\\frac{C}{(1+y)^2} \+ \\\\dots \+ \\\\frac{C+N}{(1+y)^T} \= \\\\frac{C}{y} \\\\left( 1 \- \\\\frac{1}{(1+y)^T} \\\\right) \+ \\\\frac{N}{(1+y)^T} \\\\quad \\\\text{, where } y \= \\\\text{yield-to-maturity}\\\\\\\] \\\\\\\[P\_0 \= \\\\frac{C}{(1+r\_1)} \+ \\\\frac{C}{(1+r\_2)^2} \+ \\\\dots \+ \\\\frac{C+N}{(1+r\_T)^T} \\\\quad \\\\text{, where } r\_t \= t\\\\text{-year interest rate}\\\\\\\]  
What is the price as of now (\\\\(t\_0\\\\)) of a coupon-bond which has a face value 1,694 euros, coupon rate 5% per year, yield-to-maturity 15% per year and time to maturity 23 years? Enter the answer with two decimals, **do not** enter any words (euros) or signs, separate integers and decimals with a point (.) and not a comma (,).

#### Required Formula

\\\\\\\[P\_0 \= \\\\frac{C}{y} \\\\left( 1 \- \\\\frac{1}{(1+y)^T} \\\\right) \+ \\\\frac{N}{(1+y)^T}\\\\\\\] where:

* \\\\(N\\\\) \= Face value  
* \\\\(c\\\\) \= Annual coupon rate \\\\(\\\\implies C \= c \\\\times N\\\\) (annual coupon amount in euros)  
* \\\\(y\\\\) \= Yield-to-maturity (YTM)  
* \\\\(T\\\\) \= Time to maturity in years

#### Numerical Application

1. **Compute annual coupon payment \\\\(C\\\\):** \\\\\\\[C \= 5% \\\\times 1,694 \= 0.05 \\\\times 1,694 \= 84.70\\\\text{ euros}\\\\\\\]  
2. **Calculate Present Value of Coupon Annuity:** \\\\\\\[\\\\text{PV}(\\\\text{Coupons}) \= \\\\frac{84.70}{0.15} \\\\left( 1 \- \\\\frac{1}{(1 \+ 0.15)^{23}} \\\\right)\\\\\\\] \\\\\\\[\\\\text{PV}(\\\\text{Coupons}) \= 564.6667 \\\\times \\\\left( 1 \- \\\\frac{1}{24.891404} \\\\right) \= 564.6667 \\\\times 0.959826 \= 541.9815\\\\text{ euros}\\\\\\\]  
3. **Calculate Present Value of Face Value:** \\\\\\\[\\\\text{PV}(\\\\text{Face Value}) \= \\\\frac{1,694}{(1.15)^{23}} \= \\\\frac{1,694}{24.891404} \= 68.0555\\\\text{ euros}\\\\\\\]  
4. **Sum the two components to get \\\\(P\_0\\\\):** \\\\\\\[P\_0 \= 541.9815 \+ 68.0555 \= \\\\mathbf{610.04\\\\text{ euros}}\\\\\\\]

*(Format for exam submission: **610.04**)*

### Question 4

#### Original Question & Cheat Sheet

**Bonds** Bond A has a face value equal to 1000 euros, coupon rate 13% per year, time to maturity 2 years and yield-to-maturity 10% per year. Bond B has a face value equal to 1000 euros, coupon rate 13% per year, time to maturity 16 years and yield-to-maturity 10% per year. What is the **time to maturity** of the bond that has a **higher** sensitivity to changes in interest rates. For ex., if your answer is 5 years, just enter 5\.

#### Required Formula & Fundamental Principle

Bond price sensitivity to interest rate fluctuations is quantified by **Macaulay Duration** (\\\\(D\\\_{\\\\text{Mac}}\\\\)) and **Modified Duration** (\\\\(D\\\_{\\\\text{Mod}}\\\\)): \\\\\\\[D\\\_{\\\\text{Mod}} \= \\\\frac{D\\\_{\\\\text{Mac}}}{1+y}, \\\\quad \\\\text{where } \\\\frac{\\\\Delta P}{P\_0} \\\\approx \- D\\\_{\\\\text{Mod}} \\\\cdot \\\\Delta y\\\\\\\]  
**Key Property of Duration:** All else being equal (holding face value, coupon rate, and YTM constant), **duration increases with time to maturity (\\\\(T\\\\))**. Therefore, the bond with the longer time to maturity has a higher duration and higher price sensitivity to interest rate changes.

#### Numerical Application

* **Compare parameters:**  
* Both bonds have \\\\(N \= 1,000\\\\text{ euros}\\\\), coupon rate \\\\(= 13%\\\\), YTM \\\\(= 10%\\\\).  
* Bond A: \\\\(T \= 2\\\\text{ years} \\\\implies D\\\_{\\\\text{Mod}} \\\\approx 1.72\\\\text{ years}\\\\)  
* Bond B: \\\\(T \= 16\\\\text{ years} \\\\implies D\\\_{\\\\text{Mod}} \\\\approx 7.47\\\\text{ years}\\\\)  
* **Conclusion:**  
* Bond B (\\\\(T \= 16\\\\text{ years}\\\\)) has the higher duration and thus higher sensitivity.  
* The question asks specifically for the **time to maturity** of that bond.

*(Format for exam submission: **16**)*

### Question 5

#### Original Question & Cheat Sheet

**Forwards & Futures** One week ago, you sold 88 forward contracts (i.e., you entered 88 short positions) with the following characteristics: Underlying asset is Apple Inc. shares; each forward contract is on 100 shares; contract maturity is 21/11/2025; one week ago, the price of the forward was \\\\(F\\\_{21/11/25} \= 151\\\\text{ USD/share}\\\\). **What is your payoff on 21/11/2025 if, at that date, the spot price of one Apple Inc. share is 139 USD?**

#### Required Formula

For a **short forward position** on \\\\(N\\\_{\\\\text{shares}}\\\\) at forward delivery price \\\\(F\_0\\\\) and spot price at maturity \\\\(S\_T\\\\): \\\\\\\[\\\\text{Payoff}*{\\\\text{short, per share}} \= F\_0 \- S\_T\\\\\\\] \\\\\\\[\\\\text{Total Payoff} \= N*{\\\\text{contracts}} \\\\times m \\\\times (F\_0 \- S\_T)\\\\\\\] where \\\\(m\\\\) is the multiplier (number of shares per contract).

#### Numerical Application

* **Identify inputs:**  
* \\\\(N\\\_{\\\\text{contracts}} \= 88\\\\) contracts (short position)  
* \\\\(m \= 100\\\\) shares/contract  
* Total underlying shares \\\\(= 88 \\\\times 100 \= 8,800\\\\text{ shares}\\\\)  
* Agreed forward price \\\\(F\_0 \= 151\\\\text{ USD/share}\\\\)  
* Spot price at maturity \\\\(S\_T \= 139\\\\text{ USD/share}\\\\)  
* **Calculate payoff per share:** \\\\\\\[\\\\text{Payoff}\\\_{\\\\text{per share}} \= 151 \- 139 \= \+12\\\\text{ USD/share}\\\\\\\]  
* **Calculate total payoff:** \\\\\\\[\\\\text{Total Payoff} \= 8,800\\\\text{ shares} \\\\times 12\\\\text{ USD/share} \= \\\\mathbf{105,600\\\\text{ USD}}\\\\\\\]

