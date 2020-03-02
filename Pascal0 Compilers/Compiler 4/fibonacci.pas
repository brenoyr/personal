VAR A;

FUNCTION FIBONACCI(VAL N);
    BEGIN
        IF (N < 3) THEN
            IF (N = 1) THEN
                FIBONACCI := 0
            ELSE
                FIBONACCI := 1
        ELSE
            FIBONACCI := CALL FIBONACCI(N - 1) + CALL FIBONACCI(N - 2);
    END;

BEGIN
    FOR A := 1 TO 19 DO
        WRITE(CALL FIBONACCI(A));
    WRITELN(CALL FIBONACCI(A));
END.