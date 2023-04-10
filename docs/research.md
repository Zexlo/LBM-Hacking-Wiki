---
hide:
  - toc
---

<figure markdown> 
# Research
</figure>

!!! warn "Note"
	This page should be considered as a work in progress. Generally, this should help with understanding how various parts of the game work, and that understanding may not always be 100% correct.

##Observers
One of the things that people seem to have the most trouble understanding is Observers, so here is a small rundown:

Observers are essentially "mini-programs" that constantly ask the game questions about what the current state of the game is. (Eg: "Are all the ghosts in this wave captured yet?", "Is flag 23 turned on?"). 
Think of them like an invisible eye that consistently monitors what condition needs to be met so that something can be done.

They are used for everything from making ghosts spawn to making the lights turn on when you've captured all the ghosts in a room.

Let's look at an example:

!!! example " diagram"

	``` mermaid
	graph LR
	A[Start] --> B{All ghosts caught?};
	B -->|No| C[Go back to start];
	C --> A;
	B ---->|Yes| E[Turn on lights];
	```

	
1. The observer will ask the game a "question" (Eg: "Have all the candles in this room been blown out?") - In programming terms these "questions" are known as Conditions.
2. The game itself will reply with an "answer" of either True (Yes) or False (No). - In programming terms these "answers" are known as bool's / Booleans.
3. If the reply from the game is True (Yes) then the observer will do something - More accurately, it will do whatever is specified in the observer's do_type field.

By using the cond_string_arg0 and string_arg0 fields in the observers you can link a multiple observers to activate after just one observer activates,

this will allow you to do more than just one thing after a ghost wave has been defeated for example.

You could however also create a "observer chain" to do this; "Is all the ghosts in this wave captured yet?" (True) -> Light Up The Room (True) -> Unlock The Doors (True) -> Spawn Chest (True)

"There's multiple ways to Rome" - You can get similar results with different approaches, we recommend you choose one that you find the most understandable / easy to use.

And that is essentially how all observers in the game work.

Now go experiment! - That's the best way of learning! :)
