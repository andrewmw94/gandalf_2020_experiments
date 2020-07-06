prism minex1.nm -pf "Pmin=? [ G F (x=1 & (X x=1)) ]" -pathviaautomata -exportpropaut my_automata.hoa
prism minex1.nm -pf "Pmin=? [ G F (x=1 & (X x=1)) ]" -ltl2datool ./hoa_mona_ltlf2dfa_for_prism -ltl2dasyntax spot


export PATH=/home/awells/Development/prism/prism/bin:$PATH
prism minex.nm minex2.props -pathviaautomata -exportpropaut my_automata.hoa
prism minex.nm minex2.props -ltl2datool ./hoa_mona_ltlf2dfa_for_prism -ltl2dasyntax spot


rosrun syft ltlf2fol ltlf3.ltlf NNF > minex3.mona
mona -w -u tall_out.mona

ltlfilt --from-ltlf ltlf3.ltlf > ltl3.props



prism minLTL.nm ltl3.props -pathviaautomata -exportpropaut my_automata.hoa
prism minLTL.nm ltl3.props -ltl2datool ./hoa_mona_ltlf2dfa_for_prism -ltl2dasyntax spot