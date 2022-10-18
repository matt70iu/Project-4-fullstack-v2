# Code Zone Testing

## Login/Logout

The purpose of this test is to ensre that the user can log in and out with a success message displayed.

The user is presented with the homepage which contains all posts in a list format.

![Home-page](screenshots/home-page.png)

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

The create post form also contains validation, requiring a minmium of a post title, title tag and snippet.

![New-post-validation](screenshots/new-post-validation.png)

During testing, I discovered a spelling mistake in the success message, which I have now corrected, other than that, the app behaved as expected.

## Edit a post

The purpose of this test is to confirm that a user can edit a post that they created.

A post can be edited in one of two ways.

From the homepage, the user can select Edit link attached to the post they wish to edit.

![Edit-post-home](screenshots/edit-post-home.png)
![Edit-post-home-link](screenshots/edit-post-link-home.png)

They can also select the edit link from the post/article detail page'

![Article-detail-edit](screenshots/article-detail-edit-post.png)
![Article-detail-edit-link](screenshots/article-detail-edit-post-link.png)

The user will then be presented with an Edit Post page.

![Edit-post-page-1](screenshots/edit-post-page-1.png)
![Edit-post-page-2](screenshots/edit-post-page-2.png)

The user can now make their changes to the relevent post and then click the Edit Post button at the bottom of the page.

![Edit-post-button](screenshots/edit-post-button-2.png)

The user will then be redirected to the homepage with a confirmation message that the edit was successful.

![Edit-post-success](screenshots/edit-post-success.png)

During testing, I discovered that the edit button was in a default bootstrap colour, changed colour to suit site theme.
Other than this, the app behaved as expected.

## Delete a post

The purpose of this test is to confirm that a user can delete a post that they created, while logged in.

A post can be deleted in one of two ways.

From the homepage, the user can select the delete link attached to the post they wish to delete. 

![Delete-post-home](screenshots/delete-post-home.png)
![Delete-post-home-link](screenshots/delete-post-home-link.png)

They can also choose the delete link from within the post itself.

![Article-detail-delete](screenshots/article-detail-delete.png)
![Article-detail-delete-link](screenshots/article-detail-delete-link.png)

Which ever option the user chooses, they will be directed to a Delete Post page.

![Delete-post-page](screenshots/delete-post-page.png)
![Delete-post-button](screenshots/delete-post-button.png)

The user then needs to click delete post and they will be redirected to the homepage with a message confirming successful deletion.

![Delete-success](screenshots/delete-success.png)

I can confirm after this test, that the app behaved as expected.


## Like/unlike post

The purpose of this test is to confirm that a logged in user is able to like/unlike a post.

In order for the user to like/unlike a post, they must first select the post they wish to like/unlike.

![Select-post-like/unlike](screenshots/select-post-like-unlike.png)

They will then be presented with the main post/article body.

![Article-detail-like-unlike](screenshots/article-detail-like-unlike.png)

At the bottom of the article, the user simply needs to click the like button in order to register their like.

![Like-button](screenshots/like-button.png)
![Like-button-clicked](screenshots/like-button-clicked.png)

I can confirm after this test, that the app behaved as expected.

## Comment on a post

The purpose of this test is to confirm that a user can add a comment to a post.

Within any post, the user can add a comment by clicking on the Add One... link at the bottom of the page.

![Article-detail-add-comment](screenshots/article-detail-comment.png)
![Article-detail-add-comment-link](screenshots/add-comment-link.png)

The user will then be brought to the Add Comment page.

![Add-comment-page](screenshots/add-comment-page.png)

The user can then fill out their comment and submit by clicking the Add Comment button.

![Add-comment-button](screenshots/add-comment-button.png)

They will then be brought back to the home page with a success message.

![Add-comment-success](screenshots/add-comment-success.png)

During testing, I discovered that the add comment button was still the default bootstrap colour. I have ammended the add comment template to correct this, all else went as expected.

## Create a new category

The purpose of this test is to ensure a user can create a new category when logged in.

From the homepage, the user must select Create New Category.

![Create-new-category-home](screenshots/create-new-category-home.png)
![Create-new-category-button](screenshots/create-new-category-button.png)

They will then be presented with the create new category page.

![Create-new-category-page](screenshots/create-new-category-page.png)

The user then simply needs to type a category name and then click Create New Categoey.

![Create-new-category-button-2](screenshots/create-new-category-button-2.png)

The user will then be redirected back to the homepage with a success message confirming that the new category has been added.

![New-category-success](screenshots/new-category-success-message.png)

I can confirm that the app behaved as expected after this test.

## Select a category from dropdown menu

The purpose of this test is to ensure that the homepage is filtered by the selected category that the user selects form the category dropdown menu.

![Category-dropdown](screenshots/category-drop-down.png)

I selected Python and was presented with the filtered results.

![Python-filtered-results](screenshots/python-filtered-results.png)

There was a couple of unexpected issues that came up here.

- The tags for the main article body are still showing.

![p-tags-showing](screenshots/p=tags-showing.png)

- Issue with p tags showing rectified by inserting safe tag into template.

- The user is also presented with the option to edit/delete posts which they didn't create, although when they do this, they are told the action is not permitted.

![action-not-pernitted](screenshots/action-not-permitted.png)

- I have rectified the issue with the html/<p> tags showing by adding the safe tag to the python code, so the html can be injected into the template.

- I have rectified the issue with the edit/delete options being available to users who did not create the post by adding an additional if and endif statment within the categories template.

![categories-page-bug-fixes](screenshots/categories-page-bug-fixes.png)

- The categories page is now displaying without the option to edit/delete posts which do not belong to the user, as well as no longer displaying the template html tags.

## Authentication


The purpose of this thest is to ensure that a logged in user can only access pages they are permitted to and are presented with an error, should they try to access pages for which they have not been authenicated.

- When logged in as Matthew Adams, if i attempt to acces the page to delete the post, I am presented with the below error:

![auth-testing](screenshots/auth-testing.png)

- I can confirm after this test, that the app behaved as expected.





















