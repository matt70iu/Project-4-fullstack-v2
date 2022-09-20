# Code Zone Testing

## Login/Logout

The purpose of this test is to ensre that the user can log in and out with a success message displayed.

The user is presented with the homepage which contains all posts in a list format.

![Home-page](screenshots/testing/homepage.png)

To login, the user must select the login button.

![Login-button](screenshots/login-button.png)

They will then be asked to enter their username and password.

![Login-screen](screenshots/login-screen.png)

After entering the required info, they must then click the login button.

![Login-button-2](screenshots/login-button-2.png)

If all credentials are correct, a success message will confirm to the user that they are now logged in.

![Login-success](screenshots/login-success.png)

The homepage now gives the user the option to filter by categoey, create a new post, or create a new categoey.

![Logged-in-homepage](screenshots/logged-in-homepage.png)

The logged in user is also displayed with a dropdown menu in the top right of the page, which contains the option to logout.

![Profile-logout-menu](screenshots/profile-logout-menu.png)

The user simply needs to click logout and they will be greeted with a logout success message and be brought back to the homepage.

![Logout-success](screenshots/logout-success.png)

If a user attempts to enter invalid details at the login screen, they are also presented with an error message.

![Invalid-details](screenshots/invalid-login.png)

I can confirm after this test, that the app has behaved as expected.



## Register New User

The purpose of this test is to ensure that a new user can register a new account and then complete a successful login.

From the homepage, the user must click on register to create a new account.

![Register-button](screenshots/register-button.png)

They will then be presented with a registration page.

![Register-page-1](screenshots/register-1.png)
![Register-page-2](screenshots/register-2.png)

Once the user has filled out all the required details, they will be redirected back to the login page, with a message confirming successful registrtion and requesting that they log in.

![Account-success-login](screenshots/account-success.png)

The registration page also contains built in validation, which will not let the user proceed if they enter an invalid email or password for example.

![registration-validation](screenshots/registration-validation.png)

I can confirm after this test, that the app has behaved as expected.


## Create New Post

The purpose of this test is to ensure that a user can add a new post to the blog.

In order to create a new post, the user must first be logged in. They must then click on the Create New Post button on the homepage.

![Create-new-post-button](screenshots/create-new-post-button.png)

They will then be presented with the Create New Post page

![Create-new-post-page-1](screenshots/create-new-post-page-1.png)
![Create-new-post-page-2](screenshots/create-new-post-page-2.png)

Once the user has filled out their post, addming any images etc if needed, they must then click on the Create New Post button.

![Create-new-post-button](screenshots/create-new-post-button-2.png)

The user will then be redirected back to the home page with a success message.

![New-post-created](screenshots/new-post-has-been-created.png)

During testing, I discovered a spelling mistake in the success message, which I have now corrected, other than that, the app behaved as expected.














