#!/usr/bin/env python

from z3 import *

s = Solver()

i_0 = BitVec("i_0", 8)
i_1 = BitVec("i_1", 8)
i_2 = BitVec("i_2", 8)
i_3 = BitVec("i_3", 8)
i_4 = BitVec("i_4", 8)
i_5 = BitVec("i_5", 8)
i_6 = BitVec("i_6", 8)
i_7 = BitVec("i_7", 8)
i_8 = BitVec("i_8", 8)
i_9 = BitVec("i_9", 8)
i_10 = BitVec("i_10", 8)
i_11 = BitVec("i_11", 8)
i_12 = BitVec("i_12", 8)
i_13 = BitVec("i_13", 8)
i_14 = BitVec("i_14", 8)
i_15 = BitVec("i_15", 8)
i_16 = BitVec("i_16", 8)
i_17 = BitVec("i_17", 8)
i_18 = BitVec("i_18", 8)
i_19 = BitVec("i_19", 8)
i_20 = BitVec("i_20", 8)
i_21 = BitVec("i_21", 8)
i_22 = BitVec("i_22", 8)
i_23 = BitVec("i_23", 8)
i_24 = BitVec("i_24", 8)
i_25 = BitVec("i_25", 8)
i_26 = BitVec("i_26", 8)
i_27 = BitVec("i_27", 8)
i_28 = BitVec("i_28", 8)
i_29 = BitVec("i_29", 8)
i_30 = BitVec("i_30", 8)
i_31 = BitVec("i_31", 8)
i_32 = BitVec("i_32", 8)
i_33 = BitVec("i_33", 8)
i_34 = BitVec("i_34", 8)
i_35 = BitVec("i_35", 8)
i_36 = BitVec("i_36", 8)
i_37 = BitVec("i_37", 8)
i_38 = BitVec("i_38", 8)
i_39 = BitVec("i_39", 8)
i_40 = BitVec("i_40", 8)
i_41 = BitVec("i_41", 8)
i_42 = BitVec("i_42", 8)
i_43 = BitVec("i_43", 8)
i_44 = BitVec("i_44", 8)
i_45 = BitVec("i_45", 8)
i_46 = BitVec("i_46", 8)
i_47 = BitVec("i_47", 8)
i_48 = BitVec("i_48", 8)
i_49 = BitVec("i_49", 8)
i_50 = BitVec("i_50", 8)

s.add(i_0 != 0)
s.add(i_1 != 0)
s.add(i_2 != 0)
s.add(i_3 != 0)
s.add(i_4 != 0)
s.add(i_5 != 0)
s.add(i_6 != 0)
s.add(i_7 != 0)
s.add(i_8 != 0)
s.add(i_9 != 0)
s.add(i_10 != 0)
s.add(i_11 != 0)
s.add(i_12 != 0)
s.add(i_13 != 0)
s.add(i_14 != 0)
s.add(i_15 != 0)
s.add(i_16 != 0)
s.add(i_17 != 0)
s.add(i_18 != 0)
s.add(i_19 != 0)
s.add(i_20 != 0)
s.add(i_21 != 0)
s.add(i_22 != 0)
s.add(i_23 != 0)
s.add(i_24 != 0)
s.add(i_25 != 0)
s.add(i_26 != 0)
s.add(i_27 != 0)
s.add(i_28 != 0)
s.add(i_29 != 0)
s.add(i_30 != 0)
s.add(i_31 != 0)
s.add(i_32 != 0)
s.add(i_33 != 0)
s.add(i_34 != 0)
s.add(i_35 != 0)
s.add(i_36 != 0)
s.add(i_37 != 0)
s.add(i_38 != 0)
s.add(i_39 != 0)
s.add(i_40 != 0)
s.add(i_41 != 0)
s.add(i_42 != 0)
s.add(i_43 != 0)
s.add(i_44 != 0)
s.add(i_45 != 0)
s.add(i_46 != 0)
s.add(i_47 != 0)
s.add(i_48 != 0)
s.add(i_49 != 0)
s.add(i_50 != 0)

s.add(i_0 == ord('C'))
s.add(i_1 == ord('T'))
s.add(i_2 == ord('F'))
s.add(i_3 == ord('{'))
s.add(i_50 == ord('}'))

s.add( (((i_30 ^ i_38) - i_8) + i_6) == i_0 )
s.add( (((i_36 + i_44) + i_0) - i_3) == i_18 )
s.add( (((i_19 ^ i_20) ^ i_38) ^ i_42) == i_1 )
s.add( ((((i_36 + i_35) - i_19) - i_3) - i_44) == i_2 )
s.add( ((((i_41 - i_10) - i_10) ^ i_17) + i_19) == i_3 )
s.add( (i_33 - i_21) == i_4 )
s.add( (((i_39 ^ i_8) ^ i_4) ^ i_4) == i_5 )
s.add( (((i_25 + i_10) - i_39) ^ i_14) == i_6 )
s.add( ((i_1 ^ i_15) + i_32) == i_7 )
s.add( ((i_5 + i_8) - i_5) == i_8 )
s.add( (i_7 ^ i_24) == i_9 )
s.add( (((i_17 ^ i_49) - i_4) + i_32) == i_10 )
s.add( (((i_38 ^ i_42) - i_17) - i_8) == i_11 )
s.add( (i_8 + i_14) == i_12 )
s.add( (i_20 + i_45) == i_13 )
s.add( (((i_25 - i_48) ^ i_20) + i_9) == i_14 )
s.add( (i_18 - i_31) == i_15 )
s.add( (i_46 ^ i_24) == i_16 )
s.add( (((i_2 + i_13) + i_47) ^ (i_50 ^ i_14)) == i_17  )
s.add( (((i_44 + i_36) + i_0) - i_3) == i_18 )
s.add( (((i_30 ^ i_41) - i_25) - i_28) == i_19 )
s.add( (i_44 ^ i_25) == i_20 )
s.add( (((i_28 + i_22) ^ (i_21 ^ i_39)) + i_25) == i_21 )
s.add( ((((i_44 - i_4) - i_12) ^ i_31) - i_30) == i_22 )
s.add( ((i_32 - i_14) ^ i_39) == i_23 )
s.add( (((i_21 ^ i_18) ^ i_0) ^ i_21) == i_24 )
s.add( (((i_17 ^ i_12) + (i_4 + i_18)) - i_11) == i_25 )
s.add( ((i_46 ^ i_32) + (i_20 + i_49)) == i_26 )
s.add( (((i_39 + i_25) + i_36) - i_48) == i_27 )
s.add( (i_15 ^ i_14) == i_28 )
s.add( ((i_35 + i_1) - i_42) == i_29 )
s.add( (((i_8 - i_31) - i_30) - i_24) == i_30 )
s.add( (((i_18 + i_15) - i_29) ^ i_42) == i_31 )
s.add( (((i_15 + i_5) + i_14) - i_44) == i_32 )
s.add( (((i_45 - i_15) ^ i_20) - i_32) == i_33 )
s.add( (((i_33 ^ i_3) - i_20) - i_10) == i_34 )
s.add( (((i_6 - i_43) ^ i_44) + (i_1 - i_44)) == i_35 )
s.add( (((i_25 + i_31) - i_28) ^ i_49) == i_36 )
s.add( (((i_31 ^ i_34) - i_34) + i_11) == i_37 )
s.add( (((i_36 ^ i_27) - i_5) + i_42) == i_38 )
s.add( (i_37 ^ i_8) == i_39 )
s.add( (((i_28 + i_7) ^ i_44) - i_10) == i_40 )
s.add( (((i_26 ^ i_17) ^ i_7) ^ i_20) == i_41 )
s.add( ((i_1 + i_50) - i_28) == i_42 )
s.add( ((i_33 + i_46) - i_15) == i_43 )
s.add( (((i_42 + i_24) + i_16) ^ (i_21 ^ i_45)) == i_44 )
s.add( (i_22 - i_40) == i_45 )
s.add( (((i_12 - i_46) - i_7) - i_35) == i_46 )
s.add( (((i_26 + i_15) ^ i_39) - i_12) == i_47 )
s.add( ((i_15 - i_8) ^ i_11) == i_48 )
s.add( (i_37 ^ i_27) == i_49 )
s.add( (((i_8 + i_13) + i_17) ^ (i_15 ^ i_24)) == i_50 )

while s.check() == sat:
	print chr(s.model()[i_0].as_long()) + chr(s.model()[i_1].as_long()) + chr(s.model()[i_2].as_long()) + chr(s.model()[i_3].as_long()) + chr(s.model()[i_4].as_long()) + chr(s.model()[i_5].as_long()) + chr(s.model()[i_6].as_long()) + chr(s.model()[i_7].as_long()) + chr(s.model()[i_8].as_long()) + chr(s.model()[i_9].as_long()) + chr(s.model()[i_10].as_long()) + chr(s.model()[i_11].as_long()) + chr(s.model()[i_12].as_long()) + chr(s.model()[i_13].as_long()) + chr(s.model()[i_14].as_long()) + chr(s.model()[i_15].as_long()) + chr(s.model()[i_16].as_long()) + chr(s.model()[i_17].as_long()) + chr(s.model()[i_18].as_long()) + chr(s.model()[i_19].as_long()) + chr(s.model()[i_20].as_long()) + chr(s.model()[i_21].as_long()) + chr(s.model()[i_22].as_long()) + chr(s.model()[i_23].as_long()) + chr(s.model()[i_24].as_long()) + chr(s.model()[i_25].as_long()) + chr(s.model()[i_26].as_long()) + chr(s.model()[i_27].as_long()) + chr(s.model()[i_28].as_long()) + chr(s.model()[i_29].as_long()) + chr(s.model()[i_30].as_long()) + chr(s.model()[i_31].as_long()) + chr(s.model()[i_32].as_long()) + chr(s.model()[i_33].as_long()) + chr(s.model()[i_34].as_long()) + chr(s.model()[i_35].as_long()) + chr(s.model()[i_36].as_long()) + chr(s.model()[i_37].as_long()) + chr(s.model()[i_38].as_long()) + chr(s.model()[i_39].as_long()) + chr(s.model()[i_40].as_long()) + chr(s.model()[i_41].as_long()) + chr(s.model()[i_42].as_long()) + chr(s.model()[i_43].as_long()) + chr(s.model()[i_44].as_long()) + chr(s.model()[i_45].as_long()) + chr(s.model()[i_46].as_long()) + chr(s.model()[i_47].as_long()) + chr(s.model()[i_48].as_long()) + chr(s.model()[i_49].as_long()) + chr(s.model()[i_50].as_long())
  	s.add(i_6 != s.model()[i_6], i_8 != s.model()[i_8], i_30 != s.model()[i_38], i_30 != s.model()[i_30])

