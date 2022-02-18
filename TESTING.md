<h1 align="center">Testing</h1>

---

## Index 
- <a href="#manual-testing">1. Manual testing</a>
    - <a href="#visitor-goals">1.1 Visitor goals</a>
    - <a href="#unregistered-user-goals">1.2 First-time visitors/unregistered user goals</a>
    - <a href="#registered-user-goals">1.3 Registered/authenticated user goals</a>
    - <a href="#consumer-goals">1.4 Consumer goals</a>
    - <a href="#admin-goals">1.5 Admin goals</a>
- <a href="#automated-testing">2. Automated testing</a>
- <a href="#validators">3. Code validators</a>
- <a href="#responsiveness">4. Responsiveness</a>
- <a href="#browser-compatibility">5. Browser compability</a>
- <a href="#other">6. Other</a>
- <a href="#bugs">7. Bugs</a>
- <a href="#future-testing">8. Future testing</a>

[Go to README.md file](README.md).
---

<span id="manual-testing"></span>

## 1. Manual testing

**All User Stories are tested with manual testing.**



<span id="visitor-goals"></span>
### 1.1 Visitor goals
1. As a visitor, I want to get information about different furniture and materials.
    **Testing**
    - The website is offering a broad list of products of different materials.
    - All products are having descriptions and information if the products are in stock or not.
    **Result:** Test passed
2. Purchase the furniture on the website in a safe and secure way
    **Testing**
    - verify that the text and images(Order summary) are displayed correctly
    - try to put an incorrect information (e.g. email without @)
    - in the Payment section enter the testing 4242 4242 4242 4242 card number, any expiration date in future and any CVC, and then click on the "Proceed to payment" button (this was also checked on Stripe Dashbord to see if the order was created)
    - try to enter different and incomplete card numbers, the expiration date in the past to check the error messages
    - temporary comment out the code line form.submit(); in stripe.js file and then try to submit the form clicking the "Proceed to payment" button. After that check the Stripe Dashboard and also Order model in Admin panel to make sure the order was created via webhooks and was saved to the database.
    **Result:** Test passed
    - order summary displays the order correctly
    - if the incorrect or incomplete card details were entered, the error messages are displayed as expected under the Payment field.
    - testing 4242 4242 4242 4242 card number leads to the successfull payment, that was confirmed in the Stripe Dashboard.
    - when the order was created via webhooks (after commenting out form.submit(); in stripe.js), the payment was successfully proceeded and the order was saved in the database
    - after the valid form was submitted, the confirmation email was recieved in the email provided with all the correct order info. As well as that, the checkout page renders showing the order summary.
    - when the order was completed by the logged in user in the checkout success page, the "View full order history" button redirects to the Order history page. "Keep shopping" button is displayed for both non-logged in and logged in users and redirects to the products page
    
<span id="unregistered-user-goals"></span>

### 1.2 First-time visitors/unregistered user goals

3. As a visitor  I want to access the website from any device, to be able to use it anytime, anywhere.
    **Testing**
    - The visitor can visite the website on any device. The website is designed for computer, mobile and tablet. The test for the responsiveness with different devices can be found
    <a href="#responsiveness">here</a>
    **Result:** Test passed
4. As a visitor, I want to navigate easily through the website, to be able to view all products.
    **Testing**
    - A visitor can navigate throug the website with the navbar on top of the website and through the footer. There is a hamburger menu for mobile visitors, where they can easily can go to every relevant page.
    - The main navigation is through the navbar and contains the following: 
        - Search functionality, where visitors can search for products. The search functionality is based on the title or descriptin of a product.
        - Login and Register pages
        - The shopping bag icon is a link to the shopping bag and you see the amount of dollars that are in your shoppingbag. 
        - Links to all categories of furniture and special deals.
        - Easy to see a banner with the latest deal
        - Links to information about how to buy. Information for unregistered and registered user.
        - Link to the contact page, where visitors can contect the owners of the website. 
    **Result:** Test passed. All links are working.The search functionality and the profile functionality with showing the right links whether a visitor is logged in or logged out are working correct.
5. As a visitor, I want to contact the owners of the website,  to be able to easily ask a question.
    **Testing**
    - The contact page on the nav bar on the website. 
    - There is a contact page where visitors can send their questions. 
    - On the contact page stands contact information such as the email address and phonenumber. 
    **Result:** Test passed. Visitors can fill in the form with any questions or can contact the company through email of phone.
7. As a visitor, I want to navigate easily through the website, to be able to view a specific category of products(sofas, chairs, tables)
    **Testing**
    - The products page gives an overview of all products. All products are standing on this page. 
    - The page shows a back to top button in case the website has a lot of products and the visitor has scrolled down a lot.
    - There is also a navigation of the products page for the different category. Visitors can sort the products on all, sofas, chairs and tables, deals, news.
    - Visitors can sort the products based on price from low to high or from high to low. 
    - And visitors can sort the products based on alphabet from A - Z or Z - A
    **Result** Test passed. All products are on the products page, the back to top button works and the category links are showing the right results.
8. As a visitor, I want to navigate easily through the website, to be able to view details for a specific product.
    **Testing**
    - Visitors can visit the product detail page by clicking on the image of the product. 
    - The product detail page will shows the following information: name, price, category, if the product is in stock, ratings, link to reviews and description. 
    - Visitors can buy the product and set the quantity of the product if the product is in stock, add to bag button and back to all products list with a keep shopping button.
    **Result:** Test passed: All product information is on the detail page works good.
9.  As a visitor, I want to navigate easily through the website, to be able to quickly identify deals, special offers.
    **Testing**
    Visistor can click on a sepcial offers category and find all websites deals and all new products.
    **Result:** Test passed
10. As a visitor, I want to easily find products rating, to be able to se customers experiences and opinions about the products.
    **Testing**
    Visitors are able to see ratins for every product on the list with all products.
    The reviews from the buyers are visible on the product detail page 
    **Result:** Test passed

<span id="registered-user-goals"></span>
### 1.3 Registered/authenticated user goals

11. As a registered user, I want to create an account, to be able to log in and logout.
    **Testing**
    - The Registered user can login and logout through the links in the navbar.
    - On the login page, when "Forgot password" link is clicked, a user is redirected to the password reset page and asked for their email address, then an email is sent with a link to reset password. After entering new password twice, the password is reset and user can login with a new password 
    - The Registered user has a logout button.
    - when logout link in the navbar is clicked, the login page opens asking for confirmation to logout, when it is confirmed, the user is logged out and the session is stopped
    - An registered user has a change password page in My Account on the navbar where is able to change the password if needed and then a button with back to profile that can redirect the registered user too.
    - the login and registration page are only available to unregistered users
    - **Result:** Test passed. The Registered user can login, logout easily and reset the password. 
12. As a registered user, I want to receive an email confirmation after registering in my new account, to be able to authenticat my self.
     **Testing**
    - The Registered user will receive an confirm email to authentificate him self on the website. 
    - The Registered user has a logout button.
    **Result:** Test passed.
13. As a registered user, I want to edit my profile, to be able to view my profile updated.
    **Testing**
    - Registered user has a link in My Account on the navbar where my profile page can be found.
    - Registered user is able to fill in a details form and click on the "Update information" button
    **Result:** Test passed.
14. As a registered user, I want to edit my profile, to be able to access my order history.
    **Testing**
    - Registered user has a link in My Account on the navbar where order history can be found.
    - Registered user is able see the following details about the purchases: order number, date, Item and total price.
    **Result:** Test passed.
15. As a registered user, I want to easily recover my password if forget it, to be able to use my       account.
    **Testing**
    - On the login page, when "Forgot password" link is clicked, a user is redirected to the password reset page and asked for their email address, then an email is sent with a link to reset password. After entering new password twice, the password is reset and user can login with a new password.
    **Result:** Test passed. The password change functionality is working

<span id="consumer-goals"></span>
### 1.4 Consumer goals
16. As a consumer, I want to easily select the product that I wish, to be able to purchase it.
17. As a consumer, I want to view my bag to be purchased, to be able to ajust the quantity of the product.
18. As a consumer, I want to view my bag to be purchased, to be able to see the total price and shipping costs of my order.
19. As a consumer, I want to easily enter my payment information, to be able to purchase a product.
20. As a consumer, I want to pay with a card in a safe and secure way, to be able to know that my payment was successfull.
21. As a consumer, I want to receive a confirmation email of the order, to be able know that the order
    **Testing**
    - verify that the text and images of the added items are displayed correctly
    - click on the "Continue shopping" link at the top of the page
    - try to update the item quantity
    - try to manually enter invalid quantity (negative, decimal dot)
    - click on the "Checkout" button
    - remove all the items and check the empty cart, click on the "keep shopping" button
    - the safety of payment is texted to both unregistered and unregistered users.
    **Result:** Test passed.
    - information abour all the items is displayed correctly on different screens
    - clicking "keep shopping" link leads to the products page
    - update functionality works well for products(the bug during the testing was found and fixed, see  bugs paragraph below)
    - clicking "Checkout" button redirects to the Checkout page
    - toast messages are always displayed as expected after each update/remove action
    - if the cart is empty, the paragraph informs a user that the cart is empty; clicking "keep shopping" button redirects to the products page
<span id="admin-goals"></span>
### 1.5 Admin goals
22. As a website owner, I want to add, edit/update and delete products to be able to keep the site up to date with products portofolio.
    **Testing**
    - The admin can add a product by clicking on admin in navbar. The admin gets a form to fill in and can add a product to the website. 
    - The admin can edit a product by clicking on the product detail page of the product and click on the edit link. The admin gets a filled in form with the details of the product. The details of the product can be updated and be saved. 
    - The admin can remove products by clicking on the product detail page of the product and click on the delete link. A notification will show if the admin is sure to delete the item. The product is deleted by clicking on delete again. 
    **Results:** Test passed. The add, edit and delete functionallity is working as it should be.

<span id="automated-testing"></span>

## 2. Automated testing

### Testing apps
Automated testing is used to support the manual testing. The manual testing helped by testing mostly the back-end code with views, models and forms.
The unit tests can be found in the apps in the `test_models.py`, `test_views.py` and  `test_forms.py` files.

The tests provide little coverage due to time constraints. In the future, with more time and knowledge about Django testing, I would like to improve the coverage to a minimum of 80%.

<span id="validators"></span>

## 3. Validators

 - **[HTML Validator](https://validator.w3.org/):** No big errors to show.
    - I tested the HTML code by running my server locally and used view page source. This code I passed through the validator.

    **The following errors/warnings are showing**
    - Error ```Element li not allowed as child of element nav in this context. (Suppressing further errors from this subtree.)```. This is due to the way the menu is constructed. Due to time constraints, I didn't fix this error.
    - Warning: ```the type attribute is unnecessary for JavaScript resources```.

    **Result:** The rest of the code passed and there were no errors.

- **[CSS Validator](https://jigsaw.w3.org/css-validator/):** No errors found.

    **Results:**
    - base.css: no errors found
    - checkout.css: no errors found
    - profiles.css: no errors found
    - products.css: no errors found


- **[JS Hint](https://jshint.com/):** No errors found.
    
    **Results:**
    - no errors found
- **[Python validator | PEP8](http://pep8online.com/):** No errors found

    **Results:** No errors found!

---

<span id="responsiveness"></span>

## 4. Responsiveness 
- Responsiveness of the site is tested with [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).
- The site is tested on the following devices: 
    - Desktop: 1024px, 1366px, 1440px, 1600px and 1680px. 
    - Mobile & Tablet: Galaxy S5, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 plus, iPhone x, iPad and  iPad Pro

---

<span id="browser-compatibility"></span>

## 5. Browser compatibility
- No issues were found.

--- 

<span id="other"></span>

### 6. Other

- During developing the website, the debugger in `settings.py` was set to `debug=True`. The **debugger** showed errors and allowed me to find the errors quickly and fix them.
- Custom error pages for errors 404 and 500 are showing up in the same design as the website. 
- Url access/security was tested. The results: 
    - Pages that do not exist are headed to a 404 page. 
    - Users who visit pages that require login while the user is not logged in will be redirected to the login page.
    - Users who want to visit superuser access pages are getting redirected to the login page.

--- 

<span id="bugs"></span>

## 7. Bugs 

1. An error was found in the following piece of code:
bag/views.py:
```
quantity = int(request.POST.get('quantity'))
```
Whenever the user entered a quantity as a decimal number (ex 1.5), the page crashed with a 500 error due to converting the string to int.

I solved this error by enclosing the line of code between a try/except clause, as in the below example:

bag/views.py:
```
    try:
        quantity = int(request.POST.get('quantity'))
    except ValueError:
        messages.error(request, f'Invalid quantity!')
        return redirect(reverse('view_bag'))    
```
After that, the error disappeared.

Further, I enhanced the client side validation by not allowing a decimal dot in the input, using the solutions on the following sites:
- https://stackoverflow.com/a/15472787
- https://stackoverflow.com/a/47600422
- https://stackoverflow.com/a/455634

---

<span id="future-testing"></span>

## 8. Future testing 

Testing is a big part that has to be done after you created the project. In the future, with more time and knowlegde, I would like to impove testing and make the quality of the project better. 

I would like to improve the automated testing by testing the apps looking at `views`, `models`, and `forms`. My coverage at this moment is quite low and I would like to impove this to a minimum of 80%.

---

[Go to README.md file](README.md).