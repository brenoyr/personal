CONST A = 5;
VAR B;

FUNCTION TWO(REF K; REF L; VAL M; VAL N);
  BEGIN
    L := L + 1;
    M := M - 1;
    TWO := L + K * M / N;
  END;

PROCEDURE ONE(VAL X; REF Y);
  BEGIN
    WRITELN(CALL TWO(X, Y, X, Y));
  END;

BEGIN
  B := A;
  CALL ONE(A, B);
END.
