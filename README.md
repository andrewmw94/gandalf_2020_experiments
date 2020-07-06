# Experiments used in our GandALF submission

## Instructions
Running the LTL pipeline takes some effort, as formulas must be converted from LTLf to LTL. The process for doing so is as follows:

1. Write LTLf specification (we'll use the filename spec.ltlf)
2. Run ltlfilt --from-ltlf spec.ltlf > spec.ltl
3. ltlfilt removes quotes so you need to add these to make PRISM parse the LTL spec. Also, PRISM reserves "alive" so you must replace it with another name e.g.: (!"done")
4. Run PRISM on the LTL spec and a modified MDP that, at every state, includes an action with probability 1 of transitioning to the terminal state.

### Help
Feel free to reach out with any questions or issues you have running the examples.