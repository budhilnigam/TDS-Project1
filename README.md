# TDS-Project1
## 1. Explanation of data scraping
  1. First, I extracted all the users in the city of Tokyo with over 200 followers from the endpoint https://api.github.com/search/users . Since the response can only contain upto 100 results per page so we had to iterate each page of the response.

     The query made to the endpoint was `q=type:user+location:Tokyo+followers:>200&per_page=100&page={page}` wher `page` was a number iterable to iterate each page of response.
All the response pages are written to **tokyo.txt** which was later converted to **tokyo.json** after some cleaning and modification.

  2. Now, we iterate over the json objects in the *items* property of **tokyo.json** and use the *login* property value in the endpoint https://api.github.com/users/{login} which gives the details about the user like *login, name, company, location, email, hireable, bio, public_repos, followers, following, created_at*.
 
     Similarly for fetching information upto 500 most recently pushed repositories for each user we make use the endpoint https://api.github.com/users/{login}/repos with the query:

     `sort=pushed&per_page=100&page={page}` where `page` is again an iterable since all the results won't come in a single page. This gives us details about each repository of the user like *login, full_name, created_at, stargazers_count, watches_count, language, has_projects, has_wiki, license_name*.

## 2. Interesting fact
The most interesting fact I found out after analyzing the data using the **GitHub API** was the performance of the API, if it were not for the rate limit the data acquisition from the api is quite fast for such a large amount of data, it were able to give me info of upto 500 repositories of 592 users in Tokyo in a matter of few minutes which were 66463 recors in total.

## 3. Actionable Recommendation
The use of personal access token (PAT) or fine-grained tokens are of great use in using **GitHub API** since it increases your rate limit and also ensures security by allowing you to set it's permissions.
