# Experiments used in our GandALF submission

## Instructions
Running the LTL pipeline takes some effort, as formulas must be converted from LTLf to LTL. The process for doing so is as follows:

1. Write LTLf specification (we'll use the filename spec.ltlf)
2. Run ltlfilt --from-ltlf spec.ltlf > spec.ltl
3. ltlfilt removes quotes so you need to add these to make PRISM parse the LTL spec. Also, PRISM reserves "alive" so you must replace it with another name e.g.: (!"done")
4. Run PRISM on the LTL spec and a modified MDP that, at every state, includes an action with probability 1 of transitioning to the terminal state.

(MDPs and modified MDPs may be generated by setting the value of print_LTL_game to True or False)

### Running Various experiments
Format:
```Instructions for running native pipeline```
```Instructions for running LTL pipeline```

To run with other tools (e.g., SPOT) please see the PRISM website: [http://www.prismmodelchecker.org/manual/ConfiguringPRISM/AutomataGeneration]

For Gridworld variants:
```prism grid.nm ltlf.props -ltl2datool ./hoa_mona_ltlf2dfa_for_prism -ltl2dasyntax spot```

```prism gridLTL.nm ltl.props```

For Nim:
```prism nim.nm spec.props -ltl2datool ./hoa_mona_ltlf2dfa_for_prism -ltl2dasyntax spot```

```prism nimLTL.nm specltl.props```

For Counter:
```prism game.nm spec.props -ltl2datool ./hoa_mona_ltlf2dfa_for_prism -ltl2dasyntax spot```

```prism gameLTL.nm specltl.props```

For Dining Philosophers:
```prism lr5.nm ltlf.props -ltl2datool ./hoa_mona_ltlf2dfa_for_prism -ltl2dasyntax spot```

```prism lr5_ltl.nm ltl.props```

### Help
Feel free to reach out with any questions or issues you have running the examples.

These should allow you to reproduce all experiments contained in our paper (with small modifications, e.g., changing the grid size).