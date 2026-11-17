### Formula Header (Aide-mémoire)

* **Zero-coupon bond pricing & yield-to-maturity:** \\\\\\\[Z\_0 \= \\\\frac{N}{(1+y)^T} \\\\iff y \= \\\\left(\\\\frac{N}{Z\_0}\\\\right)^{1/T} \- 1\\\\\\\]  
* **Spot rates and forward rates:** \\\\\\\[(1+r\_T)^T \= (1+r\_t)^t \\\\times (1+f\\\_{t \\\\to T})^{(T-t)}, \\\\quad \\\\text{where } T \\\> t\\\\\\\]  
* **Law of One Price (No-Arbitrage Replication):** \\\\\\\[\\\\text{If } \\\\text{CF}(\\\\text{Bond}\\\_1) \= \\\\sum\_i w\_i , \\\\text{CF}(\\\\text{Bond}\\\_i) \\\\text{ with identical default risk, then } P\_1 \= \\\\sum\_i w\_i , P\_i\\\\\\\]  
* **1-year Holding Period Return (HPR) for a zero-coupon bond:** \\\\\\\[\\\\text{HPR} \= \\\\frac{P\_1 \- P\_0}{P\_0} \= \\\\frac{P\_1}{P\_0} \- 1\\\\\\\]  
* **Short Forward Contract Payoff at Maturity \\\\(T\\\\):** \\\\\\\[\\\\text{Payoff}*{\\\\text{short}} \= \\\\text{Number of contracts} \\\\times \\\\text{Contract size} \\\\times (F*{0,T} \- S\_T)\\\\\\\]

### Question 1

**Verbatim Question:**  
*"Today (at t=0), a 15-year US government-issued default-risk-free zero-coupon bond with a par value (face value) of N=1000 \$ has a yield-to-maturity of 3.7% per year. Suppose that exactly one year from now (i.e., as of date t \= 1 year) the same zero-coupon bond has a yield-to-maturity of 1.1% per year. What would be your 1-year holding period return (HPR) if you buy this zero-coupon bond today at t \= 0 and sell it after 1-year at t \= 1?* *If your answer is \+1.23% enter it as 0.0123, if your answer is \-1.23% enter it as \-0.0123"*

#### 1\. Required Formula:

Since a zero-coupon bond pays no intermediate coupon (\\\\(C \= 0\\\\)), its price at \\\\(t \= 0\\\\) (with \\\\(T \= 15\\\\) years remaining) and at \\\\(t \= 1\\\\) (with \\\\(T \- 1 \= 14\\\\) years remaining) are: \\\\\\\[P\_0 \= \\\\frac{N}{(1+y\_0)^T}, \\\\qquad P\_1 \= \\\\frac{N}{(1+y\_1)^{T-1}}\\\\\\\]  
The 1-year holding period return (\\\\(\\\\text{HPR}\\\\)) is: \\\\\\\[\\\\mathbf{\\\\text{HPR} \= \\\\frac{P\_1 \- P\_0}{P\_0} \= \\\\frac{(1+y\_0)^T}{(1+y\_1)^{T-1}} \- 1}\\\\\\\]  
*(Exam shortcut: notice \\\\(N\\\\) cancels out, so you can compute \\\\(\\\\frac{(1+y\_0)^T}{(1+y\_1)^{T-1}} \- 1\\\\) directly\!)*

#### 2\. Numerical Application:

* **Given data:** \\\\(N \= 1000\\\\text{ \$}\\\\), \\\\(T \= 15\\\\text{ years}\\\\), \\\\(y\_0 \= 3.7% \= 0.037\\\\), \\\\(y\_1 \= 1.1% \= 0.011\\\\)  
1. **Price at \\\\(t=0\\\\):** \\\\\\\[P\_0 \= \\\\frac{1000}{(1.037)^{15}} \= \\\\frac{1000}{1.724572} \= \\\\mathbf{579.853996\\\\text{ \$}}\\\\\\\]  
2. **Price at \\\\(t=1\\\\) (14 years remaining to maturity):** \\\\\\\[P\_1 \= \\\\frac{1000}{(1.011)^{14}} \= \\\\frac{1000}{1.165510} \= \\\\mathbf{857.993152\\\\text{ \$}}\\\\\\\]  
3. **1-year Holding Period Return:** \\\\\\\[\\\\text{HPR} \= \\\\frac{857.993152 \- 579.853996}{579.853996} \= \\\\mathbf{0.479671}\\\\\\\]

#### Final Answer:

**0.4797**

### Question 2

**Verbatim Question:**  
*"Consider the US government zero-coupon bond (STRIPS) market. Today (at t=0), the required rate of return on a 4-year zero-coupon bond is 4.3% per year. As of today, the 1-year forward interest rate starting with date t=4 is 8.4% per year. What must be the required rate of return on a per-year basis on the 5-year government zero-coupon bond such that there is no arbitrage opportunity? If your answer is \+1.23% enter it as 0.0123."*

#### 1\. Required Formula:

Using the relationship between spot rates and forward rates (\\\\(t \= 4\\\\), \\\\(T \= 5\\\\)): \\\\\\\[(1+r\_5)^5 \= (1+r\_4)^4 \\\\times (1+f\\\_{4 \\\\to 5})^1\\\\\\\]  
Solving for the 5-year spot rate \\\\(r\_5\\\\): \\\\\\\[\\\\mathbf{r\_5 \= \\\\left\\\[(1+r\_4)^4 \\\\times (1+f\\\_{4 \\\\to 5})\\\\right\\\]^{1/5} \- 1}\\\\\\\]

#### 2\. Numerical Application:

* **Given data:** \\\\(r\_4 \= 4.3% \= 0.043\\\\), \\\\(f\\\_{4 \\\\to 5} \= 8.4% \= 0.084\\\\)  
1. **5-year compounding factor:** \\\\\\\[(1+r\_5)^5 \= (1.043)^4 \\\\times (1.084) \= 1.18345705 \\\\times 1.084 \= \\\\mathbf{1.28286744}\\\\\\\]  
2. **Extract annual 5-year spot rate:** \\\\\\\[r\_5 \= (1.28286744)^{1/5} \- 1 \= 1.051074 \- 1 \= \\\\mathbf{0.051074}\\\\\\\]

#### Final Answer:

**0.0511**

### Question 3

**Verbatim Question:**  
*"Consider the following bonds:* *Bond1: Maturity \= 2 years; Face value \= 100; coupon rate \= 0%, Credit rating \= AA* *Bond2: Maturity \= 2 years; Face value \= 50; coupon rate \= 100% (hundred percent) per year, Credit rating \= AA; Price \= 136* *Bond3: Maturity \= 1 year; Face value \= 50; coupon rate \= 0%, Credit rating \= AA; Price \= 48* *Bond4: Maturity \= 2 years; Face value \= 50; coupon rate \= 100% (hundred percent) per year, Credit rating \= BB; Price \= 151* *Bond5: Maturity \=1 years; Face value \= 50; coupon rate \= 0%, Credit rating \= BB; Price \= 50* *What is the no-arbitrage price of bond Bond1?"*

#### 1\. Required Formula:

By the **Law of One Price**, two portfolios with the **same default risk (credit rating)** and **identical future cash flows** must have the same price today.

* **Important check:** Bond1 has credit rating **AA**, so we must replicate it using **Bond2** and **Bond3** (which are also **AA**), and ignore Bond4 and Bond5 (which are **BB**).

Let \\\\(n\_2\\\\) and \\\\(n\_3\\\\) be the number of units of Bond2 and Bond3 needed to replicate Bond1: \\\\\\\[\\\\mathbf{P\\\_{\\\\text{Bond1}} \= n\_2 \\\\times P\\\_{\\\\text{Bond2}} \+ n\_3 \\\\times P\\\_{\\\\text{Bond3}}}\\\\\\\]

#### 2\. Numerical Application:

* **Cash flows of each AA-rated bond:**  
* **Bond1:** \\\\(t=1: 0\\\\), \\\\(t=2: 100\\\\)  
* **Bond2** (coupon \\\\(C \= 100% \\\\times 50 \= 50\\\\)): \\\\(t=1: 50\\\\), \\\\(t=2: 50 \+ 50 \= 100\\\\), with \\\\(P\\\_{\\\\text{Bond2}} \= 136\\\\)  
* **Bond3:** \\\\(t=1: 50\\\\), \\\\(t=2: 0\\\\), with \\\\(P\\\_{\\\\text{Bond3}} \= 48\\\\)  
* **Find the replicating portfolio:**  
* At \\\\(t=2\\\\): \\\\(100 \\\\times n\_2 \= 100 \\\\implies \\\\mathbf{n\_2 \= 1}\\\\)  
* At \\\\(t=1\\\\): \\\\(50 \\\\times n\_2 \+ 50 \\\\times n\_3 \= 0 \\\\implies 50(1) \+ 50n\_3 \= 0 \\\\implies \\\\mathbf{n\_3 \= \-1}\\\\) (short 1 unit of Bond3)  
* **Apply the Law of One Price:** \\\\\\\[P\\\_{\\\\text{Bond1}} \= (1 \\\\times 136\) \+ (-1 \\\\times 48\) \= 136 \- 48 \= \\\\mathbf{88}\\\\\\\]

#### Final Answer:

**88**

### Question 4

**Verbatim Question:**  
*"Consider the government bonds-based term structure of interest rates as of today (t=0). The 4-year interest rate on the related yield curve is equal to r4 \= 3.5% per year. The following year's zero-coupon bond rate r4+1 is 25 basis points higher than 3.5%. As of today, what is, f4→4+1 , i.e., the one-year forward interest rate starting with date 4?* *Use only 4 decimals after the decimal point, do not use a comma or a % sign. For ex., for 1.23% enter only 0.0123"*

#### 1\. Required Formula:

Relating the 4-year and 5-year spot rates to the 1-year forward rate starting at \\\\(t=4\\\\): \\\\\\\[(1+r\_5)^5 \= (1+r\_4)^4 \\\\times (1+f\\\_{4 \\\\to 5})\\\\\\\]  
Solving for \\\\(f\\\_{4 \\\\to 5}\\\\): \\\\\\\[\\\\mathbf{f\\\_{4 \\\\to 5} \= \\\\frac{(1+r\_5)^5}{(1+r\_4)^4} \- 1}\\\\\\\]

#### 2\. Numerical Application:

* **Given data:**  
* \\\\(r\_4 \= 3.5% \= 0.035\\\\)  
* \\\\(r\_5 \= r\\\_{4+1} \= 3.5% \+ 25\\\\text{ bps} \= 3.5% \+ 0.25% \= 3.75% \= \\\\mathbf{0.0375}\\\\) *(since \\\\(1\\\\text{ bp} \= 0.01% \= 0.0001\\\\))*  
1. **Compute compound factors:** \\\\\\\[(1+r\_5)^5 \= (1.0375)^5 \= \\\\mathbf{1.20209981}\\\\\\\] \\\\\\\[(1+r\_4)^4 \= (1.035)^4 \= \\\\mathbf{1.14752300}\\\\\\\]  
2. **Compute the forward rate:** \\\\\\\[f\\\_{4 \\\\to 5} \= \\\\frac{1.20209981}{1.14752300} \- 1 \= 1.04756054 \- 1 \= \\\\mathbf{0.047561}\\\\\\\]

#### Final Answer:

**0.0476**

### Question 5

**Verbatim Question:**  
*"You just entered into 58 short positions for a forward contract with the following features:* *Underline asset: gold* *size per contract: 197 grams* *Maturity: 16 months* *Forward price F(0, 16 months) \= F0, 16 months \= 41 euros/gram* *Settlement type: cash* *If after 16 months the price of gold is S16 months \= 48 €/gram in the spot market, what is your payoff?* *Enter your answer in full euros: if your answer is \+123 enter 123, if your answer is \-123 enter \-123 (i.e., do not enter any cents, do not use the decimal point, do not enter any letters or € sign, do not use any commas, do not write formulas, do not write letters, etc)."*

#### 1\. Required Formula:

For a **short** forward position (obligation to sell at the contracted forward price \\\\(F\\\_{0,T}\\\\) when the market spot price at maturity is \\\\(S\_T\\\\)): \\\\\\\[\\\\mathbf{\\\\text{Payoff}*{\\\\text{short}} \= \\\\text{Number of contracts} \\\\times \\\\text{Size per contract} \\\\times (F*{0,T} \- S\_T)}\\\\\\\]

#### 2\. Numerical Application:

* **Given data:**  
* Number of short contracts \\\\(= 58\\\\)  
* Size per contract \\\\(= 197\\\\text{ grams}\\\\)  
* Forward price \\\\(F\\\_{0, 16\\\\text{m}} \= 41\\\\text{ €/gram}\\\\)  
* Spot price at maturity \\\\(S\\\_{16\\\\text{m}} \= 48\\\\text{ €/gram}\\\\)  
1. **Total quantity of gold:** \\\\\\\[\\\\text{Total quantity} \= 58 \\\\times 197 \= \\\\mathbf{11{,}426\\\\text{ grams}}\\\\\\\]  
2. **Payoff per gram:** \\\\\\\[F\\\_{0, 16\\\\text{m}} \- S\\\_{16\\\\text{m}} \= 41 \- 48 \= \\\\mathbf{-7\\\\text{ €/gram}}\\\\\\\]  
3. **Total payoff:** \\\\\\\[\\\\text{Payoff}\\\_{\\\\text{short}} \= 11{,}426 \\\\times (-7) \= \\\\mathbf{-79{,}982\\\\text{ €}}\\\\\\\]

#### Final Answer:

**\-79982** *(enter without commas or € sign)*  
