VAR F;

FUNCTION FIBONACCI(VAL N);
    BEGIN
        IF (N <= 2) THEN
            IF (N = 0) THEN
                FIBONACCI := 0
            ELSE
                FIBONACCI := 1
        ELSE
            FIBONACCI := CALL FIBONACCI(N - 1) + CALL FIBONACCI(N -2);
    END;

BEGIN
    FOR F := 1 TO 19 DO
        WRITE(CALL FIBONACCI(F));
    WRITELN(CALL FIBONACCI(F));
END.