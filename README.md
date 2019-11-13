# Felipe Spoliante Litran Portfolio - Oui Chef!

## About

<img src="static/images/desktop-view.gif" width="300">

This application (app) consists of a website where users can find recipes from the best cuisines in the world with a step-by-step decription on how make them at home.

#### Functionality
The application consists of 4 main sections providing the user with the possibility of:
1. Homepage: Find the most popular recipes which are displayed in the homepage
2. Find Recipe: Fitler throught a variety of recipes from France, italy, Brawil among others
3. Create Recipe: Share his cooking skills by posting a recipe on Oui Chef!
4. Sign Up & Login: Like, dislike and post his opinions on the recipes of Oui Chef!

#### Goal

The application is designed to users who often or acasssionaly buy look for a recipe based on his needs and preferences such as recipe origin, skill level, preparation time and serving size.

#### Images

<img src="static/images/desktop-view.gif" width="300">

## UX

#### Layout
 
- The Multiple Page Apps (MPA) design was due to the complexity and CRUD charactheristic of the app where user can manipulate data by creating, reading, updating, and deleting interactions. Therefore, having an user-friendly design was needed in order to make it easy for users to create, like, dislike, delete and update new or existing recipes..
- The database selected was MongoDB Atals, where all CRUD operations are handled in an effective and fast way. 
- The app is designed for users to interact with each other by sharing their cooking experiences and opinions.

#### Important Note

- It is important to emphasize that the application heavily relies on the users when it comes to the expansion of its database. Its main goal is to create a common and friendly place where people can share their recipes and learn about different cuisines.

#### Colour Scheme

- Taking into account the main theme of the app, the idea is to have the looks of a modern kitchen by applying grey and white resembling a fridge, stove, oven, kitchen cabinets and table.
- [Adobe Color](https://color.adobe.com/create/color-wheel/) provided me with complementary, compound, analogous, and monochromatic shades of grey and white.
- Color
    - ![#404040](https://placehold.it/15/404040/000000?text=+) `#404040` colour description: Grey.
    - ![#fffff9](https://placehold.it/15/fffff9/000000?text=+) `#fffff9` colour description: White. 
    - ![#ffab40](https://placehold.it/15/ffab40/000000?text=+) `#ffab40` colour description: Orange. 

#### Font

- The font used was Roboto as I decided to apply [Materialize's theme](https://materializecss.com/about.html/).

## Technologies Used

#### Languages Frameworks Tools

- HTML5
- CSS3
- Python3
- AWS-Cloud9
- MongoDB Atlas
- Heroku
- jQuery 3.2.1
- Font Awesome - v4.7.0

#### Other Resources

- [Materialize](https://materializecss.com/about.html/)
- [Adobe Color](https://color.adobe.com/create/color-wheel/)
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)

## Features

#### Existing Features

As the applications consists of a MPA, I applied an easy navigation where the user can clearly see where to create, search, or look for a recipe:

- Find Recipe: In the Find Recipe section, users can select and filter the recipes by country of origin, difficulty, preparation time. and serving size. In case he/she is not satisfied with the filtering chosen, they can reset the selected criteria in order to fit thie needs. 
- Create Recipe: In the Create Recipe section the user has the possibility to create and update existing recipes.
- Like & Dislike: When accessing a recipe page, users can like or dislike the recipe. Users must be logged in to like/dislike a recipe.
- Comment Section: Once logged in, users can leave a comment on a recipe's page.

#### Features Left to Implement

- I wish to implement a profile page for each user. In this way, users can share their cooking preferences in a detailed manner.
- A feature which I wil soon implement is the possibility for user to upload videos when cooking a recipe.
- The possibility to sign up using a facebook or gmail is also a feature which will be implement in the application.

## Syntax Testing

Resources & Tools Used for Testing

#### HTML
-[W3 HTML Validator](https://validator.w3.org/)

#### CSS
-[W3 CSS Validator](https://jigsaw.w3.org/css-validator/)

#### Devices Tested

- Responsive design has been applied to all kinds of devices including small, medium, and large phones as well as tablets, laptop, and desktop views. 

#### Testing Criteria

- In this session, testing user interface was done by running multiple combinations using all four filtering types aiming to have the expected outcome. One example of criteria set is shown below:
    1. Country of Origin: Brazilian
    2. Variety: Bordeaux Style Red Blend
    3. Points: Excellent Above 95
    4. Price: Above $100

#### Testing Outcome

- The results came out as expected showing all titles corresponding to the criteria selected. 
- All external links in the header section worked properly.
- All external links in the footer section worked as expected.
- In the suggestion section, all wine cards successfully redirected the user to a new tab and third-party website where the titles can be purchased.

#### Issues During Testing Sessions

- The data had to refined multiple times due to a recurring error: Error: Invalid value for attribute transform="translate(NaN,NaN)"
- The error was due to blank values and special characters present in the dataset

## Deployment

This website has been hosted on GitHub pages, and it is deployed directly from the master branch. Therefore, once a new commit has been done the changes will automatically take effect on the master branch. 

Additionally, if you wish to run the code locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/Litran1990/InteractiveFrontEndMilestoneProject` into your terminal. In order to cut ties with this GitHub repository, type `git remote rm origin` into the terminal.


## Credits

#### Dataset
- The data used for this project was obtained from [Kaggle](https://www.kaggle.com/zynicide/wine-reviews)

#### Media
- The photos used in this project were obtained from Google Images.

#### Acknowledgements

- I received inspiration for this project from Code Institute's Interactive Front End - Mini Project.
    