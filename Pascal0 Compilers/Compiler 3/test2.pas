VAR N;

FUNCTION J;
  BEGIN
    IF (N = 1) THEN
      J := 7
    ELSE
      IF (N = 6) THEN
        J := 0;
  END;

FUNCTION S;
  BEGIN
    IF (N = 0) THEN
      S := -1
    ELSE
      IF (N = 1) THEN
        S := 1;
  END;

VAR I, M, K;

BEGIN
  I := 1;
  M := 8;
  K := 12;
  IF (I = 1) AND (M = 8) THEN
    WRITELN(-10);
  IF (I = 9) OR (K = 12) THEN
    WRITELN(-20);
  IF NOT (K = 10) THEN
    WRITELN(-30);
  N := 1;
  WRITELN(CALL J);
  N := 0;
  WRITELN(CALL S);
END.
