Feature: Validate Transaction and Customer Data

    Scenario: Validate all transactions belong to existing customers
        Given the transactions and customer tables are available
        When we fetch transactions with invalid customer_id
        Then there should be no such transactions

    Scenario: Validate no credit transaction has negative amount
        Given the transactions table is available
        When we fetch credit transactions with negative amount
        Then there should be no such records

    Scenario: Validate all transaction dates are not in future
        Given the transactions table is available
        When we fetch transactions with future dates
        Then there should be no such records

    Scenario: Validate no duplicate customer emails exist
        Given the customers table is available
        When we search for duplicate customer emails
        Then there should be no duplicates

    Scenario: Validate all mandatory fields are not null in customers table
        Given the customers table is available
        When we fetch records with null values in mandatory columns
        Then there should be no such records

    Scenario: Validate total transaction amount per customer is calculated correctly
        Given the transactions and customer tables are available
        When we aggregate transaction amount per customer
        Then the total should match expected values

    Scenario: Validate transaction type only contains allowed values
        Given the transactions table is available
        When we fetch records with invalid transaction types
        Then there should be no such records
