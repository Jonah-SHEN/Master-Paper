libname Hold 'G:\Master_paper\Holding_Period';
run;

proc import out= Hold.Rt_fct_hy
     datafile="G:\Master_paper\Holding_Period\Rt_ptf_all_hy.xlsx"
	 dbms=excel replace;
	 getnames=yes;
run;

proc univariate data= Hold.Rt_fct_hy;
  var  Rt_m1 Rt_m2 Rt_m3 Rt_m4 Rt_m5 Rt_m6 Rt_m7 Rt_m8 Rt_m9;
  var  Rt1 Rt2 Rt3 Rt4 Rt5 Rt6 Rt7 Rt8 Rt9;
  var  Rt_f1 Rt_f2 Rt_f3 Rt_f4 Rt_f5 Rt_f6 Rt_f7 Rt_f8 Rt_f9;
  run;

proc reg data = Hold.Rt_fct_hy;
  ptf_hold_1: model Rt_f1 = RMRF SMB HML ;
  ptf_hold_2: model Rt_f2 = RMRF SMB HML ;
  ptf_hold_3: model Rt_f3 = RMRF SMB HML ;
  ptf_hold_4: model Rt_f4 = RMRF SMB HML ;
  ptf_hold_5: model Rt_f5 = RMRF SMB HML ;
  ptf_hold_6: model Rt_f6 = RMRF SMB HML ;
  ptf_hold_7: model Rt_f7 = RMRF SMB HML ;
  ptf_hold_8: model Rt_f8 = RMRF SMB HML ;
  ptf_hold_9: model Rt_f9 = RMRF SMB HML ;
  run;

  quit;

  proc import out= Hold.Rt_fct_ay
     datafile="G:\Master_paper\Holding_Period\Rt_ptf_all_ay.xlsx"
	 dbms=excel replace;
	 getnames=yes;
run;

proc univariate data= Hold.Rt_fct_ay;
   var  Rt_m1 Rt_m2 Rt_m3 Rt_m4 Rt_m5 Rt_m6 Rt_m7 Rt_m8 Rt_m9;
   var  Rt1 Rt2 Rt3 Rt4 Rt5 Rt6 Rt7 Rt8 Rt9;
   var  Rt_f1 Rt_f2 Rt_f3 Rt_f4 Rt_f5 Rt_f6 Rt_f7 Rt_f8 Rt_f9;
  run;

proc reg data = Hold.Rt_fct_ay;
  ptf_hold_1: model Rt_f1 = RMRF SMB HML ;
  ptf_hold_2: model Rt_f2 = RMRF SMB HML ;
  ptf_hold_3: model Rt_f3 = RMRF SMB HML ;
  ptf_hold_4: model Rt_f4 = RMRF SMB HML ;
  ptf_hold_5: model Rt_f5 = RMRF SMB HML ;
  ptf_hold_6: model Rt_f6 = RMRF SMB HML ;
  ptf_hold_7: model Rt_f7 = RMRF SMB HML ;
  ptf_hold_8: model Rt_f8 = RMRF SMB HML ;
  ptf_hold_9: model Rt_f9 = RMRF SMB HML ;
  run;

  quit;

  proc univariate data= Hold.Rt_fct_ay;
   var  SMB HML RMRF;
  run;
   quit;

   proc univariate data= Hold.Rt_fct_hy;
   var  SMB HML RMRF;
  run;
   quit;
