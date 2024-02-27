DECLARE 
    N1 NUMBER(2) := &N1;
    N2 NUMBER(2) := &N2;
    N3 NUMBER(2) := &N3;
    S NUMBER(3);
    A NUMBER(3);
BEGIN
    S:= N1 + N2 + N3;
    A = S/3;
    DBMS_OUTPUT.PUT_LINE('SUM = '||S);
    DBMS_OUTPUT.PUT_LINE('AVG = '||A);
END;