# Financial-Data-Analytics-and-Forecasting-Models

# Fintech Econometrics

### Definition :

```

- Financial Econometrics will be defined as the Application of statistical Techniques and Methods to Financial Problems.

- Financial Econometrics is useful in testing the theories in finance,determining the risks,returns,predictive errors,relationship between the variables.

```

---

### Why we Use Econometrics in Finance :

```
The value of econometrics:

   (1) Testing whether financial markets are weak-form informational efficient.

   (2) Testing whether the Capital Asset Pricing Model (CAMP) or Arbitrage Pricing Theory (APT) represent superior models for the determination of returns on risky assets

   (3) Measuring and forecasting the volatility of bond returns

   (4) Explaining the determinants of bond credit ratings used by the ratings agencies

   (5) Modelling long-term relationships between prices and exchange rates

   (6) Determining the optimal hedge ratio for a spot position in oil

   (7) Testing technical trading rules to determine which makes the most money

   (8) Testing the hypothesis that earnings or dividend announcements have no effect on stock prices

   (9) Testing whether spot or futures markets react more rapidly to news

   (10) Forecasting the correlation between the stock indices of two countries.

```

---

### Difference between Financial Econometrics VS Economical Econometrics :

---

## FINANCIAL ECONOMETRICS :

### 1. In Financial Econometrics the emphasis and the set of problems that are encountered when we can analyzing two set of data which are slightly different.

### 2. Financial data often differ from macroeconomic data in terms of their frequency, accuracy, seasonality and other properties.

### 3.Financial data come in many shapes and forms, but in general the prices and other entities that are recorded are those at which trades actually took place, or which were quoted by information providers.

### 4. In financial data are observed at much higher frequencies than macroeconomic data. Asset prices or yields are often available at daily, hourly, or minute-by-minute frequencies.(Data is in large amount and without altered or manuplicated).It is a setback as processing the large amount of data leads to problems in developing optimized methodology.

---

## ECONOMIC ECONOMETRICS :

### 1. A serious problem is often a lack of data at hand for testing the theory or hypothesis of interest -- this is often called a ‘small samples problem’.

### 2. Two other problems that are often encountered in conducting applied econometric work (data collection for analyzing ) in the arena of economics are those of measurement error and data revisions.

---

## Types of DATA :

</br>

### 1. TIME SERIES DATA :

. The Data is Collected over a period of Time on one or more variables.

. Example : Stock price analysis/prediction,the stock data is Time-Series data .

. Time Series is collection of data points.

. It is also necessary requirement that all data used in a model be of the same frequency of observation.
</br>

### USAGE OF TIME SERIES DATA :

-> How the value of a country’s stock index has varied with that country’s macroeconomic fundamentals

-> How the value of a company’s stock price has varied when it announced the value of its dividend payment also.

### \*\* Dividend = directly indicates the company's profit.

-> The effect on a country’s exchange rate of an increase in its trade deficit.
</br>

### 2. CROSS SECTIONAL DATA :

. Cross-sectional data are data on one or more variables collected at a single point in time.

. A simple RBI bonds credits is basically for a period of time like for semi-anally or quarterly.
</br>

### USAGE OF CROSS-SECTIONAL DATA :

-> The relationship between company size and the return to investing in its shares.

-> The relationship between a country’s GDP level and the probability that the government will default on its sovereign debt.
</br>

### 3. PANEL DATA :

. Panel data is a type of data that consists of observations over multiple time periods on the same units (e.g., individuals, companies, countries). It combines both cross-sectional and time-series dimensions.

. It allows for studying the effects of variables that change over time and seeing patterns or trends.

. provides more accurate inference of model parameters.

. Contains more variability, reducing collinearity among explanatory variables.

### USAGE OF PANEL DATA :

-> We might use it to study how changes in government policy (over time) impact different regions or sectors(at present changes).

-> Analysts could study how different firms' stock prices consecutive quarters or years.

---

### CONTINUOUS VS DISCRETE DATA :

---

### CONTINUOUS DATA :

1. Represents measurements and can take infinite number of values within a given range.

2. The Data can be further sub-divided into infinite data points.

3. It is like a straight line having infinite number of points.

4. The data is collected by measuring process & methodology.

5. The Graphical representation of data is generally a curve.(can be parabolic also)

6. Some Examples are :

   - Stock Prices: The price of a stock at a given point in time is continuous.

   - Interest Rates: An interest rate can be 5%, 5.01%, 5.001%, etc. It's a continuous measure as it can take any value within a possible range.

### DISCRETE DATA :

1. Represents information that can be categorized into a distinct number of values.(specific and countable).

2. It cannot be further sub-divided.

3. The Discrete data is collected by counting process or methodology.

4. The Graphical representation of discrete data is generally isolated data points.

5. Some Examples are :

   - Number of Shares: If you're analyzing a portfolio, the number of shares of each stock you own would be discrete data.

   - Credit Rating: Companies might be rated on a scale.Each rating is a distinct category.

---

## Nominal Data/Numbers :

1.  Represents categories or labels and cannot be ordered or quantified.

2.  Example :

    - Back Account Numbers : if any one has a A/C number as : 198383 and another A/C : 166625 so we don't compare the bank account numbers.

## Ordinal Data/Numbers :

1. Represents categories with a specific order or ranking, but the differences between the ranks are not uniform.

2. Example :

   - Investment Risk Levels :Some investment portfolio is categorized into risks levels (Aggressive,Medium,low).
     Here the levels don't have any such value range.

## Cardinal Data/Numbers :

1. Represents actual numeric values where both order and magnitude are meaningful.

2. Example :

   - Stock Prices: If a stock A is at 150 and stock B is at 100,So we can say that stock A is more valued than stock B.

---

## Steps involved in forming an econometric model

![plot](./fig1.png)

---

## Detailed Explanation of Each Step :

### STAGE 1a & 1b :

- General Statement of the Problem
- Involves formulation of a theoretical model from the theoretical information.
- Identifies the dependent and independent variables,factors affecting the dependent variables and the relationship between the variables.

### STAGE 2 :

- Collection of Data which is relevant to the Model.
- The data required may be recorded in digital formats or survey reports or general data reports.

### STAGE 3 :

- Choosing an estimation method which is relevant to the model.
- like choose single equation technique or multiple equation technique etc.

### STAGE 4 :

- Statistical Evaluation of the Model Developed.
- which assumptions are needed to optimized the model.
- does the data was enough for the model training.
- did data covered all the types and conditions.
- if the data is not perfect then we have to go to stage 2 .

### STAGE 5 :

- Evaluation of the Model from a Theoretical point-of-view.
- Analyzing the model working ,inputs,outputs by referring the theory which is used.
- Try to Dry-run the Model to understand the deviation from desired output.

### STAGE 6 :

- Use of Model.
- When all the unit testing and model is ready for deployment then we tests the theory that we have developed in Stage 1.

---

## PACKAGES USED IN ECONOMETRICS :

### -> Famous Packages used :

<br>
- SPSS : Statistical Package for the Social Sciences(used for statistic analysis).

- USED for :

      - Descriptive statistics
      - Hypothesis testing
      - Regression analysis
      - Cluster analysis

  <br>

- MATLAB : MATrix LABoratory, is a high-level programming language

  - USED for :

        - Signal processing
        - Image processing
        - Financial modeling

    <br>

- SHAZAM : It provides a variety of econometric and statistical techniques, including linear regression, hypothesis testing, non-linear estimation

---

### Why do we Use these Packages ?

. These packages are used for following reasons :

1. Complex Calculations : Complicated Mathematical equations that are very time-consuming.

2. Data Handling : These process can process large data-sets.

3. Accuracy : It reduces the risk of Human Errors.

4.Integration and Interoperability: Some software can collaborate with other packages and interfaces like MATLAB can integrate python and R.

5. Specialized Functions : Many Softwares or Packages provides specialized or customized toolboxes or modules or libraries.

6. Visualization : Software packages offer advanced data visualization tools, enabling users to create a wide variety of graphs, plots, and charts.

---

### How to choose a package ?

- Choosing the right software package depends on several factors :

  1. As per the " Needs " :

     - Type of Data
     - Nature of the Data
     - Future Scalability
     - Tasks to be performed

  2. User Interface

  3. Documentation related to Software/Package

  4. Community Support

  5. Interoperability & Integration : (if the software can be integrated with other tools and packages/softwares).

  6. Security & Privacy: The Data security.

  7. Flexibility & Customization

  8. Trial & Evaluation

---

## Regression Model

-> Regression is basically describing/explaining and evaluating the relationship between the give variables
(can be multiple variables).

-> Regression tries to explain the movements of the variable with respect to other variables.

-> Let put this into an Equation :

## &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 𝓎 = 𝓍𝟣 + 𝓍𝟤 + 𝓍𝟥 +.....+ 𝓍𝓀

```
1. y -> Dependent Variable

2. x1,x2,x3....xk -> Independent Variables

3. k -> Number of Factors or Variables.
```

---

## Naming of y and x in regression models :

| Synonyms for y        | Synonyms for xs       |
| --------------------- | --------------------- |
| Dependent variable    | Independent variables |
| Regressand            | Regressors            |
| Causal variables      | Effect variable       |
| Explanatory variables | Explained variable    |

---

## Regression VS Correlation :

## Correlation

### Correlation : It is between two variables which is the measurement of the degree of linear association between them.

### It simply measures the association between variables but does not allow for predictions based on the data.

### Typically deals with the relationship between two variables.

### If it states that x and y are correlated, so it doesn't define that in changes in x will lead to changes in y or vice-versa, but simply states that there is a evidence for a linear association/relationship.

## Regression

### Regression : In this the dependent variable '<em>y</em>' and independent variables '<em>x's</em>' both are different entities and the relation between them is defined/stated.

### Regression for analysis is more powerful than correlation because if we have a regression model, we can input new data to predict the dependent variable.

### Multiple regression allows you to consider the relationship between one dependent variable and several independent variables.

---

## SIMPLE REGRESSION

-> It is used to analyze and study the relationship between 2 continuous variables.

-> Here one variable is independent and another one is dependent variable.

-> It is used to analyze trends,making predictions etc.

### -> Applications of Simple Regression :

         - Risk Assessment
         - Investment Analysis
         - Economic Analysis

### -> Advantages :

      - Simplicity (easy to implement)
      - Predictions from the established Relationship

### -> Disadvantages :

      - Linearity : Assumption that there is a linear relation between the variables.
      - Only one dependent variable (factors).

### -> Stating the Equation :

## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;𝔂 = 𝓫0 + 𝓫1𝔁 + 𝓔

### -> <em>'𝓔'</em> is the Error term or Deviation between the predicted value and actual value.

---

## OLS METHOD (Ordinary Least Squares)

- It is basically used to validate the assumptions of linear regression model.

- Most common method to estimate the coefficients of a linear regression model.

- The Main objective of OLS is to minimize the sum of the squared differences between the actual values and predicted values.

- Stating the Equation :

## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;∑ ( 𝓨𝓲 − 𝓨𝓸 ) ^2

### . 𝓨𝓲 -> actual value

### . 𝓨𝓸 -> predicted value

---

### Why Square the Residuals?

1. If we don't do then the negative and positive residuals might cancel each other out which leads to many points to lie in the best-fit-line.

2. Squaring ensures all are positive, then we can focus on minimizing actual prediction errors.

---

## Graphical Representation of Simple Regression

### -> x vs y data point scatter graph

![plot](./fig2.png)

### ANALYSIS OF THE PLOT

```

1.Approximate we can see a positive linear relationship between x and y which means that increases in x we can see an increase in y also.

2. We can draw a best fit line which will intersects the maximum data-points.

3.The vertical distances from the best-fit-line is called deviation or error-term.

```

### Adding the Best-Fit-Line to the Scattered Data Point Graph

![plot](./fig3.png)

### Analysis of Best-Fit-Line Plotted Graph :

```

1. Finding the Best Line: The "best" line is determined by values of α (intercept) and β (slope) that minimize the RSS.

```

### Using the OLS METHOD TO VALIDATE THE MODEL'S OUTPUT :

![plot](./fig4.png)

### Analysis of OLS Plotted Graph :

```
1.The primary goal of OLS is to find a line (or a "fitted line") that best fits a set of data points.

2. '𝓨𝓲' is actual value and '𝓨𝓸' is predicted value and difference between them is called " 𝓻𝓮𝓼𝓲𝓭𝓾𝓪𝓵 " (residual) .

3. Here we will find RSS (Residual Sum of Squares) : This is the sum of all the squared residuals.It indicates the errors our model has proposed.

```

---

## Linearity and possible forms of regression function :

### -> So for using OLS the model should be linear that means the relation between ' 𝔁 ' and ' 𝔂 ' should be described through a straight line.

### -> Here the parameters should be also linear.(α,β)

## \*\* That means α,β should not be multiplied,squared,cubed,etc.

## Exponential Regression Model :

### -> In Exponential regression model since Y varies according to some exponent (power) function of X.

### -> Here we need to convert this exponential equation into a linear equation so we have to use log both sides and simply the equation and then we can use OLS(Ordinary Least Square).

```

               Y = A * X^β * e^ut

```

---

## Assumptions in Linear Regression Model :

| Technical notation | Interpretation                                                                      |
| ------------------ | ----------------------------------------------------------------------------------- |
| E(ut ) = 0         | The errors have zero mean                                                           |
| var(ut ) = σ 2 < ∞ | The variance of the errors is constant and finite over all values of xt             |
| cov(ui , u j ) = 0 | The errors are linearly independent of one another using Covariance function        |
| cov(ut , xt ) = 0  | There is no relationship between the error and x variable using Covariance function |

---

## HYPOTHESIS TESTING :

### -> Hypothesis testing is a statistical method which is used to draw conclusions for the financial theories and the analysis model.

### -> It is a Structured way to determine whether there is enough data to support an assumption.

### -> There are 2 Categories of Hypothesis :

### - Null Hypothesis

```
** Here we say there is no relation between the variables .

1. It is a Statement which has default status and zero happening.

2. So we assume that the assumption is true until we find any proof against the statement.

3. It is a quantitative analysis.

4. The Conclusion statement if the Null hypothesis fails will be :

" The given set of data does not provide strong evidence against the null hypothesis because of insufficient evidence ."

```

### - Alternative Hypothesis :

```
** It test over the Relationship between the two variables.

1. Here we assume a statement that there is a relation between the variables and then test to prove this assumption.

2. Like assuming that x is inversely proportional to y and z then we have to use a data set to prove this statement.

3. The Conclusion statement if the Alternative hypothesis fails will be :

" The given set of data does not provide strong evidence against the relationship between the x and y variables because of insufficient evidence ."

```

---

## The Confidence Level While doing Regression :

### While doing Null Testing & Alternative Testing and finding out the confidence range from the given sample data.

### The Plots to Explain the Analysis Results :

### Here the ' 𝓑^ ' -> Standard errors away from the best fit line.

### Here the ' 𝓑\* ' -> Value obtained from Null hypothesis testing.

### Determining the Rejection by Certain Conditions.

### \*\*\* 𝐻𝑜 is Null Hypothesis Testing O/P or VALUE.

### \*\*\* 𝐻𝟣 is Alternative Hypothesis Testing O/P or VALUE.

---

### Condition 1 : if 𝐻𝑜 : 𝓑 = 𝓑\* && 𝐻𝟣 : 𝓑 != 𝓑\*

## ![plot](./fig5.png)

---

### Condition 2 : if 𝐻𝑜 : 𝓑 = 𝓑\* && 𝐻𝟣 : 𝓑 < 𝓑\*

## ![plot](./fig7.png)

---

### Condition 3 : if 𝐻𝑜 : 𝓑 = 𝓑\* && 𝐻𝟣 : 𝓑 > 𝓑\*

![plot](./fig8.png)

---

## A special type of hypothesis test: the t-ratio :

### 1. To determine predictions we perform a hypothesis test on our developed method/model.

### 2. The t-ratio is a measure used to determine how many standard errors a coefficient is away from zero (or any other value we want to test against, but in this case, it's zero).

### 3. Equation :

```

               t−ratio =  (β^ - β*)
                         ------------
                           SE( β^ )

```

### 4. Terms

- (β^ - β\*) -> difference between the estimated coefficient and testing coefficient (generally zero) .

- SE( β^ ) -> Standard Error of the Coefficient.

---

## Analysis by T-Ratio :

1. The t-ratio will tell us if the change is statistically significant or if it's likely just due to random chance .

2. A large t-ratio means that it's less likely that our observed relationship between two variables is due to random fluctuations .

3. By using the t-ratio, we can determine if financial factors have a real and statistically significant impact on other financial metrics .

---

## Explain, with the use of equations, the difference between the sample regression function and the population regression function.

### 1.Population Regression Function (PRF) :

```

1. PRF function represents true relationship between the two variables where one is dependent and another is independent .

2. EQUATION :

    --- --- --- --- --- --- ---
   |      Y = α + βX + u       |
    --- --- --- --- --- --- ---

3. Terms :

         . Y -> Dependent Variable
         . X -> Independent Variable
         . β -> Slope Coefficient
         . u -> ERROR TERM
         . α -> INITIAL EXPECTED VALUE

```

### 2. Sample Regression Function (SRF) :

```

1. SRF is a estimation for PRF function in this we just take sample data set to check the relation between the variables .

2. EQUATION :

         --- --- --- --- --- --- ---
        |    Y^ = α^ + β^X + u^     |
         --- --- --- --- --- --- ---

3. TERMS :

      . Y^ -> Predicted value of Dependent Variable
      . α^ -> Estimated Initial Expected Value
      . β^ -> Estimated slope coefficient
      . u^ -> Estimated Error term
      . X -> Independent Variable

```

---

## Generalizing the simple model to multiple linear regression

### -> Bivariate Equation for Regression Model.

### -> But There are not just one factor of influence but there are multiple factors.

### Taking an Example of Stock the Factors that influences the price of the stock are :

         . inflation
         . Sector of the company
         . products of the company
         . Company's new policies
         . etc

### So by above explanation the Equation for multivariate factors will be :

---

             yt = β1 + β2.x2t + β3.x3t + ··· + βk.xkt + ut , where t =1,2,...,T

---

#### - x2t , x3t , x4t , x5t ... xkt -> Independent Variables .

#### - β1 , β2 , β3 .... βk -> Estimated Coefficients .

#### - ut -> ERROR Term

#### - yt -> Independent Variable

### WE CAN COMPRESS THIS IN SIMPLE LINEAR REGRESSION EQUATION BY USING MATRICES

```

   - y = X.β + u

   - where: y is of dimension T × 1 X is of dimension T × k

   - β is of dimension k × 1 u is of dimension T × 1


```

![plot](./fig9.png)

---

## Testing multivariate hypotheses: the " F - TEST "

### - As t-test was used to test single hypotheses but multiple variables there will be multiple restrictions and multiple assumptions so we use F - Test .

### - F-test framework where two regressions are required, known as the unrestricted and the restricted regressions.

### - The unrestricted regression is the one in which the coefficients are freely and are composed by previous data .

### - The restricted regression is the one in where the coefficients are restricted, i.e. the restrictions are imposed .

### - Thus the F-test in hypothesis testing is also termed restricted least squares.

### - The residual sums of squares from each regression are determined, and the two residual sums of squares are ‘compared’ .

### - EQUATION FOR F - TEST :

```

              F - Ratio  =   RRSS − URSS  ×  T − k
                             ------------    -------
                                 URSS           m

```

- URSS = residual sum of squares from unrestricted regression

- RRSS = residual sum of squares from restricted regression

- m = number of restrictions

- T = number of observations

- k = number of previous data values

### \*\*\* RRSS == URSS only at very extreme circumstances this would be the case when the restriction was already present in the data.

### RELATIONSHIP BETWEEN &nbsp; " T - Test " &nbsp; and &nbsp;" F - Test "

- T-test is used for just one dependent and independent variable , whereas F-test is used for multiple independent variable.

- We can say that T - test is a special case of F - test as we square the T-test value it will be approxly equal to F-test value.

- So T-test value is = Z and F-test Value is = Z^2

### How to Find Restrictions in Hypothesis ?

1. The number of restrictions in a hypothesis can be calculated as the number of equality signs in the null hypothesis.
   Eg:

   ```
         case 1 : β1 + β2 =2                    1  restriction
         case 2 : β2 = 1 and β3 = −1            2 restrictions
         case 3 : β2 = 0 , β3 = 0 and β4 = 0    3 restrictions

   ```

2. If all coefficients are zero, and the null hypothesis isn't rejected, it implies none of the independent variables in the model can explain variations in the dependent variable,so no relation.

---

## Goodness of fit ( R^2 ) :

- A part of Analysis after performing linear regression.

- It is the Coefficient of Determination, which is used as an indicator of the goodness of fit.

- It shows how many points fall on the regression line

- In our example, R^2 is 0.91 (rounded to 2 digits), which is fairy good. It means that 91% of our values fit the regression analysis model. In other words, 91% of the dependent variables (y-values) are explained by the independent variables (x-values). Generally, R Squared of 95% or more is considered a good fit.

- Multiple R : It is the Correlation Coefficient that measures the strength of a linear relationship between two variables.

```
   1 means a strong positive relationship
  -1 means a strong negative relationship
   0 means no relationship at all

```

-
- EQUATION :

      ```
               ESS
        R^2  = ---
               TSS
      ```

- ESS -> Explained Sum of Squares
- TSS -> Total Sum of Squares

### Problems With R^2 :

- R^2 is defined in terms of variance so we cannot compare the R^2 values with different Models.

- In Simple Regression model it forms patterns and clusters of the data points.so for simple or incorrect model R^2 may show a high value because it is analyzing patterns and not the relationships between variables.

---

---

# TIME SERIES DATA ANALYSIS :

### -> First We check if the data is <em> Stationary </em> or not .

### I. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Strictly Stationary Process :

<br>

- A process is said to strictly stationary if it's joint distribution does not change when shifted with time.

- Example :

```
         T1  |  T2  | T3
---------------------------
yt   |  200  | 220  | 231
     |       |      |
yt+s |  180  | 200  | 210



. yt => CT1 = CT2 = CT3

. yt+s => CT1 = CT2 = CT3

<!-- So we can call this as strictly stationary -->

```

### II. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Weakly Stationary Process :

- A process is weakly stationary if its mean, variance, and covariance are unchanged by time shifts.

- We can say the Process is Weak stationary if it satisfies
  one of these conditions :

            ```

               . E (yt) = μ
                  - The series has a constant mean over time, denoted by  μ

               . Var (Yt) = σ²
                  - The series has a constant variance, meaning its volatility doesn't change over time. This is denoted by σ² and is always a finite value.

               . Cov (Yt , Y (t - h)) = γ(h)
                  - Covariance (relationship) between the two values in the series depends only on the lag (or gap) between those two time points, not on the actual time. This relationship is called the auto-covariance, denoted by γ .

            ```

## AUTO-COVARIANCE :

- It measures how a value in the series relates to its previous values.

- The autocovariance are not a particularly useful measure of the relationship between y and its previous values, however the values of the autocovariance depend on the measurement of y and hence the values that they take have no immediate interpretation.

- Example:

```
For instance, the relationship of a value with the previous day's value is the same as its relationship with the value.

```

## AUTO-CORRELATION ( ACF ):

- While autocovariance is useful but its values are not bounded, meaning they can take on any number from negative to positive infinity, making problem in isolation. This is where autocorrelation is being used.

- The autocorrelation function is simply the auto-covariance divided by the variance,By dividing with the variance, we normalize the it and the resulting autocorrelation values will always lie between -1 and 1.

- ANALYSIS BY VALUES :

```

      1 -> perfect positive linear from lagged value
     -1 -> perfect negative linear  from lagged value
      0 -> no linear from lagged value.

```

## PARTIAL AUTO-CORRELATION ( PACF ):

- A partial correlation is a conditional correlation.

- It is the correlation between two variables under the assumption that we know and take into account the values of some other set of variables.

- Using a half of the data set for calculating the Auto-correlation between the variables.

## WHITE NOISE PROCESS :

- A white noise process is a random process of random variables that are not correlated, have constant mean and variance.

- The Correlation function will give zero.

- ***

## MOVING AVERAGE PROCESS :

### 1. A moving average is an average of data points (usually price) for a specific time period.

### 2. Time Series model is also called as ARIMA Models.

### 3. It includes auto-regressive terms and moving average terms.

### 4. A moving average model is simply a linear combination of white noise processes, so that yt depends on the current and previous values of a white noise disturbance term.

### 5. There are Two Types of Moving Averages :

         1. Simple Moving Average (SMA)
         2. Exponential Moving Average (EMA)

### Lag Factor in Moving Averages :

- Moving Averages are based on past data, they tend to lag behind the previous data points.

- The longer the moving average, the more the lag.

## Simple Moving Average

1. A simple moving average is calculated by computing the averages over a specific period of time.

2. EXAMPLE :

```

Daily Closing Prices of a Stock: 11,12,13,14,15,16,17

First day of 5-day SMA: (11 + 12 + 13 + 14 + 15) / 5 = 13

Second day of 5-day SMA: (12 + 13 + 14 + 15 + 16) / 5 = 14

Third day of 5-day SMA: (13 + 14 + 15 + 16 + 17) / 5 = 15

```

## Exponential Moving Average :

1. Exponential moving averages (EMAs) reduce the lag by applying more weight to recent values.

2. Here we distribute weights to values which decides the priority.

3. There are three steps to calculating an exponential moving average (EMA).

   - First, calculate the simple moving average for the initial EMA value.

   - Second, calculate the weight multiplier.

   - Third, calculate the exponential moving average for each day between the initial EMA value and today, using the price, the multiplier, and the previous period's EMA value.

4. EXAMPLE :

```
         Initial SMA = 10- period-sum / 10

         Multiplier = (2 / (Time periods + 1) ) = (2 / (10 + 1) ) = 0.1818 (18.18%)

         EMA = {Close - EMA(previous day)} x multiplier + EMA(previous day).

```

## ARMA METHODOLOGY

### ARMA : ( Mixed ) autoregressive moving average processes

### Process consists of both autoregressive and moving average terms.

### If the process has terms from both an AR(p) and MA(q) process, then the process is called ARMA(p, q)

### We can straightforwardly see that by setting p != 0 and q = 0 we recover the AR(p) model. Similarly if we set p = 0 and q != 0 then we recover the MA(q) model.

### The acf alone can distinguish between a pure autoregressive and a pure moving average process.

### ARMA process will have a geometrically declining acf.

### So Pacf is useful for distinguishing between an AR(p) process and an ARMA(p,q) process.

## SUMMARY ANALYSIS :

### An autoregressive process has :

```

● a geometrically decaying acf
● a number of non-zero points of pacf = AR order.

```

### A moving average process has:

```

● number of non-zero points of acf = MA order
● a geometrically decaying pacf.

```

### A combination autoregressive moving average process has:

```

● a geometrically decaying acf
● a geometrically decaying pacf.

```

## ACF AND PACF PLOTS OF THE ARMA MODEL :

```
In figure 1, the MA(1) has an acf that is significant for only lag 1, while the pacf declines geometrically, and is significant until lag 7. The acf at lag 1 and all of the pacfs are negative as a result of the negative coefficient in the MA generating process.

```

### `In Fig 1`

```

   1. It is a MA(1) model.

   2. It represents the relationship between an observation and  error from a moving average model by lagged observations.

   3. The equation  " yt = − 0.5ut0 + ut " means that the current value is influenced by the error term of previous value .

   4. The ACF is significant spike only for lag 1 for an MA(1) model and further it will decline.

```

## ![plot](./fig16.png)

---

### `In Fig 2`

```
   1. It is a MA(1) model.

   2. It represents the relationship between an observation and  error from a moving average model by lagged observations.

   3. The equation  " yt = − 0.5ut0 + ut " means that the current value is influenced by the error term of previous value .

   4. The ACF is significant spike only for lag 1 for an MA(1) model and further it will decline,but there is a spike in 2nd lag also which indicates that there is a strong co-relation between the values.

```

## ![plot](./fig15.png)

---

### `In Fig 3`

```
1. It is an  AR(1) model, or Autoregressive model of order 1, which is an  another type of time series model.

2. It describes the relationship between an current data point and its previous data point.

3. The given equation for the AR(1) process is
   yt = 0.9 yt0 + ut

      - yt0 is prev dp
      - ut is error term

4. A coefficient of 0.9 in the AR(1) model means that the current observation is strongly influenced by the previous observation.So as the far over the lags the relationship influence decreases.

5. For an AR(1) process, especially one with a coefficient close to 1 (like 0.9), the ACF will show a slow decline/decay.


6.In an AR(1) process, the PACF is typically significant for the first lag (lag 1) and not significant for subsequent lags.

```

## ![plot](./fig14.png)

---

### `In Fig 4`

```
1. It is an  AR(1) model, or Autoregressive model of order 1, which is an  another type of time series model.

2. It describes the relationship between an current data point and its previous data point.

3. The given equation for the AR(1) process is
   yt = 0.5 yt0 + ut

      - yt0 is prev dp
      - ut is error term

4. A coefficient of 0.5 in the AR(1) model means that the current observation is influenced by the previous observation.So as the far over the lags the relationship influence decreases.

5. For an AR(1) process, especially one with a coefficient close to 1 (like 0.5), the ACF will show a significant decline/decay.


6.In an AR(1) process, the PACF is typically significant for the first lag (lag 1) and not significant for subsequent lags.

```

## ![plot](./fig13.png)

---

### `In Fig 5`

```
1. It is an AR(1) Model.

2. The provided equation for the AR(1) process is

            `yt = −0.5yt0 + ut.`

3. The coefficient of the previous observation is -0.5, indicating that the series is negatively influenced by its past value.

4. The coefficient (0.5 in absolute terms) is farther from 1. Hence, the series will have rapid decay/decline.

5. But we can see a spike at 2nd position/lag which indicates that there is strong correlation between the lags.

6. For an AR(1) model with a coefficient of -0.5, the ACF will show an alternating pattern because of the negative coefficient.

```

## ![plot](./fig12.png)

---

### `In Fig 6`

```
1. It is an ARMA Model.

2. The given equation for the ARMA(1, 1) process is

               yt = 0.5yt0 + 0.5ut0 + ut

            - yt is predictive value
            - yt0 is previous actual value
            - ut0 is the previous error term
            - ut is the current error term

3. The coefficient of the lagged error term is also 0.5, suggesting the model is influenced by past errors.

4. Both PCAF AND ACF GRAPH WILL DECAY/DECLINE OVER THE LAGS.

```

## ![plot](./fig11.png)

---

## SELECTION OF ARMA MODEL

### 1. There are two main elements for selecting a model.

         - How the Model Fits the DATA . (Can be determined by RSS value)

         - A punishment for adding more parameter.

### 2. The R^2 value is also used for model selection.

### 3. The criteria are used with constraints on the maximum number of regressive and moving average terms are allowed.

### 4. When selecting an ARMA model for time series data, information constraints helps to choose the right complexity. They ensure the model fits the data well but doesn't overflows by becoming too complicated.

---

## ARIMA MODEL

### 1. ARIMA : AutoRegressive Integrated Moving Average

### 2. It is combination of MA(p) and AR(q).

### 3. ARIMA is a model used for time series data that might not be stationary. It involves differencing the data until it becomes stationary and then applying an ARMA model. The combined process helps in capturing trends, seasonality, and other patterns in time series data.

---

## ARIMA VS ARMA

| ARIMA                                     | ARMA                                                       |
| ----------------------------------------- | ---------------------------------------------------------- |
| Auto Regressive Integrated Moving Average | Auto Regressive Moving Average                             |
| Here AR(p) and MA(q) is Integrated        | Here AR(p) and MA(p) both of the combination is being used |
| Here Data set used is not Stationary.     | Here Data set used is Stationary.                          |
| Variance and Mean is not Constant         | Mean and Variance is not Constant                          |
| New constraints can be added here         | New Constraints cannot be added here                       |

---

## FORECASTING IN ECONOMETRICS :

1. Forecasting is basically predicting future value by past and current data .

2. Useful for financial decision which can affect in future.

3. There are two ways to do forecasting in econometrics :

   1. Econometric (structural) Forecasting : Independents variable influences dependent variables.

   2. Time Series Forecasting : Focuses on predicting future values by solely from past data.

4.Challenge with Structural Models:

      If you want to forecast a dependent variable using a structural model, you also need to forecast all the independent variables.

5.  Forecasting with Time Series vs. Structural Models:

         1. Time Series Models: Typically better for forecasting since they focus on past values to predict future ones.

         2. Structural Models: Require forecasts of all independent variables, which can be complex.

---

## WHY FORECASTING ?

- Forecasts help in making informed financial decisions.

- The better the forecast, the better financial decisions one can make.

- Applications in Finance:

        .  Predicting stock returns.
        .  Estimating house prices.
        .  Anticipating market volatility.
        .  Estimating correlations between different stock markets.
        .  Predicting loan defaults.

---

## -> Parallel Data

## -> Cross -Section Data & Cross Section Data Analysis

## -> Mean Median Mode Variance & deviation Definition and Usage of them nalysis

## -> Explanation over using a specific type of analysis for any situation/stock (for an example)

         1. we can use MA
         2. we can also use Recursive MA
         3. how many values to reject (like should take multiple of 2 or multiple of 3 ) in MA or in Recursive MA
