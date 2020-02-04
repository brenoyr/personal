CONST A = 5, B = 10;
VAR C, D, E;

PROCEDURE ONE;
  VAR B, C;

  PROCEDURE TWO;
    VAR C, D;

    BEGIN
      C := 1;
      D := 5;
      IF C = D THEN
        CALL TWO
      ELSE
        WRITE(1);
      IF A <> D THEN
        CALL ONE;
    END;

  PROCEDURE THREE;
    VAR X, Y, Z, A, B, C;

    BEGIN
      X := 1;
      C := 2;
      IF C < X THEN
        BEGIN
          CALL THREE;
          CALL ONE;
        END;
      FOR B := X TO C * C DO
        WRITE(B);
      FOR B := C DOWNTO X DO
        WRITE(B);
      WRITELN(X, C);
    END;

  BEGIN
    B := 2;
    C := 3;
    IF B <= -(5 + C * A) THEN
      B := B + 1;
    E := 1;
    CALL TWO;
    CALL THREE;
    REPEAT
      WRITE(B);
      B := B - 1;
    UNTIL B < -A;
    CASE B / C OF
      A: B := B * 100;
      0: B := B + 100;
    CEND;
  END;

VAR X, Y, Z;

BEGIN
  C := 1;
  C := +(C - 1);
  CALL ONE;
  WHILE A > C * 3 / 2 DO
    WHILE B >= C DO
      BEGIN
        IF ODD E THEN
          E := E - 1;
        C := C + 1;
      END;
  WRITELN(C, A, B);
END.
