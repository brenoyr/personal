VAR A,B,C;

FUNCTION ALL(REF K, L; VAL M);

  PROCEDURE ONE(VAL X; REF Y);
    BEGIN
      WRITELN(X, Y, K, L, M, A, B, C);
      X := X - Y;
      Y := Y + 55;
      WRITELN(X, Y, K, L, M, A, B, C)
    END;

  PROCEDURE TWO(REF Q, P);
    BEGIN
      WRITELN(Q, P, K, L, M, A, B, C);
      Q := Q * 2;
      P := P - 5;
      WRITELN(Q, P, K, L, M, A, B, C);
      CALL ONE(Q, P);
      WRITELN(Q, P, K, L, M, A, B, C)
    END;

  BEGIN
    K := K + 10;
    L := L - 20;
    CALL ONE(K, K);
    CALL TWO(M, M);
    ALL := 777
  END;

BEGIN
  A := 500;
  B := 900;
  C := 800;
  WRITELN(CALL ALL(A, B, CALL ALL(A, B, C)));
  WRITELN(A, B, C)
END.
