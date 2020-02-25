VAR S;

FUNCTION A(VAL X; REF Y);
  BEGIN
    IF X < 10 THEN
      BEGIN
        X := X + 1;
        Y := Y - 1;
        X := X + CALL A(X, X) + CALL A(Y, Y);
        A := X * Y;
      END
    ELSE
      A := 1;
  END;

BEGIN
  S := 11;
  S := S + CALL A(CALL A(9, S), S);
END.
