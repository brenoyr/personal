CONST G = 100;
VAR X;

PROCEDURE TWO(REF P; VAL L; REF M);
  BEGIN
    P := 300 + L;
    L := X + G;
    REPEAT
      WHILE (P = M) DO;
    UNTIL (1 = 1);
  END;

VAR A;

FUNCTION ONE(REF N; VAL M);
  BEGIN
    IF NOT (1 = 1) OR (M = N) AND (N = M) THEN
    ELSE;
    ONE := CALL ONE(M, CALL ONE(N, N + M))
  END;

.
