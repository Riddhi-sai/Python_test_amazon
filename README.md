# Python_test_amazon
## Test Results: Search Product on Amazon India

*Test Case: Search and product purchase through https://www.amazon.in/*

*Test Scenario 1:* Search for "waterbottle for office" on Amazon India

*Steps:*
1. Open Amazon India website.
2. Enter "waterbottle for office" in the search box.
3. Submit the search.

*Expected Results:*
- The page title should include "waterbottle for office".

*Actual Results:*
- The page title included "waterbottle for office".
- Search results were displayed correctly.

*Status:* Passed


*Test Scenario 2 :* Filtering the search results

*precondition:* The user is on the desired product listing page.

*Steps:*
1. Filter the products list based on the price filter. 
2. Select the minimum = 300 and maximum = 1000 price range. 
3. Submit the Range.

*Expected Results:*
- The page results should only include "waterbottle for office" of the price range Rs. 300 - 1000 .

*Actual Results:*
- The page result included only products of the price range Rs. 400-1000. 
- Search results were displayed correctly.

*Status:* Passed



*Test Scenario 3 :* Adding a product to a shopping cart

*precondition:* The user is on the  filtered desired product listing page.


*Steps:*
1. Select a product of desired size/color.
2. Add the product to the cart. 

*Expected Results:*
- The desired product should be added in the shopping cart.

*Actual Results:*
- The desired product is added in the shopping cart. 

*Status:* Passed



*Test Scenario 4 :* Proceeding to Checkout

*precondition:* The user has added a desired product in the cart.


*Steps:*
1.Add desired products to the shopping cart.

*Expected Results:*
- The desired product should be added in the shopping cart.

*Actual Results:*
- The desired product is added in the shopping cart. 

*Status:* Passed


*Test Scenario 5 :* Filling out the personal detail and payment details.
 
*precondition:* The user has added a desired product in the cart.

*Steps:*
1. Add desired products to the shopping cart.
2. Select proceed to buy. 
3. Fill in the buyer information.
4. Fill in the payment details. 

*Expected Results:*
- The  user information and the payments details to be added. 

*Actual Results:*
- Not able to detect the elements in the card details section as it is in the Shadow DOM structure. 

*Status:* Failed

