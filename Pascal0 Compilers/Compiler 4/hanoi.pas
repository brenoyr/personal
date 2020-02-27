PROCEDURE HANOI(VAL N, F, T, U);
    BEGIN
        IF (N = 1) THEN
            WRITELN(F, T)
        ELSE
            BEGIN
                CALL HANOI(N - 1, F, U, T);
                CALL HANOI(1, F, T);
                CALL HANOI(N - 1, U, T, F);
            END
    END;

BEGIN
    CALL HANOI(4, 1, 3, 2);
END.