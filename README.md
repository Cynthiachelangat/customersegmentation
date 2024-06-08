# **Customer Segmentation Analysis for Credit Card Users: Enhancing Marketing Strategies through Behavioral Insights**

## Project Overview

In the highly competitive financial services sector, particularly in credit card services, understanding customer behavior is crucial for developing targeted marketing strategies. This project focuses on developing a customer segmentation model for a bank based on the usage behavior of credit card holders. The insights derived from this model will help in tailoring marketing strategies, improving customer retention, and identifying potential areas for product development.

## Problem Statement

The objective of this project is to create a customer segmentation model based on the behavioral data of approximately 9,000 active credit card holders over the past six months. By analyzing various behavioral metrics, we aim to identify distinct customer segments that exhibit similar usage patterns. These segments will be used to design personalized marketing campaigns and strategies to enhance customer engagement and profitability.

Key questions to address include:
- What are the main behavioral patterns among credit card holders?
- How can these patterns be grouped into distinct customer segments?
- What characteristics define each segment?
- How can these segments be leveraged to improve marketing strategies?

## Data Understanding

The dataset comprises 18 behavioral variables collected at the customer level, providing a comprehensive view of credit card usage over the last six months. Below is a summary of the key variables in the dataset:

1. **CUST_ID:** Unique identifier for each credit card holder (Categorical).
2. **BALANCE:** Remaining balance amount in the account.
3. **BALANCE_FREQUENCY:** Frequency of balance updates, scored between 0 and 1 (1 = frequently updated).
4. **PURCHASES:** Total amount of purchases made from the account.
5. **ONEOFF_PURCHASES:** Maximum amount of a single purchase transaction.
6. **INSTALLMENTS_PURCHASES:** Total amount of purchases made in installments.
7. **CASH_ADVANCE:** Total cash advance amount taken by the user.
8. **PURCHASES_FREQUENCY:** Frequency of purchases, scored between 0 and 1 (1 = frequently purchased).
9. **ONEOFF_PURCHASES_FREQUENCY:** Frequency of one-off purchases, scored between 0 and 1 (1 = frequently purchased).
10. **PURCHASES_INSTALLMENTS_FREQUENCY:** Frequency of installment purchases, scored between 0 and 1 (1 = frequently done).
11. **CASH_ADVANCE_FREQUENCY:** Frequency of cash advances, scored between 0 and 1 (1 = frequently done).
12. **CASH_ADVANCE_TRX:** Number of transactions made with cash advances.
13. **PURCHASES_TRX:** Number of purchase transactions made.
14. **CREDIT_LIMIT:** Credit limit assigned to the user.
15. **PAYMENTS:** Total amount of payments made by the user.
16. **MINIMUM_PAYMENTS:** Minimum payments made by the user.
17. **PRC_FULL_PAYMENT:** Percentage of full payment made by the user.
18. **TENURE:** Duration of credit card usage by the user.

## Project Structure

- **data/**: Contains the dataset used for the analysis.
- **notebooks/**: Jupyter notebooks used for data exploration, preprocessing, and modeling.
- **models/**: Saved models and scalers.
- **app/**: Flask application for deploying the model.
- **client/**: React application for the front-end.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Node.js and npm

### Installation

1. Clone the repository
    ```sh
    git clone https://github.com/Cynthiachelangat/customer-segmentation.git
    cd customer-segmentation
    ```

2. Install Python dependencies
    ```sh
    pip install -r requirements.txt
    ```

3. Install React dependencies
    ```sh
    cd client
    npm install
    cd ..
    ```

### Usage

1. Preprocess the data and train the model using the notebooks in the `notebooks/` directory.
2. Save the trained model and scaler.
3. Start the Flask application
    ```sh
    cd app
    python app.py
    ```

4. Start the React application
    ```sh
    cd client
    npm start
    ```

## Results

### Cluster Characteristics

**Cluster 0:**

Spending Behavior: High-spending customers.

This cluster consists of high-spending, frequent buyers who manage large balances and have high credit limits. They often make significant payments, indicating strong financial activity.

**Cluster 1:**

Spending Behavior: Moderate-spending customers.

This cluster includes customers who spend moderately and prefer installment payments. They have moderate credit limits and tend to manage their balances conservatively.

**Cluster 2:**

Spending Behavior: Low purchase activity but high cash advances.

This cluster represents customers who rely heavily on cash advances, maintain high balances, and make fewer purchases. They tend to make high minimum payments but rarely pay off their balances in full.

**Cluster 3:**

Spending Behavior: Low-spending customers.

This cluster includes low-spending customers who make few purchases and rely moderately on cash advances. They have low credit limits and low payments, indicating minimal financial activity.

### Strategy Formulation Recommendation

**Cluster 0 (High-Spending Customers):**

- Premium Loyalty Program: Provide exclusive access to new products, higher credit limits, and special rewards for frequent purchases.
- Personalized Offers: Use purchase history to suggest high-value products.

**Cluster 1 (Moderate-Spending Customers):**

- Installment Plans: Promote installment-based payment plans to encourage higher spending.
- Engagement Campaigns: Offer moderate rewards for increased spending and frequency of purchases.

**Cluster 2 (Cash Advance Dependent Customers):**

- Financial Education: Offer educational content on managing credit and reducing dependency on cash advances.
- Lower-Interest Products: Introduce products with lower interest rates to shift away from high cash advance usage.

**Cluster 3 (Low-Spending Customers):**

- Discount Programs: Provide discounts and cashback offers to incentivize spending.
- Retention Campaigns: Focus on engagement strategies to maintain and increase customer activity.

