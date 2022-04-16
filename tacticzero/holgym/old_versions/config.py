import json
import re
import random
random.seed(0)

HOLPATH = "/home/wu099/temp/HOL/bin/hol --maxheap=256"

try: 
    with open("dict.json") as f:
        dictionary = json.load(f)
except:
    dictionary = {}
    
MAX_LEN = 128
MAX_ASSUMPTIONS = 3
MAX_CONTEXTS = 8
PRINT_EXCEPTION = False
UNEXPECTED_REWARD = -1000

# MODE = "train"
CONTINUE = False


# DELSIMPS = ["HD", "TL_DEF", "APPEND", "FLAT", "LENGTH", "MAP", "LIST_TO_SET_DEF", "FILTER", "EVERY_DEF", "EXISTS_DEF", "MAP2_DEF", "APPEND_NIL", "LENGTH_APPEND", "MAP_ID", "FLAT_APPEND", "EL_restricted", "EL_simp_restricted", "LIST_REL_def", "LIST_REL_NIL", "REVERSE_DEF", "REVERSE_REVERSE", "REVERSE_11", "MEM_REVERSE", "LENGTH_REVERSE", "REVERSE_EQ_NIL", "REVERSE_EQ_SING", "LAST_CONS", "FRONT_CONS", "LENGTH_FRONT_CONS", "FRONT_CONS_EQ_NIL", "LAST_APPEND_CONS", "TAKE_nil", "TAKE_cons", "DROP_nil", "DROP_cons", "TAKE_0", "TAKE_LENGTH_ID", "LENGTH_TAKE", "DROP_0", "TAKE_DROP", "LENGTH_DROP", "ALL_DISTINCT", "LIST_TO_SET_APPEND", "LIST_TO_SET_EQ_EMPTY", "FINITE_LIST_TO_SET", "LIST_TO_SET_REVERSE", "SET_TO_LIST_EMPTY", "SET_TO_LIST_SING", "ALL_DISTINCT_SET_TO_LIST", "isPREFIX", "isPREFIX_THM", "SNOC", "LENGTH_SNOC", "LAST_SNOC", "FRONT_SNOC", "SNOC_11", "LENGTH_GENLIST", "GENLIST_AUX_compute", "EL_GENLIST", "GENLIST_NUMERALS", "INFINITE_LIST_UNIV", "LENGTH_LUPDATE", "LIST_BIND_THM", "SINGL_LIST_APPLY_L", "SINGL_SINGL_APPLY", "dropWhile_def", "APPEND_11"]

# DELSIMPS = ["HD", "TL_DEF", "APPEND", "FLAT", "LENGTH", "MAP", "LIST_TO_SET_DEF", "FILTER", "EVERY_DEF", "EXISTS_DEF", "MAP2_DEF", "APPEND_NIL", "LENGTH_APPEND", "MAP_ID", "FLAT_APPEND", "EL_restricted", "EL_simp_restricted", "LIST_REL_def", "LIST_REL_NIL", "REVERSE_DEF", "REVERSE_REVERSE", "REVERSE_11", "MEM_REVERSE", "LENGTH_REVERSE", "REVERSE_EQ_NIL", "REVERSE_EQ_SING", "LAST_CONS", "FRONT_CONS", "LENGTH_FRONT_CONS", "FRONT_CONS_EQ_NIL", "LAST_APPEND_CONS", "TAKE_nil", "TAKE_cons", "DROP_nil", "DROP_cons", "TAKE_0", "TAKE_LENGTH_ID", "LENGTH_TAKE", "DROP_0", "TAKE_DROP", "LENGTH_DROP", "ALL_DISTINCT", "LIST_TO_SET_APPEND", "LIST_TO_SET_EQ_EMPTY", "FINITE_LIST_TO_SET", "LIST_TO_SET_REVERSE", "SET_TO_LIST_EMPTY", "SET_TO_LIST_SING", "ALL_DISTINCT_SET_TO_LIST", "isPREFIX", "isPREFIX_THM", "SNOC", "LENGTH_SNOC", "LAST_SNOC", "FRONT_SNOC", "SNOC_11", "LENGTH_GENLIST", "GENLIST_AUX_compute", "EL_GENLIST", "GENLIST_NUMERALS", "INFINITE_LIST_UNIV", "LENGTH_LUPDATE", "LIST_BIND_THM", "SINGL_LIST_APPLY_L", "SINGL_SINGL_APPLY", "dropWhile_def", "APPEND_11", "MAP2_NIL", "LENGTH_MAP2", "MAP_EQ_NIL", "MAP_EQ_SING", "LENGTH_NIL", "LENGTH_NIL_SYM", "ALL_DISTINCT_REVERSE", "ALL_DISTINCT_FLAT_REVERSE", "isPREFIX_NILR", "LUPDATE_NIL", "SHORTLEX_THM", "SHORTLEX_NIL2", "WF_SHORTLEX", "LLEX_THM", "LLEX_NIL2", "nub_set", "EVERY2_THM", "oHD_thm", "LIST_TO_SET", "LENGTH_MAP", "MEM_APPEND", "SING_HD", "APPEND_eq_NIL", "NULL_APPEND", "FILTER_F", "FILTER_T", "MEM", "LENGTH_ZIP_MIN", "LAST_MAP", "TAKE_EQ_NIL", "MEM_SET_TO_LIST", "MEM_SNOC", "LIST_REL_eq"]

DELSIMPS = ["ALL_DISTINCT.1", "ALL_DISTINCT.2", "ALL_DISTINCT_FLAT_REVERSE.1", "ALL_DISTINCT_REVERSE.1", "ALL_DISTINCT_SET_TO_LIST.1", "APPEND.1", "APPEND.2", "APPEND_11.1", "APPEND_11.2", "APPEND_ASSOC.1", "APPEND_NIL.1", "APPEND_eq_NIL.1", "APPEND_eq_NIL.2", "APPEND_eq_NIL.3", "APPEND_eq_NIL.4", "CONS.1", "CONS_11.1", "CONS_11.2", "CONS_ACYCLIC.1", "CONS_ACYCLIC.2", "CONS_ACYCLIC.3", "CONS_ACYCLIC.4", "DROP_0.1", "DROP_cons.1", "DROP_nil.1", "EL_GENLIST.1", "EL_restricted.1", "EL_restricted.2", "EL_simp_restricted.1", "EL_simp_restricted.2", "EVERY2_THM.1", "EVERY2_THM.2", "EVERY2_THM.3", "EVERY2_THM.4", "EVERY_APPEND.1", "EVERY_DEF.1", "EVERY_DEF.2", "EVERY_SIMP.1", "EXISTS_APPEND.1", "EXISTS_DEF.1", "EXISTS_DEF.2", "EXISTS_SIMP.1", "FILTER.1", "FILTER.2", "FILTER_F.1", "FILTER_T.1", "FINITE_LIST_TO_SET.1", "FLAT.1", "FLAT.2", "FLAT_APPEND.1", "FOLDL.1", "FOLDL.2", "FOLDL2_def.1", "FOLDL2_def.2", "FOLDL2_def.3", "FOLDL_ZIP_SAME.1", "FOLDR.1", "FOLDR.2", "FRONT_CONS.1", "FRONT_CONS.2", "FRONT_CONS_EQ_NIL.1", "FRONT_CONS_EQ_NIL.2", "FRONT_CONS_EQ_NIL.3", "FRONT_SNOC.1", "GENLIST_AUX_compute.1", "GENLIST_AUX_compute.2", "GENLIST_AUX_compute.3", "GENLIST_NUMERALS.1", "GENLIST_NUMERALS.2", "HD.1", "INFINITE_LIST_UNIV.1", "LAST_APPEND_CONS.1", "LAST_CONS.1", "LAST_CONS.2", "LAST_MAP.1", "LAST_SNOC.1", "LENGTH.1", "LENGTH.2", "LENGTH_APPEND.1", "LENGTH_DROP.1", "LENGTH_FRONT_CONS.1", "LENGTH_GENLIST.1", "LENGTH_LUPDATE.1", "LENGTH_MAP.1", "LENGTH_MAP2.1", "LENGTH_NIL.1", "LENGTH_NIL_SYM.1", "LENGTH_REVERSE.1", "LENGTH_SNOC.1", "LENGTH_TAKE.1", "LENGTH_UNZIP.1", "LENGTH_UNZIP.2", "LENGTH_ZIP.1", "LENGTH_ZIP.2", "LENGTH_ZIP_MIN.1", "LIST_BIND_THM.1", "LIST_BIND_THM.2", "LIST_REL_NIL.1", "LIST_REL_NIL.2", "LIST_REL_def.1", "LIST_REL_def.2", "LIST_REL_def.3", "LIST_REL_def.4", "LIST_REL_eq.1", "LIST_TO_SET.1", "LIST_TO_SET.2", "LIST_TO_SET_APPEND.1", "LIST_TO_SET_DEF.1", "LIST_TO_SET_DEF.2", "LIST_TO_SET_EQ_EMPTY.1", "LIST_TO_SET_EQ_EMPTY.2", "LIST_TO_SET_REVERSE.1", "LLEX_NIL2.1", "LLEX_THM.1", "LLEX_THM.2", "LLEX_THM.3", "LLEX_THM.4", "LUPDATE_LENGTH.1", "LUPDATE_NIL.1", "MAP.1", "MAP.2", "MAP2.1", "MAP2.2", "MAP2_DEF.1", "MAP2_DEF.2", "MAP2_DEF.3", "MAP2_NIL.1", "MAP_APPEND.1", "MAP_EQ_NIL.1", "MAP_EQ_NIL.2", "MAP_EQ_SING.1", "MAP_EQ_SING.2", "MAP_ID.1", "MAP_ID.2", "MAP_ZIP_SAME.1", "MEM.1", "MEM.2", "MEM_APPEND.1", "MEM_REVERSE.1", "MEM_SET_TO_LIST.1", "MEM_SNOC.1", "NOT_CONS_NIL.1", "NOT_CONS_NIL.2", "NOT_EVERY.1", "NOT_EXISTS.1", "NOT_NIL_CONS.1", "NOT_NIL_CONS.2", "NULL_APPEND.1", "NULL_DEF.1", "NULL_DEF.2", "REVERSE_11.1", "REVERSE_DEF.1", "REVERSE_DEF.2", "REVERSE_EQ_NIL.1", "REVERSE_EQ_SING.1", "REVERSE_REVERSE.1", "SET_TO_LIST_EMPTY.1", "SET_TO_LIST_SING.1", "SHORTLEX_NIL2.1", "SHORTLEX_THM.1", "SHORTLEX_THM.2", "SHORTLEX_THM.3", "SHORTLEX_THM.4", "SINGL_LIST_APPLY_L.1", "SINGL_SINGL_APPLY.1", "SING_HD.1", "SING_HD.2", "SNOC.1", "SNOC.2", "SNOC_11.1", "SNOC_11.2", "SUM.1", "SUM.2", "TAKE_0.1", "TAKE_DROP.1", "TAKE_EQ_NIL.1", "TAKE_EQ_NIL.2", "TAKE_LENGTH_ID.1", "TAKE_cons.1", "TAKE_nil.1", "TL_DEF.1", "TL_DEF.2", "UNZIP.1", "UNZIP.2", "UNZIP_ZIP.1", "WF_SHORTLEX.1", "ZIP.1", "ZIP.2", "ZIP_UNZIP.1", "dropWhile_def.1", "dropWhile_def.2", "isPREFIX.1", "isPREFIX.2", "isPREFIX_NILR.1", "isPREFIX_THM.1", "isPREFIX_THM.2", "isPREFIX_THM.3", "list_case_def.1", "list_case_def.2", "nub_set.1", "oHD_thm.1", "oHD_thm.2", "FINITE_common_prefixes.1", "IS_PREFIX_APPEND3.1", "IS_PREFIX_APPENDS.1", "IS_PREFIX_REFL.1", "IS_SUFFIX_REFL.1", "LENGTH_FLAT_REPLICATE.1", "LENGTH_REPLICATE.1", "LIST_REL_APPEND_SING.1", "LIST_REL_REVERSE_EQ.1", "NIL_IN_common_prefixes.1", "REPLICATE.1", "REPLICATE.2", "REVERSE_REPLICATE.1", "SUM_REPLICATE.1", "common_prefixes_NONEMPTY.1", "common_prefixes_NONEMPTY.2", "common_prefixes_PAIR.1", "common_prefixes_PAIR.2", "common_prefixes_PAIR.3", "longest_prefix_EMPTY.1", "longest_prefix_SING.1"]

DELSIMPS2 = ["FINITE_common_prefixes.1", "IS_PREFIX_APPEND3.1", "IS_PREFIX_APPENDS.1", "IS_PREFIX_REFL.1", "IS_SUFFIX_REFL.1", "LENGTH_FLAT_REPLICATE.1", "LENGTH_REPLICATE.1", "LIST_REL_APPEND_SING.1", "LIST_REL_REVERSE_EQ.1", "NIL_IN_common_prefixes.1", "REPLICATE.1", "REPLICATE.2", "REVERSE_REPLICATE.1", "SUM_REPLICATE.1", "common_prefixes_NONEMPTY.1", "common_prefixes_NONEMPTY.2", "common_prefixes_PAIR.1", "common_prefixes_PAIR.2", "common_prefixes_PAIR.3", "longest_prefix_EMPTY.1", "longest_prefix_SING.1"]

DELSIMPS3 = ["LIST_EQ_SIMP_CONV"]

# DELSIMPS3 = ["list$list simpl.rewrite: 1.1","list$list simpl.rewrite: 1.2", "list$list simpl.rewrite: 2.1","list$list simpl.rewrite: 2.2", "list$list simpl.rewrite: 3.1","list$list simpl.rewrite: 3.2", "list$list simpl.rewrite: 4.1","list$list simpl.rewrite: 4.2"]

dels = re.sub("\'","\"",str(DELSIMPS))
dels2 = re.sub("\'","\"",str(DELSIMPS2))
dels3 = re.sub("\'","\"",str(DELSIMPS3))

with open("polished_def_dict.json") as f:
    defs = json.load(f)
    # print(list(dictionary.keys()))
with open("polished_thm_dict.json") as f:
    pthms = json.load(f)

if CONTINUE:
    with open("fact_pool.json") as f:
        fact_pool = json.load(f)
else:
    fact_pool = list(defs.keys())

    
new_facts = {}

thms_tactic = ["simp", "fs", "metis_tac"]

thm_tactic = ["irule"]

term_tactic = ["Induct_on"]

no_arg_tactic = ["strip_tac"]

tactic_pool = thms_tactic + thm_tactic + term_tactic + no_arg_tactic

with open("thm_dict.json") as f:
    thms = json.load(f)
    # print(list(dictionary.keys()))

GOALS = list(thms.keys())
TEST_GOALS = [GOALS[5]]
random.shuffle(GOALS)
TEST = GOALS[:(len(GOALS)//4)]
TRAIN = GOALS[(len(GOALS)//4):]
