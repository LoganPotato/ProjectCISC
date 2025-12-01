---
title: Number Targetter
emoji: 🎯
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "6.0.1"
app_file: app.py
pinned: false
---

## Number Targetter App
- Chose to use a Linear Search method along with the sort built in function provided by python.
- I chose to use the linear search method because it is what I am most comfortable with. It's the simplest and allows me to work on a list that is not sorted.
  to show every step of the code when checking each element within the list which helps me since I chose to display all the steps it peforms. It is beginner friendly
  and because I am only search through 10-15 elements the linear search is fast enough to iterate through all of the elements.
- I chose to use the python built in function because it is just the simplest and time efficient method to sort. It also helps to keep my code simple and readable
  whereas if I used another sort method it may be a longer piece of code and possibly more errors to encounter. Using the built in function also helped me make it easier
  to peform displays of an image, sound of when a button is clicked.
  
## Demo
- https://streamable.com/njeuhj

## Problem Breakdown & Computational Thinking
## Decomposition 
- Generate a random list of integers
- Sort the list in ascending order
- Take the users input for desired target number
- Check users input to see if it is valid
- Linear search to see if the target number is present in the list
- Each iterarion we keep record each search/range step to then print in a cell
- Display the final result telling us if the target number was found, if it wasn't found or if the user's input was invalid

## Pattern Recognition
- The program repeatedly compared each element of the list with the target number give by the user
- Recoreds the steps for the search/range snapshots for each iteration
- Stops all checks once the target number is found

## Abstraction
- The user only sees: The sorted list, each iterations comparison side by side, snapshots, the final result and an bullseye image for when the target is found
- Iternal loops, tracking the indexs, Audio trigger on the Generate button is all hidden

## Algorithm Design
- Generate a list and sort it in ascending order
- Take the target input
- Check if proper input is given
- Iterate through the list
- Recored each iteration comparisons
- Check if the target number is found
- Display result 

## Steps to Run
1. Open the app in a browser using Hugging Space
2. Click "Generate List" to create a random list of numbers
3. Enter a positive whole number to search for
4. Click "Search" to see all of the steps that the code performs and if the target is in the list

## Hugging Face Link
- https://huggingface.co/spaces/LoganPotato/NumberTargeter
  
## Author & Acknowledgment
- Logan
- AI Disclaimer: ChatGPT was used to aid me in creating the application
- Gradio