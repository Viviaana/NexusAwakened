# NexusAwakened

This is the first project we did using Python, it was a group project built with 3 people, one doing the coding and another writing the story and completing the planning stages.
We used Trello and draw.io to make the plans and assign the work.

## Trello Board
https://trello.com/b/pVSz6OX5/cn-game-board

##Planning process

The story was written step by step in a flowchart to create the different levels and rooms of the game allowing us to plan for certain story elements and add in ways to end the game early or add additional elements in.
This was amended as the project continued and we learned more so we could add complicated methods. For example we originally had a room that would have an attack sequence, you could choose to fight or run and the outcome was always the same. 
I added a random number generator to this with more story options so the outcome of the choice to defend yourself would be different each time.

## Story

Set in a seemingly desert space shuttle, the player wakes to find themselves surrounded by the bodies of fellow crew members, the aim is to work through different rooms to piece together what happened. Originally the ending just sent out an SOS but with only 1 survivor the stakes didn't seem very high so I added a quarantine section to the final room including other survivors to make the final puzzle seem more worth it.

## Gameplay

We simplified it to just giving the user a few choices, either yes or no or selecting a letter, this eliminated potential for the user to break the game by entering different things, only specified options work, any other input will loop the question. the beginning is a linear story but once reaching the main area of the ship there was more choice in how to proceed, this meant a lot of fail-safes had to be added so events wouldn't repeat and players always had somewhere to go, with some rooms doing nothing the first time but later having something added when you visited another room.

## Testing

At first this was just done by running the code after each section was added, testing out invalid inputs and ensuring each option lead to the correct part of the story. We also had people outside the process play through once it was complete just to make sure it made sense and was easy to follow, as well as looking out for anything additional we hadn't considered.
