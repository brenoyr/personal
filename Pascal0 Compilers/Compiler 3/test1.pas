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

VAR X,Y;

BEGIN
  X := CALL J;
  Y := CALL S;
END.
