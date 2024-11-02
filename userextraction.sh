#!/bin/bash

source .env

# Set the initial page number
PAGE=1

# Empty or create a.txt to store all results
> tokyo.txt

# Loop through each page of results until an empty result is returned
while true; do
  echo "Fetching page $PAGE..."

  # Fetch users for the current page
  RESPONSE=$(curl -L -H "Authorization: Bearer $GITHUB_TOKEN" \
      -H "Accept: application/vnd.github+json" \
      "https://api.github.com/search/users?q=type:user+location:Tokyo+followers:>200&per_page=100&page=$PAGE")

  # Append the response to a.txt
  echo "$RESPONSE" >> tokyo.txt

  # Check if the response contains users, otherwise break the loop
  if [[ "$RESPONSE" == *"\"total_count\": 0"* || "$RESPONSE" == "[]" ]]; then
    echo "No more users found."
    break
  fi

  # Increment the page number
  PAGE=$((PAGE + 1))

  # Optional: add a short delay to avoid hitting rate limits
  sleep 1
done

echo "All users fetched and saved to tokyo.txt."