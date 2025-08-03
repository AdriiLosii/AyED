//C++ code

void drawSpiral(Turtle myTurtle, int lineLen)
{
    // Compare with ActiveCode 2
    if (lineLen > 0)
    {
        myTurtle.forward(lineLen);
        myTurtle.right(90);
        drawSpiral(myTurtle, lineLen - 5);
    }
}