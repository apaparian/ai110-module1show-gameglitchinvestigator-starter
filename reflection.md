# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | | Submitting a guess gives feedback on whether the number is too high or too low | Feedback is always "Go LOWER!"
| | | | | New Game clears the feedback window | "Game over" persists and guesses are no longer accepted
| | | | | Difficutly level dropwdown updates the range | Range remains unchanged
| | | | | Show hint toggles the hint | Show hit toggles off but not on until next hint
| | | | | Submit gives feedback on each guess | Guesses seem to require two clicks of submit after the first attempt

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

Claude Code
I accepted a change that limited its edits to casting the secret as an int
I accepted a second change that swapped the Lower/Higher messages
I rejected a change that overwrote additional method defintions and commented explanations in logic_utils.py
I rejected a change that attempted to remove the existing try and except blocks that convert the guess string if needed

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I verified the changes with pytest first, and then in browser
The code didn't have any output, only verified that all tests passed
AI helped me understand why pytest was not importing modules

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
